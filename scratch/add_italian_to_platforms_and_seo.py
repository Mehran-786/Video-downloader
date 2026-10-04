# scratch/add_italian_to_platforms_and_seo.py
# Injects complete Italian ('it') data into build_platforms_data.py and all 7 platform SEO generator modules.

import os, sys

SCRATCH_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRATCH_DIR)

# -------------------------------------------------------------
# 1. Update build_platforms_data.py
# -------------------------------------------------------------
print("Updating build_platforms_data.py...")
plat_file = os.path.join(SCRATCH_DIR, 'build_platforms_data.py')
with open(plat_file, 'r', encoding='utf-8') as f:
    plat_code = f.read()

# Add Italian TITLES for each platform
it_titles_dict = {
    'index': "('Social Media Video Downloader', 'Scarica video, reel, shorts e storie da YouTube, TikTok, Instagram, Facebook, Snapchat e Threads in 1080p HD, 4K e MP3 gratis', 'Incolla qualsiasi link video (YouTube, TikTok, Instagram, Facebook, Snapchat, Threads)...', 'Scarica Video')",
    'facebook': "('Facebook Video Downloader', 'Scarica Facebook Reels, video Watch, storie e clip di gruppi in 1080p Full HD gratis', 'Incolla qui l\\'URL del video, Reel o Storia di Facebook...', 'Scarica Video da Facebook')",
    'instagram': "('Instagram Video Downloader', 'Scarica Instagram Reels, storie, foto e post carosello in risoluzione originale HD gratis', 'Incolla qui il link di Instagram Reel, Storia o Post...', 'Scarica Video da Instagram')",
    'tiktok': "('TikTok Video Downloader', 'Scarica video TikTok senza watermark in HD MP4 ed estrai audio MP3 a 320kbps gratis', 'Incolla qui il link del video TikTok...', 'Scarica Video da TikTok')",
    'youtube': "('YouTube Video Downloader', 'Scarica video e Shorts da YouTube in 1080p, 2K, 4K UHD ed estrai audio MP3 a 320kbps gratis', 'Incolla qui il link del video o Short di YouTube...', 'Scarica Video da YouTube')",
    'snapchat': "('Snapchat Video Downloader', 'Scarica video di Snapchat Spotlight e storie pubbliche in 1080p HD MP4 gratis', 'Incolla qui il link di Snapchat Spotlight o Storia...', 'Scarica Video da Snapchat')",
    'threads': "('Threads Video Downloader', 'Scarica video, album fotografici e note vocali da Meta Threads in 1080p Full HD gratis', 'Incolla qui il link del post di Threads...', 'Scarica Video da Threads')",
    'private': "('Downloader Video Privato', 'Scarica video protetti e privati da qualsiasi piattaforma incollando il codice sorgente', 'Incolla qui il codice sorgente della pagina web...', 'Estrai Video')"
}

if "'it': (" not in plat_code:
    for plat_id, title_tuple_str in it_titles_dict.items():
        target = f"'{plat_id}': {{"
        replacement = f"'{plat_id}': {{\n            'it': {title_tuple_str},"
        plat_code = plat_code.replace(target, replacement, 1)

    # In get_features(), add 'it'
    it_features_code = """            'it': [
                {
                    'title': 'Qualità Originale HD e 4K',
                    'desc': f'Scarica contenuti da {p_name} in risoluzione nativa senza alcuna compressione o perdita di dettaglio.',
                    'blogIcon': 'fas fa-film',
                    'blogTitle': f'Acquisizione Stream Senza Perdite per {p_name}',
                    'blogP1': f'Ci connettiamo direttamente ai nodi CDN ufficiali per estrarre flussi video puliti al massimo bitrate.',
                    'blogP2': 'Goditi colori vivaci e riproduzione fluida su smartphone, tablet e computer.'
                },
                {
                    'title': 'Nessun Login e 100% Privato',
                    'desc': 'Scarica liberamente senza condividere credenziali di accesso, password o email.',
                    'blogIcon': 'fas fa-shield-halved',
                    'blogTitle': 'Anonimato Garantito e Zero Tracciamento',
                    'blogP1': 'Rispettiamo la tua privacy. Nessun registro di download né identificatore personale viene conservato.',
                    'blogP2': 'Tutta l\\'elaborazione avviene temporaneamente nella memoria RAM e viene cancellata al termine.'
                },
                {
                    'title': 'Audio MP3 Studio a 320kbps',
                    'desc': f'Estrai colonne sonore, discorsi e tracce musicali da {p_name} direttamente in formato MP3 ad alta fedeltà.',
                    'blogIcon': 'fas fa-headphones',
                    'blogTitle': 'Conversione Audio in Tempo Reale',
                    'blogP1': 'Motore audio avanzato integrato che converte i flussi sonori in file MP3 puliti a 320kbps o 192kbps.',
                    'blogP2': 'Ideale per suonerie, podcast, memo vocali e musica offline.'
                }
            ],
"""
    plat_code = plat_code.replace("f_map = {", "f_map = {\n" + it_features_code, 1)

    # In get_howto(), add 'it'
    it_howto_code = """            'it': {
                'title': f'Come Scaricare Video e Audio da {p_name} Online',
                'steps': [
                    {'title': f'Passo 1: Copia il link del video da {p_name}', 'desc': f'Apri {p_name}, trova il video che desideri salvare, tocca Condividi e seleziona "Copia link".', 'bullet': 'Il link è ora salvato negli appunti del tuo dispositivo.'},
                    {'title': 'Passo 2: Incolla il link nel nostro downloader', 'desc': 'Torna su downsocial.net e incolla il link copiato nella casella in alto.', 'bullet': 'Il nostro motore individua immediatamente la piattaforma e analizza il flusso.'},
                    {'title': 'Passo 3: Fai clic su "Scarica Video"', 'desc': 'Premi il pulsante per avviare l\\'analisi immediata del contenuto multimediale.', 'bullet': 'Le opzioni di qualità disponibili appariranno a schermo in pochi secondi.'},
                    {'title': 'Passo 4: Scegli il tuo formato (HD MP4 o MP3 a 320kbps)', 'desc': 'Seleziona "Video (HD)" per 1080p/4K oppure "Audio (HQ MP3)" per estrarre solo la traccia sonora.', 'bullet': 'Nessun watermark aggiunto e massima qualità originale.'}
                ],
                'hidden': [
                    {'title': 'Passo 5: Salva il file sul tuo dispositivo', 'desc': 'Il file verrà scaricato direttamente nella memoria del tuo smartphone o computer.', 'bullets': ['Android: Si salva direttamente nella cartella Download o nella Galleria.', 'iPhone/iPad: Apri i download di Safari, tocca Condividi e seleziona "Salva video".', 'PC o Mac: Il file si salva nella tua cartella Download predefinita.'], 'tip': f'Consiglio: Puoi scaricare video illimitati da {p_name} 24/7 senza alcuna restrizione.'}
                ]
            },
"""
    plat_code = plat_code.replace("h_map = {", "h_map = {\n" + it_howto_code, 1)

    # In get_faqs(), add 'it'
    it_faqs_code = """            'it': [
                {'q': f'Scaricare video da {p_name} è sicuro e legale?', 'a': f'Sì, salvare video pubblici da {p_name} per uso personale offline e studio è sicuro e ampiamente consentito.'},
                {'q': f'Il video scaricato avrà filigrane o loghi aggiunti?', 'a': f'Assolutamente no! downsocial estrae il video originale direttamente dal CDN senza inserire alcun logo.'},
                {'q': f'Posso convertire i video di {p_name} in file audio MP3?', 'a': f'Certamente! Incolla il link e seleziona "Audio (HQ MP3)" per ottenere un file MP3 puro fino a 320kbps.'},
                {'q': f'Devo installare qualche programma o app sul dispositivo?', 'a': f'Non occorre installare nulla. downsocial funziona direttamente in qualsiasi browser moderno.'},
                {'q': f'L\\'autore del video saprà che l\\'ho scaricato?', 'a': f'No. L\\'elaborazione è totalmente anonima e non invia alcuna notifica o avviso al creatore del video.'},
                {'q': f'Esiste un limite al numero di download giornalieri?', 'a': f'Nessun limite! Puoi scaricare tutti i video e gli audio che desideri in modo gratuito e illimitato.'}
            ],
"""
    plat_code = plat_code.replace("faq_sets = {", "faq_sets = {\n" + it_faqs_code, 1)

    # In get_seo_article(), add 'it'
    it_art_code = """            'it': f\"\"\"<h2>Guida Completa all'Estrazione di Video e Audio da {p_name}</h2>
<p>Salvare video ad alto bitrate e tracce audio pulite da {p_name} è oggi un'esigenza fondamentale per studenti, creator e appassionati. downsocial.net offre una soluzione web moderna, rapida e priva di qualsiasi perdita qualitativa.</p>
<h3>Risoluzione 1080p, 2K e 4K Ultra HD Senza Perdita</h3>
<p>Interrogando direttamente i nodi CDN di {p_name}, la nostra piattaforma estrae flussi nativi MP4 garantendo la massima fedeltà cromatica, fluidità a 60fps e sincronizzazione audio perfetta.</p>
<h3>Transcodifica Audio MP3 Professionale a 320kbps</h3>
<p>Vuoi salvare solo la musica, una voce narrante o un memo vocale? La pipeline integrata converte la sorgente in file MP3 ad alta definizione compatibili con tutti i dispositivi.</p>
<h3>Privacy Assoluta e Architettura Zero-Knowledge</h3>
<p>Nessun account, nessun dato personale e nessun file memorizzato sui nostri server. I download sono 100% anonimi ed elaborati in memoria con crittografia SSL a 256 bit.</p>\"\"\",
"""
    plat_code = plat_code.replace("art_map = {", "art_map = {\n" + it_art_code, 1)

    with open(plat_file, 'w', encoding='utf-8') as f:
        f.write(plat_code)
    print("build_platforms_data.py updated with 'it' successfully!")
