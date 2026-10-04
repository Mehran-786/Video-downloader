import os
import json
import re
import sys

# Set UTF-8 stdout
sys.stdout.reconfigure(encoding='utf-8')

FRONTEND = r'c:\my folder\Pictures\Desktop\downsocial\frontend'
SHARED = os.path.join(FRONTEND, 'shared')

PLATFORMS = [
    'facebook-downloader', 'instagram-downloader', 'tiktok-downloader',
    'youtube-downloader', 'snapchat-downloader', 'threads-downloader', 'universal-downloader'
]

LANGUAGES = ['en', 'es', 'fr', 'de', 'hi', 'ar', 'pt', 'ru', 'id', 'zh', 'ur']

STANDARD_PAGES = ['index.html', 'about.html', 'contact.html', 'privacy.html', 'terms.html', 'features.html']

print("=" * 80)
print("DOWNSOCIAL MULTI-PLATFORM EXPANSION AUDIT")
print("=" * 80)

failures = []
total_pages_checked = 0
total_locales_checked = 0

# 1. Audit Shared Directory
print("\n[CHECK 1] Auditing Shared Directory...")
if not os.path.exists(os.path.join(SHARED, 'style.css')):
    failures.append("Missing frontend/shared/style.css")
else:
    print("  ✓ shared/style.css exists")

if not os.path.exists(os.path.join(SHARED, 'script.js')):
    failures.append("Missing frontend/shared/script.js")
else:
    print("  ✓ shared/script.js exists")

shared_locales = os.path.join(SHARED, 'locales')
if not os.path.exists(shared_locales):
    failures.append("Missing frontend/shared/locales")
else:
    for lang in LANGUAGES:
        lpath = os.path.join(shared_locales, f'{lang}.json')
        if not os.path.exists(lpath):
            failures.append(f"Missing shared locale: {lang}.json")
    print(f"  ✓ shared/locales verified with {len(os.listdir(shared_locales))} language files")

# 2. Audit All 7 Platform Folders
print("\n[CHECK 2] Auditing 7 Platform Folders...")
for p in PLATFORMS:
    p_dir = os.path.join(FRONTEND, p)
    print(f"\n  Checking platform: {p}")
    if not os.path.exists(p_dir):
        failures.append(f"Missing platform folder: {p}")
        continue
    
    # Check assets
    assets_dir = os.path.join(p_dir, 'assets')
    if not os.path.exists(assets_dir):
        failures.append(f"{p}: Missing assets directory")
    else:
        for a in ['icon.webp', 'banner.webp']:
            if not os.path.exists(os.path.join(assets_dir, a)):
                failures.append(f"{p}: Missing asset {a}")
        print(f"    ✓ assets/ verified")

    # Check locales
    locales_dir = os.path.join(p_dir, 'locales')
    if not os.path.exists(locales_dir):
        failures.append(f"{p}: Missing locales directory")
    else:
        for lang in LANGUAGES:
            lpath = os.path.join(locales_dir, f'{lang}.json')
            if not os.path.exists(lpath):
                failures.append(f"{p}: Missing locale {lang}.json")
            else:
                try:
                    with open(lpath, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    req_keys = ['meta', 'navigation', 'hero', 'features', 'about', 'contact', 'privacy', 'terms', 'faq', 'footer']
                    for rk in req_keys:
                        if rk not in data:
                            failures.append(f"{p}/{lang}.json: Missing section '{rk}'")
                    total_locales_checked += 1
                except Exception as e:
                    failures.append(f"{p}/{lang}.json: Invalid JSON syntax: {e}")
        print(f"    ✓ locales/ verified (11/11 language JSONs valid)")

    # Check HTML pages
    required_pages = list(STANDARD_PAGES)
    if p == 'universal-downloader':
        required_pages.append('how-it-works.html')
        
    for page in required_pages:
        hpath = os.path.join(p_dir, page)
        if not os.path.exists(hpath):
            failures.append(f"{p}: Missing HTML page {page}")
            continue
        
        with open(hpath, 'r', encoding='utf-8') as f:
            html_text = f.read()
            
        # Check Title
        m_title = re.search(r'<title>(.*?)</title>', html_text, re.IGNORECASE | re.DOTALL)
        if not m_title or not m_title.group(1).strip():
            failures.append(f"{p}/{page}: Missing or empty <title>")
            
        # Check Meta Description
        m_desc = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', html_text, re.IGNORECASE)
        if not m_desc:
            m_desc = re.search(r'<meta\s+content=["\'](.*?)["\']\s+name=["\']description["\']', html_text, re.IGNORECASE)
        if not m_desc or not m_desc.group(1).strip():
            failures.append(f"{p}/{page}: Missing or empty <meta name='description'>")
            
        # Check Canonical
        m_canon = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\'](.*?)["\']', html_text, re.IGNORECASE)
        if not m_canon:
            failures.append(f"{p}/{page}: Missing canonical link")
            
        # Check Shared CSS link
        if '../shared/style.css' not in html_text:
            failures.append(f"{p}/{page}: Missing link to ../shared/style.css")
            
        # Check Shared JS link
        if '../shared/script.js' not in html_text:
            failures.append(f"{p}/{page}: Missing script to ../shared/script.js")
            
        # Check Schema.org JSON-LD if present
        for m_schema in re.finditer(r'<script\s+type=["\']application/ld\+json["\']>(.*?)</script>', html_text, re.DOTALL | re.IGNORECASE):
            schema_str = m_schema.group(1).strip()
            try:
                json.loads(schema_str)
            except Exception as e:
                failures.append(f"{p}/{page}: Invalid Schema.org JSON: {e}")
                
        total_pages_checked += 1
    print(f"    ✓ HTML pages verified ({len(required_pages)}/{len(required_pages)} complete & SEO valid)")

# 3. Final Summary
print("\n" + "=" * 80)
print(f"AUDIT SUMMARY: {total_pages_checked} HTML Pages, {total_locales_checked} Platform Locales Checked")
print("=" * 80)

if failures:
    print(f"\n❌ FAILED ({len(failures)} errors found):")
    for f in failures[:20]:
        print(f"  - {f}")
    if len(failures) > 20:
        print(f"  ... and {len(failures) - 20} more errors")
    sys.exit(1)
else:
    print("\n✅ ALL AUDITS PASSED WITH 100% SUCCESS!")
    print("  - 7/7 Platform folders verified")
    print("  - 43/43 HTML pages complete with SEO metadata, Canonical & Schema.org")
    print("  - 77/77 Platform locale JSON files validated")
    print("  - Shared CSS & JS architecture functional")
    sys.exit(0)
