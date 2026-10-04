import json
import os

locales_dir = r"c:\my folder\Pictures\Desktop\downsocial\frontend\facebook-downloader\locales"
en_path = os.path.join(locales_dir, "en.json")

with open(en_path, "r", encoding="utf-8") as f:
    en_data = json.load(f)

def get_keys(d, prefix=""):
    keys = set()
    for k, v in d.items():
        curr_key = f"{prefix}.{k}" if prefix else k
        keys.add(curr_key)
        if isinstance(v, dict):
            keys.update(get_keys(v, curr_key))
    return keys

en_keys = get_keys(en_data)
print(f"Base en.json has {len(en_keys)} total nested keys.")

languages = ["ar", "bn", "de", "es", "fr", "hi", "id", "pt", "ru", "ur", "zh"]
all_valid = True

for lang in languages:
    fpath = os.path.join(locales_dir, f"{lang}.json")
    if not os.path.exists(fpath):
        print(f"ERROR: Missing {lang}.json")
        all_valid = False
        continue
    try:
        with open(fpath, "r", encoding="utf-8") as f:
            data = json.load(f)
        lang_keys = get_keys(data)
        missing = en_keys - lang_keys
        extra = lang_keys - en_keys
        if missing:
            print(f"ERROR: {lang}.json is missing keys: {missing}")
            all_valid = False
        if extra:
            print(f"ERROR: {lang}.json has extra keys: {extra}")
            all_valid = False
        if not missing and not extra:
            print(f"PASS: {lang}.json matches en.json structure 100% ({len(lang_keys)} keys).")
    except Exception as e:
        print(f"ERROR: Could not parse {lang}.json: {e}")
        all_valid = False

if all_valid:
    print("ALL 11 LOCALE FILES ARE 100% VALID AND IN PERFECT SYNC WITH EN.JSON!")
else:
    print("VALIDATION FAILED!")
