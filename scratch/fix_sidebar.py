import os

root_dir = r"c:\my folder\Pictures\Desktop\downsocial\frontend"

platform_dirs = [
    "facebook-downloader",
    "instagram-downloader",
    "tiktok-downloader",
    "youtube-downloader",
    "snapchat-downloader",
    "threads-downloader",
    "universal-downloader"
]

for pdir in platform_dirs:
    p_path = os.path.join(root_dir, pdir, "index.html")
    if not os.path.exists(p_path):
        continue
    with open(p_path, "r", encoding="utf-8") as f:
        content = f.read()

    modified = False

    # Check if inside #sidebar the private-downloader link is missing
    sidebar_idx = content.find('id="sidebar"')
    if sidebar_idx != -1:
        sidebar_part = content[sidebar_idx:]
        if 'private-downloader/index.html' not in sidebar_part:
            # Add after the Home link in sidebar
            target_home = '<a href="../index.html"><i class="fas fa-home"></i> <span data-key="homeBtn">Home</span></a></li>'
            if target_home in sidebar_part:
                link_html = '<li><a href="../private-downloader/index.html"><i class="fas fa-user-lock"></i> <span>Private Downloader</span></a></li>'
                new_sidebar_part = sidebar_part.replace(target_home, target_home + '\n        ' + link_html, 1)
                content = content[:sidebar_idx] + new_sidebar_part
                modified = True
            else:
                target_home_gen = '<a href="../index.html"><i class="fas fa-home"></i>'
                if target_home_gen in sidebar_part:
                    # Find closing </li>
                    end_li = sidebar_part.find('</li>', sidebar_part.find(target_home_gen))
                    if end_li != -1:
                        end_li += 5
                        link_html = '\n        <li><a href="../private-downloader/index.html"><i class="fas fa-user-lock"></i> <span>Private Downloader</span></a></li>'
                        new_sidebar_part = sidebar_part[:end_li] + link_html + sidebar_part[end_li:]
                        content = content[:sidebar_idx] + new_sidebar_part
                        modified = True
                else:
                    # universal-downloader uses href="index.html"
                    target_home_u = '<a href="index.html"><i class="fas fa-home"></i>'
                    if target_home_u in sidebar_part:
                        end_li = sidebar_part.find('</li>', sidebar_part.find(target_home_u))
                        if end_li != -1:
                            end_li += 5
                            link_html = '\n        <li><a href="../private-downloader/index.html"><i class="fas fa-user-lock"></i> <span>Private Downloader</span></a></li>'
                            new_sidebar_part = sidebar_part[:end_li] + link_html + sidebar_part[end_li:]
                            content = content[:sidebar_idx] + new_sidebar_part
                            modified = True

    if modified:
        with open(p_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Added mobile sidebar link to {pdir}/index.html")
    else:
        print(f"{pdir}/index.html already has sidebar link or not modified")

print("SIDEBAR_FIX_COMPLETE")
