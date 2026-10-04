# scratch/update_all_to_target_languages.py
# Injects Italian ('it') data and aligns all data sources to target 6 languages:
# ['en', 'es', 'pt', 'de', 'fr', 'it']

import os, sys, json

SCRATCH_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRATCH_DIR)

TARGET_LANGUAGES = ['en', 'es', 'pt', 'de', 'fr', 'it']

print("--- Step 1: Updating data_common_seo.py ---")
import data_common_seo

common_it = {
    'langBtn': 'Lingua', 'extBtn': 'Estensione', 'soonBadge': 'Presto',
    'homeBtn': 'Home', 'privateBtn': 'Downloader Privato', 'featuresBtn': 'Funzionalità',
    'aboutBtn': 'Chi Siamo', 'contactBtn': 'Contatti', 'privacyBtn': 'Informativa sulla Privacy', 'termsBtn': 'Termini di Servizio',
    'moreTools': 'Altri Strumenti', 'downloadBtn': 'Scarica Video',
    'readyTitle': 'Pronto per il Download!', 'infoText': 'Scegli la qualità preferita qui sotto.',
    'dlVidHigh': 'Video (HD)', 'dlVidNorm': 'Video (Normale)',
    'dlAudHigh': 'Audio (HQ MP3)', 'dlAudNorm': 'Audio (Normale MP3)',
    'moreDetails': 'Maggiori Dettagli', 'showLess': 'Meno Dettagli',
    'readMore': 'Leggi di Più', 'readLess': 'Leggi di Meno',
    'footerAboutTitle': 'downsocial.net',
    'footerAboutDesc': 'La piattaforma all-in-one di riferimento per scaricare video e audio dai social media. Download HD veloci, sicuri e senza filigrana o registrazione.',
    'footerToolsTitle': 'Strumenti di Download', 'footerLegalTitle': 'Azienda e Note Legali', 'footerSupportTitle': 'Supporto',
    'footerCopyright': '© 2026 downsocial.net. Tutti i diritti riservati.',
    'footerDisclaimer': 'Disclaimer: downsocial è un\'utilità tecnica indipendente e non è affiliata, approvata o sponsorizzata da Meta, Facebook, Instagram, TikTok, ByteDance, YouTube, Google, Snapchat, Snap Inc. o Threads. Tutti i marchi appartengono ai rispettivi proprietari.',
    'emptyLinkAlert': 'Per favore incolla prima un link video valido!',
    'processing': 'Elaborazione del flusso in corso...', 'successMsg': '✅ Video pronto per il download!', 'errorServer': 'Errore del server di streaming. Verifica l\'URL.'
}

notif_it = {
    'title': 'Tutte le 6 Piattaforme Online! 🚀',
    'time': 'Proprio ora',
    'content': 'Scarica video HD e audio MP3 da YouTube, TikTok, Instagram, Facebook, Snapchat e Threads senza watermark!'
}

# Update common module in-memory
data_common_seo.LANGUAGES = TARGET_LANGUAGES
data_common_seo.COMMON['it'] = common_it
data_common_seo.NOTIFICATIONS['it'] = notif_it

# Append to data_common_seo.py file
common_file = os.path.join(SCRATCH_DIR, 'data_common_seo.py')
with open(common_file, 'r', encoding='utf-8') as f:
    common_code = f.read()

if "'it':" not in common_code:
    # Update LANGUAGES line
    common_code = common_code.replace("LANGUAGES = ['en', 'es', 'fr', 'de', 'hi', 'ar', 'pt', 'bn', 'ru', 'id', 'zh', 'ur']",
                                      "LANGUAGES = ['en', 'es', 'pt', 'de', 'fr', 'it']")
    # Add it to COMMON
    it_common_str = f"    'it': {repr(common_it)},\n"
    common_code = common_code.replace("COMMON = {", "COMMON = {\n" + it_common_str)
    # Add it to NOTIFICATIONS
    it_notif_str = f"    'it': {repr(notif_it)},\n"
    common_code = common_code.replace("NOTIFICATIONS = {", "NOTIFICATIONS = {\n" + it_notif_str)
    with open(common_file, 'w', encoding='utf-8') as f:
        f.write(common_code)
    print("data_common_seo.py updated with 'it'")
else:
    print("data_common_seo.py already has 'it'")


