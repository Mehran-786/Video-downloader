import os
import re

FRONTEND = r'c:\my folder\Pictures\Desktop\downsocial\frontend'

PLATFORM_MAP = [
    ('facebook-video-downloader.html', 'facebook-downloader', 'Facebook', 'fab fa-facebook-f', 'orbit-center-facebook'),
    ('instagram-video-downloader.html', 'instagram-downloader', 'Instagram', 'fab fa-instagram', 'orbit-center-instagram'),
    ('tiktok-video-downloader.html', 'tiktok-downloader', 'TikTok', 'fab fa-tiktok', 'orbit-center-tiktok'),
    ('youtube-video-downloader.html', 'youtube-downloader', 'YouTube', 'fab fa-youtube', 'orbit-center-youtube'),
    ('snapchat-video-downloader.html', 'snapchat-downloader', 'Snapchat', 'fab fa-snapchat-ghost', 'orbit-center-snapchat'),
    ('threads-video-downloader.html', 'threads-downloader', 'Threads', 'fa-brands fa-threads', 'orbit-center-threads'),
    ('index.html', 'universal-downloader', 'Universal', 'fas fa-globe', '')
]

ALL_TOOLS = [
    ('threads-downloader', 'Threads', 'fa-brands fa-threads', 'orbit-threads threads', 'th-pill'),
    ('facebook-downloader', 'Facebook', 'fab fa-facebook-f', 'orbit-facebook facebook', 'fb-pill'),
    ('instagram-downloader', 'Instagram', 'fab fa-instagram', 'orbit-instagram instagram', 'ig-pill'),
    ('tiktok-downloader', 'TikTok', 'fab fa-tiktok', 'orbit-tiktok tiktok', 'tt-pill'),
    ('youtube-downloader', 'YouTube', 'fab fa-youtube', 'orbit-youtube youtube', 'yt-pill'),
    ('snapchat-downloader', 'Snapchat', 'fab fa-snapchat-ghost', 'orbit-snapchat snapchat', 'snap-pill'),
    ('universal-downloader', 'Universal', 'fas fa-globe', 'orbit-universal universal', 'active')
]

