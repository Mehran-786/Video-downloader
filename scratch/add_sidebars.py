import glob, re

sidebar_html = '''
<div class="sidebar mobile-nav" id="sidebar">
    <div class="close-btn" id="closeBtn" aria-label="Close Menu"><i class="fas fa-times"></i></div>
    <ul class="menu-links" style="margin-top: 60px;">
        <li class="sidebar-theme-item" style="padding: 15px 20px;">
            <div class="theme-segmented-control" data-theme-switcher style="width: 100%;">
                <div class="theme-pill"></div>
                <button type="button" class="theme-btn" data-theme-val="premium" aria-label="Premium Mode" title="Premium Mode">
                    <i class="fas fa-crown"></i> <span>Premium</span>
                </button>
                <button type="button" class="theme-btn active" data-theme-val="dark" aria-label="Dark Mode" title="Dark Mode">
                    <i class="fas fa-moon"></i> <span>Dark</span>
                </button>
                <button type="button" class="theme-btn" data-theme-val="light" aria-label="Light Mode" title="Light Mode">
                    <i class="fas fa-sun"></i> <span>Light</span>
                </button>
            </div>
        </li>
        <li><a href="../index.html"><i class="fas fa-home"></i> <span data-key="homeBtn">Home</span></a></li>
        <li><a href="../private-downloader/index.html"><i class="fas fa-user-lock"></i> <span>Private Downloader</span></a></li>
        <li><a href="#"><i class="fas fa-puzzle-piece"></i> <span data-key="extBtn">Extension</span> <span class="soon-badge" data-key="soonBadge" style="margin-left: 10px;">Soon</span></a></li>

        <li class="dropdown">
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
        </li>
    </ul>
</div>'''

for f in sorted(glob.glob('frontend/**/*.html', recursive=True)):
    with open(f, 'r', encoding='utf-8') as fp:
        html = fp.read()
    
    if 'mobile-top-bar' in html and 'id="sidebar"' not in html:
        # insert right after the mobile-top-bar closing </div>
        # Find closing </div> of <div class="mobile-top-bar ...>
        idx = html.find('class="mobile-top-bar')
        if idx != -1:
            # find end of this top-bar div
            # usually ends after nav-brand-container or nav-brand-home </div></div>
            # Let's find </nav-brand-home> or <div class="nav-brand-container"> ... </div>\s*</div>
            m = re.search(r'(<div class="mobile-top-bar[^>]*>.*?</div>\s*</div>)', html, re.DOTALL)
            if m:
                end_pos = m.end()
                new_html = html[:end_pos] + sidebar_html + html[end_pos:]
                with open(f, 'w', encoding='utf-8') as fp:
                    fp.write(new_html)
                print(f"Added sidebar to: {f}")
            else:
                print(f"Could not find end of mobile-top-bar in {f}")

print("Sidebar addition complete.")
