import glob, re, os

for root, dirs, files in os.walk('frontend'):
    for f in files:
        if f.endswith('.html'):
            path = os.path.join(root, f)
            content = open(path, encoding='utf-8').read()
            scripts = re.findall(r'src=["\']([^"\']+\.js)["\']', content)
            print(f"{path}: {scripts}")
