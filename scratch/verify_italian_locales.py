# scratch/verify_italian_locales.py
import os, json

DEST_DIRS = [
    r'c:\my folder\Pictures\Desktop\downsocial\frontend\locales',
    r'c:\my folder\Pictures\Desktop\downsocial\frontend\shared\locales',
    r'c:\my folder\Pictures\Desktop\downsocial\frontend\facebook-downloader\locales',
    r'c:\my folder\Pictures\Desktop\downsocial\frontend\instagram-downloader\locales',
    r'c:\my folder\Pictures\Desktop\downsocial\frontend\tiktok-downloader\locales',
    r'c:\my folder\Pictures\Desktop\downsocial\frontend\youtube-downloader\locales',
    r'c:\my folder\Pictures\Desktop\downsocial\frontend\snapchat-downloader\locales',
    r'c:\my folder\Pictures\Desktop\downsocial\frontend\threads-downloader\locales',
    r'c:\my folder\Pictures\Desktop\downsocial\frontend\universal-downloader\locales',
    r'c:\my folder\Pictures\Desktop\downsocial\frontend\private-downloader\locales'
]

TARGET_LANGS = {'en', 'es', 'pt', 'de', 'fr', 'it'}

print("--- 1. Check directory contents (Must strictly be 6 languages) ---")
all_strict = True
for d in DEST_DIRS:
    files = set(f[:-5] for f in os.listdir(d) if f.endswith('.json'))
    if files != TARGET_LANGS:
        print(f"FAILED in {d}: found {files}")
        all_strict = False
    else:
        print(f"OK: {os.path.basename(os.path.dirname(d)) or 'root'}/locales has exact 6 target languages: {sorted(files)}")

if all_strict:
    print("SUCCESS: All 10 directories have strictly and only the 6 target languages!")

print("\n--- 2. Inspect Italian ('it.json') structure & SEO/AEO/GEO depth ---")
root_it_path = os.path.join(DEST_DIRS[0], "it.json")
with open(root_it_path, "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"Total top-level keys in it.json: {list(data.keys())}")
print(f"Common langBtn: {data['common']['langBtn']}")
print(f"Common downloadBtn: {data['common']['downloadBtn']}")

platforms = ['index', 'facebook', 'instagram', 'tiktok', 'youtube', 'snapchat', 'threads']
for p in platforms:
    p_data = data.get(p, {})
    art = p_data.get('seoArticle', '')
    title = p_data.get('title', '')
    qa = "Risposta" in art or "qa_title" in art or "quick-answer" in art
    table = "<table" in art
    print(f"Platform [{p}]: Title='{title[:35]}...' | Article Length={len(art)} chars | AEO Quick Answer={qa} | GEO Table={table}")

print("\n--- 3. Static pages in it.json ---")
for sp in ['about', 'features', 'contact', 'privacy', 'terms']:
    sp_data = data.get(sp, {})
    content = sp_data.get('content', '') or sp_data.get('pageHtml', '')
    print(f"Static [{sp}]: Length={len(content)} chars")
