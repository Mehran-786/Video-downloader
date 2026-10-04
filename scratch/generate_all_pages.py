import os
import html

BASE_DIR = r'c:\my folder\Pictures\Desktop\downsocial\frontend'

PLATFORM_CONFIGS = {
    'facebook-downloader': {
        'folder': 'facebook-downloader',
        'key': 'facebook',
        'name': 'Facebook',
        'icon_class': 'fab fa-facebook',
        'color': '#1877F2',
        'accent_badge': 'badge-facebook',
        'meta_title': 'Facebook Video Downloader HD — Download FB Videos, Reels & Stories Free | downsocial',
        'meta_desc': 'Free online Facebook video downloader in 1080p Full HD, 2K & 4K. Download Facebook Reels, Watch videos, stories & convert FB to MP3 with no watermark. Fast & safe.',
        'meta_keywords': 'facebook video downloader, download facebook video, fb video download, facebook reel downloader, fb reel download, download facebook stories, facebook watch downloader, facebook to mp3, fdown alternative, snapsave facebook, savefrom facebook, download fb video online',
        'hero_title': 'Download Facebook Videos in HD',
        'hero_subtitle': 'Free, fast, and without watermarks. Download FB Reels, Stories, Watch & Live videos in 1080p, 2K & 4K MP4 or convert to MP3 audio.',
        'input_placeholder': 'Paste Facebook video, Reel, or Story link here (e.g. https://www.facebook.com/watch?v=...)...',
        'cta_text': 'Download Facebook Video',
        'competitors': 'FDown, SnapSave, SaveFrom',
        'features_cards': [
            {'title': 'Facebook Reels Downloader', 'icon': 'fas fa-film', 'desc': 'Extract and save Facebook Reels in pristine 1080p Full HD quality with original audio tracks and zero compression.'},
            {'title': 'Facebook Stories Saver', 'icon': 'fas fa-history', 'desc': 'Backup ephemeral 24-hour Facebook Stories before they expire. Save video and photo stories directly to your phone or PC.'},
            {'title': 'Facebook to MP3 Converter', 'icon': 'fas fa-music', 'desc': 'Extract pure audio streams from Facebook speeches, music performances, and podcasts in crystal clear 192kbps or 320kbps MP3.'},
            {'title': 'Zero Watermark or Logo', 'icon': 'fas fa-check-double', 'desc': 'Get clean, unbranded video files without any added watermarks, lower thirds, or intrusive website stamps.'},
            {'title': 'Private & Group Video Support', 'icon': 'fas fa-users', 'desc': 'Download shared videos from public groups, pages, creator profiles, and feed posts effortlessly.'},
            {'title': 'Lightning-Fast Direct CDN', 'icon': 'fas fa-bolt', 'desc': 'Direct streaming connection to Facebook CDN servers ensures ultra-fast downloads without server buffering.'}
        ],
        'specs': [
            ('Supported Media Types', 'Facebook Reels, Watch Videos, 24h Stories, Public Group Videos, Live Stream Recordings'),
            ('Video Output Formats', 'MP4 (1080p Full HD, 720p HD, 480p SD, 2K & 4K where available)'),
            ('Audio Output Formats', 'MP3 High Quality (192kbps / 320kbps Stereo)'),
            ('Watermark Policy', '100% Clean — Zero Added Watermarks or Brand Overlays'),
            ('Platform Compatibility', 'iOS (Safari), Android (Chrome), Windows, macOS, Linux, iPadOS'),
            ('Account Requirement', 'No Login Required — Completely Anonymous & Free')
        ]
    },
    'instagram-downloader': {
        'folder': 'instagram-downloader',
        'key': 'instagram',
        'name': 'Instagram',
        'icon_class': 'fab fa-instagram',
        'color': '#E4405F',
        'accent_badge': 'badge-instagram',
        'meta_title': 'Instagram Reels Downloader HD — Save IG Reels, Stories & Posts Free | downsocial',
        'meta_desc': 'Free Instagram video downloader. Download Instagram Reels, Stories, Photos & Carousel posts in original 1080p HD without watermark. Fast online IG downloader.',
        'meta_keywords': 'instagram reels downloader, save instagram posts, download instagram stories, instagram video downloader, ig reels download, instagram video without watermark, ig story saver, snapinsta alternative, igram alternative, download instagram audio mp3',
        'hero_title': 'Download Instagram Reels & Stories HD',
        'hero_subtitle': 'Save Instagram Reels, Stories, Photos & Carousel posts in original high resolution with crystal clear audio and zero watermarks.',
        'input_placeholder': 'Paste Instagram Reel, Story, or Post link here (e.g. https://www.instagram.com/reel/...)...',
        'cta_text': 'Download Instagram Media',
        'competitors': 'SnapInsta, iGram, SaveInsta',
        'features_cards': [
            {'title': 'Instagram Reels in 1080p', 'icon': 'fas fa-video', 'desc': 'Download trending Instagram Reels with original high-bitrate audio and crystal clear video definition.'},
            {'title': 'Stories & Highlights Archiver', 'icon': 'fas fa-clock', 'desc': 'Save ephemeral 24-hour Instagram Stories and creator Highlights permanently before they disappear forever.'},
            {'title': 'Carousel Album Unpacker', 'icon': 'fas fa-images', 'desc': 'Effortlessly extract all photos and videos contained in multi-slide Instagram carousel posts.'},
            {'title': 'High-Res Photo Downloader', 'icon': 'fas fa-camera', 'desc': 'Download full-resolution Instagram feed photos, portrait shots, and square photos in original JPEG format.'},
            {'title': 'Instagram Audio to MP3', 'icon': 'fas fa-headphones', 'desc': 'Extract viral background music, voiceovers, and original audio tracks from any Reel as high-fidelity MP3.'},
            {'title': 'No Account Connection', 'icon': 'fas fa-shield-alt', 'desc': 'Safe and secure with zero login required. We never request your Instagram username, password, or cookies.'}
        ],
        'specs': [
            ('Supported Media Types', 'Instagram Reels, Stories, Highlights, Feed Posts, Carousel Multi-Media, IGTV'),
            ('Video Output Formats', 'MP4 (1080p Full HD, 720p HD, 60FPS original bitrate)'),
            ('Audio Output Formats', 'MP3 Audio (192kbps HQ / Normal MP3)'),
            ('Image Output Formats', 'Original JPEG / WebP High Resolution'),
            ('Platform Compatibility', 'iPhone (iOS Safari), Android (Chrome, Firefox), Mac, PC, Tablets'),
            ('Privacy & Security', 'Zero Account Login — 100% Anonymous Stream Extraction')
        ]
    },
    'tiktok-downloader': {
        'folder': 'tiktok-downloader',
        'key': 'tiktok',
        'name': 'TikTok',
        'icon_class': 'fab fa-tiktok',
        'color': '#00f2fe',
        'accent_badge': 'badge-tiktok',
        'meta_title': 'TikTok Video Downloader Without Watermark — Save HD TikToks Free | downsocial',
        'meta_desc': 'Download TikTok videos without watermark in Full HD MP4. Extract trending TikTok music and audio as MP3. Free, fast, unlimited TikTok saver for mobile & desktop.',
        'meta_keywords': 'tiktok downloader no watermark, tiktok video saver, download tiktok without watermark, tiktok to mp3, tiktok music extractor, save tiktok sounds, snaptik alternative, ssstik alternative, tiktok slideshow downloader, download tiktok hd 1080p',
        'hero_title': 'Download TikTok Videos Without Watermark',
        'hero_subtitle': 'Automatic watermark removal, trending MP3 music extraction & crystal-clear 1080p 60FPS video downloads. Fast, free and unlimited.',
        'input_placeholder': 'Paste TikTok video link here (e.g. https://www.tiktok.com/@user/video/... or vt.tiktok.com/...)...',
        'cta_text': 'Download TikTok Video',
        'competitors': 'SnapTik, SSSTik, TikMate',
        'features_cards': [
            {'title': '100% Watermark Free', 'icon': 'fas fa-magic', 'desc': 'Clean, unbranded TikTok videos with the bouncing watermark logo completely removed.'},
            {'title': 'Trending Sounds to MP3', 'icon': 'fas fa-music', 'desc': 'Extract viral TikTok sounds, speech clips, and trending songs directly as high-bitrate MP3 audio.'},
            {'title': 'Photo Slideshow Saver', 'icon': 'fas fa-clone', 'desc': 'Download multi-slide TikTok photo carousels and slideshows alongside their background audio track.'},
            {'title': 'Full 60FPS HD Quality', 'icon': 'fas fa-tachometer-alt', 'desc': 'Preserve original high frame rates and sharp 1080p resolution with zero compression artifacts.'},
            {'title': 'Short Links Supported', 'icon': 'fas fa-link', 'desc': 'Seamlessly handles both mobile app short links (vt.tiktok.com) and full desktop browser URLs.'},
            {'title': 'Works on iOS & Android', 'icon': 'fas fa-mobile-alt', 'desc': 'Save directly to your iPhone Camera Roll or Android Gallery without installing sketchy third-party apps.'}
        ],
        'specs': [
            ('Supported Media Types', 'Standard TikTok Videos, Duets, Stitches, Photo Slideshows, Trending Sounds'),
            ('Video Output Formats', 'MP4 (1080p HD, 720p, 60FPS Without Watermark)'),
            ('Audio Output Formats', 'MP3 Audio (192kbps / 320kbps Pure Sound)'),
            ('Watermark Removal', 'Automatic Server-Side Stream De-branding'),
            ('Supported Link Formats', 'tiktok.com/@user/video/..., vt.tiktok.com/..., vm.tiktok.com/...'),
            ('Device Compatibility', 'All Devices: iPhone, iPad, Android Phones, Mac, Windows, Linux')
        ]
    },
    'youtube-downloader': {
        'folder': 'youtube-downloader',
        'key': 'youtube',
        'name': 'YouTube',
        'icon_class': 'fab fa-youtube',
        'color': '#FF0000',
        'accent_badge': 'badge-youtube',
        'meta_title': 'YouTube Video Downloader 4K — Download YT Videos & Shorts Free | downsocial',
        'meta_desc': 'Free YouTube video downloader and MP3 audio converter. Download YouTube Shorts, 1080p Full HD, 2K & 4K Ultra HD MP4 videos with no ads or software required.',
        'meta_keywords': 'youtube video downloader, youtube downloader 4k, download youtube videos in 4k, youtube shorts downloader, youtube music converter mp3, youtube to mp4 1080p, y2mate alternative, savefrom youtube, clipconverter alternative, free youtube video download online',
        'hero_title': 'Download YouTube Videos & Shorts in 4K',
        'hero_subtitle': 'Ultra-fast YouTube video downloader & MP3 converter. Download YouTube Shorts, 1080p Full HD, 2K, 4K & 8K MP4 free without ads or limits.',
        'input_placeholder': 'Paste YouTube video or Shorts link here (e.g. https://www.youtube.com/watch?v=... or youtu.be/...)...',
        'cta_text': 'Download YouTube Video',
        'competitors': 'Y2Mate, SaveFrom, ClipConverter',
        'features_cards': [
            {'title': '4K & 8K Ultra HD Support', 'icon': 'fas fa-tv', 'desc': 'Enjoy the pinnacle of video fidelity with full support for 1080p Full HD, 1440p 2K, and 2160p 4K streams.'},
            {'title': 'YouTube Shorts Downloader', 'icon': 'fas fa-bolt', 'desc': 'Instant 1-click download for YouTube Shorts in vertical 9:16 aspect ratio with original stereo audio.'},
            {'title': 'YouTube to MP3 (320kbps)', 'icon': 'fas fa-music', 'desc': 'Convert music videos, podcasts, and interviews into high-fidelity 320kbps MP3 audio with instant conversion.'},
            {'title': 'Smart Stream Muxing', 'icon': 'fas fa-cogs', 'desc': 'High-performance server muxing seamlessly combines separate adaptive audio and video streams with zero desync.'},
            {'title': 'Zero Ads or Popups', 'icon': 'fas fa-ban', 'desc': 'Clean, safe, and modern UI. No malicious redirects, no popup spam, and zero deceptive download buttons.'},
            {'title': 'Unlimited Free Downloads', 'icon': 'fas fa-infinity', 'desc': 'No daily quotas or length caps. Download videos of any duration completely free and without registration.'}
        ],
        'specs': [
            ('Supported Media Types', 'Standard YouTube Videos, YouTube Shorts, Live Stream Replays, Music Clips'),
            ('Video Output Formats', 'MP4 (4K 2160p, 2K 1440p, 1080p Full HD, 720p, 480p)'),
            ('Audio Output Formats', 'MP3 Audio (192kbps / 320kbps High Fidelity)'),
            ('Audio-Video Sync', 'Real-Time FFmpeg Muxing with Perfect Lip Sync'),
            ('Supported Link Formats', 'youtube.com/watch?v=..., youtu.be/..., youtube.com/shorts/...'),
            ('Platform Compatibility', 'Web-Based — iOS, Android, macOS, Windows, Linux, Smart TVs')
        ]
    },
    'snapchat-downloader': {
        'folder': 'snapchat-downloader',
        'key': 'snapchat',
        'name': 'Snapchat',
        'icon_class': 'fab fa-snapchat',
        'color': '#FFFC00',
        'accent_badge': 'badge-snapchat',
        'meta_title': 'Snapchat Video Downloader — Save Spotlight Videos & Stories | downsocial',
        'meta_desc': 'Free Snapchat video downloader. Save Snapchat Spotlight clips, public Stories & Memories in full vertical 9:16 HD before they expire. Fast & anonymous.',
        'meta_keywords': 'snapchat video downloader, download snapchat stories, snapchat story saver, snapchat spotlight saver, save snapchat videos, snapchat memory backup tool, download snapchat videos before they expire, snapchat spotlight downloader hd',
        'hero_title': 'Download Snapchat Spotlight & Stories',
        'hero_subtitle': 'Save Snapchat Spotlight vertical videos, public Stories & Memories in full 9:16 HD before they expire. Fast, private, and 100% free.',
        'input_placeholder': 'Paste Snapchat Spotlight or Story link here (e.g. https://www.snapchat.com/t/... or story link)...',
        'cta_text': 'Download Snapchat Video',
        'competitors': 'Generic Online Savers',
        'features_cards': [
            {'title': 'Snapchat Spotlight in 1080p', 'icon': 'fas fa-fire', 'desc': 'Download trending viral Spotlight clips in full 9:16 vertical resolution with crystal-clear audio.'},
            {'title': 'Save Stories Before Expiry', 'icon': 'fas fa-hourglass-half', 'desc': 'Archive public friend and creator Stories permanently before the 24-hour expiration timer runs out.'},
            {'title': 'Discover Publisher Clips', 'icon': 'fas fa-newspaper', 'desc': 'Download high-production Discover shows, creator series, and publisher highlights effortlessly.'},
            {'title': 'Clean Output Without UI', 'icon': 'fas fa-crop', 'desc': 'Saves clean video files without Snapchat buttons, icons, or interface elements cluttering the view.'},
            {'title': 'Anonymous Saving', 'icon': 'fas fa-user-secret', 'desc': 'Creators are never notified when you download a video. No screenshot warnings or alerts are triggered.'},
            {'title': 'Instant Mobile Downloads', 'icon': 'fas fa-mobile', 'desc': 'Save directly into iPhone Files/Photos or Android Gallery with a single tap in your web browser.'}
        ],
        'specs': [
            ('Supported Media Types', 'Snapchat Spotlight Clips, Public Stories, Discover Shows, Publisher Clips'),
            ('Video Output Formats', 'MP4 (Full Vertical 9:16 1080p / 720p HD)'),
            ('Audio Output Formats', 'Original Stereo Audio Track (MP4 / MP3)'),
            ('Notification Policy', '100% Silent — No Screenshot or Download Notification Sent'),
            ('Supported Link Formats', 'snapchat.com/t/..., snapchat.com/spotlight/..., snapchat.com/add/...'),
            ('Device Compatibility', 'iPhone, Android, Windows, Mac, iPad')
        ]
    },
    'threads-downloader': {
        'folder': 'threads-downloader',
        'key': 'threads',
        'name': 'Threads',
        'icon_class': 'fas fa-at',
        'color': '#ffffff',
        'accent_badge': 'badge-threads',
        'meta_title': 'Threads Video Downloader HD — Save Meta Threads Posts & Videos | downsocial',
        'meta_desc': 'The first specialized Meta Threads downloader. Download Threads videos, quote posts, multi-photo carousels & audio in high definition. 100% free and fast.',
        'meta_keywords': 'threads video downloader, save threads posts, meta threads downloader, threads content backup tool, download threads videos hd, save meta threads conversations, threads to mp4, threads photo download, threads video download online',
        'hero_title': 'Download Threads Videos & Posts HD',
        'hero_subtitle': 'The first specialized Meta Threads downloader. Save Threads videos, quote posts, carousels & conversations in HD without login.',
        'input_placeholder': 'Paste Threads post link here (e.g. https://www.threads.net/@user/post/...)...',
        'cta_text': 'Download Threads Media',
        'competitors': 'First-to-Market Solution',
        'features_cards': [
            {'title': 'Threads Video Extraction', 'icon': 'fas fa-play-circle', 'desc': 'Save high-bitrate Meta Threads video posts in crisp 1080p Full HD with synchronized stereo audio.'},
            {'title': 'Multi-Image Albums', 'icon': 'fas fa-images', 'desc': 'Download entire multi-slide photo carousels from Threads posts in original uncompressed quality.'},
            {'title': 'Quote-Thread Captures', 'icon': 'fas fa-quote-right', 'desc': 'Preserve quote-thread discussion clips, nested replies, and viral reaction videos effortlessly.'},
            {'title': 'Offline Conversation Archival', 'icon': 'fas fa-archive', 'desc': 'Archive important creator insights, news updates, and memorable community threads offline.'},
            {'title': 'Meta URL Compatibility', 'icon': 'fas fa-check-circle', 'desc': 'Fully compatible with all official Threads app share links and desktop web URLs.'},
            {'title': 'Zero Tracking or Profiling', 'icon': 'fas fa-shield-alt', 'desc': 'Complete user privacy. No Meta account login, zero tracking cookies, and zero server logging.'}
        ],
        'specs': [
            ('Supported Media Types', 'Threads Videos, Multi-Photo Albums, Quote Threads, Reply Clips'),
            ('Video Output Formats', 'MP4 (1080p Full HD, Original Meta Stream Bitrate)'),
            ('Image Output Formats', 'Full Resolution JPEG / WebP'),
            ('Audio Output Formats', 'MP3 Audio (192kbps Stereo)'),
            ('Supported Link Formats', 'threads.net/@user/post/..., threads.net/t/...'),
            ('Device Compatibility', 'All Modern Web Browsers on Mobile, Tablet & Desktop')
        ]
    },
    'universal-downloader': {
        'folder': 'universal-downloader',
        'key': 'universal',
        'name': 'Universal',
        'icon_class': 'fas fa-globe',
        'color': '#818cf8',
        'accent_badge': 'badge-universal',
        'meta_title': 'All-in-One Video Downloader HD — Download from Any Social Media | downsocial',
        'meta_desc': 'Universal online video downloader for Facebook, Instagram, TikTok, YouTube, Snapchat & Threads. Fast, free, and no watermark. High quality MP4 & MP3.',
        'meta_keywords': 'all in one video downloader, multi platform downloader, download videos from any social media, universal video saver, best multi-platform downloader, social media video downloader, free online video downloader, convert video to mp3',
        'hero_title': 'All-in-One Social Media Video Downloader',
        'hero_subtitle': 'One universal tool for Facebook, Instagram, TikTok, YouTube, Snapchat & Threads. Fast, free & HD with no watermarks or login required.',
        'input_placeholder': 'Paste any social media link here (Facebook, Instagram, TikTok, YouTube, Snapchat, Threads)...',
        'cta_text': 'Download Video',
        'competitors': 'Fragmented Single-Site Downloaders',
        'features_cards': [
            {'title': 'Smart Auto-Detection', 'icon': 'fas fa-brain', 'desc': 'Automatically identifies the platform from any pasted link without requiring manual selection.'},
            {'title': '6+ Major Platforms Supported', 'icon': 'fas fa-cubes', 'desc': 'Complete coverage for Facebook, Instagram, TikTok, YouTube, Snapchat, and Meta Threads in one hub.'},
            {'title': 'Crystal Clear HD & 4K', 'icon': 'fas fa-tv', 'desc': 'Download videos in their highest native resolution up to 4K Ultra HD with original audio tracks.'},
            {'title': 'Universal MP3 Audio Ripper', 'icon': 'fas fa-headphones', 'desc': 'Convert video streams from any supported social network into clean 192kbps or 320kbps MP3 audio.'},
            {'title': 'Interactive Brand Orbit', 'icon': 'fas fa-compass', 'desc': 'Seamlessly navigate between dedicated platform tools with our interactive radial tool navigator.'},
            {'title': '100% Free & Anonymous', 'icon': 'fas fa-user-shield', 'desc': 'Unlimited downloads with zero fees, no accounts, no subscriptions, and complete zero-log privacy.'}
        ],
        'specs': [
            ('Supported Platforms', 'Facebook, Instagram, TikTok, YouTube, Snapchat, Meta Threads (More Coming Soon)'),
            ('Video Formats & Quality', 'MP4 (4K, 2K, 1080p Full HD, 720p HD, 480p SD, 60FPS)'),
            ('Audio Formats & Quality', 'MP3 Audio (192kbps HQ / 320kbps High Fidelity Stereo)'),
            ('Watermark Policy', 'Zero Added Watermarks — Automatic TikTok Watermark Removal'),
            ('Auto-Detection Engine', 'Instant Server-Side URL Regex & Parser Optimization'),
            ('Platform Compatibility', 'Universal — iOS Safari, Android Chrome, Windows, macOS, Linux')
        ]
    }
}

