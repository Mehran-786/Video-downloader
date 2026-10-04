import glob, re

for f in sorted(glob.glob('frontend/**/index.html', recursive=True)):
    with open(f, encoding='utf-8') as fp:
        html = fp.read()
    
    start_str = '<div class="seo-article-wrapper">'
    end_str = '<!-- Global Other Tools'
    if start_str in html and end_str in html:
        s_idx = html.find(start_str) + len(start_str)
        e_idx = html.find(end_str)
        # get last closing div before end_str
        sub = html[s_idx:e_idx]
        last_div = sub.rfind('</div>')
        body = sub[:last_div].strip()
        h2s = re.findall(r'<h[23][^>]*>(.*?)</h[23]>', body)
        has_table = '<table' in body
        print(f"{f}: len={len(body)}, tables={has_table}, headings={len(h2s)}")
        for h in h2s:
            print(f"    - {h.strip()[:60]}")
    else:
        print(f"{f}: NO seo-article-wrapper")
