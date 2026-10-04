import os
import re

FRONTEND = r'c:\my folder\Pictures\Desktop\downsocial\frontend'

PLATFORMS = [
    'facebook-downloader', 'instagram-downloader', 'tiktok-downloader',
    'youtube-downloader', 'snapchat-downloader', 'threads-downloader', 'universal-downloader'
]

# Patterns of links to remove from header nav:
# <li><a href="features.html">...</a></li>
# <li><a href="about.html">...</a></li>
# <li><a href="contact.html">...</a></li>
# Also platform toggle dropdown if present in nav-links

patterns_to_remove = [
    r'<li>\s*<a\s+href=["\']features\.html["\'][^>]*>.*?</a>\s*</li>',
    r'<li>\s*<a\s+href=["\']about\.html["\'][^>]*>.*?</a>\s*</li>',
    r'<li>\s*<a\s+href=["\']contact\.html["\'][^>]*>.*?</a>\s*</li>',
    r'<li\s+class=["\']dropdown["\']>\s*<a\s+href=["\']#["\']\s+id=["\']platformToggle["\'][^>]*>.*?</ul>\s*</li>'
]

count_modified = 0

for p in PLATFORMS:
    p_dir = os.path.join(FRONTEND, p)
    if not os.path.exists(p_dir):
        continue
    for fname in os.listdir(p_dir):
        if fname.endswith('.html'):
            fpath = os.path.join(p_dir, fname)
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()

            # Target only inside <nav class="top-nav desktop-nav"> ... </nav>
            nav_match = re.search(r'(<nav class="top-nav desktop-nav">.*?</nav>)', content, re.DOTALL)
            if nav_match:
                orig_nav = nav_match.group(1)
                clean_nav = orig_nav
                for pat in patterns_to_remove:
                    clean_nav = re.sub(pat, '', clean_nav, flags=re.DOTALL | re.IGNORECASE)

                # Also ensure Extension and Language are present if missing
                # Check if clean_nav changed
                if clean_nav != orig_nav:
                    content = content.replace(orig_nav, clean_nav)
                    with open(fpath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    count_modified += 1
                    print(f"Cleaned header nav in: {p}/{fname}")

print(f"\nTotal files cleaned: {count_modified}")
