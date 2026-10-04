import glob, re

desktop_lang_html = '''        <li class="dropdown">
            <a href="#" id="desktopLangToggle"><i class="fas fa-globe"></i> <span data-key="langBtn">Language</span> <i class="fas fa-caret-down"></i></a>
            <ul class="dropdown-menu" id="desktopLangMenu">
                <li><a href="#" onclick="changeLanguage('en')">English</a></li>
                <li><a href="#" onclick="changeLanguage('es')">Español (Spanish)</a></li>
                <li><a href="#" onclick="changeLanguage('fr')">Français (French)</a></li>
                <li><a href="#" onclick="changeLanguage('de')">Deutsch (German)</a></li>
                <li><a href="#" onclick="changeLanguage('hi')">हिन्दी (Hindi)</a></li>
                <li><a href="#" onclick="changeLanguage('ar')">العربية (Arabic)</a></li>
                <li><a href="#" onclick="changeLanguage('pt')">Português (Portuguese)</a></li>
                <li><a href="#" onclick="changeLanguage('bn')">বাংলা (Bengali)</a></li>
                <li><a href="#" onclick="changeLanguage('ru')">Русский (Russian)</a></li>
                <li><a href="#" onclick="changeLanguage('id')">Bahasa Indonesia</a></li>
                <li><a href="#" onclick="changeLanguage('zh')">中文 (Chinese)</a></li>
                <li><a href="#" onclick="changeLanguage('ur')">اردو (Urdu)</a></li>
            </ul>
        </li>'''

mobile_lang_html = '''        <li class="dropdown">
            <a href="#" id="mobileLangToggle"><i class="fas fa-globe"></i> <span data-key="langBtn">Language</span> <i class="fas fa-caret-down" style="margin-left:auto;"></i></a>
            <ul class="dropdown-menu-mobile" id="mobileLangMenu">
                <li><a href="#" onclick="changeLanguage('en')">English</a></li>
                <li><a href="#" onclick="changeLanguage('es')">Español (Spanish)</a></li>
                <li><a href="#" onclick="changeLanguage('fr')">Français (French)</a></li>
                <li><a href="#" onclick="changeLanguage('de')">Deutsch (German)</a></li>
                <li><a href="#" onclick="changeLanguage('hi')">हिन्दी (Hindi)</a></li>
                <li><a href="#" onclick="changeLanguage('ar')">العربية (Arabic)</a></li>
                <li><a href="#" onclick="changeLanguage('pt')">Português (Portuguese)</a></li>
                <li><a href="#" onclick="changeLanguage('bn')">বাংলা (Bengali)</a></li>
                <li><a href="#" onclick="changeLanguage('ru')">Русский (Russian)</a></li>
                <li><a href="#" onclick="changeLanguage('id')">Bahasa Indonesia</a></li>
                <li><a href="#" onclick="changeLanguage('zh')">中文 (Chinese)</a></li>
                <li><a href="#" onclick="changeLanguage('ur')">اردو (Urdu)</a></li>
            </ul>
        </li>'''

all_files = sorted(glob.glob('frontend/**/*.html', recursive=True))

for f in all_files:
    with open(f, 'r', encoding='utf-8') as fp:
        html = fp.read()
    
    changed = False
    
    # 1. Desktop Nav
    if 'desktopLangToggle' not in html:
        # insert before the closing </ul> of desktop nav
        # look for <nav class="top-nav desktop-nav"> ... <ul class="nav-links"> ... </ul>
        nav_pattern = r'(<nav[^>]*desktop-nav[^>]*>.*?<ul class="nav-links">)(.*?)(</ul>\s*</nav>)'
        m = re.search(nav_pattern, html, re.DOTALL)
        if m:
            new_nav = m.group(1) + m.group(2) + '\n' + desktop_lang_html + '\n    ' + m.group(3)
            html = html[:m.start()] + new_nav + html[m.end():]
            changed = True
        else:
            print(f"Warning: Could not match desktop nav in {f}")

    # 2. Mobile Sidebar
    if 'mobileLangToggle' not in html:
        sidebar_pattern = r'(<div[^>]*id="sidebar"[^>]*>.*?<ul class="menu-links"[^>]*>)(.*?)(</ul>\s*</div>)'
        m = re.search(sidebar_pattern, html, re.DOTALL)
        if m:
            new_sidebar = m.group(1) + m.group(2) + '\n' + mobile_lang_html + '\n    ' + m.group(3)
            html = html[:m.start()] + new_sidebar + html[m.end():]
            changed = True
        else:
            print(f"Warning: Could not match sidebar in {f}")
            
    if changed:
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(html)
        print(f"Added language dropdowns to: {f}")

print("Done updating language dropdowns.")