ALL_PLATFORM_LINKS = [
    ('facebook-downloader', 'Facebook', 'fab fa-facebook', 'fb-pill'),
    ('instagram-downloader', 'Instagram', 'fab fa-instagram', 'ig-pill'),
    ('tiktok-downloader', 'TikTok', 'fab fa-tiktok', 'tt-pill'),
    ('youtube-downloader', 'YouTube', 'fab fa-youtube', 'yt-pill'),
    ('snapchat-downloader', 'Snapchat', 'fab fa-snapchat', 'snap-pill'),
    ('threads-downloader', 'Threads', 'fas fa-at', 'th-pill'),
    ('universal-downloader', 'Universal', 'fas fa-globe', 'active')
]

def render_nav(cfg, active_page='index'):
    p_name = cfg['name']
    p_folder = cfg['folder']
    
    # Platform dropdown items
    p_dropdown = "".join([
        f'<li><a href="../{folder}/index.html"><i class="{icon}"></i> {name} Downloader</a></li>\n'
        for folder, name, icon, _ in ALL_PLATFORM_LINKS
    ])
    
    return f'''
<nav class="top-nav desktop-nav">
    <div class="nav-brand-container">
        <a href="index.html" class="nav-brand">
            <img src="../shared/icon-nav.webp" alt="downsocial Logo" width="44" height="44" fetchpriority="high">
            <span>downsocial<span class="domain-ext">.net</span></span>
        </a>
        <a href="index.html" class="nav-brand-home"><i class="fas fa-arrow-left"></i> <span>Home</span></a>
    </div>
    
    <ul class="nav-links">
        <li class="dropdown">
            <a href="#" id="platformToggle"><i class="{cfg['icon_class']}"></i> <span>{p_name}</span> <i class="fas fa-caret-down"></i></a>
            <ul class="dropdown-menu" id="platformMenu">
                {p_dropdown}
            </ul>
        </li>
        <li><a href="features.html"><i class="fas fa-star"></i> <span data-key="navigation.features">Features</span></a></li>
        <li><a href="about.html"><i class="fas fa-info-circle"></i> <span data-key="navigation.about">About</span></a></li>
        <li><a href="contact.html"><i class="fas fa-envelope"></i> <span data-key="navigation.contact">Contact</span></a></li>
        
        <li class="theme-switcher-wrapper">
            <div class="theme-segmented-control" data-theme-switcher>
                <div class="theme-pill"></div>
                <button type="button" class="theme-btn" data-theme-val="premium" aria-label="Premium Mode" title="Premium Mode">
                    <i class="fas fa-crown"></i> <span>Premium</span>
                </button>
                <button type="button" class="theme-btn active" data-theme-val="dark" aria-label="Dark Mode" title="Dark Mode">
                    <i class="fas fa-moon"></i> <span>Dark</span>
                </button>
                <button type="button" class="theme-btn" data-theme-val="light" aria-label="Light Mode" title="Light Mode">
                    <i class="fas fa-sun"></i> <span>Light</span>
                </button>
            </div>
        </li>
        
        <li class="dropdown">
            <a href="#" id="desktopLangToggle"><i class="fas fa-globe"></i> <span data-key="common.langBtn">Language</span> <i class="fas fa-caret-down"></i></a>
            <ul class="dropdown-menu" id="desktopLangMenu">
                <li><a href="#" onclick="changeLanguage('en')">English</a></li>
                <li><a href="#" onclick="changeLanguage('es')">Español (Spanish)</a></li>
                <li><a href="#" onclick="changeLanguage('fr')">Français (French)</a></li>
                <li><a href="#" onclick="changeLanguage('de')">Deutsch (German)</a></li>
                <li><a href="#" onclick="changeLanguage('hi')">हिन्दी (Hindi)</a></li>
                <li><a href="#" onclick="changeLanguage('ar')">العربية (Arabic)</a></li>
                <li><a href="#" onclick="changeLanguage('pt')">Português (Portuguese)</a></li>
                <li><a href="#" onclick="changeLanguage('ru')">Русский (Russian)</a></li>
                <li><a href="#" onclick="changeLanguage('id')">Bahasa Indonesia</a></li>
                <li><a href="#" onclick="changeLanguage('zh')">中文 (Chinese)</a></li>
                <li><a href="#" onclick="changeLanguage('ur')">اردو (Urdu)</a></li>
            </ul>
        </li>
    </ul>
</nav>

<div class="mobile-top-bar mobile-nav">
    <div class="menu-icon" id="menuIcon"><i class="fas fa-bars"></i></div>
    <div class="nav-brand-container">
        <a href="index.html" class="nav-brand">
            <img src="../shared/icon-nav.webp" alt="downsocial Logo" width="38" height="38" fetchpriority="high">
            <span>downsocial<span class="domain-ext">.net</span></span>
        </a>
        <a href="index.html" class="nav-brand-home"><i class="fas fa-arrow-left"></i> <span>Home</span></a>
    </div>
    
    <div class="dropdown notification-wrapper mobile-bell">
        <a href="#" id="mobileNotifToggle" class="bell-icon">
            <i class="fas fa-bell"></i>
            <span class="notif-dot"></span>
        </a>
        <div class="notification-panel" id="mobileNotifPanel">
            <div class="notif-header">
                <h4>Notifications</h4>
                <span class="badge">1 New</span>
            </div>
            <div class="notif-body">
                <div class="notif-item">
                    <p style="font-size:13px;color:#fff;">🚀 <strong>{p_name} Downloader v3.0 Live!</strong> Fast HD downloads and clean audio extraction ready.</p>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="sidebar mobile-nav" id="sidebar">
    <div class="close-btn" id="closeBtn"><i class="fas fa-times"></i></div>
    <ul class="menu-links" style="margin-top: 60px;">
        <li class="sidebar-theme-item" style="padding: 15px 20px;">
            <div class="theme-segmented-control" data-theme-switcher style="width: 100%;">
                <div class="theme-pill"></div>
                <button type="button" class="theme-btn" data-theme-val="premium" aria-label="Premium Mode"><i class="fas fa-crown"></i> <span>Premium</span></button>
                <button type="button" class="theme-btn active" data-theme-val="dark" aria-label="Dark Mode"><i class="fas fa-moon"></i> <span>Dark</span></button>
                <button type="button" class="theme-btn" data-theme-val="light" aria-label="Light Mode"><i class="fas fa-sun"></i> <span>Light</span></button>
            </div>
        </li>
        <li><a href="index.html"><i class="fas fa-home"></i> <span>Home</span></a></li>
        <li><a href="features.html"><i class="fas fa-star"></i> <span>Features</span></a></li>
        <li><a href="about.html"><i class="fas fa-info-circle"></i> <span>About</span></a></li>
        <li><a href="contact.html"><i class="fas fa-envelope"></i> <span>Contact</span></a></li>
        <li><a href="privacy.html"><i class="fas fa-shield-alt"></i> <span>Privacy Policy</span></a></li>
        <li><a href="terms.html"><i class="fas fa-file-contract"></i> <span>Terms of Service</span></a></li>
        <li class="dropdown">
            <a href="#" id="mobileLangToggle"><i class="fas fa-globe"></i> <span>Language</span> <i class="fas fa-caret-down" style="margin-left:auto;"></i></a>
            <ul class="dropdown-menu-mobile" id="mobileLangMenu">
                <li><a href="#" onclick="changeLanguage('en')">English</a></li>
                <li><a href="#" onclick="changeLanguage('es')">Español</a></li>
                <li><a href="#" onclick="changeLanguage('fr')">Français</a></li>
                <li><a href="#" onclick="changeLanguage('de')">Deutsch</a></li>
                <li><a href="#" onclick="changeLanguage('hi')">हिन्दी</a></li>
                <li><a href="#" onclick="changeLanguage('ar')">العربية</a></li>
                <li><a href="#" onclick="changeLanguage('pt')">Português</a></li>
                <li><a href="#" onclick="changeLanguage('ru')">Русский</a></li>
                <li><a href="#" onclick="changeLanguage('id')">Bahasa Indonesia</a></li>
                <li><a href="#" onclick="changeLanguage('zh')">中文</a></li>
                <li><a href="#" onclick="changeLanguage('ur')">اردو</a></li>
            </ul>
        </li>
    </ul>
</div>
'''

