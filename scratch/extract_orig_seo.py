import glob, os

platforms = ['index', 'facebook', 'instagram', 'tiktok', 'youtube', 'snapchat', 'threads']
files = {
    'index': 'frontend/index.html',
    'facebook': 'frontend/facebook-downloader/index.html',
    'instagram': 'frontend/instagram-downloader/index.html',
    'tiktok': 'frontend/tiktok-downloader/index.html',
    'youtube': 'frontend/youtube-downloader/index.html',
    'snapchat': 'frontend/snapchat-downloader/index.html',
    'threads': 'frontend/threads-downloader/index.html'
}

for p, f in files.items():
    with open(f, 'r', encoding='utf-8') as fp:
        html = fp.read()
    
    start_str = '<div class="seo-article-wrapper">'
    end_str = '<!-- Global Other Tools'
    if start_str in html and end_str in html:
        s_idx = html.find(start_str) + len(start_str)
        e_idx = html.find(end_str)
        sub = html[s_idx:e_idx]
        last_div = sub.rfind('</div>')
        body = sub[:last_div].strip()
        out_f = f'scratch/orig_seo_{p}.html'
        with open(out_f, 'w', encoding='utf-8') as out:
            out.write(body)
        print(f"Extracted original SEO article for {p}: length {len(body)} -> {out_f}")
    else:
        print(f"No seo article found in {f}")
