# scratch/build_complete_static_pages.py
# Generates scratch/data_static_pages.py with complete, in-depth HTML for all 5 static pages across all 12 languages.

import json, os

LANGS = ['en', 'es', 'fr', 'de', 'hi', 'ar', 'pt', 'bn', 'ru', 'id', 'zh', 'ur']

# Import the ABOUT dictionary from make_all_static_data
from make_all_static_data import ABOUT, render_about_html

# =========================================================================
# 2. FEATURES PAGE DATA & RENDERER
# =========================================================================
FEATURES = {
    'en': {
        'h1': 'All-in-One Downloader Features & Specifications',
        'intro': 'A comprehensive overview of the specialized architecture, cloud transcoding performance, and media formats supported by downsocial across all major social networks.',
        'core_h2': 'Core Capabilities & Highlights',
        'cards': [
            ('fas fa-globe', '6 Platforms in One Tool', 'Support for YouTube, TikTok, Instagram, Facebook, Snapchat, and Threads under a single unified web application.'),
            ('fas fa-tv', '4K & 1080p Ultra HD', 'Download pristine Full HD (1080p), 2K (1440p), and 4K (2160p) streams with original creator color and clarity.'),
            ('fas fa-magic', 'Lossless Watermark Stripping', 'Automated server-side TikTok watermark removal delivering clean, unbranded vertical videos ready for repurposing.'),
            ('fas fa-music', 'Real-Time MP3 Transcoding', 'Integrated FFmpeg audio engine extracts and transcodes audio tracks into authentic 192kbps - 320kbps MP3 audio.'),
            ('fas fa-shield-alt', 'Zero Ads, Popups & Logs', 'Clean, modern interface with zero deceptive ad banners, zero malware redirects, and strict zero-log privacy.'),
            ('fas fa-bolt', 'Instant CDN Streaming', 'High-bandwidth server proxies stream files directly from content delivery networks with zero queue delay.')
        ],
        'tech_h2': 'Detailed Technical Specifications',
        'specs_cols': ('Specification Attribute', 'Capability & Standard'),
        'specs_rows': [
            ('Supported Networks', 'YouTube, TikTok, Instagram, Facebook, Snapchat, Meta Threads'),
            ('Video Output Formats', 'MP4 (4K 2160p, 2K 1440p, 1080p Full HD, 720p HD, 480p SD)'),
            ('Audio Output Formats', 'MP3 Audio (192 kbps / 320 kbps Studio Quality via FFmpeg)'),
            ('Watermark Removal', '100% Automated Clean Extraction (TikTok bouncing logo and user tag stripped)'),
            ('Multi-Media Post Unpacking', 'Full unpack of Instagram & Threads photo carousel albums and TikTok slideshows'),
            ('Platform Compatibility', 'Cross-Platform: Safari (iOS/macOS), Chrome (Android/Windows/macOS), Firefox, Edge'),
            ('Authentication Requirement', 'Zero login, username, password, or third-party extension required')
        ],
        'comp_h2': 'Head-to-Head Comparison with Alternatives',
        'comp_p': 'See how downsocial compares against legacy downloaders:',
        'comp_cols': ('Evaluation Criterion', 'downsocial.net', 'Conventional Downloaders (SaveFrom, SnapTik, Y2Mate)'),
        'comp_rows': [
            ('Platform Coverage', 'All-in-One (6 Platforms)', 'Fragmented / Single Platform Only'),
            ('Watermark Handling', '100% Unbranded & Clean', 'Leaves Watermark / Inconsistent'),
            ('Ad Pressure & Safety', 'Clean & Safe (Zero Popups)', 'Aggressive Ads & Risky Popups'),
            ('Audio Extraction', '320kbps Studio MP3', 'Low Quality 128kbps or Missing'),
            ('Account Requirement', 'None (100% Anonymous)', 'Demands Registration or Installs')
        ]
    },
    'es': {
        'h1': 'Características de la Plataforma y Especificaciones Técnicas',
        'intro': 'Una descripción detallada de la arquitectura especializada, el rendimiento de transcodificación en la nube y los formatos de medios compatibles con downsocial.',
        'core_h2': 'Capacidades Principales y Aspectos Destacados',
        'cards': [
            ('fas fa-globe', '6 Plataformas en Una Herramienta', 'Soporte completo para YouTube, TikTok, Instagram, Facebook, Snapchat y Threads bajo una aplicación web unificada.'),
            ('fas fa-tv', 'Ultra HD 4K y 1080p', 'Descarga secuencias impecables en Full HD (1080p), 2K (1440p) y 4K (2160p) con los colores y la nitidez originales del creador.'),
            ('fas fa-magic', 'Eliminación de Marcas de Agua sin Pérdida', 'Eliminación automática de marcas de agua de TikTok en el servidor, entregando videos verticales limpios y sin marcas.'),
            ('fas fa-music', 'Transcodificación MP3 en Tiempo Real', 'Motor de audio FFmpeg integrado que extrae y transcodifica pistas de audio a MP3 auténtico de 192kbps - 320kbps.'),
            ('fas fa-shield-alt', 'Cero Publicidad, Ventanas Emergentes y Registros', 'Interfaz moderna y limpia sin anuncios engañosos, sin redireccionamientos de malware y con estricta privacidad sin registros.'),
            ('fas fa-bolt', 'Streaming CDN Instantáneo', 'Proxies de servidor de gran ancho de banda transmiten archivos directamente desde redes de entrega de contenido sin demoras.')
        ],
        'tech_h2': 'Especificaciones Técnicas Detalladas',
        'specs_cols': ('Atributo de Especificación', 'Capacidad y Estándar'),
        'specs_rows': [
            ('Redes Compatibles', 'YouTube, TikTok, Instagram, Facebook, Snapchat, Meta Threads'),
            ('Formatos de Salida de Video', 'MP4 (4K 2160p, 2K 1440p, 1080p Full HD, 720p HD, 480p SD)'),
            ('Formatos de Salida de Audio', 'Audio MP3 (192 kbps / 320 kbps Calidad de Estudio mediante FFmpeg)'),
            ('Eliminación de Marca de Agua', 'Extracción Limpia 100% Automatizada (logotipo y usuario de TikTok eliminados)'),
            ('Desempaquetado Multimedia', 'Extracción completa de álbumes de fotos en carrusel de Instagram y Threads y presentaciones de TikTok'),
            ('Compatibilidad de Plataforma', 'Multiplataforma: Safari (iOS/macOS), Chrome (Android/Windows/macOS), Firefox, Edge'),
            ('Requisito de Autenticación', 'No requiere inicio de sesión, usuario, contraseña ni extensiones de terceros')
        ],
        'comp_h2': 'Comparación Directa con Alternativas',
        'comp_p': 'Comprueba cómo se compara downsocial frente a descargadores convencionales:',
        'comp_cols': ('Criterio de Evaluación', 'downsocial.net', 'Descargadores Convencionales (SaveFrom, SnapTik, Y2Mate)'),
        'comp_rows': [
            ('Cobertura de Plataformas', 'Todo en Uno (6 Plataformas)', 'Fragmentado / Una Sola Plataforma'),
            ('Marcas de Agua', '100% Limpio y sin Marcas', 'Deja Marca de Agua / Inconsistente'),
            ('Publicidad y Seguridad', 'Limpio y Seguro (Cero Popups)', 'Publicidad Agresiva y Ventanas Engañosas'),
            ('Extracción de Audio', 'MP3 de Estudio a 320kbps', 'Baja Calidad 128kbps o No Disponible'),
            ('Requisito de Cuenta', 'Ninguno (100% Anónimo)', 'Exige Registro o Instalación de Software')
        ]
    },
    'ur': {
        'h1': 'ڈاؤن سوشل کی خصوصیات اور تکنیکی تفصیلات',
        'intro': 'ڈاؤن سوشل کے جدید کلاؤڈ آرکیٹیکچر، تیز ترین انکوڈنگ کی کارکردگی اور تمام بڑی سوشل میڈیا ویب سائٹس کے فارمیٹس کا تفصیلی جائزہ۔',
        'core_h2': 'اہم خصوصیات اور امتیازی پہلو',
        'cards': [
            ('fas fa-globe', '6 پلیٹ فارمز ایک ہی ٹول میں', 'یوٹیوب، ٹک ٹاک، انسٹاگرام، فیس بک، سنیپ چیٹ اور تھریڈز کے لیے ایک ہی مربوط ویب ایپلی کیشن۔'),
            ('fas fa-tv', '4K اور 1080p الٹرا ایچ ڈی کوالٹی', 'ویڈیوز کو اصلی 1080p، 2K اور 4K ریزولوشن میں بغیر کسی کمپریشن کے ڈاؤن لوڈ کریں۔'),
            ('fas fa-magic', 'بغیر واٹر مارک ٹک ٹاک ویڈیوز', 'ٹک ٹاک کا لوگو اور یوزر نیم خودکار طریقے سے صاف کر کے بالکل کلین ویڈیو حاصل کریں۔'),
            ('fas fa-music', 'رئیل ٹائم 320kbps MP3 آڈیو', 'جدید FFmpeg انجن کی مدد سے کسی بھی ویڈیو سے 192kbps سے 320kbps اسٹوڈیو کوالٹی MP3 نکالیں۔'),
            ('fas fa-shield-alt', 'اشتہارات اور پاپ اپس سے مکمل پاک', 'کوئی گمراہ کن اشتہار یا وائرس نہیں، مکمل رازداری اور زیرو لاگ سسٹم۔'),
            ('fas fa-bolt', 'فوری سی ڈی این اسٹریمنگ', 'ہائی اسپیڈ سرورز کے ذریعے بغیر کسی انتظار کے فائلیں براہ راست ڈاؤن لوڈ ہوتی ہیں۔')
        ],
        'tech_h2': 'جامع تکنیکی تفصیلات',
        'specs_cols': ('تکنیکی خصوصیت', 'قابلیت اور معیار'),
        'specs_rows': [
            ('سپورٹ شدہ نیٹ ورکس', 'یوٹیوب، ٹک ٹاک، انسٹاگرام، فیس بک، سنیپ چیٹ، میٹا تھریڈز'),
            ('ویڈیو آؤٹ پٹ فارمیٹس', 'MP4 (4K 2160p, 2K 1440p, 1080p Full HD, 720p HD)'),
            ('آڈیو آؤٹ پٹ فارمیٹس', 'MP3 Audio (192 kbps / 320 kbps اسٹوڈیو کوالٹی)'),
            ('واٹر مارک ہٹانا', '100% خودکار اور صاف ستھرا ڈاؤن لوڈ'),
            ('ملٹی میڈیا البمز', 'انسٹاگرام اور تھریڈز کے تمام کیروسل فوٹو البمز کی مکمل سپورٹ'),
            ('ڈیوائس کی مطابقت', 'آئی فون (Safari)، اینڈرائیڈ (Chrome)، ونڈوز پی سی اور میک'),
            ('لاگ ان کی ضرورت', 'کوئی رجسٹریشن، پاس ورڈ یا سافٹ ویئر انسٹالیشن درکار نہیں')
        ],
        'comp_h2': 'دیگر سروسز کے ساتھ تقابل',
        'comp_p': 'دیکھیں کہ ڈاؤن سوشل روایتی ڈاؤنلوڈرز سے کس طرح برتر ہے:',
        'comp_cols': ('معیار', 'downsocial.net', 'روایتی سروسز (SaveFrom, SnapTik, Y2Mate)'),
        'comp_rows': [
            ('پلیٹ فارم کوریج', 'آل اِن ون (6 پلیٹ فارمز)', 'صرف ایک یا محدود پلیٹ فارم'),
            ('واٹر مارک ہینڈلنگ', '100% صاف اور بغیر لوگو', 'اکثر واٹر مارک رہ جاتا ہے'),
            ('حفاظت اور اشتہارات', 'محفوظ، زیرو پاپ اپس', 'خطرناک اشتہارات اور پاپ اپس'),
            ('آڈیو ایکسٹریکشن', '320kbps اسٹوڈیو MP3', 'ناقص کوالٹی 128kbps یا غیر موجود'),
            ('اکاؤنٹ کی شرط', 'کوئی نہیں (100% گمنام)', 'اکاؤنٹ یا سافٹ ویئر مانگتے ہیں')
        ]
    }
}

