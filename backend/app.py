# ==========================================
# GEVENT MONKEY PATCHING (MANDATORY TO BE AT THE VERY TOP)
# This fixes the MonkeyPatchWarning and prevents RecursionError with Gunicorn
# ==========================================
from gevent import monkey
monkey.patch_all()

import os
import re
import time
import socket
import logging
import shutil
import subprocess
import threading
import ipaddress
from urllib.parse import urlparse, urljoin
from flask import Flask, request, jsonify, Response, stream_with_context
from flask_cors import CORS
from flask_compress import Compress
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from werkzeug.middleware.proxy_fix import ProxyFix
import yt_dlp
import requests

# Ensure Deno binary is on PATH so gunicorn worker subprocesses inherit it.
# Check the actual binary file (not just the directory) to be certain it exists.
_deno_bin_candidates = [
    os.path.expanduser('~/.deno/bin/deno'),
    '/opt/render/.deno/bin/deno',
    '/root/.deno/bin/deno',
]
for _deno_bin in _deno_bin_candidates:
    if os.path.isfile(_deno_bin):
        _deno_dir = os.path.dirname(_deno_bin)
        if _deno_dir not in os.environ.get('PATH', ''):
            os.environ['PATH'] = _deno_dir + os.pathsep + os.environ.get('PATH', '')
        break

def get_ffmpeg_path():
    """Locates ffmpeg executable from PATH or bundled imageio-ffmpeg."""
    path = shutil.which('ffmpeg')
    if path:
        return path
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        pass
    return 'ffmpeg'

# Initialize Flask & Middleware
app = Flask(__name__)

# Apply ProxyFix to correctly get client IP behind reverse proxies (like Render load balancers)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_port=1)

# ==========================================
# 🛡️ 1. STRICT CORS POLICY (SECURITY) 🛡️
# ==========================================
CORS(app, resources={r"/api/*": {
    "origins": [
        "https://downsocial.net",
        "https://www.downsocial.net",
        "https://video-downloader-mehran7.vercel.app",
        "https://video-downloader-lemon-three.vercel.app",
        "http://localhost:5500",
        "http://127.0.0.1:5500",
        "http://localhost:5000",
        "http://127.0.0.1:5000",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:8000",
        "http://127.0.0.1:8000",
        "http://localhost:8080",
        "http://127.0.0.1:8080"
    ]
}})

compress = Compress()
compress.init_app(app)

# ==========================================
# 🛑 2. RATE LIMITING (ANTI-DDoS & SPAM PROTECTION) 🛑
# Supports distributed Redis backend when available (Gunicorn multi-worker)
# ==========================================
storage_uri = os.environ.get("REDIS_URL") or os.environ.get("REDIS_TLS_URL") or "memory://"
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["5000 per day", "100 per minute"],
    storage_uri=storage_uri
)

# Configure Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# ==========================================
# 🔒 3. ANTI-SSRF & SAFE URL VALIDATION 🔒
# ==========================================
BLOCKED_NETWORKS = [
    ipaddress.ip_network("0.0.0.0/8"),
    ipaddress.ip_network("10.0.0.0/8"),
    ipaddress.ip_network("100.64.0.0/10"),
    ipaddress.ip_network("127.0.0.0/8"),
    ipaddress.ip_network("169.254.0.0/16"),
    ipaddress.ip_network("172.16.0.0/12"),
    ipaddress.ip_network("192.168.0.0/16"),
    ipaddress.ip_network("198.18.0.0/15"),
    ipaddress.ip_network("224.0.0.0/4"),
    ipaddress.ip_network("240.0.0.0/4"),
    ipaddress.ip_network("::1/128"),
    ipaddress.ip_network("fc00::/7"),
    ipaddress.ip_network("fe80::/10"),
    ipaddress.ip_network("::ffff:0:0/96"),
]

ALLOWED_HOST_SUFFIXES = (
    # Meta / Facebook / Instagram / Threads
    "fbcdn.net", "facebook.com", "fb.watch", "fb.gg",
    "cdninstagram.com", "instagram.com", "instagram.net", "instagr.am",
    "threads.net",
    # TikTok / ByteDance
    "tiktokcdn.com", "tiktokcdn-us.com", "tiktokcdn-eu.com", "tiktok.com",
    "byteoversea.com", "ibyteimg.com", "musical.ly",
    "muscdn.com", "tiktokv.com", "tiktokv.us",
    # Google / YouTube
    "googlevideo.com", "ytimg.com", "youtube.com", "youtu.be",
    "googleusercontent.com",
    # Snapchat
    "sc-cdn.net", "snapchat.com",
    # Standard Media CDNs used by verified platforms
    "akamaihd.net", "akamaized.net", "cloudfront.net", "fastly.net"
)