def render_footer(cfg):
    p_name = cfg['name']
    p_folder = cfg['folder']
    
    # 7 tool pills in footer grid
    pills_html = ""
    for folder, name, icon, pill_class in ALL_PLATFORM_LINKS:
        is_active = "active" if folder == p_folder else ""
        pills_html += f'<a href="../{folder}/index.html" class="tool-pill {pill_class} {is_active}"><i class="{icon}"></i> <span>{name}</span></a>\n'
    
    return f'''
<footer class="footer">
    <div class="footer-links">
        <a href="index.html" class="footer-btn">Home</a>
        <a href="features.html" class="footer-btn">Features</a>
        <a href="about.html" class="footer-btn">About</a>
        <a href="contact.html" class="footer-btn">Contact</a>
        <a href="privacy.html" class="footer-btn">Privacy Policy</a>
        <a href="terms.html" class="footer-btn">Terms of Service</a>
        {"<a href='how-it-works.html' class='footer-btn'>How It Works</a>" if p_folder == 'universal-downloader' else ''}
    </div>
    
    <div class="footer-tools-container" style="max-width: 960px; margin: 25px auto 20px; padding: 0 15px;">
        <div style="font-size: 13px; font-weight: 700; color: var(--text-sub); text-align: center; margin-bottom: 12px; text-transform: uppercase; letter-spacing: 0.5px;">
            Other Social Media Downloaders
        </div>
        <div class="footer-tools-grid">
            {pills_html}
        </div>
    </div>

    <div class="copyright">
        &copy; 2026 downsocial.net — {p_name} Video Downloader. All rights reserved.
    </div>
</footer>
'''

