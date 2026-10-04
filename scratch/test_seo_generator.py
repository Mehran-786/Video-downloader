# scratch/test_seo_generator.py
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
import translate_seo_articles as t

for lang in ['en', 'es', 'ur', 'fr']:
    art = t.get_translated_seo_article('index', lang)
    print(f"index [{lang}] len={len(art)}, has_table={'table' in art}")
    art_fb = t.get_translated_seo_article('facebook', lang)
    print(f"facebook [{lang}] len={len(art_fb)}, has_table={'table' in art_fb}")
