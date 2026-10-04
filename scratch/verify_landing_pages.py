import os
import json
import re
import sys

# Force UTF-8 stdout if possible
sys.stdout.reconfigure(encoding='utf-8')

FRONTEND_DIR = os.path.join(os.path.dirname(__file__), '..', 'frontend')

pages = [
    'index.html',
    'facebook-video-downloader.html',
    'instagram-video-downloader.html',
    'snapchat-video-downloader.html',
    'youtube-video-downloader.html',
    'tiktok-video-downloader.html',
    'threads-video-downloader.html',
    'about.html',
    'privacy.html',
    'terms.html'
]

print("=" * 75)
print("COMPREHENSIVE SEO, SCHEMA & ACCESSIBILITY AUDIT (STANDARD LIB)")
print("=" * 75)

all_passed = True

for page in pages:
    filepath = os.path.join(FRONTEND_DIR, page)
    if not os.path.exists(filepath):
        print(f"[FAIL] [MISSING FILE]: {page}")
        all_passed = False
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    print(f"\nAuditing: {page}")

    # 1. Title Tag
    title_match = re.search(r'<title>(.*?)</title>', html, re.DOTALL | re.IGNORECASE)
    if title_match and title_match.group(1).strip():
        title_text = title_match.group(1).strip()
        print(f"  [PASS] Title ({len(title_text)} chars): {title_text[:65]}...")
    else:
        print(f"  [FAIL] Missing or empty <title>")
        all_passed = False

    # 2. Meta Description
    meta_desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', html, re.IGNORECASE)
    if not meta_desc_match:
        meta_desc_match = re.search(r'<meta\s+content=["\'](.*?)["\']\s+name=["\']description["\']', html, re.IGNORECASE)
    if meta_desc_match:
        desc_text = meta_desc_match.group(1).strip()
        print(f"  [PASS] Meta Description ({len(desc_text)} chars): {desc_text[:65]}...")
    else:
        print(f"  [FAIL] Missing <meta name='description'>")
        all_passed = False

    # 3. Canonical Link
    canonical_match = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\'](.*?)["\']', html, re.IGNORECASE)
    if canonical_match:
        print(f"  [PASS] Canonical: {canonical_match.group(1)}")
    else:
        print(f"  [FAIL] Missing canonical tag")
        all_passed = False

    # 4. OpenGraph Tags
    og_title_match = re.search(r'<meta\s+property=["\']og:title["\']', html, re.IGNORECASE)
    og_img_match = re.search(r'<meta\s+property=["\']og:image["\']', html, re.IGNORECASE)
    if og_title_match and og_img_match:
        print(f"  [PASS] OpenGraph Tags Present (og:title & og:image)")
    else:
        print(f"  [FAIL] Missing OpenGraph tags")
        all_passed = False

    # 5. Schema.org JSON-LD Validation
    json_ld_matches = re.findall(r'<script\s+type=["\']application/ld\+json["\']>(.*?)</script>', html, re.DOTALL | re.IGNORECASE)
    if json_ld_matches:
        valid_schemas = []
        for raw_json in json_ld_matches:
            try:
                data = json.loads(raw_json.strip())
                if '@graph' in data:
                    types = [item.get('@type') for item in data['@graph']]
                    valid_schemas.extend(types)
                elif '@type' in data:
                    valid_schemas.append(data['@type'])
            except Exception as e:
                print(f"  [FAIL] Invalid JSON-LD syntax: {e}")
                all_passed = False
        print(f"  [PASS] JSON-LD Schemas: {', '.join(valid_schemas)}")
    else:
        print(f"  [FAIL] No JSON-LD Structured Data Found")
        all_passed = False

    # 6. Check interactive IDs on downloader pages
    if 'downloader' in page or page == 'index.html':
        required_ids = ['videoUrl', 'downloadBtn', 'resultCard', 'videoPreview', 'brandOrbit', 'orbitCenterBtn']
        missing_ids = [rid for rid in required_ids if f'id="{rid}"' not in html and f"id='{rid}'" not in html]
        if not missing_ids:
            print(f"  [PASS] All Required Downloader DOM IDs Present ({', '.join(required_ids)})")
        else:
            print(f"  [FAIL] Missing DOM IDs: {missing_ids}")
            all_passed = False

    # 7. Check Footer Tools Section
    if 'footer-tools-section' in html and 'tool-pill' in html:
        pills_count = len(re.findall(r'class=["\'][^"\']*tool-pill[^"\']*["\']', html))
        print(f"  [PASS] Footer 'Other Tools' Section Present with {pills_count} Tool Links")
    else:
        print(f"  [FAIL] Missing footer-tools-section")
        all_passed = False

print("\n" + "=" * 75)
if all_passed:
    print(f"\nALL {len(pages)} PAGES PASSED 100% SEO, SCHEMA & DOM VALIDATION CHECKS!")
else:
    print("\n[ERROR] SOME PAGES FAILED VALIDATION!")
    sys.exit(1)
print("=" * 75)