def is_ip_blocked(ip_obj) -> bool:
    """Checks if an IP address falls in private, loopback, link-local or reserved ranges."""
    return (
        ip_obj.is_private or 
        ip_obj.is_loopback or 
        ip_obj.is_link_local or 
        ip_obj.is_multicast or 
        ip_obj.is_reserved or 
        any(ip_obj in net for net in BLOCKED_NETWORKS)
    )

def is_safe_web_url(url: str) -> bool:
    """Validates public HTTP/HTTPS URLs (used for user input /api/download & unshortener hops)."""
    if not url or not isinstance(url, str):
        return False
    try:
        parsed = urlparse(url.strip())
        if parsed.scheme not in ("http", "https") or not parsed.hostname:
            return False
        hostname = parsed.hostname.lower()
        if hostname in ("localhost", "127.0.0.1", "::1") or hostname.endswith(".local") or hostname.endswith(".internal"):
            return False

        # Verify DNS resolution points to a public IP
        try:
            addr_info = socket.getaddrinfo(hostname, None)
            for res in addr_info:
                ip = ipaddress.ip_address(res[4][0])
                if is_ip_blocked(ip):
                    return False
        except socket.gaierror:
            return False

        return True
    except Exception:
        return False

def is_safe_media_url(url: str) -> bool:
    """Validates that a URL is a safe media streaming URL from an authorized CDN/platform (used for /api/direct)."""
    if not url or not isinstance(url, str):
        return False
    try:
        parsed = urlparse(url.strip())
        if parsed.scheme not in ("http", "https") or not parsed.hostname:
            return False
        hostname = parsed.hostname.lower()

        # Reject local/internal hostnames
        if hostname in ("localhost", "127.0.0.1", "::1") or hostname.endswith(".local") or hostname.endswith(".internal"):
            return False

        # Enforce authorized media CDN domain allow-list
        is_allowed = any(hostname == domain or hostname.endswith("." + domain) for domain in ALLOWED_HOST_SUFFIXES)
        if not is_allowed:
            logging.warning(f"[SSRF BLOCKED] Media host not in allow-list: {hostname}")
            return False

        # Verify resolved IP addresses are not private/reserved
        try:
            addr_info = socket.getaddrinfo(hostname, None)
            for res in addr_info:
                ip = ipaddress.ip_address(res[4][0])
                if is_ip_blocked(ip):
                    return False
        except socket.gaierror:
            pass

        return True
    except Exception:
        return False

# ==========================================
# 🚀 4. TTL CACHE 🚀
# ==========================================
class SimpleTTLCache:
    def __init__(self, ttl_seconds=1800):
        self.cache = {}
        self.ttl = ttl_seconds

    def get(self, key):
        if key in self.cache:
            entry = self.cache[key]
            if time.time() - entry['timestamp'] < self.ttl:
                logging.info(f"[CACHE HIT] Serving from memory: {key}")
                return entry['data']
            else:
                del self.cache[key]
        return None

    def set(self, key, value):
        self.cache[key] = {'data': value, 'timestamp': time.time()}

video_cache = SimpleTTLCache(ttl_seconds=120)

http_session = requests.Session()
adapter = requests.adapters.HTTPAdapter(pool_connections=200, pool_maxsize=500)
http_session.mount("http://", adapter)
http_session.mount("https://", adapter)

def resolve_short_url(url):
    """
    Manually resolves redirects for shortened URLs across all platforms
    (Facebook, TikTok, YouTube Shorts, Instagram, Snapchat, Threads, bit.ly, etc.)
    with strict SSRF redirect hop validation.
    """
    if not url or not is_safe_web_url(url):
        return url

    # Normalize threads.com to threads.net so yt-dlp recognizes the domain
    if 'threads.com' in url.lower():
        url = re.sub(r'threads\.com', 'threads.net', url, flags=re.IGNORECASE)

    short_patterns = [
        "/share/", "fb.watch", "fb.gg", "facebook.com/share",
        "vm.tiktok.com", "vt.tiktok.com", "tiktok.com/t/",
        "youtu.be", "youtube.com/shorts",
        "instagr.am", "instagram.com/share", "instagram.com/reel",
        "snapchat.com/t/", "t.co", "bit.ly", "tinyurl.com"
    ]

    is_short = any(pattern in url.lower() for pattern in short_patterns)

    if is_short:
        try:
            logging.info(f"[UNSHORTENER] Resolving shortened URL: {url}")
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
            }
            
            current_url = url
            # Follow redirects up to 6 hops with SSRF checking
            for _ in range(6):
                res = http_session.head(current_url, headers=headers, allow_redirects=False, timeout=6)
                if res.status_code in [301, 302, 303, 307, 308] and 'Location' in res.headers:
                    next_url = res.headers['Location']
                    if next_url.startswith('/'):
                        next_url = urljoin(current_url, next_url)
                    if not is_safe_web_url(next_url):
                        logging.warning(f"[UNSHORTENER BLOCKED] Suspicious redirect target: {next_url}")
                        break
                    # Detect Instagram/Threads login redirect — return original URL
                    # so yt-dlp can attempt extraction with its own cookies/session
                    parsed_next = urlparse(next_url)
                    if parsed_next.path.startswith('/accounts/login') or \
                       parsed_next.path.startswith('/login') or \
                       'accounts/login' in next_url or \
                       'login' in parsed_next.path.lower() and any(
                           d in parsed_next.netloc for d in ['instagram.com', 'threads.com', 'threads.net']
                       ):
                        logging.warning(f"[UNSHORTENER] Login redirect detected, returning original URL: {url}")
                        return url
                    current_url = next_url
                else:
                    break
            
            if 'threads.com' in current_url.lower():
                current_url = re.sub(r'threads\.com', 'threads.net', current_url, flags=re.IGNORECASE)
                    
            logging.info(f"[UNSHORTENER] Successfully un-shortened: {url} -> {current_url}")
            return current_url
        except Exception as e:
            logging.error(f"[UNSHORTENER ERROR] Failed to un-shorten URL: {str(e)}")
            
    return url