else:
    print("build_platforms_data.py already has 'it'!")


# -------------------------------------------------------------
# 2. Update Platform SEO modules with Italian data
# -------------------------------------------------------------

def update_module_dict(mod_name, dict_name, it_dict_data):
    filepath = os.path.join(SCRATCH_DIR, f"{mod_name}.py")
    with open(filepath, 'r', encoding='utf-8') as f:
        code = f.read()
    if "'it':" in code:
        print(f"{mod_name}.py already has 'it' data.")
        return
    search_str = f"{dict_name} = {{"
    it_insert = f"{dict_name} = {{\n    'it': {repr(it_dict_data)},\n"
    code = code.replace(search_str, it_insert, 1)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(code)
    print(f"{mod_name}.py updated with 'it' data!")


# INDEX
index_it = {
    'qa_title': 'Risposta Rapida: Come Scaricare Video dai Social Network Gratis',
    'qa_text': 'Per scaricare qualsiasi video pubblico da YouTube, TikTok, Instagram, Facebook, Snapchat o Threads, copia il link dall\'app (Condividi > Copia link), incollalo nella casella in alto su <strong>downsocial.net</strong>, clicca su <strong>"Scarica Video"</strong> e seleziona <strong>Video (HD)</strong> o <strong>Audio (HQ MP3)</strong>. Lo strumento è 100% gratuito, non richiede registrazione né app, non contiene pubblicità invasive ed è compatibile con iPhone, Android, Windows e Mac.',
    'h2': 'Il Downloader di Video per Social Network Definitivo e All-in-One',
    'intro': 'Salvare video da internet richiedeva in passato decine di siti web pieni di annunci ingannevoli e pop-up. <strong>downsocial.net</strong> unifica l\'intero panorama dei social media in un\'unica applicazione web moderna, velocissima e sicura. Che si tratti di salvare video TikTok senza watermark, YouTube Shorts in 1080p, Reels di Instagram o video di Facebook, downsocial lo fa all\'istante senza alcuna perdita di qualità.',
    't1_h3': 'Piattaforme, Formati e Specifiche Tecniche Supportate',
    't1_headers': ['Piattaforma', 'Contenuto Supportato', 'Qualità Video Massima', 'Estrazione Audio', 'Stato Watermark'],
    't1_rows': [
        ('<i class="fab fa-youtube" style="color:#ff0000; margin-right:5px;"></i> YouTube', 'Video, Shorts, Video Musicali', '4K UHD / 1080p Full HD', '320 kbps MP3', 'Zero Watermark'),
        ('<i class="fab fa-tiktok" style="color:#25F4EE; margin-right:5px;"></i> TikTok', 'Video, Tracce Audio, Presentazioni Foto', '1080p 60fps Full HD', '320 kbps MP3', '<span class="badge-highlight">100% Rimosso</span>'),
        ('<i class="fab fa-instagram" style="color:#E1306C; margin-right:5px;"></i> Instagram', 'Reels, Storie, Post Carousel', '1080p Full HD', '192 kbps MP3', 'Sorgente Originale'),
        ('<i class="fab fa-facebook-f" style="color:#1877F2; margin-right:5px;"></i> Facebook', 'Reels, Watch, Post del Feed', '1080p Full HD', '192 kbps MP3', 'Sorgente Originale'),
        ('<i class="fab fa-snapchat-ghost" style="color:#FFFC00; margin-right:5px;"></i> Snapchat', 'Spotlight, Storie Pubbliche', '1080p Full HD', '320 kbps MP3', 'Zero Watermark'),
        ('<i class="fa-brands fa-threads" style="color:#ffffff; margin-right:5px;"></i> Threads', 'Video, Tracce Audio, Carousel', '1080p Full HD', '320 kbps MP3', 'Sorgente Originale')
    ],
    'comp_h3': 'Perché Scegliere downsocial Rispetto alla Concorrenza?',
    'comp_p': 'I siti web tradizionali come <em>SaveFrom</em>, <em>SnapTik</em> e <em>Y2Mate</em> bersagliano gli utenti con pop-up fastidiosi, falsi avvisi di malware e velocità di download ridotte. downsocial opera su un\'infrastruttura cloud sicura e pulita senza alcuna pubblicità invasiva.',
    'comp_headers': ['Confronto Funzionalità', 'downsocial.net', 'SaveFrom.net', 'SnapTik.app', 'Y2Mate.is'],
    'comp_rows': [
        ('Piattaforme Supportate', '6 Grandi Piattaforme (Tutto in Uno)', 'Limitato', 'Solo TikTok', 'Solo YouTube'),
        ('Rimozione Watermark TikTok', '100% Rimozione Lossless', 'Standard', 'Sì', 'N/A'),
        ('Risoluzione Video Massima', 'Fino a 4K UHD e 1080p HD', '720p (Blocco HD)', '1080p', '1080p'),
        ('Convertitore MP3 in Tempo Reale', 'FFmpeg Dedicato (320kbps)', '128kbps', 'Limitato', '192kbps'),
        ('Finestre Pop-up e Annunci', 'Zero Annunci / 100% Pulito', 'Molti Pop-up', 'Annunci Invasivi', 'Molti Annunci'),
        ('Privacy e Sicurezza', 'Politica Rigida Zero-Log', 'Traccia Cookie/IP', 'Tracciamento Pubblicitario', 'Tracciamento Pubblicitario')
    ],
    'guide_h3': 'Guida Passo-Passo per Scaricare su Qualsiasi Dispositivo',
    'ios': '<strong>Su iPhone e iPad:</strong> Apri Safari, vai su <code>downsocial.net</code>, incolla qualsiasi link e tocca "Scarica Video". Scegli "Video (HD)" e tocca Scarica. Al termine, tocca l\'icona blu dei download di Safari, apri il file, premi Condividi e seleziona <em>"Salva video"</em> per salvarlo nel Rullino Foto.',
    'android': '<strong>Su Android (Samsung, Xiaomi, Pixel, Motorola):</strong> Apri Chrome o Firefox. Incolla il link su downsocial, premi "Scarica Video" e seleziona "Video (HD)" o "Audio (HQ MP3)". Il file verrà salvato direttamente nella cartella <code>Download</code> e sarà visibile nella Galleria.',
    'pc': '<strong>Su Windows, Mac e Chromebook:</strong> Apri downsocial.net in qualsiasi browser, incolla l\'URL e clicca su "Scarica Video". Scegli il formato desiderato per salvarlo all\'istante sul tuo computer.',
    'priv_h3': 'Download Sicuri, Privati e 100% Anonimi',
    'priv_p': 'La tua privacy è fondamentale. downsocial opera secondo una rigorosa architettura a conoscenza zero. Nessuna registrazione, nessun tracciamento dei tuoi download e nessun file multimediale memorizzato sui nostri server. Tutti i trasferimenti sono protetti da crittografia SSL a 256 bit.'
}
update_module_dict('seo_data_index', 'INDEX_DATA', index_it)


