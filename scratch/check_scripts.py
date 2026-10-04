import glob, re

pages = [
    'frontend/index.html',
    'frontend/threads-downloader/index.html',
    'frontend/facebook-downloader/index.html',
    'frontend/private-downloader/index.html',
    'frontend/about.html'
]
for p in pages:
    content = open(p, encoding='utf-8').read()
    print(p, re.findall(r'src=["\']([^"\']+\.js)["\']', content))
