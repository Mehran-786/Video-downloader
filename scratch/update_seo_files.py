import os
from datetime import datetime

frontend = r'c:\my folder\Pictures\Desktop\downsocial\frontend'
today = datetime.now().strftime('%Y-%m-%d')

platforms = [
    'facebook-downloader', 'instagram-downloader', 'tiktok-downloader',
    'youtube-downloader', 'snapchat-downloader', 'threads-downloader', 'universal-downloader'
]

pages = ['index.html', 'features.html', 'about.html', 'contact.html', 'privacy.html', 'terms.html']

urls = [
    ('https://downsocial.net/', '1.0', 'daily'),
]

for p in platforms:
    urls.append((f'https://downsocial.net/{p}/', '0.9', 'daily'))
    urls.append((f'https://downsocial.net/{p}/features.html', '0.8', 'weekly'))
    urls.append((f'https://downsocial.net/{p}/about.html', '0.7', 'monthly'))
    urls.append((f'https://downsocial.net/{p}/contact.html', '0.6', 'monthly'))
    urls.append((f'https://downsocial.net/{p}/privacy.html', '0.5', 'monthly'))
    urls.append((f'https://downsocial.net/{p}/terms.html', '0.5', 'monthly'))
    if p == 'universal-downloader':
        urls.append((f'https://downsocial.net/{p}/how-it-works.html', '0.8', 'weekly'))

# Also keep root legacy pages
legacy_pages = [
    'facebook-video-downloader.html', 'instagram-video-downloader.html',
    'snapchat-video-downloader.html', 'youtube-video-downloader.html',
    'tiktok-video-downloader.html', 'threads-video-downloader.html',
    'about.html', 'privacy.html', 'terms.html'
]
for lp in legacy_pages:
    urls.append((f'https://downsocial.net/{lp}', '0.7', 'weekly'))

sitemap_entries = []
for u, prio, freq in urls:
    sitemap_entries.append(f"""  <url>
    <loc>{u}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>{freq}</changefreq>
    <priority>{prio}</priority>
  </url>""")

sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{"\n".join(sitemap_entries)}
</urlset>
"""

with open(os.path.join(frontend, 'sitemap.xml'), 'w', encoding='utf-8') as f:
    f.write(sitemap_xml)

print("Updated sitemap.xml with all multi-platform URLs!")

# Update llms.txt
llms_txt = f"""# downsocial — All-in-One Multi-Platform Social Media Video Downloader Suite
> Web suite providing 7 specialized social media downloaders for Facebook, Instagram, TikTok, YouTube, Snapchat, and Threads.

## Platforms & Dedicated Downloaders
- Universal All-in-One Downloader: https://downsocial.net/universal-downloader/
- Facebook Video Downloader: https://downsocial.net/facebook-downloader/
- Instagram Reels & Stories Downloader: https://downsocial.net/instagram-downloader/
- TikTok No-Watermark Downloader: https://downsocial.net/tiktok-downloader/
- YouTube 4K & Shorts Downloader: https://downsocial.net/youtube-downloader/
- Snapchat Spotlight & Story Saver: https://downsocial.net/snapchat-downloader/
- Meta Threads Video & Carousel Downloader: https://downsocial.net/threads-downloader/

## API Endpoints
- POST /api/download?url={{url}} : Resolves video and audio stream links for any supported platform
- GET /api/direct?url={{cdn_url}}&type={{mp4|mp3}}&q={{hd|sd|hq|normal}} : Streams and converts media files directly with content disposition

## Features
- 100% Free and Unlimited Downloads
- Zero added watermarks or brand stamps
- Automatic TikTok watermark removal
- Real-time MP3 audio conversion (192kbps - 320kbps)
- Supported video resolutions up to 4K Ultra HD
- Multi-language support across 11 languages (EN, ES, FR, DE, HI, AR, PT, RU, ID, ZH, UR)
- Zero account login, strict zero-log privacy architecture
"""

with open(os.path.join(frontend, 'llms.txt'), 'w', encoding='utf-8') as f:
    f.write(llms_txt)

print("Updated llms.txt!")