def generate_index_html(cfg):
    p_folder = cfg['folder']
    p_name = cfg['name']
    
    # FAQs list
    faqs_html = ""
    for i, card in enumerate(cfg['features_cards'][:5]):
        faqs_html += f'''
        <div class="accordion-item {'active' if i == 0 else ''}">
            <div class="accordion-header">
                <span>How do I use the {p_name} Downloader for {card['title']}?</span>
                <i class="fas fa-plus"></i>
            </div>
            <div class="accordion-body">
                {card['desc']} Simply copy the {p_name} media URL, paste it into our input box above, and click Download to save the clean file instantly.
            </div>
        </div>
        '''
        
    features_html = ""
    for card in cfg['features_cards']:
        features_html += f'''
        <div class="feature-detail-card">
            <div class="feature-detail-icon"><i class="{card['icon']}"></i></div>
            <h3>{card['title']}</h3>
            <p>{card['desc']}</p>
        </div>
        '''

    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{cfg['meta_title']}</title>
    <meta name="description" content="{cfg['meta_desc']}">
    <meta name="keywords" content="{cfg['meta_keywords']}">
    <link rel="icon" type="image/webp" href="../shared/icon-nav.webp">
    <link rel="apple-touch-icon" href="../shared/icon-nav.webp">
    <link rel="canonical" href="https://downsocial.net/{p_folder}/">
    <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">

    <!-- Fonts & CSS -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
    <link rel="stylesheet" href="../shared/style.css">

    <!-- Open Graph -->
    <meta property="og:locale" content="en_US">
    <meta property="og:type" content="website">
    <meta property="og:title" content="{cfg['meta_title']}">
    <meta property="og:description" content="{cfg['meta_desc']}">
    <meta property="og:url" content="https://downsocial.net/{p_folder}/">
    <meta property="og:site_name" content="downsocial">
    <meta property="og:image" content="https://downsocial.net/icon.webp">

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{cfg['meta_title']}">
    <meta name="twitter:description" content="{cfg['meta_desc']}">
    <meta name="twitter:image" content="https://downsocial.net/icon.webp">

    <!-- Schema.org JSON-LD -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@graph": [
        {{
          "@type": "WebApplication",
          "@id": "https://downsocial.net/{p_folder}/#webapp",
          "url": "https://downsocial.net/{p_folder}/",
          "name": "downsocial {p_name} Video Downloader",
          "applicationCategory": "MultimediaApplication",
          "operatingSystem": "All (Windows, Mac, iOS, Android, Linux)",
          "browserRequirements": "Requires JavaScript. Requires HTML5.",
          "offers": {{
            "@type": "Offer",
            "price": "0",
            "priceCurrency": "USD"
          }},
          "description": "{cfg['meta_desc']}",
          "featureList": [
            "Download {p_name} Videos in 1080p Full HD & 4K",
            "No Watermarks or Logos",
            "Extract {p_name} Audio to High-Quality MP3",
            "100% Free and Unlimited Downloads",
            "No Registration or Software Installation"
          ]
        }},
        {{
          "@type": "BreadcrumbList",
          "@id": "https://downsocial.net/{p_folder}/#breadcrumbs",
          "itemListElement": [
            {{
              "@type": "ListItem",
              "position": 1,
              "name": "Home",
              "item": "https://downsocial.net/"
            }},
            {{
              "@type": "ListItem",
              "position": 2,
              "name": "{p_name} Downloader",
              "item": "https://downsocial.net/{p_folder}/"
            }}
          ]
        }}
      ]
    }}
    </script>
    <script>
        (function() {{
            var t = localStorage.getItem('siteTheme') || 'dark';
            document.documentElement.setAttribute('data-theme', t);
        }})();
    </script>
