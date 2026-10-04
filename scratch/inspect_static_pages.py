import re, os

pages = ['about.html', 'features.html', 'contact.html', 'privacy.html', 'terms.html']
for p in pages:
    path = os.path.join('frontend', p)
    with open(path, encoding='utf-8') as f:
        html = f.read()
    
    print(f"=== {p} ===")
    # find where main content starts
    start_tag = None
    for tag in ['<div class="page-content-wrapper">', '<main class="page-container"']:
        if tag in html:
            start_tag = tag
            break
    
    end_tag = '<!-- Global Other Tools'
    if start_tag and end_tag in html:
        start_idx = html.find(start_tag)
        end_idx = html.find(end_tag)
        body = html[start_idx:end_idx].strip()
        print(f"  Container: {start_tag}")
        print(f"  Total Length: {len(body)}")
        # find headings
        headings = re.findall(r'<h[1-3][^>]*>(.*?)</h[1-3]>', body)
        print(f"  Headings: {[h.strip() for h in headings]}")
    else:
        print("  Could not delimit content")