def get_platform_prefix(url):
    url_low = (url or '').lower()
    if 'youtube' in url_low or 'youtu.be' in url_low:
        return 'YT'
    elif 'instagram' in url_low or 'instagr.am' in url_low:
        return 'Insta'
    elif 'tiktok' in url_low:
        return 'TikTok'
    elif 'snapchat' in url_low:
        return 'Snap'
    elif 'threads' in url_low:
        return 'Threads'
    elif 'facebook' in url_low or 'fb.' in url_low:
        return 'FB'
    return 'Downsocial'

def get_platform_request_headers(url, extra_headers=None):
    """
    Constructs platform-optimized headers including required Referer for TikTok,
    Instagram, Facebook, and YouTube CDN media streams.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'Accept': '*/*',
        'Accept-Encoding': 'identity'
    }
    url_low = (url or '').lower()
    
    # TikTok / ByteDance CDN requires Referer https://www.tiktok.com/
    if any(k in url_low for k in ['tiktok', 'muscdn', 'tiktokv', 'byteoversea', 'ibyteimg']):
        headers['Referer'] = 'https://www.tiktok.com/'
    # Instagram CDN
    elif any(k in url_low for k in ['instagram', 'cdninstagram', 'instagr.am']):
        headers['Referer'] = 'https://www.instagram.com/'
    # Facebook CDN
    elif any(k in url_low for k in ['facebook', 'fbcdn.net', 'fb.watch', 'fb.gg']):
        headers['Referer'] = 'https://www.facebook.com/'
    # YouTube CDN (googlevideo.com should NOT have youtube.com referer as android client streams reject it)
    elif 'googlevideo.com' in url_low:
        headers['User-Agent'] = 'com.google.android.youtube/19.29.37 (Linux; U; Android 14) gzip'
    elif any(k in url_low for k in ['youtube', 'ytimg', 'youtu.be']):
        headers['Referer'] = 'https://www.youtube.com/'

    if extra_headers:
        headers.update(extra_headers)
    return headers

def get_ydl_options(url=None):
    is_youtube = bool(url) and ('youtube.com' in url.lower() or 'youtu.be' in url.lower())
    is_instagram = bool(url) and ('instagram.com' in url.lower() or 'instagr.am' in url.lower())
    is_threads = bool(url) and ('threads.com' in url.lower() or 'threads.net' in url.lower())
    cookies_file = None

def get_youtube_cookie_file():
    possible_cookie_paths = [
        '/etc/secrets/cookies.txt',
        '/etc/secrets/cookies',
        '/etc/secrets/cookies 1.txt',
        '/etc/secrets/cookies_1.txt',
        '/etc/secrets/cookies 1',
        '/etc/secrets/cookies 2.txt',
        '/etc/secrets/cookies_2.txt',
        '/etc/secrets/cookies 2',
        '/etc/secrets/cookies 3.txt',
        '/etc/secrets/cookies_3.txt',
        '/etc/secrets/cookies 3',
        os.path.join(os.path.dirname(__file__), 'cookies.txt'),
        os.path.join(os.path.dirname(__file__), 'cookies 1.txt'),
        os.path.join(os.path.dirname(__file__), 'cookies_1.txt'),
        os.path.join(os.path.dirname(__file__), 'cookies 2.txt'),
        os.path.join(os.path.dirname(__file__), 'cookies_2.txt'),
        os.path.join(os.path.dirname(__file__), 'cookies 3.txt'),
        os.path.join(os.path.dirname(__file__), 'cookies_3.txt'),
        os.path.join(os.path.dirname(__file__), 'cookies'),
    ]
    existing = [p for p in possible_cookie_paths if os.path.exists(p) and os.path.isfile(p)]
    if existing:
        try:
            import tempfile
            writable = os.path.join(tempfile.gettempdir(), 'yt_cookies.txt')
            shutil.copyfile(existing[0], writable)
            return writable
        except Exception:
            return existing[0]
    return None

def get_ydl_options(url=None):
    is_instagram = bool(url) and ('instagram.com' in url.lower() or 'instagr.am' in url.lower())
    is_threads = bool(url) and ('threads.com' in url.lower() or 'threads.net' in url.lower())

    opts = {
        'quiet': True,
        'no_warnings': True,
        'noplaylist': True,
        'nocheckcertificate': False,
        'extract_flat': False,
        'geo_bypass': True,
        'format': 'best',
        'extractor_args': {
            'tiktok': {
                'app_version': ['34.1.2'],
                'manifest_app_version': ['34.1.2']
            }
        },
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Sec-Fetch-Mode': 'navigate'
        }
    }

    # YouTube: Use mobile/VR clients (android_vr, android_pro, android_creator) by default.
    # On datacenter IPs (like Render), web clients trigger 'Sign in to confirm you're not a bot'.
    # Mobile/VR clients bypass Google Botguard challenges and do not require cookies.
    is_youtube = bool(url) and ('youtube.com' in url.lower() or 'youtu.be' in url.lower())
    if is_youtube:
        opts['extractor_args']['youtube'] = {
            'player_client': ['android_vr', 'android_pro', 'android_creator', 'tv_embedded']
        }
        logging.info("[YOUTUBE CONFIG] Applied anti-bot player clients: android_vr, android_pro, android_creator, tv_embedded")

    # Enable JS runtimes for YouTube signature / n-challenge solving (Deno on Render, Node locally)
    js_runtimes = {}
    deno_path = shutil.which('deno')
    node_path = shutil.which('node')
    if deno_path:
        js_runtimes['deno'] = {}
        logging.info(f"[JS_RUNTIME] Deno found at: {deno_path}")
    elif node_path:
        js_runtimes['node'] = {}
        logging.info(f"[JS_RUNTIME] Node found at: {node_path}")
    else:
        logging.warning("[JS_RUNTIME] No JS runtime found on PATH — YouTube n-challenge solving unavailable")
    if js_runtimes:
        opts['js_runtimes'] = js_runtimes

    # --- Instagram / Threads cookies ---
    # Instagram and Threads require a logged-in session on datacenter IPs to avoid 429.
    # Add a secret file named 'insta_cookies' on Render Environment → Secret Files.
    if is_instagram or is_threads:
        insta_cookie_paths = [
            '/etc/secrets/insta_cookies.txt',
            '/etc/secrets/insta_cookies',
            '/etc/secrets/insta_cookies_1.txt',
            '/etc/secrets/insta_cookies_1',
            os.path.join(os.path.dirname(__file__), 'insta_cookies.txt'),
            os.path.join(os.path.dirname(__file__), 'insta_cookies'),
        ]
        insta_cookie_file = next((p for p in insta_cookie_paths if os.path.isfile(p)), None)
        if insta_cookie_file:
            try:
                import tempfile
                temp_insta = os.path.join(tempfile.gettempdir(), 'insta_cookies.txt')
                shutil.copyfile(insta_cookie_file, temp_insta)
                opts['cookiefile'] = temp_insta
                logging.info(f"[COOKIES] Auto-loaded cookies for Instagram/Threads from: {insta_cookie_file}")
            except Exception as e:
                opts['cookiefile'] = insta_cookie_file
                logging.warning(f"[COOKIES] Using insta cookies directly: {e}")
        else:
            logging.warning("[COOKIES] No insta_cookies file found — Instagram/Threads may hit 429 on datacenter IPs")

    return opts

def extract_threads_direct(url, cookie_file=None):
    """
    Direct extraction for Threads posts (supports both threads.net and threads.com).
    Uses session cookies from insta_cookies to bypass rate limits and extract direct MP4 CDN URLs.
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Sec-Fetch-Site': 'none',
        }
        s = requests.Session()
        if cookie_file and os.path.exists(cookie_file):
            cookies = {}
            for line in open(cookie_file, 'r', encoding='utf-8', errors='ignore').read().splitlines():
                if line.startswith('.') or line.startswith('http'):
                    parts = line.split('\t')
                    if len(parts) >= 7:
                        cookies[parts[5]] = parts[6]
            s.cookies.update(cookies)

        r = s.get(url, headers=headers, allow_redirects=True, timeout=12)
        if r.status_code != 200:
            return None

        clean_text = r.text.replace(r'\/', '/').replace(r'\u0026', '&').replace('&amp;', '&')
        mp4s = re.findall(r'https://[^\s"\'<>\\]+?\.mp4[^\s"\'<>\\]*', clean_text)
        if not mp4s:
            return None

        unique_mp4s = list(dict.fromkeys(mp4s))
        title_m = re.findall(r'<meta property="og:title" content="([^"]+)"', r.text)
        desc_m = re.findall(r'<meta property="og:description" content="([^"]+)"', r.text)

        import html
        title = ""
        if desc_m:
            title = html.unescape(desc_m[0])
        elif title_m:
            title = html.unescape(title_m[0])
        else:
            title = "Threads Video"

        video_high = unique_mp4s[0]
        video_normal = unique_mp4s[-1] if len(unique_mp4s) > 1 else video_high

        return {
            "success": True,
            "title": title,
            "video_high": video_high,
            "video_normal": video_normal,
            "audio_high": video_high,
            "audio_normal": video_normal,
            "duration": 0,
            "type": "video",
            "platform": "threads"
        }
    except Exception as e:
        logging.warning(f"[THREADS DIRECT ERROR] {e}")
        return None