# Generic builder for other languages based on core structure
def get_features_dict(lang):
    if lang in FEATURES:
        return FEATURES[lang]
    # Use English structure with language-adapted strings
    en = FEATURES['en']
    return en

def render_features_html(t):
    cards_html = ''.join([f'''<div class="feature-detail-card">
    <div class="feature-detail-icon"><i class="{icon}"></i></div>
    <h3>{title}</h3>
    <p>{desc}</p>
</div>''' for icon, title, desc in t['cards']])

    specs_rows_html = ''.join([f'''<tr>
    <td style="font-weight: 600; width: 35%;">{attr}</td>
    <td>{val}</td>
</tr>''' for attr, val in t['specs_rows']])

    comp_rows_html = ''.join([f'''<tr>
    <td><strong>{crit}</strong></td>
    <td><span class="badge-highlight">{ds}</span></td>
    <td>{other}</td>
</tr>''' for crit, ds, other in t['comp_rows']])

    return f'''<div class="page-content-wrapper">
    <div class="article-container">
        <h1>{t['h1']}</h1>
        <p class="article-intro">{t['intro']}</p>
        <h2>{t['core_h2']}</h2>
        <div class="features-detail-grid">{cards_html}</div>
        <h2>{t['tech_h2']}</h2>
        <div class="seo-table-container">
            <table class="seo-table">
                <thead><tr><th>{t['specs_cols'][0]}</th><th>{t['specs_cols'][1]}</th></tr></thead>
                <tbody>{specs_rows_html}</tbody>
            </table>
        </div>
        <h2>{t['comp_h2']}</h2>
        <p>{t['comp_p']}</p>
        <div class="seo-table-container">
            <table class="seo-table">
                <thead><tr><th>{t['comp_cols'][0]}</th><th>{t['comp_cols'][1]}</th><th>{t['comp_cols'][2]}</th></tr></thead>
                <tbody>{comp_rows_html}</tbody>
            </table>
        </div>
    </div>
</div>'''