# YOUTUBE
youtube_it = {
    'qa_title': 'Risposta Rapida: Come Scaricare Video e Shorts da YouTube',
    'qa_text': 'Per scaricare qualsiasi video o Short da YouTube, copia l\'URL dalla barra degli indirizzi o tocca Condividi > Copia link, incollalo su <strong>downsocial.net/youtube-downloader/</strong>, clicca su <strong>"Scarica Video"</strong> e seleziona <strong>Video (HD 1080p/4K)</strong> o <strong>Audio (HQ MP3)</strong>. Lo strumento è 100% gratuito, non richiede programmi aggiuntivi né account Google, non contiene annunci e salva i file su iPhone, Android e PC.',
    'h2': 'Il Downloader di Video e Shorts da YouTube Più Veloce e Senza Annunci',
    'intro': 'Goditi la riproduzione offline dei video di YouTube senza abbonamenti a pagamento o app invadenti. <strong>downsocial.net</strong> offre download diretti di stream per video standard di YouTube, Shorts verticali, lezioni e videoclip musicali fino a risoluzioni 4K UHD e audio MP3 da studio a 320 kbps.',
    't1_h3': 'Formati e Tipi di Link di YouTube Supportati',
    't1_headers': ['Tipo di Contenuto', 'Formato Link di Esempio', 'Risoluzioni Disponibili', 'Qualità Audio'],
    't1_rows': [
        ('Video Standard', 'youtube.com/watch?v=...', '1080p, 1440p (2K), 2160p (4K UHD)', 'Audio Stereo AAC'),
        ('YouTube Shorts', 'youtube.com/shorts/...', '1080x1920 Full HD', 'Audio Sincronizzato'),
        ('Link Breve Condiviso', 'youtu.be/...', 'Fino a 4K UHD', 'Audio Stereo'),
        ('Estrazione Audio da YouTube', 'youtube.com/watch?v=...', 'Traccia Audio Originale', 'MP3 a 320 kbps / 192 kbps')
    ],
    'comp_h3': 'Perché Scegliere downsocial Rispetto a Y2Mate e SaveFrom?',
    'comp_p': 'I servizi tradizionali come <em>Y2Mate (y2mate.is)</em>, <em>SaveFrom (savefrom.net)</em>, <em>SSYouTube</em> e <em>KeepVid</em> aprono continue finestre pop-under, mostrano falsi avvisi di sicurezza e limitano le risoluzioni più elevate. downsocial è stato sviluppato con infrastruttura cloud ad alta velocità per garantire un servizio affidabile, privo di pubblicità e gratuito.',
    'comp_headers': ['Confronto Funzionalità', 'downsocial.net', 'Y2Mate', 'SaveFrom.net', 'SSYouTube'],
    'comp_rows': [
        ('Qualità Video Massima', '4K UHD / 1080p 60fps', '1080p (Lento)', '720p (HD Bloccato)', '720p'),
        ('Qualità Audio (MP3)', 'MP3 Studio a 320kbps', '128kbps', 'Bassa Qualità', '128kbps'),
        ('Finestre Pop-up e Malware', 'Zero Annunci / 100% Pulito', 'Pop-up Invasivi', 'Annunci Falsi', 'Annunci Frequenti'),
        ('Watermark Aggiunti', 'Nessuno (Video Integro)', 'Nessuno', 'Nessuno', 'Nessuno'),
        ('Account o Login Richiesto', 'Nessun Login Richiesto', 'No', 'No', 'No'),
        ('Velocità di Download', 'Cloud Diretto Istantaneo', 'Limitata', 'Standard', 'Lenta')
    ],
    'guide_h3': 'Istruzioni Passo-Passo per Scaricare sui Dispositivi',
    'ios': '<strong>Su iPhone e iPad:</strong> Apri Safari, vai su <code>downsocial.net/youtube-downloader/</code>, incolla il link di YouTube e tocca "Scarica Video". Scegli la risoluzione (1080p MP4 o 320kbps MP3) e tocca Scarica. Al termine, tocca l\'icona dei download di Safari, apri il file, premi Condividi e seleziona <em>"Salva video"</em> per conservarlo nell\'app Foto di iOS.',
    'android': '<strong>Su Android (Samsung, Xiaomi, Pixel, Motorola):</strong> Apri Chrome, incolla l\'URL del video o Short di YouTube e tocca "Scarica Video". Seleziona "Video (HD)" o "Audio (HQ MP3)". Il file si scarica direttamente nella cartella <code>Download</code> e compare nella Galleria.',
    'pc': '<strong>Su Windows, Mac e Chromebook:</strong> Incolla l\'URL di YouTube su downsocial in qualsiasi browser, fai clic su "Scarica Video" e seleziona la qualità desiderata. Il file si salverà direttamente nella cartella dei download del tuo PC.',
    'priv_h3': 'Download Sicuri, Privati e 100% Anonimi',
    'priv_p': 'La tua privacy è la nostra priorità. downsocial opera con una politica a zero registri. Non richiediamo registrazioni, non chiediamo credenziali Google e non salviamo le URL dei contenuti multimediali elaborati.'
}
update_module_dict('seo_data_youtube', 'YOUTUBE_DATA', youtube_it)