print("--- Step 2: Updating data_seo_static.py ---")
import data_seo_static

seo_titles_it = {
    'index': 'Scaricare Video dai Social Network HD — All-in-One 1080p e 4K MP4 / MP3',
    'facebook': 'Scaricare Video da Facebook HD — Salva Reel, Storie e Video FB Gratis',
    'instagram': 'Scaricare Video da Instagram HD — Salva Reel, Storie, Foto e Carousel',
    'tiktok': 'Scaricare Video TikTok Senza Watermark — Download Video e MP3 HD',
    'youtube': 'Scaricare Video da YouTube HD — Download YouTube Shorts e MP3 320kbps',
    'snapchat': 'Scaricare Video da Snapchat HD — Salva Spotlight e Storie Pubbliche',
    'threads': 'Scaricare Video da Threads HD — Salva Video, Foto e Audio da Meta Threads',
    'private': 'Downloader Video Privato — Salva Video Tramite Codice Sorgente',
    'about': 'Chi Siamo — downsocial.net Downloader Social Media Gratuito',
    'features': 'Funzionalità e Specifiche Tecniche — downsocial.net',
    'contact': 'Contatti e Supporto Tecnico — downsocial.net',
    'privacy': 'Informativa sulla Privacy — downsocial.net',
    'terms': 'Termini di Servizio — downsocial.net'
}

seo_descs_it = {
    'index': 'Scarica video, reel, shorts e storie da YouTube, TikTok, Instagram, Facebook, Snapchat e Threads in 1080p HD, 4K e audio MP3 senza watermark.',
    'facebook': 'Scarica video, Facebook Reels, storie e video Watch in 1080p Full HD e audio MP3. Veloce, sicuro, senza pubblicità né login.',
    'instagram': 'Scarica Instagram Reels, Storie, Foto e post Carousel in risoluzione originale HD. Nessun watermark, 100% gratuito e anonimo.',
    'tiktok': 'Scarica video TikTok senza watermark in HD MP4 ed estrai l\'audio MP3 a 320kbps. Veloce, gratuito e senza installare app.',
    'youtube': 'Scarica video e Shorts da YouTube in 1080p, 2K, 4K UHD ed estrai tracce audio MP3 a 320kbps. Nessuna pubblicità, 100% gratuito.',
    'snapchat': 'Salva video Spotlight e storie pubbliche di Snapchat in qualità 1080p HD prima della loro scadenza. Nessuna registrazione necessaria.',
    'threads': 'Scarica video, album fotografici e note vocali da Meta Threads in 1080p Full HD e MP3. Strumento online rapido e senza limiti.',
    'private': 'Estrai e scarica video con restrizioni di privacy incollando il codice sorgente della pagina in modo sicuro sul tuo browser.',
    'about': 'Scopri di più sulla nostra missione per offrire il downloader video e audio più veloce, sicuro e privo di annunci sul web.',
    'features': 'Esplora le caratteristiche tecniche, il supporto dei codec e le capacità di estrazione video 4K e MP3 a 320kbps di downsocial.',
    'contact': 'Contatta il nostro team di assistenza clienti 24/7 per segnalare link non funzionanti o richiedere informazioni.',
    'privacy': 'Leggi la nostra politica a conoscenza zero: nessun tracciamento dei download, nessun cookie invasivo e nessuna conservazione dei file.',
    'terms': 'Consulta i termini e le condizioni d\'uso della piattaforma gratuita di download video e audio downsocial.net.'
}

for k, val in seo_titles_it.items():
    if k in data_seo_static.SEO_TITLES:
        data_seo_static.SEO_TITLES[k]['it'] = val
for k, val in seo_descs_it.items():
    if k in data_seo_static.SEO_DESCS:
        data_seo_static.SEO_DESCS[k]['it'] = val

seo_static_file = os.path.join(SCRATCH_DIR, 'data_seo_static.py')
with open(seo_static_file, 'r', encoding='utf-8') as f:
    seo_code = f.read()