</head>
<body>

{render_nav(cfg, 'index')}

<div class="main-wrapper">
    <div class="hero-container" style="text-align: center; margin-bottom: 25px;">
        <span class="platform-pill-badge {cfg['accent_badge']}">
            <i class="{cfg['icon_class']}"></i> {p_name} Downloader
        </span>
        <h1 class="main-title" data-key="hero.title">{cfg['hero_title']}</h1>
        <p class="tagline" data-key="hero.subtitle">{cfg['hero_subtitle']}</p>
    </div>

    <!-- Downloader Box -->
    <div class="search-box">
        <div class="input-group">
            <i class="fas fa-link input-icon"></i>
            <input type="text" id="videoUrl" placeholder="{cfg['input_placeholder']}" autocomplete="off" data-key="hero.placeholder">
            <button class="clear-btn" id="clearBtn" title="Clear"><i class="fas fa-times"></i></button>
            <button class="paste-btn" id="pasteBtn"><i class="fas fa-paste"></i> <span>Paste</span></button>
        </div>
        <button class="process-btn" id="downloadBtn" data-key="hero.cta_button">
            <i class="fas fa-download"></i> <span>{cfg['cta_text']}</span>
        </button>
    </div>

    <!-- Status Message -->
    <div id="statusMessage" class="status-message"></div>

    <!-- Result Card -->
    <div class="result-card" id="resultCard" style="display: none;">
        <div class="preview-container">
            <video id="videoPreview" controls playsinline></video>
            <img id="imagePreview" alt="{p_name} Media Preview" style="display: none; width: 100%; border-radius: 8px;">
        </div>
        <div class="download-btns">
            <a href="#" id="btnVidHigh" class="dl-btn dl-vid-high" target="_blank" rel="noopener"><i class="fas fa-video"></i> Video (HD)</a>
            <a href="#" id="btnVidNorm" class="dl-btn dl-vid-norm" target="_blank" rel="noopener"><i class="fas fa-video"></i> Video (SD)</a>
            <a href="#" id="btnAudHigh" class="dl-btn dl-aud-high" target="_blank" rel="noopener"><i class="fas fa-music"></i> Audio (HQ MP3)</a>
            <a href="#" id="btnAudNorm" class="dl-btn dl-aud-norm" target="_blank" rel="noopener"><i class="fas fa-music"></i> Audio (Normal MP3)</a>
        </div>
    </div>

    <!-- Features Showcase -->
    <div class="features-detail-grid">
        {features_html}
    </div>

    <!-- Step by Step How To -->
    <div class="how-to-section" style="margin: 40px 0;">
        <h2 class="section-title">How to Download {p_name} Videos in 3 Easy Steps</h2>
        <div class="how-it-works-grid">
            <div class="step-card">
                <div class="step-number">1</div>
                <h3>Copy the {p_name} Link</h3>
                <p>Open the {p_name} app or website, find the video or media you wish to save, tap Share, and select <strong>Copy Link</strong>.</p>
            </div>
            <div class="step-card">
                <div class="step-number">2</div>
                <h3>Paste URL in Downloader</h3>
                <p>Return to downsocial {p_name} downloader, paste the copied link into the input bar above, and click <strong>{cfg['cta_text']}</strong>.</p>
            </div>
            <div class="step-card">
                <div class="step-number">3</div>
                <h3>Save in HD MP4 or MP3</h3>
                <p>Select your desired resolution (HD / Normal) or MP3 audio format to download and enjoy the media offline immediately.</p>
            </div>
        </div>
    </div>

    <!-- FAQ Accordion -->
    <div class="faq-section" style="margin: 40px 0;">
        <h2 class="section-title">{p_name} Video Downloader FAQs</h2>
        <div class="accordion">
            {faqs_html}
        </div>
    </div>

    <!-- Educational Deep Dive SEO Section -->
    <div class="seo-article-wrapper article-container" style="margin-top: 40px;">
        <h2>The Leading {p_name} Video Downloader Solution</h2>
        <p class="article-intro">
            Welcome to the official <strong>downsocial {p_name} Video Downloader</strong>. Whether you want to save inspiring Reels, preserve Stories before they vanish, or convert captivating discussions into high-fidelity MP3 audio, downsocial delivers the fastest, cleanest, and most reliable experience on the internet.
        </p>

        <h3>Why Choose downsocial over Competitors like {cfg['competitors']}?</h3>
        <p>
            Traditional social media downloaders are cluttered with intrusive popups, deceptive links, and annoying watermark overlays that compromise video quality. downsocial is built differently: our high-performance stream pipeline connects directly to public CDN networks to fetch the pristine master video files without modification or compression.
        </p>
        
        <div class="seo-table-container">
            <table class="seo-table">
                <thead>
                    <tr>
                        <th>Feature Comparison</th>
                        <th>downsocial {p_name} Downloader</th>
                        <th>Traditional Tools ({cfg['competitors']})</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>Watermark Removal</strong></td>
                        <td><span class="badge-highlight">100% Clean (No Watermarks)</span></td>
                        <td>Often Adds Branding or Fails</td>
                    </tr>
                    <tr>
                        <td><strong>Maximum Resolution</strong></td>
                        <td><span class="badge-highlight">1080p, 2K & 4K Ultra HD</span></td>
                        <td>Capped at 720p Compressed</td>
                    </tr>
                    <tr>
                        <td><strong>Audio Extraction</strong></td>
                        <td><span class="badge-highlight">Real-time HQ MP3 (320kbps)</span></td>
                        <td>Low Bitrate or Unavailable</td>
                    </tr>
                    <tr>
                        <td><strong>Ad Experience</strong></td>
                        <td><span class="badge-highlight">Zero Popups, Clean SaaS UI</span></td>
                        <td>Aggressive Popups & Redirects</td>
                    </tr>
                    <tr>
                        <td><strong>Account Privacy</strong></td>
                        <td><span class="badge-highlight">100% Anonymous (No Login)</span></td>
                        <td>Requires Login or Browser Extensions</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <h3>Technical Specifications & Device Compatibility</h3>
        <p>
            Our web application is optimized for cross-platform performance. Whether you are using Safari on iOS (iPhone/iPad), Chrome on Android, or a desktop browser on Windows, macOS, or Linux, downloads trigger natively into your browser download manager without needing auxiliary apps.
        </p>
    </div>
