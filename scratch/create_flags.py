# scratch/create_flags.py
import os

FLAGS_DIR = r"c:\my folder\Pictures\Desktop\downsocial\frontend\assets\flags"
SHARED_FLAGS_DIR = r"c:\my folder\Pictures\Desktop\downsocial\frontend\shared\flags"
os.makedirs(FLAGS_DIR, exist_ok=True)
os.makedirs(SHARED_FLAGS_DIR, exist_ok=True)

# 1. US Flag (en)
us_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 480" width="640" height="480">
  <path fill="#bd3d44" d="M0 0h640v480H0z"/>
  <path stroke="#fff" stroke-width="37" d="M0 55.5h640M0 129.5h640M0 203.5h640M0 277.5h640M0 351.5h640M0 425.5h640"/>
  <path fill="#192f5d" d="M0 0h260v259H0z"/>
  <!-- Stars pattern -->
  <g fill="#fff">
    <g id="s1">
      <g id="s2">
        <polygon id="star" points="0,-10 2.9,-2.2 9.5,-2.2 4.1,1.8 6.2,8.1 0,4 -6.2,8.1 -4.1,1.8 -9.5,-2.2 -2.9,-2.2"/>
        <use href="#star" x="43.3"/>
        <use href="#star" x="86.6"/>
        <use href="#star" x="130"/>
        <use href="#star" x="173.3"/>
        <use href="#star" x="216.6"/>
      </g>
      <use href="#s2" y="56"/>
      <use href="#s2" y="112"/>
      <use href="#s2" y="168"/>
      <use href="#s2" y="224"/>
    </g>
    <g id="s3" transform="translate(21.6, 28)">
      <polygon points="0,-10 2.9,-2.2 9.5,-2.2 4.1,1.8 6.2,8.1 0,4 -6.2,8.1 -4.1,1.8 -9.5,-2.2 -2.9,-2.2"/>
      <use href="#star" x="43.3"/>
      <use href="#star" x="86.6"/>
      <use href="#star" x="130"/>
      <use href="#star" x="173.3"/>
      <use href="#star" x="216.6" y="0"/>
    </g>
    <use href="#s3" y="56"/>
    <use href="#s3" y="112"/>
    <use href="#s3" y="168"/>
  </g>
</svg>'''

# 2. Spain Flag (es)
es_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 480" width="640" height="480">
  <path fill="#aa151b" d="M0 0h640v480H0z"/>
  <path fill="#f1bf00" d="M0 120h640v240H0z"/>
  <!-- Spanish Coat of arms simplified representation for flag icon -->
  <g transform="translate(180, 240) scale(0.65)">
    <!-- Crown -->
    <path fill="#d49b00" d="M-30,-75 L-40,-50 L-10,-55 L0,-78 L10,-55 L40,-50 L30,-75 Z"/>
    <circle cx="0" cy="-82" r="6" fill="#ff0000"/>
    <!-- Pillars of Hercules -->
    <rect x="-65" y="-30" width="12" height="70" fill="#c0c0c0" rx="3"/>
    <rect x="53" y="-30" width="12" height="70" fill="#c0c0c0" rx="3"/>
    <path fill="#aa151b" d="M-72, -5 h26 v8 h-26 z M46, -5 h26 v8 h-26 z"/>
    <!-- Shield -->
    <path d="M-40,-30 h80 v50 c0,30 -40,50 -40,50 c0,0 -40,-20 -40,-50 z" fill="#aa151b" stroke="#f1bf00" stroke-width="4"/>
    <!-- Shield quarters -->
    <path d="M-36,-26 h36 v36 h-36 z" fill="#aa151b"/>
    <path d="M0,-26 h36 v36 h-36 z" fill="#ffffff"/>
    <path d="M-36,10 h36 v30 c0,10 10,20 20,25 h-20 v-25 z" fill="#f1bf00"/>
    <path d="M0,10 h36 v25 c-10,5 -20,10 -20,20 v-20 h-16 z" fill="#aa151b"/>
    <!-- Center inescutcheon -->
    <ellipse cx="0" cy="10" rx="10" ry="14" fill="#003580" stroke="#aa151b" stroke-width="2"/>
    <circle cx="0" cy="10" r="4" fill="#f1bf00"/>
  </g>
</svg>'''

