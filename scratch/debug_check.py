import re

with open('frontend/index.html', encoding='utf-8') as f:
    html = f.read()

articles = re.findall(r'<div class="[^"]*(?:seo|article)[^"]*"[^>]*>', html)
print('Articles in index.html:', articles)

h2s = re.findall(r'<h2[^>]*>(.*?)</h2>', html, re.DOTALL)
print('H2s in index.html:', [h.strip()[:60] for h in h2s])

h3s = re.findall(r'<h3[^>]*>(.*?)</h3>', html, re.DOTALL)
print('H3s in index.html:', [h.strip()[:60] for h in h3s])