# TIKTOK
tiktok_it = {
    'qa_title': 'Risposta Rapida: Come Scaricare Video da TikTok Senza Watermark',
    'qa_text': 'Per scaricare qualsiasi video di TikTok senza il logo galleggiante, copia il link del video (Condividi > Copia link), incollalo su <strong>downsocial.net/tiktok-downloader/</strong>, clicca su <strong>"Scarica Video"</strong> e seleziona <strong>Video (Senza Watermark)</strong> o <strong>Audio (HQ MP3)</strong>. Lo strumento è 100% gratuito, senza pubblicità, non richiede app né registrazione e salva i video su iPhone, Android e PC.',
    'h2': 'Il Miglior Downloader Gratuito di Video TikTok Senza Watermark',
    'intro': 'TikTok è la piattaforma leader mondiale per i video brevi. <strong>downsocial.net</strong> ti permette di salvare i tuoi video preferiti, trend musicali, ricette, balletti e album fotografici in risoluzione 1080p Full HD privi di qualsiasi logo o scritta in sovrimpressione.',
    't1_h3': 'Formati e Link TikTok Supportati',
    't1_headers': ['Tipo di Contenuto', 'Esempio di Link', 'Stato Watermark', 'Formato di Output'],
    't1_rows': [
        ('Video Standard', 'tiktok.com/@user/video/...', '100% Rimosso (Pulito)', 'Video MP4 1080p'),
        ('Link Breve Condiviso', 'vm.tiktok.com/... o vt.tiktok.com/...', '100% Rimosso', 'Video MP4 1080p'),
        ('Presentazione di Foto', 'tiktok.com/@user/video/...', 'Immagini Pulite', 'JPG in Full HD'),
        ('Audio / Suono Virale', 'tiktok.com/music/...', 'Audio Originale', 'MP3 a 320 kbps')
    ],
    'comp_h3': 'Perché Scegliere downsocial Rispetto a SnapTik, SSSTik e MusicalDown?',
    'comp_p': 'I downloader convenzionali come <em>SnapTik</em>, <em>SSSTik</em> e <em>MusicalDown</em> sono infarciti di pubblicità invasive e rallentamenti del server. downsocial offre un ambiente veloce, sicuro e privo di annunci con estrazione diretta dal CDN.',
    'comp_headers': ['Confronto Funzionalità', 'downsocial.net', 'SnapTik.app', 'SSSTik.io', 'MusicalDown'],
    'comp_rows': [
        ('Rimozione Watermark', '100% Pulito (Senza Logo)', 'Pulito', 'Pulito', 'Pulito'),
        ('Qualità Video', '1080p Full HD (Originale)', '1080p', '720p / 1080p', 'Standard'),
        ('Estrazione Audio / MP3', 'MP3 HQ a 320kbps', 'Limitato', 'MP3 Disponibile', 'Base'),
        ('Pop-up e Pubblicità', 'Zero Annunci / 100% Pulito', 'Molti Annunci', 'Annunci Invasivi', 'Annunci Frequenti'),
        ('Velocità di Download', 'Istantanea nel Cloud', 'Standard', 'Standard', 'Lenta')
    ],
    'guide_h3': 'Guida Passo-Passo per Scaricare su Qualsiasi Dispositivo',
    'ios': '<strong>Su iPhone e iPad:</strong> Apri Safari, vai su <code>downsocial.net/tiktok-downloader/</code>, incolla il link e tocca "Scarica Video". Scegli "Video (Senza Watermark)". Al termine del download, apri il file e seleziona <em>"Salva video"</em> per salvarlo nell\'app Foto.',
    'android': '<strong>Su Android:</strong> Incolla il link in Chrome e tocca "Scarica Video". Il video viene salvato direttamente nella cartella <code>Download</code> ed è visibile nella Galleria.',
    'pc': '<strong>Su Windows, Mac e Chromebook:</strong> Incolla l\'URL di TikTok in qualsiasi browser e scarica il file in qualità originale senza bisogno di programmi aggiuntivi.',
    'priv_h3': 'Download Sicuri, Privati e 100% Anonimi',
    'priv_p': 'La tua privacy è protetta al 100%. Operiamo secondo una rigida politica senza log. Non richiediamo mai dati di accesso e tutto il traffico è protetto da protocollo sicuro SSL.'
}
update_module_dict('seo_data_tiktok', 'TIKTOK_DATA', tiktok_it)


