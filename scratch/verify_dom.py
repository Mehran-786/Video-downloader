import urllib.request

urls = [
    ('YouTube', 'http://127.0.0.1:5500/youtube-downloader/index.html'),
    ('Universal', 'http://127.0.0.1:5500/universal-downloader/index.html'),
    ('TikTok', 'http://127.0.0.1:5500/tiktok-downloader/index.html'),
    ('Facebook', 'http://127.0.0.1:5500/facebook-downloader/index.html')
]

for name, u in urls:
    with urllib.request.urlopen(u) as r:
        html = r.read().decode('utf-8')
    print(f"\n--- {name} ({u}) ---")
    print("brand-orbit-wrapper:", "brand-orbit-wrapper" in html)
    print("url-input:", 'class="url-input"' in html)
    print("download-btn:", 'class="download-btn"' in html)
    print("features-container:", 'class="features-container"' in html)
    print("expandable-box count:", html.count("feature-box expandable-box"))
