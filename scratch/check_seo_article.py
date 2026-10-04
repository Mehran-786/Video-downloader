import re

with open('frontend/index.html', encoding='utf-8') as f:
    html = f.read()

m = re.search(r'<div class="seo-article-wrapper">(.*?)</div>\s*<!-- Global Other Tools', html, re.DOTALL)
if m:
    print('Found seo-article-wrapper! Length:', len(m.group(1)))
    print('Start:')
    print(m.group(1)[:500])
    print('...')
    print('End:')
    print(m.group(1)[-500:])
else:
    # let's search where seo-article-wrapper starts and ends
    idx = html.find('class="seo-article-wrapper"')
    print('Index:', idx)
    if idx != -1:
        print(html[idx:idx+800])