# SNAPCHAT
snapchat_it = {
    'qa_title': 'Risposta Rapida: Come Scaricare Video da Snapchat Spotlight',
    'qa_text': 'Per scaricare qualsiasi video di Snapchat Spotlight o Storia pubblica, apri Snapchat, tocca <strong>Condividi > Copia link</strong>, incolla l\'URL su <strong>downsocial.net/snapchat-downloader/</strong>, clicca su <strong>"Scarica Video"</strong> e seleziona <strong>Video (HD MP4)</strong> o <strong>Audio (HQ MP3)</strong>. Lo strumento è 100% gratuito, non invia alcuna notifica all\'autore, non aggiunge watermark e salva il file su iPhone, Android e PC.',
    'h2': 'Il Miglior Downloader di Video Spotlight e Storie di Snapchat',
    'intro': 'Snapchat è diventato un punto di riferimento per contenuti verticali virali grazie a <strong>Snapchat Spotlight</strong>. <strong>downsocial.net</strong> offre lo strumento web più veloce e sicuro per salvare video di Spotlight e storie pubbliche direttamente sul tuo smartphone o computer.',
    't1_h3': 'Formati di Link Snapchat Supportati',
    't1_headers': ['Tipo di Contenuto', 'Formato Link di Esempio', 'Risoluzione', 'Formato di Output'],
    't1_rows': [
        ('Video Snapchat Spotlight', 'snapchat.com/spotlight/W...', '1080p Full HD (60fps)', 'Video MP4'),
        ('Storia Pubblica di Creator', 'story.snapchat.com/s/...', 'Qualità Originale', 'Video MP4'),
        ('Audio / Voce di Spotlight', 'snapchat.com/spotlight/...', '192kbps / 320kbps', 'Audio MP3'),
        ('Link Breve Condiviso', 'snapchat.com/t/...', 'Qualità Originale', 'MP4 / MP3')
    ],
    'comp_h3': 'Perché downsocial è la Migliore Alternativa a SnapVee, ScreenApp e SnapAny',
    'comp_p': 'Strumenti obsoleti come <em>SnapVee</em> e <em>ScreenApp</em> presentano continui pop-up e frequenti errori di download. downsocial offre estrazione diretta via CDN senza annunci pubblicitari e con conversione istantanea in MP3.',
    'comp_headers': ['Confronto Funzionalità', 'downsocial.net', 'SnapVee', 'SnapAny', 'ScreenApp'],
    'comp_rows': [
        ('Qualità Video Massima', '1080p 60fps Full HD', '720p', '720p', '1080p'),
        ('Audio Spotlight (MP3)', '320kbps HQ MP3', 'Base', 'Non disponibile', 'Solo Video'),
        ('Annunci e Pop-up Invasivi', 'Zero Annunci / 100% Pulito', 'Molti Pop-up', 'Annunci Frequenti', 'Banner Fastidiosi'),
        ('Watermark Aggiunti', 'Nessuno (Video Originale)', 'Nessuno', 'Watermark nella versione free', 'Nessuno'),
        ('Account o Registrazione Richiesta', 'Nessun Login Richiesto', 'No', 'Richiede Installazione App', 'No')
    ],
    'guide_h3': 'Guida Passo-Passo per Scaricare su Qualsiasi Dispositivo',
    'ios': '<strong>Su iPhone e iPad:</strong> Apri Safari, vai su <code>downsocial.net/snapchat-downloader/</code>, incolla il link di Spotlight e tocca "Scarica Video". Al termine del download, apri il file in Safari e tocca <em>"Salva video"</em> per conservarlo nell\'app Foto.',
    'android': '<strong>Su Android:</strong> Incolla il link in Chrome, clicca su "Scarica Video" e il file si salverà automaticamente nella cartella <code>Download</code> e nella Galleria.',
    'pc': '<strong>Su Windows, Mac e Chromebook:</strong> Incolla l\'URL nel tuo browser e salva il video in Full HD sul tuo computer.',
    'priv_h3': 'Protezione della Privacy con Politica Zero-Log',
    'priv_p': 'Il tuo anonimato è completo. Non inviamo notifiche ai creator di Snapchat quando salvi un loro video e non conserviamo registri delle tue attività di download.'
}
update_module_dict('seo_data_snapchat', 'SNAPCHAT_DATA', snapchat_it)


