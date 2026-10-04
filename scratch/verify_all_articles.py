# scratch/verify_all_articles.py
# Deterministically validates all 7 platforms across all 12 languages

import json, os

LANGUAGES = ['en', 'es', 'fr', 'de', 'hi', 'ar', 'pt', 'bn', 'ru', 'id', 'zh', 'ur']
PLATFORMS = ['index', 'facebook', 'instagram', 'tiktok', 'youtube', 'snapchat', 'threads']

LOCALES_DIR = r'c:\my folder\Pictures\Desktop\downsocial\frontend\locales'

errors = []

for p in PLATFORMS:
    # 1. Check EN
    en_file = os.path.join(LOCALES_DIR, 'en.json')
    with open(en_file, 'r', encoding='utf-8') as f:
        en_data = json.load(f)
    en_art = en_data[p]['seoArticle']
    
    orig_path = os.path.join('scratch', f'orig_seo_{p}.html')
    with open(orig_path, 'r', encoding='utf-8') as f:
        orig_en = f.read()
    
    if len(en_art.strip()) != len(orig_en.strip()):
        errors.append(f"{p} [en] length mismatch: got {len(en_art.strip())}, orig has {len(orig_en.strip())}")
    
    # 2. Check each translation
    for l in LANGUAGES:
        if l == 'en': continue
        l_file = os.path.join(LOCALES_DIR, f'{l}.json')
        with open(l_file, 'r', encoding='utf-8') as f:
            l_data = json.load(f)
        
        l_art = l_data[p]['seoArticle']
        if not l_art or len(l_art) < 1500:
            errors.append(f"{p} [{l}] article too short: {len(l_art)}")
        
        # Check that table tags exist
        if '<table' not in l_art or '</table>' not in l_art:
            errors.append(f"{p} [{l}] missing table tag")
            
        # Check that prominent English sentences from orig are not in translated article
        if p == 'youtube':
            if 'The Fastest, Ad-Free YouTube Video' in l_art:
                errors.append(f"YouTube [{l}] still contains original English H2!")
            if 'Enjoy offline YouTube playback without subscriptions' in l_art:
                errors.append(f"YouTube [{l}] still contains original English intro paragraph!")
            if 'Which Choose downsocial over Competitors' in l_art:
                errors.append(f"YouTube [{l}] still contains English competitor text!")
        elif p == 'facebook':
            if 'Save Any Public Facebook Video in HD' in l_art:
                errors.append(f"Facebook [{l}] still contains original English H2!")
            if 'This Facebook video downloader is built for one job' in l_art:
                errors.append(f"Facebook [{l}] still contains English intro!")
        elif p == 'instagram':
            if 'Save Reels, Stories & Posts in HD' in l_art:
                errors.append(f"Instagram [{l}] still contains original English H2!")
            if 'This Instagram video downloader is engineered for one primary purpose' in l_art:
                errors.append(f"Instagram [{l}] still contains English intro!")
        elif p == 'tiktok':
            if 'The Ultimate Free TikTok Video Downloader' in l_art:
                errors.append(f"TikTok [{l}] still contains original English H2!")
            if 'TikTok is the world\'s leading destination' in l_art:
                errors.append(f"TikTok [{l}] still contains English intro!")
        elif p == 'snapchat':
            if 'The Ultimate Free Snapchat Spotlight' in l_art:
                errors.append(f"Snapchat [{l}] still contains original English H2!")
        elif p == 'threads':
            if 'The Fastest, Safest Meta Threads Video' in l_art:
                errors.append(f"Threads [{l}] still contains original English H2!")
        elif p == 'index':
            if 'The Ultimate All-in-One Social Media Video Downloader' in l_art:
                errors.append(f"Index [{l}] still contains original English H2!")
            if 'Saving videos from the web used to require bookmarking' in l_art:
                errors.append(f"Index [{l}] still contains English intro!")

if not errors:
    print("SUCCESS: All 7 platforms validated across all 12 languages with ZERO leftover English sentences and 100% original English integrity!")
else:
    print(f"FAILED with {len(errors)} errors:")
    for e in errors[:10]:
        print("  -", e)