if "'it':" not in seo_code:
    for k, v in seo_titles_it.items():
        search_target = f"'{k}': {{"
        replacement = f"'{k}': {{\n        'it': {repr(v)},"
        seo_code = seo_code.replace(search_target, replacement)
    for k, v in seo_descs_it.items():
        search_target = f"'{k}': {{"
        replacement = f"'{k}': {{\n        'it': {repr(v)},"
        # Only replace in descs
        pos = seo_code.find("SEO_DESCS = {")
        if pos != -1:
            part1 = seo_code[:pos]
            part2 = seo_code[pos:]
            part2 = part2.replace(f"'{k}': {{", f"'{k}': {{\n        'it': {repr(v)},", 1)
            seo_code = part1 + part2
    with open(seo_static_file, 'w', encoding='utf-8') as f:
        f.write(seo_code)
    print("data_seo_static.py updated with 'it'")
else:
    print("data_seo_static.py already has 'it'")


print("--- Step 3: Updating data_static_pages.py ---")
import data_static_pages

about_it = {
    'content': '''<div class="page-content-wrapper">
    <div class="article-container">
        <h1>Chi Siamo — downsocial: Downloader Video & Audio Tutto-in-Uno Gratuito</h1>
        <p class="article-intro">Benvenuto su downsocial.net. Abbiamo sviluppato questa piattaforma con una missione precisa: offrire a tutti una soluzione rapida, sicura e senza alcuna frizione per scaricare video, reel, shorts e tracce audio MP3 da Facebook, Instagram, TikTok, YouTube, Snapchat e Threads — senza watermark, senza registrazioni e 100% gratuito.</p>
        <h2>La Nostra Missione</h2>
        <p>Crediamo che salvare video accessibili pubblicamente per lo studio offline, i viaggi, l'archiviazione personale o i ricordi debba essere un'operazione semplice e rispettosa della privacy. La maggior parte dei downloader sul web è piena di pop-up ingannevoli, annunci rischiosi o installazioni forzate. downsocial offre un'esperienza web pulita, istantanea ed elegante direttamente dal tuo browser.</p>
        <h2>Supporto Architetturale Multi-Piattaforma</h2>
        <p>downsocial elimina la necessità di navigare tra siti diversi. Un unico motore intelligente individua la piattaforma ed estrae il flusso multimediale alla massima qualità:</p>
        <ul>
            <li><strong>Facebook:</strong> Reel, video pubblici del feed, episodi Watch e Storie in 1080p Full HD.</li>
            <li><strong>Instagram:</strong> Reel ad alto bitrate, Storie 24h, post carosello multi-slide e foto in risoluzione originale.</li>
            <li><strong>TikTok:</strong> Download puliti al 100% senza watermark galleggianti ed estrazione audio a 320 kbps.</li>
            <li><strong>YouTube:</strong> Clip video in 1080p, 2K e 4K UHD, YouTube Shorts e conversione audio in MP3 studio.</li>
            <li><strong>Snapchat:</strong> Video verticali Spotlight in 9:16 e Storie pubbliche prima della scadenza.</li>
            <li><strong>Meta Threads:</strong> Video di discussione, album fotografici e note vocali.</li>
        </ul>
        <h2>Privacy Totale e Politica Zero-Log</h2>
        <p>Operiamo secondo una rigorosa architettura a conoscenza zero: nessuna registrazione di account, nessun cookie di tracciamento e nessun file memorizzato sui nostri server. I tuoi download restano privati, transitori ed elaborati con crittografia SSL a 256 bit.</p>
    </div>
    <div class="faq-section" style="max-width: 900px; margin: 30px auto 40px; padding: 25px 20px;">
        <h2 class="section-title">Domande Frequenti</h2>
        <div class="accordion">
            <div class="accordion-item">
                <div class="accordion-header"><span>downsocial è davvero gratuito?</span><i class="fas fa-plus"></i></div>
                <div class="accordion-body"><p>Sì, downsocial è 100% gratuito con download illimitati e senza alcun costo di abbonamento nascosto.</p></div>
            </div>
            <div class="accordion-item">
                <div class="accordion-header"><span>Devo creare un account per scaricare video?</span><i class="fas fa-plus"></i></div>
                <div class="accordion-body"><p>Nessuna registrazione né login richiesti. Puoi scaricare video immediatamente e in forma anonima.</p></div>
            </div>
            <div class="accordion-item">
                <div class="accordion-header"><span>Quali piattaforme sono supportate?</span><i class="fas fa-plus"></i></div>
                <div class="accordion-body"><p>downsocial supporta il download da YouTube, TikTok (senza filigrana), Instagram Reels, Facebook, Snapchat e Threads.</p></div>
            </div>
            <div class="accordion-item">
                <div class="accordion-header"><span>downsocial conserva copie dei video scaricati?</span><i class="fas fa-plus"></i></div>
                <div class="accordion-body"><p>No. Operiamo secondo il principio zero-knowledge: nessun file multimediale viene memorizzato o archiviato sui nostri server.</p></div>
            </div>
        </div>
    </div>
</div>''',
    'pageHtml': ''
}
about_it['pageHtml'] = about_it['content']

