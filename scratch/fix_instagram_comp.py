# scratch/fix_instagram_comp.py
import os, sys, re
SCRATCH_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRATCH_DIR)

import seo_data_instagram

d = seo_data_instagram.INSTAGRAM_DATA['it']
d['comp_h3'] = 'Perché downsocial supera SaveInsta, iGram e InDown'
d['comp_p'] = 'Gli strumenti tradizionali come SaveInsta (saveinsta.app), iGram (igram.world), SnapInsta e InDown (indown.io) sono pieni di pop-up invasivi e lenti nei tempi di risposta. downsocial offre estrazione diretta ad alta velocità via CDN senza annunci pubblicitari, qualità 1080p reale e conversione istantanea in MP3.'
d['comp_headers'] = ['Confronto funzionalità', 'downsocial.net', 'SaveInsta', 'iGram', 'InDown']
d['comp_rows'] = [
    ('Risoluzione video massima', '<span class="badge-highlight">1080p Full HD (60fps)</span>', '1080p', '720p / 1080p', '1080p'),
    ('Pubblicità e pop-up invasivi', '<span class="badge-highlight">Zero (Interfaccia pulita)</span>', 'Molti annunci', 'Annunci frequenti', 'Molti annunci'),
    ('Conversione audio (MP3)', '<span class="badge-highlight">HQ 192/320 kbps MP3</span>', 'Base', 'Non disponibile', 'Base'),
    ('Download anonimo delle Storie', '<span class="badge-highlight">100% anonimo</span>', 'Sì', 'Limitato', 'Sì'),
    ('Nessun login richiesto', '<span class="badge-highlight">100% anonimo</span>', 'Senza login', 'Senza login', 'Senza login')
]

file_path = os.path.join(SCRATCH_DIR, 'seo_data_instagram.py')
with open(file_path, 'r', encoding='utf-8') as f:
    code = f.read()

code = re.sub(r"'it': \{.*?\},\n(?='es')", f"'it': {repr(d)},\n", code, flags=re.DOTALL)
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated seo_data_instagram successfully!")
