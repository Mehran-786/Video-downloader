# scratch/translate_seo_articles.py
# Routes SEO article requests to comprehensive, 100% translated generator modules.

import os, sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

import seo_data_index
import seo_data_youtube
import seo_data_tiktok
import seo_data_snapchat
import seo_data_threads
import seo_data_facebook
import seo_data_instagram

def get_translated_seo_article(platform, lang):
    # For English, return exact original file
    if lang == 'en':
        orig_file = os.path.join(BASE_DIR, f'orig_seo_{platform}.html')
        if os.path.exists(orig_file):
            with open(orig_file, 'r', encoding='utf-8') as f:
                return f.read()

    if platform in ['index', 'universal']:
        return seo_data_index.render_index_html(lang)
    elif platform == 'youtube':
        return seo_data_youtube.render_youtube_html(lang)
    elif platform == 'tiktok':
        return seo_data_tiktok.render_tiktok_html(lang)
    elif platform == 'snapchat':
        return seo_data_snapchat.render_snapchat_html(lang)
    elif platform == 'threads':
        return seo_data_threads.render_threads_html(lang)
    elif platform == 'facebook':
        return seo_data_facebook.get_facebook_seo(lang)
    elif platform == 'instagram':
        return seo_data_instagram.get_instagram_seo(lang)
    elif platform == 'private':
        return seo_data_facebook.get_facebook_seo(lang)
    else:
        return ""

if __name__ == '__main__':
    for p in ['index', 'facebook', 'instagram', 'youtube', 'tiktok', 'snapchat', 'threads']:
        for l in ['en', 'es', 'pt', 'ur']:
            res = get_translated_seo_article(p, l)
            print(f"{p} [{l}]: {len(res)} chars")