features_it = {
    'content': '''<div class="page-content-wrapper">
    <div class="article-container">
        <h1>Funzionalità della Piattaforma e Specifiche Tecniche</h1>
        <p class="article-intro">Analisi approfondita dell'infrastruttura di estrazione dei flussi multimediali, codec video supportati e standard di qualità di downsocial.net.</p>
        <h2>1. Acquisizione Diretta Video 1080p, 2K & 4K Ultra HD MP4</h2>
        <p>downsocial si interfaccia direttamente con i manifest dei contenuti dei principali social network per catturare flussi video non ricompressi fino a risoluzioni 4K UHD.</p>
        <h2>2. Transcodifica Audio MP3 Professionale a 320kbps</h2>
        <p>Estrai la voce, basi musicali e audio virale in vero formato MP3 a 320kbps o 192kbps tramite pipeline di elaborazione audio ad alta fedeltà.</p>
        <h2>3. Rimozione Completa del Watermark da TikTok</h2>
        <p>Il nostro algoritmo identifica lo stream sorgente prima che il logo o l'ID utente vengano impressi in sovrimpressione, garantendo file nitidi e puliti.</p>
        <h2>4. Estrazione di Album Carosello Multi-Foto</h2>
        <p>Supporto completo per post con più diapositive su Instagram e Threads, con possibilità di scaricare ogni singola immagine o video ad alta risoluzione.</p>
        <h2>5. Architettura di Sicurezza a Conoscenza Zero</h2>
        <p>Nessuna password richiesta, nessun salvataggio delle URL elaborate e crittografia totale end-to-end con certificato SSL.</p>
    </div>
</div>''',
    'pageHtml': ''
}
features_it['pageHtml'] = features_it['content']

contact_it = {
    'content': '''<div class="page-content-wrapper">
    <div class="article-container">
        <h1>Contatti e Assistenza Clienti</h1>
        <p class="article-intro">Siamo qui per assisterti con segnalazioni di link non funzionanti, domande sul servizio o partnership commerciali.</p>
        <h2>Supporto Utenti e Richieste Tecniche</h2>
        <p>Se riscontri difficoltà nello scaricare un video o hai suggerimenti per migliorare la nostra piattaforma, il nostro desk di supporto è a tua disposizione:</p>
        <ul>
            <li><strong>Email di supporto:</strong> support@downsocial.net</li>
            <li><strong>Tempo di risposta:</strong> Garantito entro 24 ore</li>
            <li><strong>Disponibilità:</strong> 24 ore su 24, 7 giorni su 7</li>
        </ul>
        <h2>Come Segnalare un Link Non Funzionante</h2>
        <p>Per aiutarci a risolvere rapidamente il problema, includi nella tua segnalazione:</p>
        <ol>
            <li>L'URL pubblico esatto del video da Facebook, Instagram, TikTok, YouTube, Snapchat o Threads.</li>
            <li>Il browser e il sistema operativo che stai utilizzando (es. Safari su iOS 18, Chrome su Windows 11).</li>
            <li>L'eventuale messaggio di errore visualizzato a schermo.</li>
        </ol>
        <h2>Conformità DMCA e Diritto d'Autore</h2>
        <p>downsocial opera come un proxy tecnico temporaneo e non ospita né archivia alcun file multimediale. Per questioni relative a proprietà intellettuale o richieste di restrizione URL, scrivi a <strong>dmca@downsocial.net</strong>.</p>
    </div>
</div>''',
    'pageHtml': ''
}
contact_it['pageHtml'] = contact_it['content']