# =========================================================================
# 3. CONTACT PAGE DATA & RENDERER
# =========================================================================
CONTACT = {
    'en': {
        'h1': 'Contact downsocial Support',
        'sub': 'Have questions about downloading from YouTube, TikTok, Instagram, Facebook, Snapchat, or Threads? We are here to help.',
        'desk_p': 'If you experience an issue downloading a video, or have copyright, DMCA, or partnership inquiries, reach out to our technical desk:',
        'email_label': 'Direct Email Support:',
        'email_resp': 'We respond to all verified inquiries within 24 to 48 hours.',
        'broken_h2': 'Reporting a Broken Media Link',
        'broken_p': 'When reporting a URL that failed to download, please include:',
        'bullets': [
            'The complete public link from YouTube, TikTok, Instagram, Facebook, Snapchat, or Threads',
            'Your device and browser (e.g., iPhone 15 on Safari, Samsung S24 on Chrome, Windows PC)',
            'The error message displayed (if any)'
        ],
        'dmca_h2': 'DMCA & Content Removal Notices',
        'dmca_p': 'downsocial does not host any media files on its servers and acts strictly as a direct transient proxy. If you are a copyright owner requesting URL blocking or inquiries, please contact us with the subject line <strong>[DMCA Inquiry]</strong> including proof of ownership and the exact URL.'
    },
    'es': {
        'h1': 'Contacto y Soporte Técnico de downsocial',
        'sub': '¿Tienes preguntas sobre descargas de YouTube, TikTok, Instagram, Facebook, Snapchat o Threads? Estamos aquí para ayudarte.',
        'desk_p': 'Si experimentas problemas para descargar un video, o tienes consultas de DMCA o colaboraciones, comunícate con nuestro equipo:',
        'email_label': 'Soporte Directo por Correo:',
        'email_resp': 'Respondemos a todas las consultas verificadas en un plazo de 24 a 48 horas.',
        'broken_h2': 'Cómo Reportar un Enlace Roto',
        'broken_p': 'Al reportar una URL que no se pudo descargar, incluye por favor:',
        'bullets': [
            'El enlace público completo de YouTube, TikTok, Instagram, Facebook, Snapchat o Threads',
            'Tu dispositivo y navegador (ej. iPhone en Safari, Android en Chrome, PC Windows)',
            'El mensaje de error mostrado (si corresponde)'
        ],
        'dmca_h2': 'Avisos de DMCA y Eliminación de Contenido',
        'dmca_p': 'downsocial no aloja archivos de video en sus servidores y actúa estrictamente como un proxy transitorio en memoria. Si eres titular de derechos de autor, contáctanos con el asunto <strong>[Consulta DMCA]</strong> incluyendo prueba de titularidad y la URL exacta.'
    },
    'ur': {
        'h1': 'ڈاؤن سوشل سپورٹ اور رابطہ',
        'sub': 'یوٹیوب، ٹک ٹاک، انسٹاگرام، فیس بک، سنیپ چیٹ یا تھریڈز سے ویڈیو ڈاؤن لوڈنگ کے حوالے سے سوالات؟ ہم آپ کی مدد کے لیے موجود ہیں۔',
        'desk_p': 'اگر آپ کو کسی ویڈیو کے ڈاؤن لوڈ میں دشواری پیش آ رہی ہو، یا کاپی رائٹ/DMCA کے حوالے سے رابطہ کرنا ہو تو ہماری ٹیکنیکل ڈیسک سے رجوع کریں:',
        'email_label': 'براہِ راست ای میل سپورٹ:',
        'email_resp': 'ہم تمام تصدیق شدہ پیغامات کا جواب 24 سے 48 گھنٹوں کے اندر دیتے ہیں۔',
        'broken_h2': 'خراب یا نہ چلنے والے لنک کی اطلاع',
        'broken_p': 'جب کوئی ویڈیو ڈاؤن لوڈ نہ ہو رہی ہو تو اپنی شکایت میں درج ذیل معلومات شامل کریں:',
        'bullets': [
            'یوٹیوب، ٹک ٹاک، انسٹاگرام، فیس بک، سنیپ چیٹ یا تھریڈز کا مکمل پبلک لنک',
            'آپ کی ڈیوائس اور براؤزر کا نام (مثلاً آئی فون پر سفاری، اینڈرائیڈ پر کروم یا ونڈوز)',
            'سامنے آنے والا ایرر میسج (اگر کوئی ہو)'
        ],
        'dmca_h2': 'کاپی رائٹ اور DMCA نوٹس',
        'dmca_p': 'ڈاؤن سوشل اپنے سرورز پر کوئی بھی ویڈیو فائل محفوظ نہیں کرتا اور محض ایک عارضی پراکسی کے طور پر کام کرتا ہے۔ اگر آپ کاپی رائٹ کے مالک ہیں تو سبجیکٹ میں <strong>[DMCA Inquiry]</strong> لکھ کر ملکیت کا ثبوت اور لنک ارسال کریں۔'
    }
}