for src_file, dest_folder, p_name, p_icon, orbit_center_class in PLATFORM_MAP:
    src_path = os.path.join(FRONTEND, src_file)
    dest_path = os.path.join(FRONTEND, dest_folder, 'index.html')
    
    with open(src_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update stylesheet & script links to point to ../shared/
    html = html.replace('href="style.css"', 'href="../shared/style.css"')
    html = html.replace('src="script.js"', 'src="../shared/script.js"')
    html = html.replace('href="icon-nav.webp"', 'href="../shared/icon-nav.webp"')
    html = html.replace('src="icon-nav.webp"', 'src="../shared/icon-nav.webp"')
    html = html.replace('href="space-bg.webp"', 'href="../shared/space-bg.webp"')
    html = html.replace('href="icon.webp"', 'href="../shared/icon.webp"')

    # 2. Update canonical URL to platform folder
    html = re.sub(
        r'<link\s+rel=["\']canonical["\']\s+href=["\']https://downsocial\.net/[^"\']*["\']',
        f'<link rel="canonical" href="https://downsocial.net/{dest_folder}/"',
        html
    )

    # 3. Update OG URL
    html = re.sub(
        r'<meta\s+property=["\']og:url["\']\s+content=["\']https://downsocial\.net/[^"\']*["\']',
        f'<meta property="og:url" content="https://downsocial.net/{dest_folder}/"',
        html
    )

    # 4. In desktop nav, add the dedicated platform sub-page links (Features, About, Contact)
    # Check if nav-links has features/about/contact links
    nav_links_target = '<li class="theme-switcher-wrapper">'
    subpage_nav = f'''
        <li><a href="features.html"><i class="fas fa-star"></i> <span>Features</span></a></li>
        <li><a href="about.html"><i class="fas fa-info-circle"></i> <span>About</span></a></li>
        <li><a href="contact.html"><i class="fas fa-envelope"></i> <span>Contact</span></a></li>
        <li class="theme-switcher-wrapper">'''
    if 'href="features.html"' not in html:
        html = html.replace(nav_links_target, subpage_nav, 1)

    # 5. In mobile sidebar, add features/about/contact links if missing
    sidebar_home_target = '<li><a href="index.html"><i class="fas fa-home"></i> <span data-key="homeBtn">Home</span></a></li>'
    sidebar_links = f'''<li><a href="index.html"><i class="fas fa-home"></i> <span>Home</span></a></li>
        <li><a href="features.html"><i class="fas fa-star"></i> <span>Features</span></a></li>
        <li><a href="about.html"><i class="fas fa-info-circle"></i> <span>About</span></a></li>
        <li><a href="contact.html"><i class="fas fa-envelope"></i> <span>Contact</span></a></li>
        <li><a href="privacy.html"><i class="fas fa-shield-alt"></i> <span>Privacy Policy</span></a></li>
        <li><a href="terms.html"><i class="fas fa-file-contract"></i> <span>Terms of Service</span></a></li>'''
    if 'href="features.html"' not in html or 'href="contact.html"' not in html:
        html = html.replace(sidebar_home_target, sidebar_links, 1)

    # 6. Update the Brand Orbit links so each item links to ../[target-folder]/index.html
    # Replace old orbit links (e.g. href="threads-video-downloader.html")
    old_orbit_links = [
        ('threads-video-downloader.html', '../threads-downloader/index.html'),
        ('facebook-video-downloader.html', '../facebook-downloader/index.html'),
        ('instagram-video-downloader.html', '../instagram-downloader/index.html'),
        ('tiktok-video-downloader.html', '../tiktok-downloader/index.html'),
        ('youtube-video-downloader.html', '../youtube-downloader/index.html'),
        ('snapchat-video-downloader.html', '../snapchat-downloader/index.html'),
        ('index.html', '../universal-downloader/index.html')
    ]
    for old_l, new_l in old_orbit_links:
        # Only replace inside orbit items
        html = html.replace(f'href="{old_l}" target="_blank" rel="noopener noreferrer" class="orbit-item', f'href="{new_l}" class="orbit-item')
        html = html.replace(f'href="{old_l}" class="orbit-item', f'href="{new_l}" class="orbit-item')

    # 7. Update footer links and tool pills
    # Replace footer tools directory
    footer_pills_html = ""
    for folder, name, icon, _, pill_class in ALL_TOOLS:
        is_active = "active" if folder == dest_folder else ""
        link_target = "index.html" if folder == dest_folder else f"../{folder}/index.html"
        footer_pills_html += f'<a href="{link_target}" class="tool-pill {pill_class} {is_active}"><i class="{icon}"></i> <span>{name}</span></a>\n'

    # In footer-links, ensure local links to features, about, contact, privacy, terms are present
    old_footer_links = re.search(r'<div class="footer-links">(.*?)</div>', html, re.DOTALL)
    if old_footer_links:
        new_footer_links = f'''<div class="footer-links">
        <a href="index.html" class="footer-btn">Home</a>
        <a href="features.html" class="footer-btn">Features</a>
        <a href="about.html" class="footer-btn">About</a>
        <a href="contact.html" class="footer-btn">Contact</a>
        <a href="privacy.html" class="footer-btn">Privacy Policy</a>
        <a href="terms.html" class="footer-btn">Terms of Service</a>
        {"<a href='how-it-works.html' class='footer-btn'>How It Works</a>" if dest_folder == 'universal-downloader' else ''}
    </div>'''
        html = html.replace(old_footer_links.group(0), new_footer_links)

    # Replace footer tool pills in footer-tools-grid
    old_grid = re.search(r'<div class="footer-tools-grid">(.*?)</div>', html, re.DOTALL)
    if old_grid:
        html = html.replace(old_grid.group(0), f'<div class="footer-tools-grid">\n{footer_pills_html}\n        </div>')

    # Write out the perfected file
    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"[OK] Synchronized {dest_folder}/index.html from {src_file}")

print("\nAll 7 platform index.html files now have the exact perfected glowing UI!")