</div>

{render_footer(cfg)}

<!-- Shared Scripts -->
<script src="../shared/script.js"></script>
</body>
</html>
'''
    return html_content

def generate_about_html(cfg):
    p_name = cfg['name']
    p_folder = cfg['folder']
    
    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About Our {p_name} Video Downloader — Fast, Free & HD | downsocial</title>
    <meta name="description" content="Learn about our dedicated {p_name} video downloader. Discover our mission for fast, secure, watermark-free media archiving with zero logs.">
    <link rel="icon" type="image/webp" href="../shared/icon-nav.webp">
    <link rel="canonical" href="https://downsocial.net/{p_folder}/about.html">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
    <link rel="stylesheet" href="../shared/style.css">
    <script>
        (function() {{
            var t = localStorage.getItem('siteTheme') || 'dark';
            document.documentElement.setAttribute('data-theme', t);
        }})();
    </script>
</head>
<body>

{render_nav(cfg, 'about')}

<div class="page-content-wrapper">
    <div class="article-container">
        <span class="platform-pill-badge {cfg['accent_badge']}"><i class="{cfg['icon_class']}"></i> {p_name} Downloader</span>
        <h1>About Our {p_name} Video Downloader</h1>
        <p class="article-intro">
            downsocial {p_name} Downloader was created to provide users worldwide with an effortless, privacy-respecting, and lightning-fast way to save public media from {p_name} in highest fidelity.
        </p>

        <h2>1. Our Mission</h2>
        <p>
            Our mission is simple: eliminate the friction of saving important media. Creators, researchers, educators, and everyday users rely on social media videos for memories, knowledge sharing, and creative inspiration. We ensure you can archive these public videos permanently on your personal devices without intrusive watermarks or privacy trade-offs.
        </p>

        <h2>2. Why Users Prefer Our {p_name} Downloader</h2>
        <p>
            Unlike other web tools that inject ads, force extensions, or fail on high-bitrate media, our engine is built with modern web architecture:
        </p>
        <ul>
            <li><strong>Direct CDN Streaming:</strong> Videos are fetched straight from high-speed content delivery networks for maximum download speed.</li>
            <li><strong>Zero Storage Guarantee:</strong> We do not store downloaded videos on our servers; data streams in real-time straight to your device.</li>
            <li><strong>No Watermarks:</strong> We provide authentic, unbranded video files in original aspect ratio and high definition.</li>
            <li><strong>HQ Audio Extraction:</strong> Direct conversion to stereo MP3 audio for music, lectures, and podcasts.</li>
        </ul>

        <h2>3. 100% Safe, Secure & Anonymous</h2>
        <p>
            We take user security seriously. You will never be asked to log in, link your {p_name} profile, or provide personal credentials. Every request is processed transiently over encrypted HTTPS connections.
        </p>

        <div style="margin-top: 35px; text-align: center;">
            <a href="index.html" class="submit-btn" style="text-decoration: none;"><i class="fas fa-download"></i> Try {p_name} Downloader Now</a>
        </div>
    </div>
</div>

{render_footer(cfg)}

<script src="../shared/script.js"></script>
</body>
</html>
'''
    return html_content

def generate_contact_html(cfg):
    p_name = cfg['name']
    p_folder = cfg['folder']
    
    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us — {p_name} Downloader Support Desk | downsocial</title>
    <meta name="description" content="Need help with {p_name} video downloads? Contact our dedicated support team for bug reports, watermark issues, or feature requests.">
    <link rel="icon" type="image/webp" href="../shared/icon-nav.webp">
    <link rel="canonical" href="https://downsocial.net/{p_folder}/contact.html">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
    <link rel="stylesheet" href="../shared/style.css">
    <script>
        (function() {{
            var t = localStorage.getItem('siteTheme') || 'dark';
            document.documentElement.setAttribute('data-theme', t);
        }})();
    </script>
</head>
<body>

{render_nav(cfg, 'contact')}

<div class="page-content-wrapper">
    <div class="article-container">
        <span class="platform-pill-badge {cfg['accent_badge']}"><i class="{cfg['icon_class']}"></i> {p_name} Support Desk</span>
        <h1>Contact {p_name} Downloader Support</h1>
        <p class="article-intro">
            Have questions about {p_name} video formats, encountering an error with a specific link, or want to suggest an improvement? Our dedicated {p_name} technical support team is here to assist.
        </p>

        <div class="contact-grid">
            <!-- Left: Info -->
            <div class="contact-info-card">
                <h3>Direct Support Channels</h3>
                <p>For inquiries specifically regarding {p_name} video, audio, or story downloads:</p>
                
                <ul class="contact-info-list">
                    <li>
                        <i class="fas fa-envelope"></i>
                        <div>
                            <strong>Email Address</strong><br>
                            <a href="mailto:support@downsocial.net?subject={p_name}%20Downloader%20Inquiry" style="color: var(--accent-blue);">support@downsocial.net</a>
                        </div>
                    </li>
                    <li>
                        <i class="fas fa-globe"></i>
                        <div>
                            <strong>Service Scope</strong><br>
                            {p_name} Downloader Platform Services
                        </div>
                    </li>
                    <li>
                        <i class="fas fa-clock"></i>
                        <div>
                            <strong>Availability</strong><br>
                            24 Hours a Day, 7 Days a Week
                        </div>
                    </li>
                </ul>

                <div class="contact-sla-badge">
                    <i class="fas fa-bolt"></i> Average Response: Under 24 Hours
                </div>
            </div>

            <!-- Right: Form -->
            <div>
                <form id="contactForm" class="contact-form">
                    <div class="form-group">
                        <label class="form-label" for="contactName">Your Name</label>
                        <input type="text" id="contactName" class="form-input" placeholder="e.g. Alex Morgan" required>
                    </div>

                    <div class="form-group">
                        <label class="form-label" for="contactEmail">Your Email</label>
                        <input type="email" id="contactEmail" class="form-input" placeholder="e.g. alex@example.com" required>
                    </div>

                    <div class="form-group">
                        <label class="form-label" for="contactIssueType">Issue Type ({p_name} only)</label>
                        <select id="contactIssueType" class="form-select" required>
                            <option value="">Select an Issue Type...</option>
                            <option value="link_error">Download Failed / Link Not Recognized</option>
                            <option value="watermark_issue">Watermark Removal Issue</option>
                            <option value="audio_issue">Audio Desync or MP3 Issue</option>
                            <option value="quality_issue">Quality / Resolution Inquiry</option>
                            <option value="feature_request">Feature Request for {p_name}</option>
                            <option value="other">General Question</option>
                        </select>
                    </div>

                    <div class="form-group">
                        <label class="form-label" for="contactUrl">{p_name} Video Link (Optional)</label>
                        <input type="url" id="contactUrl" class="form-input" placeholder="Paste the affected {p_name} link here">
                    </div>

                    <div class="form-group">
                        <label class="form-label" for="contactMessage">Detailed Message</label>
                        <textarea id="contactMessage" class="form-textarea" placeholder="Please describe the issue or your suggestion in detail..." required></textarea>
                    </div>

                    <button type="submit" class="submit-btn">
                        <i class="fas fa-paper-plane"></i> Send {p_name} Support Message
                    </button>
                    
                    <div id="contactAlert" class="form-alert"></div>
                </form>
            </div>
        </div>
    </div>
</div>

{render_footer(cfg)}