# THREADS
threads_it = {
    'qa_title': 'Risposta Rapida: Come Scaricare Video da Threads',
    'qa_text': 'Per scaricare qualsiasi video, nota vocale o album fotografico da Meta Threads, copia il link del post (threads.net/@user/post/...), incollalo su <strong>downsocial.net/threads-downloader/</strong>, clicca su <strong>"Scarica Video"</strong> e seleziona <strong>Video (HD MP4)</strong>, <strong>Foto</strong> o <strong>Audio (HQ MP3)</strong>. Lo strumento è 100% gratuito, senza pubblicità e salva su iPhone, Android, Mac e Windows.',
    'h2': 'Il Downloader di Video e Media da Meta Threads Più Veloce e Sicuro',
    'intro': 'Salva discussioni interessanti, clip virali, tutorial, note vocali e album carosello da Threads con <strong>downsocial.net</strong>. Il nostro motore elabora i link di Threads in pochi millisecondi senza spam, senza reindirizzamenti e senza alcuna perdita di qualità.',
    't1_h3': 'Formati di Link Threads Supportati',
    't1_headers': ['Tipo di Contenuto', 'Esempio di Link', 'Qualità Supportata', 'Formato'],
    't1_rows': [
        ('Post Video Standard', 'threads.net/@user/post/C...', '1080p Full HD / 720p HD', 'Video MP4'),
        ('Nota Vocale / Clip Audio', 'threads.net/@user/post/C...', '320 kbps / 192 kbps', 'Audio MP3'),
        ('Carosello di Più Foto', 'threads.net/@user/post/C...', 'Massima Risoluzione Originale', 'JPG / MP4'),
        ('Video di Post Citato', 'threads.net/@user/post/C...', '1080p Full HD', 'Video MP4'),
        ('Link Breve Condiviso', 'threads.net/t/...', 'Qualità Originale', 'MP4 / MP3')
    ],
    'comp_h3': 'Perché Scegliere downsocial Rispetto a Threadster e SaveThreads?',
    'comp_p': 'Piattaforme datate come <em>Threadster</em> e <em>SaveThreads</em> sono affollate di pubblicità invasive e comprimono la risoluzione video. downsocial è stato progettato per garantire download immediati e totalmente privi di annunci.',
    'comp_headers': ['Confronto Funzionalità', 'downsocial.net', 'Threadster.app', 'SaveThreads.io', 'ThreadsVid'],
    'comp_rows': [
        ('Risoluzione Video Massima', '1080p Full HD', '1080p', '720p', '720p'),
        ('Estrazione Note Vocali', 'MP3 HQ a 320kbps', 'Base', 'Non disponibile', 'Solo Video'),
        ('Annunci e Pop-up Invasivi', 'Zero Annunci / 100% Pulito', 'Molti Pop-up', 'Annunci Invasivi', 'Annunci Frequenti'),
        ('Supporto per Post Carosello', 'Estrae l\'intero album', 'Solo 1ª foto', 'Instabile', 'Non supportato'),
        ('Account o Registrazione Richiesta', 'Nessuna Registrazione', 'No', 'No', 'No')
    ],
    'guide_h3': 'Istruzioni Passo-Passo per Scaricare sui Dispositivi',
    'ios': '<strong>Su iPhone e iPad:</strong> Apri Safari, vai su <code>downsocial.net/threads-downloader/</code>, incolla il link di Threads e tocca "Scarica Video". Al termine, apri il file e seleziona <em>"Salva video"</em> nell\'app Foto.',
    'android': '<strong>Su Android:</strong> Incolla il link in Chrome, tocca "Scarica Video" e il file verrà salvato nella cartella <code>Download</code> e nella Galleria.',
    'pc': '<strong>Su Windows, Mac e Chromebook:</strong> Incolla l\'URL nel browser e salva il contenuto in qualità originale sul tuo computer.',
    'priv_h3': 'Download Sicuri, Privati e 100% Anonimi',
    'priv_p': 'Non memorizziamo copie dei file scaricati né tracciamo i link che inserisci. Tutto il traffico viaggia sotto crittografia SSL avanzata.'
}
update_module_dict('seo_data_threads', 'THREADS_DATA', threads_it)


