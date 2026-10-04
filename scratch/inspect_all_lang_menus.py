# scratch/inspect_all_lang_menus.py
import os, glob, re

html_files = []
for root, dirs, files in os.walk(r"c:\my folder\Pictures\Desktop\downsocial\frontend"):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

desktop_matches = 0
mobile_matches = 0

desktop_pattern = re.compile(r'<ul\s+class="dropdown-menu"\s+id="desktopLangMenu">.*?</ul>', re.DOTALL)
mobile_pattern = re.compile(r'<ul\s+class="dropdown-menu-mobile"\s+id="mobileLangMenu">.*?</ul>', re.DOTALL)

for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    if desktop_pattern.search(content):
        desktop_matches += 1
    else:
        print(f"Missing desktop match: {fpath}")
    if mobile_pattern.search(content):
        mobile_matches += 1
    else:
        print(f"Missing mobile match: {fpath}")

print(f"Total HTML files: {len(html_files)}")
print(f"Desktop matches: {desktop_matches}")
print(f"Mobile matches: {mobile_matches}")
