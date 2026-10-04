import os

root_dir = r"c:\my folder\Pictures\Desktop\downsocial\frontend"

# ==========================================
# 1. Update frontend/index.html
# ==========================================
index_path = os.path.join(root_dir, "index.html")
with open(index_path, "r", encoding="utf-8") as f:
    c = f.read()

if "private-downloader/index.html" not in c:
    target_dt = '<li><a href="features.html"><i class="fas fa-layer-group"></i> <span>Features</span></a></li>'
    repl_dt = '<li><a href="private-downloader/index.html"><i class="fas fa-user-lock"></i> <span>Private Downloader</span></a></li>\n        ' + target_dt
    c = c.replace(target_dt, repl_dt, 1)

    target_mb = '<li><a href="index.html"><i class="fas fa-home"></i> <span data-key="homeBtn">Home</span></a></li>'
    repl_mb = target_mb + '\n        <li><a href="private-downloader/index.html"><i class="fas fa-user-lock"></i> <span>Private Downloader</span></a></li>'
    c = c.replace(target_mb, repl_mb, 1)

    target_ft = '<a href="threads-downloader/index.html" class="tool-pill th-pill">'
    repl_ft = '<a href="private-downloader/index.html" class="tool-pill" style="border-color: var(--accent-blue);"><i class="fas fa-user-lock"></i> <span>Private</span></a>\n        ' + target_ft
    c = c.replace(target_ft, repl_ft, 1)

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(c)
    print("Updated index.html")
else:
    print("index.html already has private link")

# ==========================================
# 2. Update root subpages: features, about, contact, privacy, terms
# ==========================================
root_subpages = ["features.html", "about.html", "contact.html", "privacy.html", "terms.html"]

for sp in root_subpages:
    sp_path = os.path.join(root_dir, sp)
    if not os.path.exists(sp_path):
        continue
    with open(sp_path, "r", encoding="utf-8") as f:
        content = f.read()

    modified = False

    # Desktop nav
    if 'href="private-downloader/index.html"' not in content:
        # Check if desktop nav has theme-switcher-wrapper
        if '</li>\n    </ul>\n</nav>' in content:
            dt_insert = '        <li><a href="private-downloader/index.html"><i class="fas fa-user-lock"></i> <span>Private Downloader</span></a></li>\n    </ul>\n</nav>'
            content = content.replace('</li>\n    </ul>\n</nav>', '</li>\n' + dt_insert, 1)
            modified = True
        elif '</li>\r\n    </ul>\r\n</nav>' in content:
            dt_insert = '        <li><a href="private-downloader/index.html"><i class="fas fa-user-lock"></i> <span>Private Downloader</span></a></li>\r\n    </ul>\r\n</nav>'
            content = content.replace('</li>\r\n    </ul>\r\n</nav>', '</li>\r\n' + dt_insert, 1)
            modified = True

    # Mobile sidebar
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
        <li><a href="index.html"><i class="fas fa-home"></i> <span>Home</span></a></li>
        <li><a href="private-downloader/index.html"><i class="fas fa-user-lock"></i> <span>Private Downloader</span></a></li>
        <li><a href="features.html"><i class="fas fa-layer-group"></i> <span>Features</span></a></li>
        <li><a href="about.html"><i class="fas fa-info-circle"></i> <span>About Us</span></a></li>
        <li><a href="contact.html"><i class="fas fa-envelope"></i> <span>Contact</span></a></li>
    </ul>