# 3. Portugal Flag (pt)
pt_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 480" width="640" height="480">
  <path fill="#da291c" d="M0 0h640v480H0z"/>
  <path fill="#046a38" d="M0 0h240v480H0z"/>
  <g transform="translate(240, 240) scale(0.9)">
    <!-- Armillary sphere (yellow) -->
    <circle r="65" fill="#f1bf00" stroke="#000" stroke-width="2"/>
    <circle r="48" fill="none" stroke="#685400" stroke-width="5"/>
    <line x1="-65" y1="0" x2="65" y2="0" stroke="#685400" stroke-width="5"/>
    <line x1="0" y1="-65" x2="0" y2="65" stroke="#685400" stroke-width="5"/>
    <ellipse rx="35" ry="60" fill="none" stroke="#685400" stroke-width="5" transform="rotate(35)"/>
    <!-- Portuguese Shield -->
    <path d="M-28,-36 h56 v40 c0,28 -28,42 -28,42 c0,0 -28,-14 -28,-42 z" fill="#ffffff" stroke="#da291c" stroke-width="9"/>
    <!-- 7 Castles on red border -->
    <circle cx="-20" cy="-28" r="3" fill="#f1bf00"/>
    <circle cx="0" cy="-32" r="3" fill="#f1bf00"/>
    <circle cx="20" cy="-28" r="3" fill="#f1bf00"/>
    <circle cx="-23" cy="2" r="3" fill="#f1bf00"/>
    <circle cx="23" cy="2" r="3" fill="#f1bf00"/>
    <circle cx="-14" cy="24" r="3" fill="#f1bf00"/>
    <circle cx="14" cy="24" r="3" fill="#f1bf00"/>
    <!-- Inner blue quinas -->
    <path d="M-5,-10 h10 v14 c0,5 -5,8 -5,8 c0,0 -5,-3 -5,-8 z" fill="#003580"/>
    <path d="M-5,-22 h10 v10 c0,4 -5,6 -5,6 c0,0 -5,-2 -5,-6 z" fill="#003580"/>
    <path d="M-5,4 h10 v10 c0,4 -5,6 -5,6 c0,0 -5,-2 -5,-6 z" fill="#003580"/>
    <path d="M-15,-10 h8 v10 c0,4 -4,6 -4,6 c0,0 -4,-2 -4,-6 z" fill="#003580"/>
    <path d="M7,-10 h8 v10 c0,4 -4,6 -4,6 c0,0 -4,-2 -4,-6 z" fill="#003580"/>
  </g>
</svg>'''

# 4. Germany Flag (de)
de_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 480" width="640" height="480">
  <path fill="#000000" d="M0 0h640v160H0z"/>
  <path fill="#dd0000" d="M0 160h640v160H0z"/>
  <path fill="#ffce00" d="M0 320h640v160H0z"/>
</svg>'''

# 5. France Flag (fr)
fr_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 480" width="640" height="480">
  <path fill="#002395" d="M0 0h213.3v480H0z"/>
  <path fill="#ffffff" d="M213.3 0h213.4v480H213.3z"/>
  <path fill="#ed2939" d="M426.7 0h213.3v480H426.7z"/>
</svg>'''

# 6. Italy Flag (it)
it_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 480" width="640" height="480">
  <path fill="#009246" d="M0 0h213.3v480H0z"/>
  <path fill="#ffffff" d="M213.3 0h213.4v480H213.3z"/>
  <path fill="#ce2b37" d="M426.7 0h213.3v480H426.7z"/>
</svg>'''

flags = {
    'en': us_svg,
    'es': es_svg,
    'pt': pt_svg,
    'de': de_svg,
    'fr': fr_svg,
    'it': it_svg
}

for code, svg in flags.items():
    p1 = os.path.join(FLAGS_DIR, f"{code}.svg")
    with open(p1, "w", encoding="utf-8") as f:
        f.write(svg)
    p2 = os.path.join(SHARED_FLAGS_DIR, f"{code}.svg")
    with open(p2, "w", encoding="utf-8") as f:
        f.write(svg)

print("Created 6 flag SVGs in both FLAGS_DIR and SHARED_FLAGS_DIR successfully!")