<script src="../shared/script.js"></script>
</body>
</html>
'''
    return html_content

def generate_privacy_html(cfg):
    p_name = cfg['name']
    p_folder = cfg['folder']
    
    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Privacy Policy — {p_name} Video Downloader | downsocial</title>
    <meta name="description" content="Privacy policy for downsocial's {p_name} downloader. Learn how we enforce strict zero-log privacy, encrypted streams, and zero credential storage.">
    <link rel="icon" type="image/webp" href="../shared/icon-nav.webp">
    <link rel="canonical" href="https://downsocial.net/{p_folder}/privacy.html">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
    <link rel="stylesheet" href="../shared/style.css">
    <script>
        (function() {{
            var t = localStorage.getItem('siteTheme') || 'dark';
            document.documentElement.setAttribute('data-theme', t);
        }})();
    </script>
</head>
<body>

{render_nav(cfg, 'privacy')}

<div class="page-content-wrapper">
    <div class="article-container">
        <span class="platform-pill-badge {cfg['accent_badge']}"><i class="{cfg['icon_class']}"></i> Privacy Guarantee</span>
        <h1>Privacy Policy — {p_name} Downloader</h1>
        <p class="article-intro">
            At downsocial, protecting your privacy is our foundational principle. This policy explains our zero-knowledge data architecture specifically tailored to our {p_name} media downloader.
        </p>

        <h2>1. Independent Utility Disclaimer</h2>
        <p>
            downsocial operates as an independent web application. We are not affiliated with, endorsed by, sponsored by, or formally associated with {p_name} or its parent entity. All product and company names are trademarks™ or registered® trademarks of their respective holders.
        </p>

        <h2>2. Zero Personal Data Collection</h2>
        <p>
            You are never required to register an account, sign in, or provide personal credentials (such as your {p_name} username, email, or password) to use downsocial. We do not track who you are, what profiles you visit, or what videos you download.
        </p>

        <h2>3. Ephemeral URL Stream Processing</h2>
        <p>
            When you submit a {p_name} link, our backend processes the URL transiently in temporary memory to resolve the public media stream directly from the platform CDN. Once the direct media download stream is initiated to your browser, the URL request data is discarded.
        </p>

        <h2>4. No File Hosting or Archival</h2>
        <p>
            We do not host, store, or archive copies of downloaded {p_name} media files on our servers. Media transfers directly between public CDN servers and your personal device via secure 256-bit SSL encryption.
        </p>

        <h2>5. Cookies & Local Storage</h2>
        <p>
            We use browser LocalStorage strictly for functional client-side preferences (such as your chosen Dark/Light theme mode and language preference) and your recent link history stored locally on your device only. We do not use third-party tracking cookies.
        </p>
    </div>
</div>

{render_footer(cfg)}

<script src="../shared/script.js"></script>
</body>
</html>
'''
    return html_content

def generate_terms_html(cfg):
    p_name = cfg['name']
    p_folder = cfg['folder']
    
    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Terms of Service — {p_name} Video Downloader | downsocial</title>
    <meta name="description" content="Terms of service and fair use guidelines for using the downsocial {p_name} downloader. Understand copyright compliance and personal use rights.">
    <link rel="icon" type="image/webp" href="../shared/icon-nav.webp">
    <link rel="canonical" href="https://downsocial.net/{p_folder}/terms.html">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
    <link rel="stylesheet" href="../shared/style.css">
    <script>
        (function() {{
            var t = localStorage.getItem('siteTheme') || 'dark';
            document.documentElement.setAttribute('data-theme', t);
        }})();
    </script>
</head>
<body>

{render_nav(cfg, 'terms')}

<div class="page-content-wrapper">
    <div class="article-container">
        <span class="platform-pill-badge {cfg['accent_badge']}"><i class="{cfg['icon_class']}"></i> Legal & Terms</span>
        <h1>Terms of Service — {p_name} Downloader</h1>
        <p class="article-intro">
            By accessing or using the downsocial {p_name} Downloader, you agree to be bound by these Terms of Service. Please read them carefully before downloading media.
        </p>

        <h2>1. Acceptance of Terms</h2>
        <p>
            These Terms govern your use of our free web-based utility for saving public {p_name} media. If you do not agree with any part of these terms, you must discontinue use of the service.
        </p>

        <h2>2. Permitted Personal & Fair Use</h2>
        <p>
            downsocial is intended solely for personal, non-commercial, educational, and archival purposes. You agree not to use downloaded {p_name} content for unauthorized commercial redistribution, re-broadcasting, or any purpose that infringes upon the intellectual property rights of original creators.
        </p>

        <h2>3. Respect for Copyright & Intellectual Property</h2>
        <p>
            All copyrights, trademarks, and ownership rights to videos, audio, images, and brand materials hosted on {p_name} belong strictly to their respective creators or rights holders. Users are solely responsible for ensuring they have appropriate rights or permissions to download and store media.
        </p>

        <h2>4. DMCA & Copyright Takedown Procedure</h2>
        <p>
            We respect the intellectual property of others and comply with the Digital Millennium Copyright Act (DMCA). If you are a copyright owner or authorized representative and believe content is being made accessible in violation of your rights, please contact us at <a href="mailto:dmca@downsocial.net" style="color: var(--accent-blue);">dmca@downsocial.net</a> with proof of ownership for immediate review.
        </p>

        <h2>5. Limitation of Liability</h2>
        <p>
            downsocial is provided on an "AS IS" and "AS AVAILABLE" basis without warranties of any kind. Under no circumstances shall downsocial or its operators be held liable for any direct, indirect, incidental, or consequential damages resulting from the use or inability to use this service.
        </p>
    </div>
</div>

{render_footer(cfg)}

<script src="../shared/script.js"></script>
</body>
</html>
'''
    return html_content

def generate_features_html(cfg):
    p_name = cfg['name']
    p_folder = cfg['folder']
    
    features_grid = ""
    for card in cfg['features_cards']:
        features_grid += f'''
        <div class="feature-detail-card">
            <div class="feature-detail-icon"><i class="{card['icon']}"></i></div>
            <h3>{card['title']}</h3>
            <p>{card['desc']}</p>
        </div>
        '''
        
    specs_rows = ""
    for title, val in cfg['specs']:
        specs_rows += f'''
        <tr>
            <td style="font-weight: 600; width: 35%;">{title}</td>
            <td>{val}</td>
        </tr>
        '''

    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{p_name} Downloader Features & Specs — High Definition | downsocial</title>
    <meta name="description" content="Explore complete features of downsocial's {p_name} video downloader: 1080p Full HD, 4K, no watermark, fast MP3 converter, and cross-device specs.">
    <link rel="icon" type="image/webp" href="../shared/icon-nav.webp">
    <link rel="canonical" href="https://downsocial.net/{p_folder}/features.html">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
    <link rel="stylesheet" href="../shared/style.css">
    <script>
        (function() {{
            var t = localStorage.getItem('siteTheme') || 'dark';
            document.documentElement.setAttribute('data-theme', t);
        }})();
    </script>
</head>
<body>

{render_nav(cfg, 'features')}

<div class="page-content-wrapper">
    <div class="article-container">
        <span class="platform-pill-badge {cfg['accent_badge']}"><i class="{cfg['icon_class']}"></i> Technical Capabilities</span>
        <h1>{p_name} Downloader Features & Specifications</h1>
        <p class="article-intro">
            A comprehensive overview of the specialized capabilities, performance benchmarks, and high-definition formats supported by our {p_name} video downloader.
        </p>

        <h2>Core Capabilities & Highlights</h2>
        <div class="features-detail-grid">
            {features_grid}
        </div>

        <h2>Detailed Technical Specifications</h2>
        <div class="seo-table-container">
            <table class="seo-table">
                <thead>
                    <tr>
                        <th>Specification Attribute</th>
                        <th>Capability & Standard</th>
                    </tr>
                </thead>
                <tbody>
                    {specs_rows}
                </tbody>
            </table>
        </div>

        <h2>Head-to-Head Comparison with Alternatives</h2>
        <p>See why downsocial outperforms conventional {p_name} downloaders like {cfg['competitors']}:</p>
        <div class="seo-table-container">
            <table class="seo-table">
                <thead>
                    <tr>
                        <th>Evaluation Criterion</th>
                        <th>downsocial {p_name}</th>
                        <th>Other Tools ({cfg['competitors']})</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>Watermark Handling</strong></td>
                        <td><span class="badge-highlight">100% Unbranded & Clean</span></td>
                        <td>Inconsistent / Adds Watermark</td>
                    </tr>
                    <tr>
                        <td><strong>Output Resolution</strong></td>
                        <td><span class="badge-highlight">Native 1080p, 2K & 4K</span></td>
                        <td>Frequently Degraded to 480p/720p</td>
                    </tr>
                    <tr>
                        <td><strong>Audio Extraction</strong></td>
                        <td><span class="badge-highlight">Real-time HQ MP3 Conversion</span></td>
                        <td>Separate Tool or Low Bitrate</td>
                    </tr>
                    <tr>
                        <td><strong>Safety & Ads</strong></td>
                        <td><span class="badge-highlight">No Ads, Zero Malware Risk</span></td>
                        <td>Aggressive Popups & Redirects</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div style="margin-top: 35px; text-align: center;">
            <a href="index.html" class="submit-btn" style="text-decoration: none;"><i class="fas fa-download"></i> Start Downloading {p_name} Videos</a>
        </div>
    </div>
</div>

{render_footer(cfg)}

<script src="../shared/script.js"></script>
</body>
</html>
'''
    return html_content

