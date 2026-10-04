import json, glob, os

locales = glob.glob('frontend/**/locales/*.json', recursive=True)
print(f"Found {len(locales)} locale files.")

expected_keys = [
    'seo', 'common', 'notifications', 'index', 'facebook', 'instagram',
    'tiktok', 'youtube', 'snapchat', 'threads', 'private', 'about',
    'features', 'contact', 'privacy', 'terms'
]

errors = 0
for loc in locales:
    try:
        data = json.load(open(loc, encoding='utf-8'))
        missing = [k for k in expected_keys if k not in data]
        if missing:
            print(f"ERROR in {loc}: missing keys {missing}")
            errors += 1
    except Exception as e:
        print(f"PARSE ERROR in {loc}: {e}")
        errors += 1

if errors == 0:
    print(f"ALL {len(locales)} locale files are 100% valid with all {len(expected_keys)} required top-level keys!")
else:
    print(f"Found {errors} errors.")
