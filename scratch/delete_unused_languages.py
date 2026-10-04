# scratch/delete_unused_languages.py
# Permanently removes all unused language files across all 10 locale directories.

import os

KEEP_LANGUAGES = {'en', 'es', 'pt', 'de', 'fr', 'it'}

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

deleted_count = 0
for d in DEST_DIRS:
    if not os.path.exists(d):
        continue
    for fname in os.listdir(d):
        if fname.endswith('.json'):
            lang_code = fname[:-5]
            if lang_code not in KEEP_LANGUAGES:
                fpath = os.path.join(d, fname)
                try:
                    os.remove(fpath)
                    print(f"Deleted: {fpath}")
                    deleted_count += 1
                except Exception as e:
                    print(f"Error deleting {fpath}: {e}")

print(f"\nTotal unused language files deleted: {deleted_count}")

# Verify remaining files in each directory
print("\nRemaining files in each locale directory:")
for d in DEST_DIRS:
    if os.path.exists(d):
        files = sorted(os.listdir(d))
        print(f"{os.path.basename(os.path.dirname(d)) or 'root'}/locales: {files}")