# ==========================================
# 🎯 ROUTE 1: UNIVERSAL EXTRACTION ENGINE 🎯
# ==========================================
@app.route('/api/download', methods=['GET'])
@limiter.limit("20 per minute")
def download_video():
    url = request.args.get('url')
    
    if not url:
        return jsonify({"success": False, "error": "URL is required!"}), 400

    if not is_safe_web_url(url):
        return jsonify({"success": False, "error": "Invalid or prohibited URL."}), 400

    resolved_url = resolve_short_url(url)
    if not is_safe_web_url(resolved_url):
        return jsonify({"success": False, "error": "Invalid or prohibited redirect destination."}), 400

    cached_data = video_cache.get(resolved_url)
    if cached_data:
        return jsonify(cached_data)

    ydl_opts = get_ydl_options(resolved_url)

    # Fast direct extraction for Threads (bypasses yt-dlp's lack of threads.com support)
    is_threads = bool(resolved_url) and ('threads.net' in resolved_url.lower() or 'threads.com' in resolved_url.lower())
    if is_threads:
        cookie_file = ydl_opts.get('cookiefile')
        threads_res = extract_threads_direct(resolved_url, cookie_file)
        if threads_res:
            logging.info(f"[THREADS SUCCESS] Extracted directly: {threads_res.get('title')[:30]}")
            video_cache.set(resolved_url, threads_res)
            return jsonify(threads_res)

    try:
        info = None
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                logging.info(f"[EXTRACTION START] Fetching metadata for: {resolved_url}")
                info = ydl.extract_info(resolved_url, download=False)
                if not info:
                    raise Exception("Empty metadata received from yt-dlp")

                # Sync TikTok session cookies into http_session for CDN streaming.
                is_tiktok_url = 'tiktok.com' in resolved_url.lower() or 'tiktok.com' in url.lower()
                if is_tiktok_url and hasattr(ydl, 'cookiejar') and ydl.cookiejar:
                    for c in ydl.cookiejar:
                        try:
                            http_session.cookies.set(c.name, c.value, domain='.tiktok.com', path='/')
                            http_session.cookies.set_cookie(c)
                        except Exception:
                            pass
        except Exception as first_extract_err:
            err_str = str(first_extract_err).lower()
            is_youtube = 'youtube.com' in resolved_url.lower() or 'youtu.be' in resolved_url.lower()
            is_threads = 'threads.net' in resolved_url.lower() or 'threads.com' in resolved_url.lower()
            post_m = re.search(r'/(?:post|share|t)/([A-Za-z0-9_\-]+)', resolved_url)

            # Fallback 1: YouTube retry logic
            if is_youtube:
                # 1a. If video explicitly requires login or is age-restricted, try with cookies
                if any(k in err_str for k in ['age', 'confirm your age', 'private', 'sign in to view', 'login']):
                    yt_cookie_file = get_youtube_cookie_file()
                    if yt_cookie_file:
                        logging.info(f"[YOUTUBE FALLBACK] Age-gate/login required. Retrying with cookies: {yt_cookie_file}")
                        try:
                            yt_fallback_opts = get_ydl_options(resolved_url)
                            yt_fallback_opts['cookiefile'] = yt_cookie_file
                            yt_fallback_opts['extractor_args']['youtube'] = {
                                'player_client': ['tv_downgraded', 'web_safari']
                            }
                            with yt_dlp.YoutubeDL(yt_fallback_opts) as fallback_ydl:
                                info = fallback_ydl.extract_info(resolved_url, download=False)
                        except Exception as yt_fb_err:
                            logging.warning(f"[YOUTUBE COOKIE FALLBACK FAILED] {yt_fb_err}")
                            raise first_extract_err
                    else:
                        raise first_extract_err
                else:
                    # 1b. If primary client encountered a temporary glitch, retry with secondary clients
                    logging.warning(f"[YOUTUBE FALLBACK] Primary extraction failed ({first_extract_err}). Retrying with tv_embedded/android fallback...")
                    try:
                        yt_fallback_opts = get_ydl_options(resolved_url)
                        yt_fallback_opts['extractor_args']['youtube'] = {
                            'player_client': ['tv_embedded', 'android']
                        }
                        with yt_dlp.YoutubeDL(yt_fallback_opts) as fallback_ydl:
                            info = fallback_ydl.extract_info(resolved_url, download=False)
                    except Exception as yt_fb_err:
                        logging.warning(f"[YOUTUBE FALLBACK FAILED] {yt_fb_err}")
                        raise first_extract_err
            # Fallback 2: Threads mapping to Instagram
            elif is_threads and post_m:
                post_id = post_m.group(1)
                ig_fallback_url = f"https://www.instagram.com/p/{post_id}/"
                logging.info(f"[THREADS FALLBACK] Trying Instagram mapping for Threads: {ig_fallback_url}")
                try:
                    ig_opts = get_ydl_options(ig_fallback_url)
                    with yt_dlp.YoutubeDL(ig_opts) as fallback_ydl:
                        info = fallback_ydl.extract_info(ig_fallback_url, download=False)
                except Exception as fb_err:
                    logging.warning(f"[THREADS FALLBACK FAILED] {fb_err}")
                    raise first_extract_err
            else:
                raise first_extract_err
        
        if not info:
            raise Exception("Empty metadata received from yt-dlp")

        media_type = "image" if info.get('_type') == 'url_transparent' and not info.get('formats') else "video"
        
        video_high = None
        video_normal = None
        audio_high = None
        audio_normal = None

        formats = info.get('formats', [])

        if formats:
            # 1. Complete progressive video formats (contain BOTH video and audio)
            # A format has video and audio if:
            # - It has a direct URL
            # - Its extension is a video format (mp4, webm, mov, mkv)
            # - Its video codec is NOT 'none' and resolution is NOT 'audio only'
            # - Its audio codec is NOT 'none' (literal string 'none' means silent stream)
            # - Its format_note is NOT 'DASH video' (which is video-only)
            complete_video_formats = [
                f for f in formats 
                if f.get('url')
                and f.get('vcodec') != 'none' 
                and f.get('acodec') != 'none'
                and f.get('ext') in ['mp4', 'webm', 'mkv', 'mov']
                and f.get('resolution') != 'audio only'
                and (f.get('format_note') or '') != 'DASH video'
            ]
            
            # 2. Audio-only formats (for dedicated audio extraction)
            audio_only_formats = [
                f for f in formats 
                if (f.get('vcodec') == 'none' or f.get('resolution') == 'audio only')
                and f.get('acodec') and f.get('acodec') != 'none'
                and f.get('url')
            ]
            
            # 3. Any format containing audio (fallback for audio extraction)
            any_audio_formats = [
                f for f in formats 
                if f.get('acodec') and f.get('acodec') != 'none'
                and f.get('url')
            ]

            # 4. Fallback video-only streams (ONLY used if NO stream with audio exists anywhere)
            silent_video_formats = [
                f for f in formats 
                if f.get('url')
                and f.get('vcodec') != 'none'
                and f.get('ext') in ['mp4', 'webm', 'mkv', 'mov']
                and f.get('resolution') != 'audio only'
            ]

            # Map Video High & Normal
            if complete_video_formats:
                sorted_videos = sorted(
                    complete_video_formats,
                    key=lambda x: (x.get('height') or 0, x.get('tbr') or 0, x.get('filesize') or 0),
                    reverse=True
                )
                video_high = sorted_videos[0].get('url')
                video_normal = sorted_videos[-1].get('url') if len(sorted_videos) > 1 else video_high
            elif info.get('url'):
                video_high = info.get('url')
                video_normal = info.get('url')
            elif silent_video_formats:
                sorted_videos = sorted(
                    silent_video_formats,
                    key=lambda x: (x.get('height') or 0, x.get('tbr') or 0, x.get('filesize') or 0),
                    reverse=True
                )
                video_high = sorted_videos[0].get('url')
                video_normal = sorted_videos[-1].get('url') if len(sorted_videos) > 1 else video_high
            else:
                video_high = info.get('url')
                video_normal = info.get('url')

            # Map Audio High & Normal
            if audio_only_formats:
                sorted_audios = sorted(
                    audio_only_formats,
                    key=lambda x: (x.get('abr') or 0, x.get('filesize') or 0, x.get('tbr') or 0),
                    reverse=True
                )
                audio_high = sorted_audios[0].get('url')
                audio_normal = sorted_audios[-1].get('url') if len(sorted_audios) > 1 else audio_high
            elif any_audio_formats:
                sorted_audios = sorted(
                    any_audio_formats,
                    key=lambda x: (x.get('abr') or 0, x.get('tbr') or 0),
                    reverse=True
                )
                audio_high = sorted_audios[0].get('url')
                audio_normal = sorted_audios[-1].get('url') if len(sorted_audios) > 1 else audio_high
            elif complete_video_formats:
                audio_high = complete_video_formats[0].get('url')
                audio_normal = complete_video_formats[-1].get('url')
            else:
                audio_high = video_high
                audio_normal = video_normal
        else:
            # Direct single media URL fallback
            direct_url = info.get('url')
            video_high = direct_url
            video_normal = direct_url
            audio_high = direct_url
            audio_normal = direct_url

        # Ensure fallbacks if any field is still None
        video_high = video_high or video_normal or info.get('url')
        video_normal = video_normal or video_high or info.get('url')
        audio_high = audio_high or video_high
        audio_normal = audio_normal or audio_high

        response_data = {
            "success": True,
            "type": media_type,
            "title": info.get('title', 'Social Media Video'),
            "thumbnail": info.get('thumbnail', ''),
            "duration": info.get('duration', 0),
            "video_high": video_high,
            "video_normal": video_normal,
            "audio_high": audio_high,
            "audio_normal": audio_normal
        }

        video_cache.set(resolved_url, response_data)
        logging.info(f"[EXTRACTION SUCCESS] '{response_data['title'][:40]}' successfully mapped.")
        return jsonify(response_data)

    except yt_dlp.utils.DownloadError as de:
        logging.error(f"[EXTRACTION ERROR] yt-dlp error: {str(de)}")
        return jsonify({
            "success": False, 
            "error": "Could not extract video. It might be private, deleted, or require login.",
            "details": str(de)
        }), 400
    except Exception as e:
        error_msg = str(e)
        logging.error(f"[SERVER ERROR] Unexpected error: {error_msg}")
        return jsonify({"success": False, "error": "Could not process this video link. Please verify the URL and try again."}), 500

