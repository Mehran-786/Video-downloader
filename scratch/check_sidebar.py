import glob

missing_sidebar = []
for f in sorted(glob.glob('frontend/**/*.html', recursive=True)):
    with open(f, encoding='utf-8') as fp:
        c = fp.read()
    if 'mobile-top-bar' in c and 'id="sidebar"' not in c:
        missing_sidebar.append(f)

print('Missing sidebar count:', len(missing_sidebar))
for f in missing_sidebar:
    print(' ', f)
