# scratch/check_static_data_len.py
import sys
sys.stdout.reconfigure(encoding='utf-8')
import os
sys.path.insert(0, os.path.dirname(__file__))
import data_static_pages as s

for page in ['about', 'features', 'contact', 'privacy', 'terms']:
    for lang in ['en', 'es', 'ur', 'hi', 'ar', 'zh']:
        data = s.STATIC_PAGES[page][lang]
        html = data.get('pageHtml', '')
        content = data.get('content', '')
        print(f"{page} [{lang}]: pageHtml={len(html)}, content={len(content)}")