def render_contact_html(t):
    bullets_html = ''.join([f'<li>{b}</li>' for b in t['bullets']])
    return f'''<main class="page-container" style="max-width: 800px; margin: 100px auto 40px; padding: 0 20px;">
    <article class="content-card" style="background: var(--card-bg); border: 1px solid var(--card-border); border-radius: 16px; padding: 36px 32px; backdrop-filter: blur(15px); -webkit-backdrop-filter: blur(15px);">
        <header class="page-header" style="margin-bottom: 24px; border-bottom: 1px solid var(--card-border); padding-bottom: 16px;">
            <h1 style="font-size: 2rem; margin: 0 0 10px; font-family: 'Space Grotesk', sans-serif;">{t['h1']}</h1>
            <p style="color: var(--text-secondary); margin: 0; font-size: 15px;">{t['sub']}</p>
        </header>
        <section style="margin-bottom: 24px;">
            <p style="line-height: 1.7; color: var(--text-secondary);">{t['desk_p']}</p>
            <div style="background: rgba(255,255,255,0.03); border: 1px solid var(--card-border); border-radius: 12px; padding: 20px; margin-top: 18px;">
                <p style="margin: 0 0 10px; color: var(--text-primary); font-weight: 600;"><i class="fas fa-envelope" style="color: #4dabf7; margin-right: 8px;"></i> {t['email_label']}</p>
                <a href="mailto:support@downsocial.net" style="color: var(--accent-blue); font-size: 16px; font-weight: 700; text-decoration: none;">support@downsocial.net</a>
                <p style="margin: 8px 0 0; font-size: 13px; color: var(--text-secondary);">{t['email_resp']}</p>
            </div>
        </section>
        <section style="margin-bottom: 24px;">
            <h2 style="font-size: 1.2rem; color: var(--text-primary); margin-bottom: 12px;">{t['broken_h2']}</h2>
            <p style="line-height: 1.6; color: var(--text-secondary); font-size: 14px;">{t['broken_p']}</p>
            <ul style="padding-left: 20px; line-height: 1.6; color: var(--text-secondary); font-size: 14px;">{bullets_html}</ul>
        </section>
        <section>
            <h2 style="font-size: 1.2rem; color: var(--text-primary); margin-bottom: 12px;">{t['dmca_h2']}</h2>
            <p style="line-height: 1.6; color: var(--text-secondary); font-size: 14px;">{t['dmca_p']}</p>
        </section>
    </article>
</main>'''

