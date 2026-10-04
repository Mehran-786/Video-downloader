import re

with open(r"c:\my folder\Pictures\Desktop\downsocial\frontend\facebook-downloader\index.html", "r", encoding="utf-8") as f:
    html = f.read()

checks = [
    ("Quick answer box", 'class="pro-tip quick-answer"'),
    ("At a glance table", 'id="at-a-glance"'),
    ("Supported links table", 'id="supported-links"'),
    ("Troubleshooting table", 'id="troubleshooting"'),
    ("FAQ 1", 'How do I download a Facebook video?'),
    ("FAQ 14", 'Is it legal to download Facebook videos?'),
    ("Schema WebPage", '"@type": "WebPage"'),
    ("Schema WebApplication", '"@type": "WebApplication"'),
    ("Schema FAQPage", '"@type": "FAQPage"'),
    ("Schema HowTo", '"@type": "HowTo"'),
    ("No 4K claim in title/desc", '4K' not in html[:html.find("</head>")]),
]

print("Static HTML checks (No JS execution):")
all_passed = True
for name, cond in checks:
    if isinstance(cond, str):
        passed = cond in html
    else:
        passed = bool(cond)
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}")
    if not passed:
        all_passed = False

if all_passed:
    print("Static HTML rendering check PASSED 100%!")