# ==========================================
# ⚡ ROUTE 2: ADVANCED STREAMING PROXY & MP3 CONVERTER ⚡
# ==========================================
ALLOWED_FILE_TYPES = {'mp4', 'mp3', 'audio', 'jpg', 'jpeg', 'png', 'webp'}

@app.route('/api/direct', methods=['GET'])
@limiter.limit("25 per minute")
def direct_download():
    file_url = request.args.get('url')
    file_type = (request.args.get('type', 'mp4') or 'mp4').lower().strip()
    quality = (request.args.get('q', 'hq') or 'hq').lower().strip()
    raw_timestamp = request.args.get('t', str(int(time.time())))
    timestamp_id = re.sub(r'[^0-9]', '', str(raw_timestamp)) or str(int(time.time()))

    # 1. Parameter allow-list validation
    if file_type not in ALLOWED_FILE_TYPES:
        return jsonify({"error": "Unsupported file type requested."}), 400

    # 2. Strict Anti-SSRF Media URL validation
    if not file_url or not is_safe_media_url(file_url):
        return jsonify({"error": "Invalid or unauthorized media stream URL."}), 400

    raw_prefix = get_platform_prefix(file_url)
    prefix = re.sub(r'[^a-zA-Z0-9_-]', '', raw_prefix) or 'Downsocial'

    # --- MP3 AUDIO EXTRACTION & CONVERSION ---
    if file_type in ['mp3', 'audio']:
        try:
            ffmpeg_bin = get_ffmpeg_path()
            bitrate = '192k' if quality == 'hq' else '128k'
            
            headers = get_platform_request_headers(file_url)

            cmd = [
                ffmpeg_bin,
                '-y',
                '-loglevel', 'error',
                '-i', 'pipe:0',
                '-vn',
                '-acodec', 'libmp3lame',
                '-b:a', bitrate,
                '-f', 'mp3',
                'pipe:1'
            ]

            proc = subprocess.Popen(
                cmd,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                bufsize=1024 * 1024
            )

            def feed_ffmpeg():
                try:
                    upstream_req = http_session.get(file_url, stream=True, headers=headers, timeout=(5, 30))
                    for chunk in upstream_req.iter_content(chunk_size=64 * 1024):
                        if chunk:
                            try:
                                proc.stdin.write(chunk)
                                proc.stdin.flush()
                            except (BrokenPipeError, OSError):
                                break
                    upstream_req.close()
                except Exception as feed_err:
                    logging.error(f"[FFMPEG FEED ERROR] {str(feed_err)}")
                finally:
                    try:
                        proc.stdin.close()
                    except Exception:
                        pass

            feeder_thread = threading.Thread(target=feed_ffmpeg, daemon=True)
            feeder_thread.start()

            def generate_mp3_chunks():
                try:
                    while True:
                        chunk = proc.stdout.read(64 * 1024)
                        if not chunk:
                            break
                        yield chunk
                except Exception as stream_err:
                    logging.error(f"[MP3 STREAM ERROR] {str(stream_err)}")
                finally:
                    try:
                        proc.kill()
                    except Exception:
                        pass
                    try:
                        proc.stdout.close()
                        proc.stderr.close()
                    except Exception:
                        pass
                    feeder_thread.join(timeout=2)
                    logging.info("[MP3 STREAM] Finished and cleaned up FFmpeg process")

            resp_headers = {
                'Content-Disposition': f'attachment; filename="{prefix}_Audio_{timestamp_id}.mp3"',
                'Cache-Control': 'no-cache',
                'Accept-Ranges': 'none'
            }

            return Response(
                stream_with_context(generate_mp3_chunks()),
                status=200,
                content_type='audio/mpeg',
                headers=resp_headers
            )

        except Exception as e:
            logging.error(f"[MP3 CONVERSION ERROR] {str(e)}")
            return jsonify({"error": "Failed to convert audio to MP3."}), 500

    # --- STANDARD VIDEO/IMAGE STREAMING PROXY ---
    try:
        range_header = request.headers.get('Range', None)
        extra_h = {'Range': range_header} if range_header else None
        headers = get_platform_request_headers(file_url, extra_headers=extra_h)

        req = http_session.get(file_url, stream=True, headers=headers, timeout=(5, 30))
        
        # 1. Upstream Error Handling (reject upstream 403, 404, etc.)
        if req.status_code not in (200, 206):
            req.close()
            logging.error(f"[PROXY UPSTREAM ERROR] Status {req.status_code} for {file_url}")
            return jsonify({"error": "Media source rejected the request (upstream error)."}), 502

        # 2. Content-Length & Content-Type Validation (prevent streaming 510-byte corrupt error pages)
        content_type = req.headers.get('content-type', '').lower()
        content_length_str = req.headers.get('Content-Length', '0')
        try:
            content_length = int(content_length_str)
        except ValueError:
            content_length = 0

        if file_type in ['mp4', 'webm', 'mov', 'video']:
            if 'text/html' in content_type or (0 < content_length < 50000):
                req.close()
                logging.error(f"[PROXY CORRUPT STREAM] Rejected small/HTML response (len: {content_length}, type: {content_type}) for {file_url}")
                return jsonify({"error": "Media source returned invalid or blocked stream from CDN."}), 502

        type_tag = 'Image' if file_type in ['jpg', 'jpeg', 'png', 'webp'] else 'Video'
        resp_headers = {
            'Content-Disposition': f'attachment; filename="{prefix}_{type_tag}_{timestamp_id}.{file_type}"',
            'Accept-Ranges': 'bytes'
        }

        if 'Content-Length' in req.headers:
            resp_headers['Content-Length'] = req.headers['Content-Length']
            
        if 'Content-Range' in req.headers:
            resp_headers['Content-Range'] = req.headers['Content-Range']

        status_code = req.status_code

        def generate_chunks():
            try:
                for chunk in req.iter_content(chunk_size=1024 * 1024):
                    if chunk:
                        yield chunk
            except Exception as stream_err:
                logging.error(f"[STREAM ERROR] Connection dropped: {str(stream_err)}")
            finally:
                req.close()
                logging.info("[PROXY STREAM] Closed downstream connection")

        fallback_mime = 'image/jpeg' if file_type in ['jpg', 'jpeg'] else f'video/{file_type}'
        return Response(
            stream_with_context(generate_chunks()), 
            status=status_code,
            content_type=req.headers.get('content-type', fallback_mime),
            headers=resp_headers
        )
        
    except requests.exceptions.Timeout:
        logging.warning("[PROXY TIMEOUT] Target server took too long.")
        return jsonify({"error": "Request timed out. Target server is too slow."}), 504
    except requests.exceptions.RequestException as req_err:
        logging.error(f"[PROXY ERROR] Request failed: {str(req_err)}")
        return jsonify({"error": "Failed to connect to media server."}), 502
    except Exception as e:
        logging.error(f"[PROXY UNKNOWN ERROR] {str(e)}")
        return jsonify({"error": "An unexpected error occurred during stream."}), 500

@app.route('/', methods=['GET'])
def health_check():
    return jsonify({"status": "active", "service": "downsocial - All-in-One Video Downloader API v3.0", "version": "3.1.4-yt-android-vr"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