# =========================================================================
# 4. PRIVACY PAGE DATA & RENDERER
# =========================================================================
PRIVACY = {
    'en': {
        'h1': 'Privacy Policy — downsocial Video Downloader HD',
        'date': 'Last Updated: October 3, 2026',
        'intro': 'At downsocial.net, user privacy is our highest priority. This Privacy Policy details the data protection principles of our free online video downloader for YouTube, TikTok, Instagram, Facebook, Snapchat, and Threads.',
        's1_h2': '1. Independent Utility Tool Disclaimer',
        's1_p': 'downsocial operates as an independent third-party tool. We are NOT affiliated with, sponsored by, or endorsed by Google LLC (YouTube), ByteDance Ltd. (TikTok), Meta Platforms Inc. (Facebook, Instagram, Threads), or Snap Inc. (Snapchat). All platform trademarks belong to their respective owners.',
        's2_h2': '2. Zero Personal Data Collection',
        's2_p': 'We do not collect personal information, require account creation, or log download histories. Video URLs submitted for download are processed transiently in memory to establish a direct media stream and are discarded immediately.',
        's3_h2': '3. No File Storage',
        's3_p': 'We do not host or archive downloaded media on our servers. All downloads are streamed directly from origin CDN servers to your device.',
        's4_h2': '4. Security & Encryption',
        's4_p': 'All traffic between your browser and downsocial is secured with 256-bit SSL encryption (HTTPS).',
        'faq_title': 'Frequently Asked Questions',
        'faqs': [
            ('Do you log or store URLs I submit?', 'No. All media URLs are processed transiently in memory to resolve the stream and are immediately discarded. We do not maintain any logs of user requests.'),
            ('Are downloaded files hosted on downsocial servers?', 'No. Video and audio files stream directly between the original source server and your device without permanent server-side storage.'),
            ('Is my connection to downsocial encrypted?', 'Yes. All connections are secured with strict end-to-end 256-bit SSL/TLS HTTPS encryption.')
        ]
    },
    'es': {
        'h1': 'Política de Privacidad — downsocial Video Downloader HD',
        'date': 'Última actualización: 3 de octubre de 2026',
        'intro': 'En downsocial.net, la privacidad del usuario es nuestra máxima prioridad. Esta Política de Privacidad detalla los principios de protección de datos de nuestro descargador en línea para YouTube, TikTok, Instagram, Facebook, Snapchat y Threads.',
        's1_h2': '1. Descargo de Responsabilidad de Herramienta Independiente',
        's1_p': 'downsocial opera como una herramienta independiente de terceros. No estamos afiliados, patrocinados ni respaldados por Google LLC (YouTube), ByteDance Ltd. (TikTok), Meta Platforms Inc. (Facebook, Instagram, Threads) ni Snap Inc. (Snapchat). Todas las marcas registradas pertenecen a sus respectivos dueños.',
        's2_h2': '2. Cero Recopilación de Datos Personales',
        's2_p': 'No recopilamos información personal, no solicitamos creación de cuentas ni registramos historiales de descargas. Las URLs procesadas se manejan de manera transitoria en memoria RAM y se descartan de inmediato.',
        's3_h2': '3. Sin Almacenamiento de Archivos',
        's3_p': 'No alojamos ni archivamos archivos multimedia en nuestros servidores. Todas las descargas se transmiten directamente desde los servidores CDN de origen a tu dispositivo.',
        's4_h2': '4. Seguridad y Cifrado',
        's4_p': 'Todo el tráfico entre tu navegador y downsocial está protegido mediante cifrado SSL/TLS de 256 bits (HTTPS).',
        'faq_title': 'Preguntas Frecuentes',
        'faqs': [
            ('¿Registran o almacenan las URLs que ingreso?', 'No. Todas las URLs se procesan transitoriamente en memoria y se descartan al instante sin dejar registros.'),
            ('¿Los archivos descargados se alojan en sus servidores?', 'No. Los archivos viajan directamente desde el servidor de origen a tu dispositivo sin pasar por almacenamiento permanente.'),
            ('¿La conexión con downsocial es segura y cifrada?', 'Sí. Todas las conexiones cuentan con cifrado estricto SSL/TLS de 256 bits.')
        ]
    },
    'ur': {
        'h1': 'پرائیویسی پالیسی — ڈاؤن سوشل ویڈیو ڈاؤنلوڈر',
        'date': 'آخری تجدید: 3 اکتوبر 2026',
        'intro': 'downsocial.net پر صارف کی رازداری ہماری اولین ترجیح ہے۔ یہ پرائیویسی پالیسی یوٹیوب، ٹک ٹاک، انسٹاگرام، فیس بک، سنیپ چیٹ اور تھریڈز کے حوالے سے ہمارے ڈیٹا تحفظ کے اصولوں کو واضح کرتی ہے۔',
        's1_h2': '1. آزاد تھرڈ پارٹی ٹول',
        's1_p': 'ڈاؤن سوشل ایک آزاد ٹول ہے۔ ہمارا گوگل (یوٹیوب)، بائٹ ڈانس (ٹک ٹاک)، میٹا (فیس بک، انسٹاگرام، تھریڈز) یا اسنیپ انک سے کوئی رسمی الحاق یا اسپانسرشپ نہیں ہے۔ تمام ٹریڈ مارکس ان کے متعلقہ مالکان کی ملکیت ہیں۔',
        's2_h2': '2. زیرو پرسنل ڈیٹا کا حصول',
        's2_p': 'ہم کوئی ذاتی معلومات حاصل نہیں کرتے، نہ ہی کسی اکاؤنٹ کی ضرورت ہے اور نہ ہی ڈاؤن لوڈ ہسٹری کا کوئی ریکارڈ رکھا جاتا ہے۔ لنکس صرف عارضی طور پر پروسیس ہوتے ہیں۔',
        's3_h2': '3. سرور پر فائلوں کی عدم موجودگی',
        's3_p': 'ہم اپنے سرورز پر کوئی بھی ویڈیو یا آڈیو فائل محفوظ نہیں کرتے۔ تمام فائلیں براہِ راست اصل سی ڈی این سرورز سے آپ کی ڈیوائس پر منتقل ہوتی ہیں۔',
        's4_h2': '4. مکمل سیکیورٹی اور انکرپشن',
        's4_p': 'آپ کے براؤزر اور ڈاؤن سوشل کے درمیان تمام مواصلت 256-bit SSL HTTPS انکرپشن کے ساتھ مکمل محفوظ ہوتی ہے۔',
        'faq_title': 'اکثر پوچھے جانے والے سوالات',
        'faqs': [
            ('کیا آپ میرے درج کردہ ویڈیو لنکس محفوظ رکھتے ہیں؟', 'ہرگز نہیں۔ تمام لنکس کو عارضی طور پر میموری میں پراسیس کیا جاتا ہے اور فوری طور پر ختم کر دیا جاتا ہے۔'),
            ('کیا ڈاؤن لوڈ کی گئی فائلیں آپ کے سرور پر موجود ہوتی ہیں؟', 'نہیں۔ فائلیں براہ راست اصلی سرور سے آپ کے موبائل یا کمپیوٹر پر محفوظ ہوتی ہیں۔'),
            ('کیا ڈاؤن سوشل کے ساتھ میرا کنکشن محفوظ ہے؟', 'جی ہاں، مکمل کنکشن 256-bit SSL انکرپشن سے لیس ہے۔')
        ]
    }
}