privacy_it = {
    'content': '''<div class="page-content-wrapper">
    <div class="article-container">
        <h1>Informativa sulla Privacy — downsocial.net</h1>
        <p class="article-intro">La tua privacy online è la nostra massima priorità. Questa informativa illustra chiaramente le nostre politiche sui dati e il rispetto dei tuoi diritti.</p>
        <h2>1. Politica Zero-Log</h2>
        <p>Non registriamo né archiviamo le tue ricerche, i link dei video incollati né gli indirizzi IP dei visitatori. Le operazioni di download sono elaborate in modo temporaneo ed effimero in memoria volatile.</p>
        <h2>2. Nessun Account o Password Richiesta</h2>
        <p>Non richiediamo alcuna registrazione, nome utente, indirizzo email o password dei tuoi account social per utilizzare downsocial. Il servizio è interamente anonimo.</p>
        <h2>3. Cookie e Tracciamento</h2>
        <p>downsocial utilizza unicamente cookie tecnici locali (come il localStorage) per memorizzare la tua lingua e il tema preferito (Chiaro, Scuro, Premium). Non impieghiamo cookie di profilazione pubblicitaria invasiva.</p>
        <h2>4. Crittografia SSL</h2>
        <p>Tutte le comunicazioni tra il tuo dispositivo e i nostri server sono protette tramite crittografia HTTPS con certificati SSL avanzati a 256 bit.</p>
    </div>
</div>''',
    'pageHtml': ''
}
privacy_it['pageHtml'] = privacy_it['content']

terms_it = {
    'content': '''<div class="page-content-wrapper">
    <div class="article-container">
        <h1>Termini di Servizio — downsocial.net</h1>
        <p class="article-intro">Accedendo e utilizzando downsocial.net, accetti di rispettare i seguenti Termini di Servizio.</p>
        <h2>1. Uso Personale e Consentito</h2>
        <p>downsocial è un'utilità tecnica progettata per consentire agli utenti di effettuare il download di contenuti multimediali pubblici per uso personale, didattico, di studio o per il backup dei propri file.</p>
        <h2>2. Proprietà Intellettuale e Diritto d'Autore</h2>
        <p>Tutti i diritti di copyright sui video, audio e immagini rimangono di esclusiva proprietà dei rispettivi autori. È fatto divieto di riutilizzare, vendere o ridistribuire a fini commerciali i contenuti scaricati senza la preventiva autorizzazione del titolare dei diritti.</p>
        <h2>3. Indipendenza e Marchi</h2>
        <p>downsocial è una piattaforma indipendente e non ha alcun vincolo, approvazione o partnership con Meta, Facebook, Instagram, TikTok, ByteDance, YouTube, Google, Snapchat o Snap Inc.</p>
        <h2>4. Esclusione di Responsabilità</h2>
        <p>Il servizio viene fornito "così com'è" senza garanzie implicite o esplicite sulla disponibilità ininterrotta o sulla compatibilità con link protetti o cancellati dalle piattaforme d'origine.</p>
    </div>
</div>''',
    'pageHtml': ''
}
terms_it['pageHtml'] = terms_it['content']

data_static_pages.STATIC_PAGES['about']['it'] = about_it
data_static_pages.STATIC_PAGES['features']['it'] = features_it
data_static_pages.STATIC_PAGES['contact']['it'] = contact_it
data_static_pages.STATIC_PAGES['privacy']['it'] = privacy_it
data_static_pages.STATIC_PAGES['terms']['it'] = terms_it

static_pages_file = os.path.join(SCRATCH_DIR, 'data_static_pages.py')
with open(static_pages_file, 'r', encoding='utf-8') as f:
    sp_code = f.read()

if "'it':" not in sp_code:
    # Inject it for each static page
    sp_dict = {
        'about': about_it,
        'features': features_it,
        'contact': contact_it,
        'privacy': privacy_it,
        'terms': terms_it
    }
    for p_name, p_data in sp_dict.items():
        search_key = f"'{p_name}': {{"
        insert_code = f"'{p_name}': {{\n        'it': {repr(p_data)},\n"
        sp_code = sp_code.replace(search_key, insert_code, 1)
    with open(static_pages_file, 'w', encoding='utf-8') as f:
        f.write(sp_code)
    print("data_static_pages.py updated with 'it'")
else:
    print("data_static_pages.py already has 'it'")

print("Static data updated successfully!")