def generate_how_it_works_html(cfg):
    p_name = cfg['name']
    p_folder = cfg['folder']
    
    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>How It Works — Complete Universal Social Media Video Download Guide | downsocial</title>
    <meta name="description" content="Step-by-step illustrated guide on downloading social media videos from Facebook, Instagram, TikTok, YouTube, Snapchat, and Threads on iPhone, Android & PC.">
    <link rel="icon" type="image/webp" href="../shared/icon-nav.webp">
    <link rel="canonical" href="https://downsocial.net/{p_folder}/how-it-works.html">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
    <link rel="stylesheet" href="../shared/style.css">
    <script>
        (function() {{
            var t = localStorage.getItem('siteTheme') || 'dark';
            document.documentElement.setAttribute('data-theme', t);
        }})();
    </script>
</head>
<body>

{render_nav(cfg, 'how-it-works')}

<div class="page-content-wrapper">
    <div class="article-container">
        <span class="platform-pill-badge badge-universal"><i class="fas fa-book-open"></i> User Manual</span>
        <h1>How It Works — Universal Social Media Download Guide</h1>
        <p class="article-intro">
            A comprehensive walkthrough detailing how to download videos, reels, stories, shorts, and music from any major social media platform using downsocial on iOS, Android, and PC.
        </p>

        <h2>Universal 3-Step Process</h2>
        <div class="how-it-works-grid">
            <div class="step-card">
                <div class="step-number">1</div>
                <h3>Copy the Share Link</h3>
                <p>In any app (Facebook, Instagram, TikTok, YouTube, Snapchat, or Threads), tap the <strong>Share</strong> button and choose <strong>Copy Link</strong>.</p>
            </div>
            <div class="step-card">
                <div class="step-number">2</div>
                <h3>Paste into downsocial</h3>
                <p>Open downsocial in any browser, paste the link into the search bar, and tap <strong>Download Video</strong>.</p>
            </div>
            <div class="step-card">
                <div class="step-number">3</div>
                <h3>Choose Format & Save</h3>
                <p>Pick between Video (HD), Video (Normal), or Audio (HQ MP3). The file saves instantly to your device storage.</p>
            </div>
        </div>

        <h2>Platform-Specific Instructions</h2>

        <h3>1. How to Download from Facebook</h3>
        <p>
            Open Facebook on web or mobile. On any public video, Reel, or Story, click the <strong>Share</strong> icon and select <strong>Copy link</strong>. Paste into downsocial, and choose between 1080p HD MP4 or HQ MP3.
        </p>

        <h3>2. How to Download from Instagram</h3>
        <p>
            Navigate to the Instagram Reel, Story, or Carousel post. Tap the three dots (•••) or the paper-airplane share button and select <strong>Copy Link</strong>. Paste the link into downsocial to download clean media without watermark.
        </p>

        <h3>3. How to Download from TikTok (No Watermark)</h3>
        <p>
            Open TikTok, tap the <strong>Share</strong> arrow on the right side of the screen, and select <strong>Copy Link</strong>. When pasted into downsocial, our engine automatically strips the bouncing watermark logo and provides the clean 60FPS video.
        </p>

        <h3>4. How to Download from YouTube</h3>
        <p>
            On YouTube or YouTube Shorts, click <strong>Share</strong> > <strong>Copy Link</strong>. Paste the link into downsocial to choose your desired quality up to 4K Ultra HD or extract pure 320kbps MP3 audio.
        </p>

        <h3>5. How to Download from Snapchat</h3>
        <p>
            On any Spotlight clip or public Story, tap the <strong>Share</strong> button and choose <strong>Copy Link</strong>. Save vertical 9:16 videos before the 24-hour expiration window closes.
        </p>

        <h3>6. How to Download from Meta Threads</h3>
        <p>
            On Threads, tap the paper airplane share icon on the post and tap <strong>Copy link</strong>. downsocial extracts the high-bitrate video or multi-photo album immediately.
        </p>

        <h2>Saving Videos on Mobile Devices</h2>
        <h3>📱 For iPhone & iPad (iOS Safari):</h3>
        <ol>
            <li>Open Safari and visit downsocial.net.</li>
            <li>Paste your video link and click Download.</li>
            <li>Tap the preferred quality button (e.g. Video HD). Safari will ask "Do you want to download this file?". Tap <strong>Download</strong>.</li>
            <li>Tap the blue Download arrow in the Safari address bar, open the downloaded video, tap <strong>Share</strong>, and tap <strong>Save Video</strong> to move it into your Photos app.</li>
        </ol>

        <h3>🤖 For Android Phones (Chrome / Firefox / Samsung Internet):</h3>
        <ol>
            <li>Open Chrome and visit downsocial.net.</li>
            <li>Paste your link and tap Download.</li>
            <li>Click your preferred quality button. The MP4 video will download directly into your <strong>Downloads</strong> folder and appear automatically in your Gallery.</li>
        </ol>

        <div style="margin-top: 35px; text-align: center;">
            <a href="index.html" class="submit-btn" style="text-decoration: none;"><i class="fas fa-download"></i> Try the Universal Downloader</a>
        </div>
    </div>
</div>

{render_footer(cfg)}

<script src="../shared/script.js"></script>
</body>
</html>
'''
    return html_content

total_pages_generated = 0

for p_folder, cfg in PLATFORM_CONFIGS.items():
    target_dir = os.path.join(BASE_DIR, p_folder)
    os.makedirs(target_dir, exist_ok=True)
    
    # 1. index.html
    with open(os.path.join(target_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(generate_index_html(cfg))
    total_pages_generated += 1
    
    # 2. about.html
    with open(os.path.join(target_dir, 'about.html'), 'w', encoding='utf-8') as f:
        f.write(generate_about_html(cfg))
    total_pages_generated += 1
    
    # 3. contact.html
    with open(os.path.join(target_dir, 'contact.html'), 'w', encoding='utf-8') as f:
        f.write(generate_contact_html(cfg))
    total_pages_generated += 1
    
    # 4. privacy.html
    with open(os.path.join(target_dir, 'privacy.html'), 'w', encoding='utf-8') as f:
        f.write(generate_privacy_html(cfg))
    total_pages_generated += 1
    
    # 5. terms.html
    with open(os.path.join(target_dir, 'terms.html'), 'w', encoding='utf-8') as f:
        f.write(generate_terms_html(cfg))
    total_pages_generated += 1
    
    # 6. features.html
    with open(os.path.join(target_dir, 'features.html'), 'w', encoding='utf-8') as f:
        f.write(generate_features_html(cfg))
    total_pages_generated += 1
    
    # 7. how-it-works.html (for universal-downloader)
    if p_folder == 'universal-downloader':
        with open(os.path.join(target_dir, 'how-it-works.html'), 'w', encoding='utf-8') as f:
            f.write(generate_how_it_works_html(cfg))
        total_pages_generated += 1

print(f"Successfully generated {total_pages_generated} HTML pages across all 7 platforms!")