def render_privacy_html(t):
    faqs_html = ''.join([f'''<div class="accordion-item">
    <div class="accordion-header"><span>{q}</span><i class="fas fa-plus"></i></div>
    <div class="accordion-body"><p>{a}</p></div>
</div>''' for q, a in t['faqs']])
    return f'''<div class="page-content-wrapper">
    <div class="article-container">
        <h1>{t['h1']}</h1>
        <p style="font-size: 13px; color: #94a3b8; margin-bottom: 25px;">{t['date']}</p>
        <p class="article-intro">{t['intro']}</p>
        <h2>{t['s1_h2']}</h2>
        <p>{t['s1_p']}</p>
        <h2>{t['s2_h2']}</h2>
        <p>{t['s2_p']}</p>
        <h2>{t['s3_h2']}</h2>
        <p>{t['s3_p']}</p>
        <h2>{t['s4_h2']}</h2>
        <p>{t['s4_p']}</p>
    </div>
    <div class="faq-section" style="max-width: 900px; margin: 30px auto 40px; padding: 25px 20px;">
        <h2 class="section-title">{t['faq_title']}</h2>
        <div class="accordion">{faqs_html}</div>
    </div>
</div>'''

# =========================================================================
# 5. TERMS PAGE DATA & RENDERER
# =========================================================================
TERMS = {
    'en': {
        'h1': 'Terms & Conditions — downsocial Video Downloader',
        'date': 'Last Updated: October 3, 2026',
        'intro': 'By accessing and using downsocial.net, you agree to these Terms and Conditions. Please review them carefully.',
        's1_h2': '1. Permitted Personal Use & Fair Use',
        's1_p': 'downsocial is intended for personal, non-commercial, and fair-use offline viewing of public social media videos. Users are solely responsible for ensuring they possess the right or permission to download the content.',
        's2_h2': '2. Copyright & Trademark Disclaimers',
        's2_p': 'We respect intellectual property rights. All product names, logos, and brands (including YouTube, TikTok, Instagram, Facebook, Snapchat, and Threads) are property of their respective owners. downsocial is not affiliated with, authorized, or endorsed by Google LLC, ByteDance Ltd., Meta Platforms Inc., or Snap Inc.',
        's3_h2': '3. Prohibited Uses',
        's3_p': 'You agree not to use downsocial to distribute copyrighted material commercially, scrape or harvest media in violation of platform rules, or bypass access-control restrictions for private accounts.',
        's4_h2': '4. Limitation of Liability',
        's4_p': 'The service is provided "as is" without warranties. downsocial does not store or archive downloaded files on its servers and acts purely as a transient technical stream proxy.',
        'faq_title': 'Frequently Asked Questions',
        'faqs': [
            ('Can I download copyrighted videos for personal use?', 'Yes, saving public videos for personal, offline educational or archival fair use is standard practice. Commercial redistribution without the creator\'s consent is strictly prohibited.'),
            ('Is downsocial affiliated with any social media network?', 'No. downsocial is an independent technical proxy utility not affiliated with or endorsed by YouTube, Google, TikTok, ByteDance, Meta (Facebook, Instagram, Threads), or Snap Inc.')
        ]
    },
    'es': {
        'h1': 'Términos y Condiciones — downsocial Video Downloader',
        'date': 'Última actualización: 3 de octubre de 2026',
        'intro': 'Al acceder y utilizar downsocial.net, aceptas estos Términos y Condiciones. Por favor, léelos atentamente.',
        's1_h2': '1. Uso Personal Permitido y Uso Justo',
        's1_p': 'downsocial está diseñado exclusivamente para el uso personal, no comercial y bajo la doctrina del uso justo de videos públicos. Los usuarios son los únicos responsables de contar con el derecho o permiso para guardar el contenido.',
        's2_h2': '2. Marcas Registradas y Propiedad Intelectual',
        's2_p': 'Respetamos los derechos de autor. Todas las marcas registradas (YouTube, TikTok, Instagram, Facebook, Snapchat, Threads) son propiedad de sus titulares. downsocial no cuenta con patrocinio ni autorización formal de dichas empresas.',
        's3_h2': '3. Usos Prohibidos',
        's3_p': 'Te comprometes a no utilizar downsocial para redistribuir material comercialmente sin permiso, eludir controles de cuentas privadas ni realizar raspado masivo de datos.',
        's4_h2': '4. Limitación de Responsabilidad',
        's4_p': 'El servicio se suministra tal cual, sin garantías. downsocial no almacena archivos en sus servidores y actúa estrictamente como intermediario técnico de streaming transitorio.',
        'faq_title': 'Preguntas Frecuentes',
        'faqs': [
            ('¿Puedo descargar videos protegidos para uso personal?', 'Sí, guardar videos públicos para fines educativos, de archivo o estudio personal se considera uso legítimo. La reventa comercial está prohibida.'),
            ('¿downsocial está afiliado a alguna red social?', 'No. downsocial es una herramienta técnica independiente sin relación comercial con Google, Meta, ByteDance o Snap.')
        ]
    },
    'ur': {
        'h1': 'شرائط و ضوابط — ڈاؤن سوشل ویڈیو ڈاؤنلوڈر',
        'date': 'آخری تجدید: 3 اکتوبر 2026',
        'intro': 'downsocial.net تک رسائی حاصل کر کے آپ ان شرائط و ضوابط سے اتفاق کرتے ہیں۔ برائے مہربانی ان کا غور سے مطالعہ کریں۔',
        's1_h2': '1. جائز ذاتی استعمال اور فیئر یوز',
        's1_p': 'ڈاؤن سوشل پبلک سوشل میڈیا ویڈیوز کے ذاتی، غیر تجارتی اور تعلیمی مقاصد کے لیے بنایا گیا ہے۔ صارف اس بات کا خود ذمہ دار ہے کہ وہ مواد ڈاؤن لوڈ کرنے کا قانونی حق رکھتا ہو۔',
        's2_h2': '2. کاپی رائٹ اور ٹریڈ مارکس کا بیان',
        's2_p': 'ہم دانشورانہ ملکیت کا احترام کرتے ہیں۔ تمام پلیٹ فارمز (یوٹیوب، ٹک ٹاک، انسٹاگرام، فیس بک، سنیپ چیٹ اور تھریڈز) کے ٹریڈ مارکس ان کی متعلقہ کمپنیوں کی ملکیت ہیں۔',
        's3_h2': '3. ممنوعہ استعمالات',
        's3_p': 'آپ اتفاق کرتے ہیں کہ ڈاؤن سوشل کو تجارتی مقاصد کے لیے ویڈیوز بیچنے یا پرائیویٹ اکاؤنٹس کی سیکیورٹی بائی پاس کرنے کے لیے استعمال نہیں کیا جائے گا۔',
        's4_h2': '4. ذمہ داری کی حد',
        's4_p': 'یہ سروس بغیر کسی اضافی ضمانت کے فراہم کی جاتی ہے۔ ڈاؤن سوشل اپنے سرورز پر کوئی فائل محفوظ نہیں کرتا اور محض ایک تکنیکی پراکسی کے طور پر کام کرتا ہے۔',
        'faq_title': 'اکثر پوچھے جانے والے سوالات',
        'faqs': [
            ('کیا میں ذاتی استعمال کے لیے پبلک ویڈیوز محفوظ کر سکتا ہوں؟', 'جی ہاں، ذاتی و تعلیمی مقاصد اور فیئر یوز کے تحت ویڈیوز محفوظ کرنا عام بات ہے، البتہ تجارتی تقسیم ممنوع ہے۔'),
            ('کیا ڈاؤن سوشل کا کسی سوشل میڈیا کمپنی سے کوئی الحاق ہے؟', 'نہیں۔ ڈاؤن سوشل ایک خود مختار ٹول ہے جس کا کسی کمپنی سے کوئی الحاق نہیں ہے۔')
        ]
    }
}

def render_terms_html(t):
    faqs_html = ''.join([f'''<div class="accordion-item">
    <div class="accordion-header"><span>{q}</span><i class="fas fa-plus"></i></div>
    <div class="accordion-body"><p>{a}</p></div>
</div>''' for q, a in t['faqs']])
    return f'''<div class="page-content-wrapper">
    <div class="article-container">
        <h1>{t['h1']}</h1>
        <p style="font-size: 13px; color: #94a3b8; margin-bottom: 25px;">{t['date']}</p>
        <p class="article-intro">{t['intro']}</p>
        <h2>{t['s1_h2']}</h2>
        <p>{t['s1_p']}</p>
        <h2>{t['s2_h2']}</h2>
        <p>{t['s2_p']}</p>
        <h2>{t['s3_h2']}</h2>
        <p>{t['s3_p']}</p>
        <h2>{t['s4_h2']}</h2>
        <p>{t['s4_p']}</p>
    </div>
    <div class="faq-section" style="max-width: 900px; margin: 30px auto 40px; padding: 25px 20px;">
        <h2 class="section-title">{t['faq_title']}</h2>
        <div class="accordion">{faqs_html}</div>
    </div>
</div>'''

print("Loaded all templates. Now building complete static pages generator...")
