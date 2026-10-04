import os, re

frontend_dir = r"c:\my folder\Pictures\Desktop\downsocial\frontend"

pattern_btn_premium = re.compile(
    r'(<button\s+type="button"\s+class="theme-btn[^"]*"\s+data-theme-val="premium"[^>]*>)\s*<i\s+class="fas\s+fa-crown"></i>\s*<span>Premium</span>\s*(</button>)',
    re.IGNORECASE
)
pattern_btn_dark = re.compile(
    r'(<button\s+type="button"\s+class="theme-btn[^"]*"\s+data-theme-val="dark"[^>]*>)\s*<i\s+class="fas\s+fa-moon"></i>\s*<span>Dark</span>\s*(</button>)',
    re.IGNORECASE
)
pattern_btn_light = re.compile(
    r'(<button\s+type="button"\s+class="theme-btn[^"]*"\s+data-theme-val="light"[^>]*>)\s*<i\s+class="fas\s+fa-sun"></i>\s*<span>Light</span>\s*(</button>)',
    re.IGNORECASE
)

# Pattern for Features in desktop nav
pattern_features_root = re.compile(
    r'<li><a\s+href="features\.html"[^>]*><i\s+class="fas\s+fa-layer-group"></i>\s*<span>Features</span></a></li>\s*',
    re.IGNORECASE
)
pattern_features_sub = re.compile(
    r'<li><a\s+href="\.\./features\.html"[^>]*><i\s+class="fas\s+fa-layer-group"></i>\s*<span>Features</span></a></li>\s*',
    re.IGNORECASE
)

updated_count = 0

for root, dirs, files in os.walk(frontend_dir):
    for f in files:
        if f.endswith(".html"):
            fpath = os.path.join(root, f)
            with open(fpath, "r", encoding="utf-8") as fp:
                content = fp.read()

            new_content = content

            # Only target desktop nav for removing text inside theme-btn
            # The desktop nav is between <nav class="top-nav desktop-nav"> and </nav>
            nav_match = re.search(r'(<nav\s+class="top-nav\s+desktop-nav"[^>]*>[\s\S]*?</nav>)', new_content, re.IGNORECASE)
            if nav_match:
                desktop_nav_html = nav_match.group(1)
                orig_nav_html = desktop_nav_html

                # Remove text in desktop nav theme buttons
                desktop_nav_html = pattern_btn_premium.sub(r'\1<i class="fas fa-crown"></i>\2', desktop_nav_html)
                desktop_nav_html = pattern_btn_dark.sub(r'\1<i class="fas fa-moon"></i>\2', desktop_nav_html)
                desktop_nav_html = pattern_btn_light.sub(r'\1<i class="fas fa-sun"></i>\2', desktop_nav_html)

                # Remove Features button from desktop nav
                desktop_nav_html = pattern_features_root.sub('', desktop_nav_html)
                desktop_nav_html = pattern_features_sub.sub('', desktop_nav_html)

                if desktop_nav_html != orig_nav_html:
                    new_content = new_content[:nav_match.start(1)] + desktop_nav_html + new_content[nav_match.end(1):]

            if new_content != content:
                with open(fpath, "w", encoding="utf-8") as fp:
                    fp.write(new_content)
                print(f"Cleaned header in: {os.path.relpath(fpath, frontend_dir)}")
                updated_count += 1

print(f"Total files updated: {updated_count}")