</div>
'''
    if 'id="sidebar"' not in content:
        # Insert sidebar right after mobile-top-bar
        if '</div>\n</div>\n\n<div class="page-content-wrapper">' in content:
            content = content.replace('</div>\n</div>\n\n<div class="page-content-wrapper">', '</div>\n</div>\n' + sidebar_html + '\n<div class="page-content-wrapper">', 1)
            modified = True
        elif '</div>\r\n</div>\r\n\r\n<div class="page-content-wrapper">' in content:
            content = content.replace('</div>\r\n</div>\r\n\r\n<div class="page-content-wrapper">', '</div>\r\n</div>\r\n' + sidebar_html + '\r\n<div class="page-content-wrapper">', 1)
            modified = True
        elif '</div>\n</div>\n\n<main class="page-container"' in content:
            content = content.replace('</div>\n</div>\n\n<main class="page-container"', '</div>\n</div>\n' + sidebar_html + '\n<main class="page-container"', 1)
            modified = True
        elif '</div>\r\n</div>\r\n\r\n<main class="page-container"' in content:
            content = content.replace('</div>\r\n</div>\r\n\r\n<main class="page-container"', '</div>\r\n</div>\r\n' + sidebar_html + '\r\n<main class="page-container"', 1)
            modified = True

    # Footer tools grid
    if 'href="private-downloader/index.html"' not in content and '<div class="footer-tools-grid">' in content:
        content = content.replace(
            '<div class="footer-tools-grid">',
            '<div class="footer-tools-grid">\n        <a href="private-downloader/index.html" class="tool-pill" style="border-color: var(--accent-blue);"><i class="fas fa-user-lock"></i> <span>Private</span></a>',
            1
        )
        modified = True

    if modified:
        with open(sp_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated root subpage: {sp}")
    else:
        print(f"Root subpage {sp} skipped or unchanged")

# ==========================================
# 3. Update platform pages: facebook, instagram, tiktok, youtube, snapchat, threads, universal
# ==========================================
platform_dirs = [
    "facebook-downloader",
    "instagram-downloader",
    "tiktok-downloader",
    "youtube-downloader",
    "snapchat-downloader",
    "threads-downloader",
    "universal-downloader"
]

for pdir in platform_dirs:
    p_path = os.path.join(root_dir, pdir, "index.html")
    if not os.path.exists(p_path):
        continue
    with open(p_path, "r", encoding="utf-8") as f:
        content = f.read()

    modified = False

    # Desktop nav
    if 'href="../private-downloader/index.html"' not in content and 'href="private-downloader/index.html"' not in content:
        # Find desktop nav extension item
        target_ext = '<li><a href="#"><i class="fas fa-puzzle-piece"></i>'
        if target_ext in content:
            link_path = "../private-downloader/index.html"
            repl_ext = f'<li><a href="{link_path}"><i class="fas fa-user-lock"></i> <span>Private Downloader</span></a></li>\n        ' + target_ext
            content = content.replace(target_ext, repl_ext, 1)
            modified = True

    # Mobile sidebar
    if 'href="../private-downloader/index.html"' not in content:
        target_home = '<li><a href="../index.html"><i class="fas fa-home"></i>'
        if target_home in content:
            repl_home = target_home + '\n        <li><a href="../private-downloader/index.html"><i class="fas fa-user-lock"></i> <span>Private Downloader</span></a></li>'
            content = content.replace(target_home, repl_home, 1)
            modified = True
        else:
            target_home2 = '<li><a href="index.html"><i class="fas fa-home"></i>'
            if target_home2 in content:
                repl_home2 = target_home2 + '\n        <li><a href="../private-downloader/index.html"><i class="fas fa-user-lock"></i> <span>Private Downloader</span></a></li>'
                content = content.replace(target_home2, repl_home2, 1)
                modified = True

    # Footer tools grid
    if 'href="../private-downloader/index.html"' not in content and '<div class="footer-tools-grid">' in content:
        content = content.replace(
            '<div class="footer-tools-grid">',
            '<div class="footer-tools-grid">\n        <a href="../private-downloader/index.html" class="tool-pill" style="border-color: var(--accent-blue);"><i class="fas fa-user-lock"></i> Private Downloader</a>',
            1
        )
        modified = True

    if modified:
        with open(p_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated platform page: {pdir}/index.html")
    else:
        print(f"Platform page {pdir}/index.html skipped or unchanged")

print("ALL_NAV_UPDATES_COMPLETE")
