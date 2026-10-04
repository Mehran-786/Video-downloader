# scratch/update_html_dropdowns.py
import os, re, base64, shutil

SCRATCH_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = r"c:\my folder\Pictures\Desktop\downsocial\frontend"
FLAGS_DIR = os.path.join(FRONTEND_DIR, "assets", "flags")

LANGS = ['en', 'es', 'pt', 'de', 'fr', 'it']
LANG_LABELS = {
    'en': 'English',
    'es': 'Español',
    'pt': 'Português',
    'de': 'Deutsch',
    'fr': 'Français',
    'it': 'Italian'
}

# 1. Read flags and create base64 data URIs
FLAG_DATA = {}
for l in LANGS:
    fpath = os.path.join(FLAGS_DIR, f"{l}.svg")
    with open(fpath, "rb") as f:
        b64 = base64.b64encode(f.read()).decode('utf-8')
        FLAG_DATA[l] = f"data:image/svg+xml;base64,{b64}"

print("Loaded 6 flags as base64 data URIs.")

# 2. Copy flag files to other common paths for maximum resilience
extra_flag_dirs = [
    os.path.join(FRONTEND_DIR, "flags"),
    os.path.join(FRONTEND_DIR, "shared", "flags")
]
for p in ['facebook-downloader', 'instagram-downloader', 'tiktok-downloader',
          'youtube-downloader', 'snapchat-downloader', 'threads-downloader',
          'universal-downloader', 'private-downloader']:
    extra_flag_dirs.append(os.path.join(FRONTEND_DIR, p, "flags"))

for ed in extra_flag_dirs:
    os.makedirs(ed, exist_ok=True)
    for l in LANGS:
        shutil.copy2(os.path.join(FLAGS_DIR, f"{l}.svg"), os.path.join(ed, f"{l}.svg"))

print(f"Copied flag SVGs to {len(extra_flag_dirs)} directories.")

# 3. Construct clean dropdown HTML
desktop_items = []
mobile_items = []
for l in LANGS:
    lbl = LANG_LABELS[l]
    src = FLAG_DATA[l]
    desktop_items.append(f'                <li><a href="#" onclick="changeLanguage(\'{l}\')"><img src="{src}" class="lang-flag" alt="{lbl}"> {lbl}</a></li>')
    mobile_items.append(f'                <li><a href="#" onclick="changeLanguage(\'{l}\')"><img src="{src}" class="lang-flag" alt="{lbl}"> {lbl}</a></li>')

new_desktop_menu = '<ul class="dropdown-menu" id="desktopLangMenu">\n' + '\n'.join(desktop_items) + '\n            </ul>'
new_mobile_menu = '<ul class="dropdown-menu-mobile" id="mobileLangMenu">\n' + '\n'.join(mobile_items) + '\n            </ul>'

new_desktop_toggle = f'<a href="#" id="desktopLangToggle"><img src="{FLAG_DATA["en"]}" class="lang-flag active-lang-flag" alt="Language"> <span data-key="langBtn">Language</span> <i class="fas fa-caret-down"></i></a>'
new_mobile_toggle = f'<a href="#" id="mobileLangToggle"><img src="{FLAG_DATA["en"]}" class="lang-flag active-lang-flag" alt="Language"> <span data-key="langBtn">Language</span> <i class="fas fa-caret-down" style="margin-left:auto;"></i></a>'

# 4. Update all 50 HTML files
html_files = []
for root, dirs, files in os.walk(FRONTEND_DIR):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

desktop_re = re.compile(r'<ul\s+class="dropdown-menu"\s+id="desktopLangMenu">.*?</ul>', re.DOTALL)
mobile_re = re.compile(r'<ul\s+class="dropdown-menu-mobile"\s+id="mobileLangMenu">.*?</ul>', re.DOTALL)
desktop_toggle_re = re.compile(r'<a\s+href="#"\s+id="desktopLangToggle">.*?</a>', re.DOTALL)
mobile_toggle_re = re.compile(r'<a\s+href="#"\s+id="mobileLangToggle">.*?</a>', re.DOTALL)

updated_count = 0
for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()

    orig_html = html
    html = desktop_re.sub(new_desktop_menu, html)
    html = mobile_re.sub(new_mobile_menu, html)
    html = desktop_toggle_re.sub(new_desktop_toggle, html)
    html = mobile_toggle_re.sub(new_mobile_toggle, html)

    if html != orig_html:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(html)
        updated_count += 1

print(f"Updated dropdown menus & toggles in {updated_count}/{len(html_files)} HTML files!")

# 5. Update style.css and shared/style.css
css_flag_rules = """
/* Flag icons in language dropdowns matching user design */
.lang-flag {
    width: 20px;
    height: 14px;
    border-radius: 2px;
    object-fit: cover;
    display: inline-block;
    vertical-align: middle;
    box-shadow: 0 1px 3px rgba(0,0,0,0.25);
    flex-shrink: 0;
}
.active-lang-flag {
    margin-right: 6px;
}
.dropdown-menu li a, .dropdown-menu-mobile li a {
    display: flex !important;
    align-items: center !important;
    gap: 10px !important;
}
"""

css_paths = [
    os.path.join(FRONTEND_DIR, "style.css"),
    os.path.join(FRONTEND_DIR, "shared", "style.css")
]

for cp in css_paths:
    if os.path.exists(cp):
        with open(cp, 'r', encoding='utf-8') as f:
            content = f.read()
        if ".lang-flag" not in content:
            content += "\n" + css_flag_rules
            with open(cp, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Added flag CSS to {cp}")
        else:
            print(f"CSS already contains .lang-flag in {cp}")

# 6. Update script.js and shared/script.js to dynamically switch active flag icon
js_flag_map_code = f"""
        // Dynamic Active Flag Icon Update
        const flagMap = {repr(FLAG_DATA)};
        if (flagMap[lang]) {{
            document.querySelectorAll('.active-lang-flag').forEach(img => {{
                img.src = flagMap[lang];
                img.alt = lang;
            }});
        }}
"""

js_paths = [
    os.path.join(FRONTEND_DIR, "script.js"),
    os.path.join(FRONTEND_DIR, "shared", "script.js")
]

for jp in js_paths:
    if os.path.exists(jp):
        with open(jp, 'r', encoding='utf-8') as f:
            js = f.read()
        if "Dynamic Active Flag Icon Update" not in js:
            target = "document.body.setAttribute('dir', isRtl ? 'rtl' : 'ltr');"
            replacement = target + "\n" + js_flag_map_code
            js = js.replace(target, replacement, 1)
            with open(jp, 'w', encoding='utf-8') as f:
                f.write(js)
            print(f"Added active flag switcher to {jp}")
        else:
            print(f"Active flag switcher already present in {jp}")

print("All updates completed successfully!")
