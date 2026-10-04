import urllib.request
import re

urls = [
    'http://127.0.0.1:5500/universal-downloader/index.html',
    'http://127.0.0.1:5500/youtube-downloader/index.html',
    'http://127.0.0.1:5500/facebook-downloader/index.html'
]

for u in urls:
    with urllib.request.urlopen(u) as r:
        html = r.read().decode('utf-8')
    nav_match = re.search(r'<nav class="top-nav desktop-nav">.*?</nav>', html, re.DOTALL)
    if nav_match:
        nav = nav_match.group(0)
        print(f"\n{u}:")
        print("  Features in header nav:", 'href="features.html"' in nav)
        print("  About in header nav:", 'href="about.html"' in nav)
        print("  Contact in header nav:", 'href="contact.html"' in nav)
        print("  Theme switcher in header:", 'theme-segmented-control' in nav)
        print("  Language dropdown in header:", 'desktopLangToggle' in nav)
