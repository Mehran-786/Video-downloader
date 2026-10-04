import re
import os

repo_root = r"c:\my folder\Pictures\Desktop\downsocial"
frontend_dir = os.path.join(repo_root, "frontend")

# 1. Update sitemap.xml
sitemap_path = os.path.join(frontend_dir, "sitemap.xml")
if os.path.exists(sitemap_path):
    with open(sitemap_path, "r", encoding="utf-8") as f:
        sitemap_content = f.read()

    old_sitemap_block = re.search(
        r'<url>\s*<loc>https://downsocial\.net/facebook-video-downloader\.html</loc>.*?</url>',
        sitemap_content,
        re.DOTALL
    )

    new_sitemap_entries = """<url><loc>https://downsocial.net/facebook-downloader/</loc><lastmod>2026-10-02</lastmod><changefreq>weekly</changefreq><priority>0.9</priority></url>
<url><loc>https://downsocial.net/facebook-downloader/about.html</loc><lastmod>2026-10-02</lastmod><changefreq>monthly</changefreq><priority>0.4</priority></url>
<url><loc>https://downsocial.net/facebook-downloader/contact.html</loc><lastmod>2026-10-02</lastmod><changefreq>monthly</changefreq><priority>0.4</priority></url>
<url><loc>https://downsocial.net/facebook-downloader/privacy.html</loc><lastmod>2026-10-02</lastmod><changefreq>yearly</changefreq><priority>0.3</priority></url>
<url><loc>https://downsocial.net/facebook-downloader/terms.html</loc><lastmod>2026-10-02</lastmod><changefreq>yearly</changefreq><priority>0.3</priority></url>"""

    if old_sitemap_block:
        sitemap_content = sitemap_content.replace(old_sitemap_block.group(0), new_sitemap_entries)
    else:
        # If not exact match, replace any instance
        sitemap_content = re.sub(
            r'<url>\s*<loc>https://downsocial\.net/facebook-video-downloader\.html</loc>.*?</url>',
            new_sitemap_entries,
            sitemap_content,
            flags=re.DOTALL
        )

    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(sitemap_content)
    print("Updated sitemap.xml")

# 2. Update llms.txt & llms-full.txt
for fname in ["llms.txt", "llms-full.txt"]:
    fpath = os.path.join(frontend_dir, fname)
    if os.path.exists(fpath):
        with open(fpath, "r", encoding="utf-8") as f:
            c = f.read()
        c = c.replace("facebook-video-downloader.html", "facebook-downloader/")
        c = c.replace("/facebook-video-downloader.html", "/facebook-downloader/")
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(c)
        print(f"Updated {fname}")

# 3. Update HTML files linking to facebook-video-downloader.html
for root, dirs, files in os.walk(frontend_dir):
    for file in files:
        if file.endswith(".html"):
            fpath = os.path.join(root, file)
            # determine relative path to facebook-downloader/
            rel_to_frontend = os.path.relpath(fpath, frontend_dir)
            is_subfolder = os.path.dirname(rel_to_frontend) != ""
            
            with open(fpath, "r", encoding="utf-8") as f:
                c = f.read()
            
            if "facebook-video-downloader.html" in c:
                # If file is inside frontend root: link should be "facebook-downloader/"
                # If file is inside another subfolder: link should be "../facebook-downloader/"
                target_link = "../facebook-downloader/" if is_subfolder else "facebook-downloader/"
                c = c.replace("facebook-video-downloader.html", target_link)
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(c)
                print(f"Updated links in {rel_to_frontend}")

print("All link replacements complete.")