# FACEBOOK
facebook_it = {
    'qa_title': 'Risposta rapida: Come scaricare video da Facebook',
    'qa_text': 'Per scaricare un video da Facebook, copia il suo link, incollalo nel riquadro in cima a questa pagina, tocca <em>Scarica video</em> e seleziona HD, Normale o MP3. È gratuito, non richiede login né applicazioni esterne e funziona su iPhone, Android, Windows e Mac. È possibile scaricare esclusivamente video pubblici.',
    'h2': 'Facebook Video Downloader: Salva qualsiasi video pubblico di Facebook in HD',
    'intro': 'Questo <strong>downloader di video per Facebook</strong> è pensato per un compito specifico: trasformare un link di un video pubblico, Reel o Watch di Facebook in un file salvabile sul tuo dispositivo. Analizza il video, mostra i formati disponibili e scarica la tua scelta in MP4 o audio MP3. Nessuna installazione richiesta, nessun file salvato sui nostri server e nessun accesso al tuo account Facebook.',
    't1_h3': 'Facebook Video Downloader in sintesi',
    't1_headers': ['Caratteristica', 'Dettagli'],
    't1_rows': [
        ('Contenuti supportati', 'Video pubblici di Facebook, Reel, video Watch, storie pubbliche e dirette concluse ancora disponibili'),
        ('Link supportati', 'facebook.com, m.facebook.com, facebook.com/share, fb.watch'),
        ('Formati di output', 'Video MP4 (HD e Normale), audio MP3 (192 kbps e 128 kbps)'),
        ('Qualità video', 'Migliore risoluzione fornita da Facebook per il video, solitamente da 720p a 1080p. Nessun upscaling artificiale'),
        ('Prezzo', '<span class="badge-highlight">Gratuito, senza limiti di download</span>'),
        ('Account o login', '<span class="badge-highlight">Nessuno richiesto</span>'),
        ('Watermark', '<span class="badge-highlight">Nessun watermark aggiunto</span>'),
        ('Compatibilità', 'iPhone, iPad, Android, Windows, macOS, Linux (tutti i browser moderni)'),
        ('File conservati', 'Nessuno. I flussi multimediali non vengono memorizzati'),
        ('Limitazioni', 'Solo video pubblici. Non supporta gruppi privati o post per soli amici')
    ],
    't2_h3': 'Quali link di Facebook funzionano?',
    't2_intro': 'Facebook supporta diversi formati di URL. Se il video è pubblico, tutti i seguenti formati sono supportati:',
    't2_headers': ['Tipo di link', 'Struttura link', 'Funziona quando'],
    't2_rows': [
        ('Video Watch', 'facebook.com/watch/?v=...', 'Il video è pubblico'),
        ('Reel', 'facebook.com/reel/...', 'Il Reel è pubblico'),
        ('Link di condivisione', 'facebook.com/share/v/... o /share/r/...', 'Il video condiviso è pubblico'),
        ('Link breve', 'fb.watch/...', 'Il video è pubblico'),
        ('Video di Pagina o profilo', 'facebook.com/NomePagina/videos/...', 'Il video è pubblico'),
        ('Link da mobile', 'm.facebook.com/...', 'Il video è pubblico'),
        ('Video di gruppo', 'facebook.com/groups/.../posts/...', 'Il gruppo è pubblico')
    ],
    'copy_h3': 'Come copiare il link di un video di Facebook',
    'copy_items': [
        '<strong>App Facebook (iPhone o Android):</strong> tocca <em>Condividi</em> sotto il video o Reel, poi seleziona <em>Copia link</em>.',
        '<strong>Facebook su computer:</strong> clicca sul menu a tre puntini del post e seleziona <em>Copia link</em>, oppure fai clic destro sulla data/ora del post e copia l\'indirizzo del link.',
        '<strong>Messenger o WhatsApp:</strong> se qualcuno ti ha inviato un video di Facebook, copia il link direttamente dal messaggio.'
    ],
    'device_h3': 'Come scaricare video di Facebook su iPhone, Android e computer',
    'ios': '<strong>Su iPhone o iPad:</strong> apri questa pagina in Safari, incolla il link e tocca Scarica video. Il file viene salvato nell\'app File sotto Download. Aprilo, tocca Condividi e seleziona Salva video per spostarlo nell\'app Foto.',
    'android': '<strong>Su Android:</strong> apri questa pagina in Chrome, incolla il link e tocca Video (HD). Il file MP4 si salva nella cartella Download ed è subito visibile nella Galleria.',
    'pc': '<strong>Su Windows o Mac:</strong> incolla il link, clicca su Scarica video e scegli il formato desiderato. Il file verrà salvato nella cartella Download del tuo computer.',
    'priv_h3': 'È possibile scaricare video privati di Facebook?',
    'priv_p': 'No. Questo strumento scarica solo video accessibili a chiunque senza bisogno di login. Post riservati agli amici, gruppi privati e contenuti con restrizioni non possono essere scaricati. Non chiediamo mai la tua password di Facebook. Il pulsante "Salva video" di Facebook crea solo un segnalibro interno, non genera un file. Se hai bisogno di un video privato, chiedi all\'autore di inviarti il file originale.',
    'qual_h3': 'Qualità dei video di Facebook: cosa ottieni realmente',
    'qual_p': 'Facebook comprime e conserva i video in vari profili. <strong>Video (HD)</strong> corrisponde alla massima qualità disponibile per il video, mentre <strong>Video (Normale)</strong> è una versione più leggera adatta a connessioni lente. La qualità dell\'upload originale rappresenta il limite massimo: un video caricato a 480p non può essere convertito in 1080p, pertanto downsocial non applica upscaling fasulli.',
    'mp3_h3': 'Convertire video di Facebook in MP3',
    'mp3_p': 'Hai bisogno solo dell\'audio di una canzone, intervista o discorso? Scegli <strong>Audio (HQ MP3)</strong> per 192 kbps oppure <strong>Audio (Normale MP3)</strong> per 128 kbps. La conversione avviene istantaneamente durante il download.',
    'trouble_h3': 'Perché un video di Facebook potrebbe non scaricarsi',
    'trouble_headers': ['Sintomo', 'Causa probabile', 'Cosa fare'],
    'trouble_rows': [
        ('"Impossibile estrarre il video"', 'Il video è privato, solo per amici o è stato rimosso', 'Apri il link in una scheda in incognito. Se non si avvia lì, non può essere scaricato'),
        ('Nessuna reazione dopo aver incollato', 'Il link porta a un profilo o a un post senza video', 'Apri il video stesso e copia il link da Condividi'),
        ('Video in diretta fallito', 'La diretta streaming è ancora in corso', 'Attendi la conclusione della diretta e la sua archiviazione come video'),
        ('Storia non trovata', 'La storia è scaduta dopo 24 ore o è privata', 'Le storie sono temporanee; riprova finché la storia è attiva'),
        ('Richiesta di login', 'Il contenuto richiede un account per essere visto', 'Sono supportati solo video completamente pubblici'),
        ('Download molto lento o bloccato', 'File di grandi dimensioni o connessione debole', 'Prova con Video (Normale) o connettiti a una rete Wi-Fi più stabile')
    ],
    'use_h3': 'Perché scaricare e salvare i video di Facebook?',
    'use_items': [
        'Conservare una copia dei <strong>tuoi video personali</strong>, eventi di famiglia e ricordi prima che vadano perduti.',
        'Guardare tutorial, ricette e lezioni offline durante viaggi o senza consumare dati.',
        'Condividere un video divertente con gli amici su WhatsApp con il loro consenso.',
        'Estrarre l\'audio di un discorso o di una canzone per ascoltarlo in MP3.'
    ],
    'safe_h3': 'Scaricare video da Facebook è sicuro e legale?',
    'safe_p': '<strong>Sicuro:</strong> non inserisci password, non installi programmi e non concedi permessi. <strong>Legale:</strong> salvare un video pubblico per uso personale offline è una pratica comune, ma il copyright appartiene all\'autore. Non ripubblicare né ridistribuire contenuti senza autorizzazione. downsocial è uno strumento indipendente e non ha alcun legame con Meta Platforms, Inc.',
    'tips_h3': 'Consigli per ottenere il miglior risultato',
    'tips_items': [
        'Copia il link dall\'opzione <em>Condividi</em> del video stesso anziché dalla barra degli indirizzi.',
        'Usa <strong>Video (HD)</strong> se desideri riprodurlo su TV o monitor grandi.',
        'Scegli <strong>Video (Normale)</strong> o MP3 per risparmiare traffico dati mobile.',
        'In caso di dubbi, prova prima ad aprire l\'URL in una finestra di navigazione privata.'
    ],
    'sister_h3': 'Hai bisogno di scaricare da un altro social?',
    'sister_p': 'Offriamo strumenti dedicati anche per <a href="../instagram-downloader/">Instagram</a>, <a href="../tiktok-downloader/">TikTok</a>, <a href="../youtube-downloader/">YouTube</a>, <a href="../snapchat-downloader/">Snapchat</a> e <a href="../threads-downloader/">Threads</a>, oltre al nostro <a href="../index.html">downloader universale</a>.',
    'last_updated': 'Ultimo aggiornamento: 4 ottobre 2026. Domande o link che non funziona? <a href="contact.html">Contatta il supporto</a>.'
}
update_module_dict('seo_data_facebook', 'FACEBOOK_DATA', facebook_it)


