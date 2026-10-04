import glob

missing_desktop_lang = []
missing_mobile_lang = []
all_files = sorted(glob.glob('frontend/**/*.html', recursive=True))

for f in all_files:
    with open(f, encoding='utf-8') as fp:
        c = fp.read()
    if 'desktopLangToggle' not in c:
        missing_desktop_lang.append(f)
    if 'mobileLangToggle' not in c:
        missing_mobile_lang.append(f)

print(f"Total HTML files: {len(all_files)}")
print(f"Missing desktop lang ({len(missing_desktop_lang)}):")
for f in missing_desktop_lang:
    print("  ", f)
print(f"Missing mobile lang ({len(missing_mobile_lang)}):")
for f in missing_mobile_lang:
    print("  ", f)
