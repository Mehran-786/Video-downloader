import json
import re
import os

folder = r"c:\my folder\Pictures\Desktop\downsocial\frontend\facebook-downloader"
html_files = ["index.html", "about.html", "contact.html", "privacy.html", "terms.html"]

all_valid = True
for h in html_files:
    path = os.path.join(folder, h)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    scripts = re.findall(r'<script type="application/ld\+json">(.*?)</script>', content, re.DOTALL)
    if not scripts:
        print(f"FAIL: No JSON-LD in {h}")
        all_valid = False
        continue
    
    for i, s in enumerate(scripts):
        try:
            data = json.loads(s.strip())
            graph = data.get("@graph", [])
            types = [item.get("@type") for item in graph]
            print(f"PASS: {h} JSON-LD #{i+1} valid. Types found: {types}")
        except Exception as e:
            print(f"FAIL: {h} JSON-LD parse error: {e}")
            all_valid = False

if all_valid:
    print("ALL JSON-LD SCHEMAS ARE 100% VALID SYNTAX!")