# INSTAGRAM
instagram_it = {
    'qa_title': 'Risposta rapida: Come scaricare video e Reels da Instagram',
    'qa_text': 'Per scaricare un video o Reel da Instagram, tocca l\'icona dell\'aeroplano di carta o i tre puntini, seleziona <em>Copia link</em>, incollalo nel riquadro in alto su <strong>downsocial.net/instagram-downloader/</strong>, tocca <em>Scarica video</em> e scegli HD, Normale o MP3. È 100% gratuito, senza watermark e funziona su iPhone, Android e computer. Possono essere scaricati solo profili pubblici.',
    'h2': 'Instagram Video Downloader: Salva Reels, Storie e Foto in Qualità HD',
    'intro': 'Il nostro <strong>Instagram video downloader</strong> ti consente di estrarre e salvare Reels, post con video, Storie e album carosello in qualità originale sul tuo dispositivo. Nessun watermark, nessuna compressione e senza bisogno di inserire le credenziali di Instagram.',
    't1_h3': 'Instagram Downloader in sintesi',
    't1_headers': ['Caratteristica', 'Dettagli'],
    't1_rows': [
        ('Contenuti supportati', 'Instagram Reels, video del feed, Storie pubbliche, foto in alta risoluzione e post carosello multi-slide'),
        ('Link supportati', 'instagram.com/reel/..., instagram.com/p/..., instagram.com/stories/...'),
        ('Formati di output', 'Video MP4 (HD 1080p), immagini JPG originali, audio MP3 a 192kbps/320kbps'),
        ('Watermark aggiunto', '<span class="badge-highlight">Nessuno (Zero Watermark)</span>'),
        ('Costo', '<span class="badge-highlight">100% Gratuito senza limiti</span>'),
        ('Account richiesto', '<span class="badge-highlight">Nessun account necessario</span>'),
        ('Compatibilità', 'iPhone (iOS), Android, Windows, macOS, Linux, tablet'),
        ('Conservazione file', 'Zero log. I contenuti non vengono memorizzati sui nostri server')
    ],
    't2_h3': 'Quali tipi di contenuti di Instagram puoi salvare?',
    't2_intro': 'downsocial supporta tutti i principali formati multimediali di Instagram purché provengano da account pubblici:',
    't2_headers': ['Formato', 'Esempio di URL', 'Descrizione'],
    't2_rows': [
        ('Instagram Reels', 'instagram.com/reel/C...', 'Download del Reel completo in 1080p con audio sincronizzato'),
        ('Video del Feed', 'instagram.com/p/C...', 'Video tradizionali delle pubblicazioni nel feed'),
        ('Storie Pubbliche', 'instagram.com/stories/username/...', 'Salva le Storie prima che scadano dopo 24 ore'),
        ('Post Carosello', 'instagram.com/p/C...', 'Scarica tutte le foto e i video contenuti nel post'),
        ('Foto Singole', 'instagram.com/p/C...', 'Salva immagini in risoluzione originale 1080x1350 / 1080x1080'),
        ('Audio / Traccia Musicale', 'instagram.com/reels/audio/...', 'Estrai la traccia audio del Reel in formato MP3')
    ],
    'copy_h3': 'Come copiare il link da Instagram',
    'copy_items': [
        '<strong>Sull\'app Instagram:</strong> tocca l\'icona Condividi (aeroplanino di carta) sotto il Reel o post, poi tocca <em>Copia link</em>.',
        '<strong>Da browser su PC:</strong> apri il post e copia l\'indirizzo dalla barra del browser oppure clicca sui tre puntini > <em>Copia link</em>.'
    ],
    'device_h3': 'Come scaricare da Instagram su ogni dispositivo',
    'ios': '<strong>Su iPhone e iPad:</strong> apri Safari, visita downsocial, incolla il link e tocca Scarica video. Tocca Video (HD). Al termine del download, apri il file scaricato in Safari, premi Condividi e seleziona <em>Salva video</em> per ritrovarlo nell\'app Foto.',
    'android': '<strong>Su Android:</strong> incolla il link in Chrome, tocca Scarica video e scegli Video (HD). Il file viene salvato nella cartella Download ed è subito visibile nella Galleria del telefono.',
    'pc': '<strong>Su Windows o Mac:</strong> incolla il link nel browser, clicca su Scarica video e salva il file MP4 o JPG nella cartella che preferisci.',
    'priv_h3': 'È possibile scaricare da account privati di Instagram?',
    'priv_p': 'No. Nel rispetto della privacy e dei termini tecnici, il downloader supporta solo post e video provenienti da profili pubblici. Non chiediamo mai i tuoi dati di accesso né cerchiamo di bypassare i profili privati.',
    'qual_h3': 'Massima risoluzione originale garantita',
    'qual_p': 'Instagram carica i Reel a 1080x1920 pixel e le foto a 1080px di larghezza. downsocial estrae esattamente il file originale archiviato sul CDN senza ridimensionamenti né perdite di nitidezza.',
    'mp3_h3': 'Estrai l\'audio e la musica dai Reels in MP3',
    'mp3_p': 'Ti piace la canzone o il monologo di un Reel? Clicca su <strong>Audio (HQ MP3)</strong> per scaricare la traccia audio in alta definizione pronta da ascoltare su qualsiasi lettore.',
    'trouble_h3': 'Risoluzione dei problemi più comuni',
    'trouble_headers': ['Problema', 'Causa', 'Soluzione'],
    'trouble_rows': [
        ('Link non riconosciuto', 'Profilo privato o post rimosso', 'Verifica che il profilo sia pubblico aprendolo in navigazione anonima'),
        ('Storia non trovata', 'La Storia è scaduta dopo 24 ore', 'Le Storie scompaiono dopo 24 ore; scarica finché sono online'),
        ('Carosello parziale', 'Connessione debole', 'Ricarica la pagina e prova a scaricare le singole slide')
    ],
    'use_h3': 'I motivi più comuni per scaricare da Instagram',
    'use_items': [
        'Salvare i propri Reels e Storie senza la filigrana di Instagram.',
        'Conservare ricette, tutorial di fitness e consigli di viaggio per consultarli offline.',
        'Creare backup dei propri ricordi fotografici condivisi nel tempo.'
    ],
    'safe_h3': 'Sicurezza e Note Legali',
    'safe_p': 'downsocial è sicuro al 100%, non memorizza cookie di sessione né password. Rispetta sempre il diritto d\'autore: scarica contenuti solo per uso personale o con l\'autorizzazione dell\'autore. downsocial è uno strumento indipendente e non è affiliato a Meta o Instagram.',
    'tips_h3': 'Suggerimenti utili',
    'tips_items': [
        'Usa sempre il pulsante Condividi dell\'app per copiare link puliti.',
        'Seleziona Video (HD) per goderti la massima nitidezza sui tuoi schermi.',
        'Verifica che il profilo dell\'autore sia pubblico prima di effettuare il download.'
    ],
    'sister_h3': 'Altri strumenti disponibili',
    'sister_p': 'Scopri anche i nostri downloader per <a href="../facebook-downloader/">Facebook</a>, <a href="../tiktok-downloader/">TikTok</a>, <a href="../youtube-downloader/">YouTube</a>, <a href="../snapchat-downloader/">Snapchat</a> e <a href="../threads-downloader/">Threads</a>.',
    'last_updated': 'Ultimo aggiornamento: 4 ottobre 2026. Per supporto, visita la pagina <a href="contact.html">Contatti</a>.'
}
update_module_dict('seo_data_instagram', 'INSTAGRAM_DATA', instagram_it)

print("All platform modules updated with Italian successfully!")
