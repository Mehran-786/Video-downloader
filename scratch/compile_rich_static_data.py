# scratch/compile_rich_static_data.py
import json, os
from make_all_static_data import ABOUT, render_about_html
from enrich_all_static_languages import FEATURES_ALL
from build_complete_static_pages import (
    render_features_html, render_contact_html, render_privacy_html, render_terms_html
)

LANGS = ['en', 'es', 'fr', 'de', 'hi', 'ar', 'pt', 'bn', 'ru', 'id', 'zh', 'ur']

# Complete 12-language CONTACT dictionaries
CONTACT_ALL = {
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
    'fr': {
        'h1': 'Centre d’Aide et Contact downsocial',
        'sub': 'Des questions sur le téléchargement depuis YouTube, TikTok, Instagram, Facebook, Snapchat ou Threads ? Nous sommes à votre écoute.',
        'desk_p': 'Pour tout problème de téléchargement, demande de partenariat ou question DMCA, contactez notre équipe technique :',
        'email_label': 'Support Email Direct :',
        'email_resp': 'Nous répondons à tous les messages vérifiés sous 24 à 48 heures.',
        'broken_h2': 'Signaler un Lien de Vidéo Défectueux',
        'broken_p': 'Si une vidéo ne se télécharge pas, veuillez préciser :',
        'bullets': [
            'Le lien public complet depuis YouTube, TikTok, Instagram, Facebook, Snapchat ou Threads',
            'Votre appareil et votre navigateur (ex : iPhone sur Safari, Android sur Chrome, PC Windows)',
            'Le message d’erreur affiché (le cas échéant)'
        ],
        'dmca_h2': 'Avis DMCA & Retrait de Contenu',
        'dmca_p': 'downsocial n’héberge aucun fichier sur ses serveurs. Si vous êtes titulaire de droits d’auteur, contactez-nous avec pour objet <strong>[Demande DMCA]</strong> en joignant une preuve de propriété et l’URL concernée.'
    },
    'de': {
        'h1': 'downsocial Support & Kontakt',
        'sub': 'Fragen zum Herunterladen von Videos von YouTube, TikTok, Instagram, Facebook, Snapchat oder Threads? Wir helfen Ihnen gerne weiter.',
        'desk_p': 'Bei Download-Problemen, DMCA-Meldungen oder Kooperationsanfragen wenden Sie sich bitte an unseren Support:',
        'email_label': 'Direkter E-Mail-Support:',
        'email_resp': 'Wir antworten auf alle verifizierten Anfragen innerhalb von 24 bis 48 Stunden.',
        'broken_h2': 'Fehlerhaften Videolink Melden',
        'broken_p': 'Wenn ein Download fehlschlägt, geben Sie bitte folgende Details an:',
        'bullets': [
            'Den vollständigen öffentlichen Link von YouTube, TikTok, Instagram, Facebook, Snapchat oder Threads',
            'Ihr Gerät und den Browser (z. B. iPhone mit Safari, Android mit Chrome, Windows-PC)',
            'Die angezeigte Fehlermeldung (falls vorhanden)'
        ],
        'dmca_h2': 'DMCA & Urheberrechtsanfragen',
        'dmca_p': 'downsocial hostet keine Mediendateien auf eigenen Servern und fungiert rein als flüchtiger Proxy. Urheberrechtsinhaber wenden sich bitte mit dem Betreff <strong>[DMCA Inquiry]</strong> und Nachweis an uns.'
    },
    'hi': {
        'h1': 'डाउनसोशल सहायता और संपर्क केंद्र',
        'sub': 'YouTube, TikTok, Instagram, Facebook, Snapchat या Threads से वीडियो डाउनलोड करने के संबंध में कोई प्रश्न है? हम सहायता के लिए तैयार हैं।',
        'desk_p': 'यदि आपको वीडियो डाउनलोड करने में कोई समस्या आ रही है या कॉपीराइट/DMCA से संबंधित पूछताछ है, तो हमारी तकनीकी सहायता टीम से संपर्क करें:',
        'email_label': 'प्रत्यक्ष ईमेल सहायता:',
        'email_resp': 'हम 24 से 48 घंटों के भीतर सभी सत्यापित संदेशों का उत्तर देते हैं।',
        'broken_h2': 'अमान्य या टूटे हुए लिंक की रिपोर्ट करें',
        'broken_p': 'जब कोई लिंक डाउनलोड न हो, तो कृपया निम्नलिखित जानकारी अवश्य भेजें:',
        'bullets': [
            'YouTube, TikTok, Instagram, Facebook, Snapchat या Threads का पूरा सार्वजनिक लिंक',
            'आपका डिवाइस और ब्राउज़र (जैसे iPhone पर Safari, Android पर Chrome, या Windows PC)',
            'स्क्रीन पर दिखाई देने वाला त्रुटि संदेश (यदि कोई हो)'
        ],
        'dmca_h2': 'DMCA एवं सामग्री हटाने की सूचना',
        'dmca_p': 'डाउनसोशल अपने सर्वर पर कोई भी वीडियो फ़ाइल स्टोर नहीं करता है। यदि आप कॉपीराइट स्वामी हैं, तो विषय पंक्ति में <strong>[DMCA Inquiry]</strong> लिखकर स्वामित्व के प्रमाण सहित हमसे संपर्क करें।'
    },
    'ar': {
        'h1': 'الدعم الفني والتواصل مع downsocial',
        'sub': 'هل لديك استفسارات حول التنزيل من يوتيوب، تيك توك، إنستغرام، فيسبوك، سناب شات أو ثريدز؟ فريقنا هنا لمساعدتك.',
        'desk_p': 'إذا واجهت أي مشكلة أثناء تنزيل وسائط أو كان لديك استفسار متعلق بحقوق النشر وDMCA، تواصل مع مكتبنا التقني:',
        'email_label': 'الدعم عبر البريد الإلكتروني المباشر:',
        'email_resp': 'نقوم بالرد على جميع الرسائل والطلبات المؤكدة خلال 24 إلى 48 ساعة عمل.',
        'broken_h2': 'الإبلاغ عن رابط غير صالح أو تالف',
        'broken_p': 'عند الإبلاغ عن رابط تعذر تنزيله، يُرجى تزويدنا بالتفاصيل التالية:',
        'bullets': [
            'الرابط العام الكامل من يوتيوب، تيك توك، إنستغرام، فيسبوك، سناب شات أو ثريدز',
            'نوع جهازك والمتصفح المستخدم (مثل iPhone عبر Safari أو أندرويد عبر Chrome أو جهاز كمبيوتر)',
            'رسالة الخطأ التي ظهرت لك على الشاشة (إن وجدت)'
        ],
        'dmca_h2': 'إشعارات قانون الألفية للملكية الرقمية (DMCA)',
        'dmca_p': 'لا يستضيف downsocial أي ملفات وسائط على خوادمه نهائياً، ويعمل كوسيط تقني عابر فقط. إذا كنت مالكاً لحقوق الطبع والنشر، يُرجى مراسلتنا مع ذكر <strong>[DMCA Inquiry]</strong> في عنوان الرسالة متضمنة إثبات الملكية والرابط المعني.'
    },
    'pt': {
        'h1': 'Contato e Suporte downsocial',
        'sub': 'Dúvidas sobre downloads do YouTube, TikTok, Instagram, Facebook, Snapchat ou Threads? Nossa equipe está pronta para ajudar.',
        'desk_p': 'Se encontrar problemas para baixar vídeos ou tiver dúvidas sobre DMCA e direitos autorais, fale com nosso suporte técnico:',
        'email_label': 'Suporte por E-mail Direto:',
        'email_resp': 'Respondemos a todas as mensagens verificadas em até 24 a 48 horas.',
        'broken_h2': 'Como Notificar um Link Com Problemas',
        'broken_p': 'Ao relatar uma URL que não pôde ser baixada, inclua:',
        'bullets': [
            'O link público completo do YouTube, TikTok, Instagram, Facebook, Snapchat ou Threads',
            'Seu dispositivo e navegador (ex.: iPhone no Safari, Android no Chrome, PC Windows)',
            'A mensagem de erro exibida (caso haja)'
        ],
        'dmca_h2': 'Avisos de DMCA e Remoção de Mídia',
        'dmca_p': 'O downsocial não armazena arquivos em seus servidores. Titulares de direitos autorais podem solicitar remoções pelo e-mail com o assunto <strong>[Consulta DMCA]</strong> com provas de autoria e o link exato.'
    },
    'bn': {
        'h1': 'downsocial হেল্প ডেস্ক ও যোগাযোগ',
        'sub': 'ইউটিউব, টিকটক, ইনস্টাগ্রাম, ফেসবুক, স্ন্যাপচ্যাট বা থ্রেডস ডাউনলোডিং নিয়ে কোনো প্রশ্ন আছে? আমরা সাহায্য করতে প্রস্তুত।',
        'desk_p': 'ভিডিও ডাউনলোডে কোনো সমস্যা হলে কিংবা কপিরাইট/DMCA সম্পর্কিত কোনো নোটিশ থাকলে আমাদের টেকনিক্যাল ডেস্কে যোগাযোগ করুন:',
        'email_label': 'সরাসরি ইমেইল সাপোর্ট:',
        'email_resp': 'আমরা ২৪ থেকে ৪৮ ঘণ্টার মধ্যে সকল যাচাইকৃত বার্তার উত্তর দিয়ে থাকি।',
        'broken_h2': 'কাজ না করা ভিডিও লিংকের রিপোর্ট করুন',
        'broken_p': 'কোনো লিংক থেকে ডাউনলোড ব্যর্থ হলে অনুগ্রহ করে নিচের তথ্যগুলো অন্তর্ভুক্ত করুন:',
        'bullets': [
            'ইউটিউব, টিকটক, ইনস্টাগ্রাম, ফেসবুক, স্ন্যাপচ্যাট বা থ্রেডসের সম্পূর্ণ পাবলিক লিংক',
            'আপনার ডিভাইস এবং ব্রাউজারের নাম (যেমনঃ iPhone এ Safari, Android এ Chrome, Windows PC)',
            'স্ক্রিনে প্রদর্শিত ত্রুটি বার্তা (যদি থাকে)'
        ],
        'dmca_h2': 'কপিরাইট ও DMCA নোটিশ',
        'dmca_p': 'downsocial সার্ভারে কোনো ফাইল সংরক্ষণ করে না এবং এটি কেবল একটি ট্রানজিয়েন্ট প্রক্সি হিসেবে কাজ করে। কপিরাইটের স্বত্বাধিকারী হলে <strong>[DMCA Inquiry]</strong> লিখে লিঙ্কের প্রমাণ সহ ইমেইল পাঠান।'
    },
    'ru': {
        'h1': 'Служба поддержки и контакты downsocial',
        'sub': 'Возникли вопросы по скачиванию с YouTube, TikTok, Instagram, Facebook, Snapchat или Threads? Мы готовы помочь.',
        'desk_p': 'Если у вас возникли сложности со скачиванием или имеются вопросы по DMCA и сотрудничеству, напишите нам:',
        'email_label': 'Прямая поддержка по электронной почте:',
        'email_resp': 'Мы отвечаем на все проверенные запросы в течение 24–48 часов.',
        'broken_h2': 'Сообщить о неработающей ссылке',
        'broken_p': 'При сообщении о ссылке, которую не удалось загрузить, укажите:',
        'bullets': [
            'Полную публичную ссылку из YouTube, TikTok, Instagram, Facebook, Snapchat или Threads',
            'Ваше устройство и браузер (например, iPhone в Safari, Android в Chrome, ПК на Windows)',
            'Текст ошибки на экране (при наличии)'
        ],
        'dmca_h2': 'Уведомления DMCA и защита авторских прав',
        'dmca_p': 'downsocial не хранит медиафайлы на своих серверах. Правообладатели могут направить запрос с темой <strong>[DMCA Inquiry]</strong>, подтверждением прав и точным URL.'
    },
    'id': {
        'h1': 'Pusat Bantuan & Kontak downsocial',
        'sub': 'Punya pertanyaan seputar pengunduhan dari YouTube, TikTok, Instagram, Facebook, Snapchat, atau Threads? Kami siap membantu.',
        'desk_p': 'Jika mengalami kendala teknis saat mengunduh atau ada pertanyaan DMCA/kemitraan, hubungi meja dukungan kami:',
        'email_label': 'Dukungan Email Langsung:',
        'email_resp': 'Kami merespons semua pesan terverifikasi dalam waktu 24 hingga 48 jam.',
        'broken_h2': 'Laporkan Tautan Bermasalah',
        'broken_p': 'Saat melaporkan URL yang gagal diunduh, mohon sertakan:',
        'bullets': [
            'Tautan publik lengkap dari YouTube, TikTok, Instagram, Facebook, Snapchat, atau Threads',
            'Perangkat dan peramban yang Anda gunakan (mis. iPhone di Safari, Android di Chrome, PC Windows)',
            'Pesan kesalahan yang muncul di layar (jika ada)'
        ],
        'dmca_h2': 'Pemberitahuan DMCA & Penghapusan Konten',
        'dmca_p': 'downsocial tidak menyimpan file di servernya. Pemilik hak cipta dapat mengirimkan pemberitahuan dengan subjek <strong>[DMCA Inquiry]</strong> disertai bukti kepemilikan dan URL terkait.'
    },
    'zh': {
        'h1': 'downsocial 官方技术支持与联络中心',
        'sub': '针对解析下载 YouTube、TikTok、Instagram、Facebook、Snapchat 或 Threads 有任何疑问？我们随时为您提供协助。',
        'desk_p': '如遇视频解析异常、接口报错或有版权维权、DMCA 申诉及商业合作需求，欢迎随时联系官方工程台：',
        'email_label': '官方直通支持邮箱：',
        'email_resp': '我们在收到合规请求后的 24 至 48 小时内完成人工核验并予以答复。',
        'broken_h2': '提交失效链接报错指南',
        'broken_p': '在提交无法解析的链接工单时，请随信附带以下诊断参数：',
        'bullets': [
            '完整的官方公开媒体分享链接（涵盖 YouTube、TikTok、Instagram、Facebook、Snapchat 或 Threads）',
            '您所使用的操作系统及浏览器内核（如 iPhone Safari、Android Chrome、Windows Edge）',
            '网页界面上弹出的具体错误代码或提示文本（若有）'
        ],
        'dmca_h2': 'DMCA 知识产权保护与下架声明',
        'dmca_p': 'downsocial 严格恪守零存储原则，不托管任何版权音视频文件。版权方如需申请特定直链过滤屏蔽，请在邮件主题中注明 <strong>[DMCA Inquiry]</strong> 并附带权属有效证明与侵权源 URL。'
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

# Complete 12-language PRIVACY dictionaries
PRIVACY_ALL = {
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
    'fr': {
        'h1': 'Politique de Confidentialité — downsocial HD',
        'date': 'Dernière mise à jour : 3 octobre 2026',
        'intro': 'Chez downsocial.net, la confidentialité est absolue. Cette politique décrit la protection des données lors de vos téléchargements depuis YouTube, TikTok, Instagram, Facebook, Snapchat et Threads.',
        's1_h2': '1. Indépendance de l’Outil',
        's1_p': 'downsocial est un outil tiers indépendant, sans affiliation avec Google, ByteDance, Meta ou Snap Inc. Toutes les marques appartiennent à leurs propriétaires.',
        's2_h2': '2. Aucune Collecte de Données Personnelles',
        's2_p': 'Aucune création de compte, aucun cookie et aucun historique conservé. Les liens sont traités en mémoire vive et effacés immédiatement.',
        's3_h2': '3. Aucun Stockage de Fichiers',
        's3_p': 'Les fichiers ne sont jamais hébergés sur nos serveurs et transitent directement vers votre appareil.',
        's4_h2': '4. Sécurité & Chiffrement',
        's4_p': 'Toutes les communications sont protégées par un chiffrement SSL 256 bits (HTTPS).',
        'faq_title': 'Foire Aux Questions',
        'faqs': [
            ('Enregistrez-vous les liens soumis ?', 'Non. Tous les liens sont effacés dès la fin du traitement.'),
            ('Les fichiers sont-ils stockés sur vos serveurs ?', 'Non. Tout est acheminé directement depuis les serveurs d’origine.'),
            ('La connexion est-elle sécurisée ?', 'Oui, sécurisée de bout en bout via SSL 256 bits.')
        ]
    },
    'de': {
        'h1': 'Datenschutzerklärung — downsocial HD Downloader',
        'date': 'Zuletzt aktualisiert: 3. Oktober 2026',
        'intro': 'Auf downsocial.net steht der Schutz Ihrer Privatsphäre an erster Stelle. Diese Richtlinie erklärt den sicheren Umgang mit Daten beim Downloaden von YouTube, TikTok, Instagram, Facebook, Snapchat und Threads.',
        's1_h2': '1. Unabhängiger Drittanbieter',
        's1_p': 'downsocial ist ein unabhängiges Tool ohne formelle Verbindung zu Google, ByteDance, Meta oder Snap Inc.',
        's2_h2': '2. Keine Erfassung Personenbezogener Daten',
        's2_p': 'Keine Registrierung, keine Cookies und keine Speicherung von Download-Historien. URLs werden nur flüchtig im RAM verarbeitet.',
        's3_h2': '3. Keine Dateispeicherung',
        's3_p': 'Es werden keine Mediendateien auf unseren Servern gespeichert. Der Datenstrom fließt direkt zum Endgerät.',
        's4_h2': '4. Sicherheit und Verschlüsselung',
        's4_p': 'Der gesamte Datenverkehr ist durch 256-Bit SSL/TLS (HTTPS) abgesichert.',
        'faq_title': 'Häufig Gestellte Fragen',
        'faqs': [
            ('Werden meine Links gespeichert?', 'Nein. Alle Links werden sofort nach dem Parsen gelöscht.'),
            ('Werden Videos auf Ihren Servern gespeichert?', 'Nein, es erfolgt keinerlei permanente Speicherung.'),
            ('Ist die Verbindung verschlüsselt?', 'Ja, vollständig mit 256-Bit SSL gesichert.')
        ]
    },
    'hi': {
        'h1': 'गोपनीयता नीति — डाउनसोशल वीडियो डाउनलोडर',
        'date': 'अंतिम अपडेट: 3 अक्टूबर 2026',
        'intro': 'downsocial.net पर आपकी गोपनीयता हमारी सर्वोच्च प्राथमिकता है। यह नीति YouTube, TikTok, Instagram, Facebook, Snapchat और Threads से वीडियो डाउनलोड करते समय डेटा सुरक्षा के सिद्धांतों को स्पष्ट करती है।',
        's1_h2': '1. स्वतंत्र सेवा अस्वीकरण',
        's1_p': 'डाउनसोशल एक स्वतंत्र टूल है जिसका Google, ByteDance, Meta या Snap Inc. से कोई आधिकारिक संबंध नहीं है।',
        's2_h2': '2. व्यक्तिगत डेटा का शून्य संग्रह',
        's2_p': 'हम कोई व्यक्तिगत जानकारी या डाउनलोड इतिहास संग्रहीत नहीं करते हैं। लिंक केवल अस्थायी रूप से प्रोसेस होते हैं।',
        's3_h2': '3. सर्वर पर कोई फ़ाइल स्टोरेज नहीं',
        's3_p': 'हम सर्वर पर कोई वीडियो फ़ाइल स्टोर नहीं करते हैं। फ़ाइलें सीधे स्रोत से आपके डिवाइस पर आती हैं।',
        's4_h2': '4. सुरक्षा एवं एन्क्रिप्शन',
        's4_p': 'सभी संचार 256-बिट एसएसएल एन्क्रिप्शन के साथ पूरी तरह सुरक्षित हैं।',
        'faq_title': 'अक्सर पूछे जाने वाले प्रश्न',
        'faqs': [
            ('क्या आप मेरे दर्ज किए गए लिंक स्टोर करते हैं?', 'नहीं, सभी लिंक प्रोसेस होते ही तुरंत हटा दिए जाते हैं।'),
            ('क्या डाउनलोड किए गए वीडियो आपके सर्वर पर रहते हैं?', 'नहीं, सर्वर पर कोई फ़ाइल नहीं रखी जाती।'),
            ('क्या मेरा कनेक्शन सुरक्षित है?', 'हाँ, 256-बिट SSL के साथ 100% सुरक्षित है।')
        ]
    },
    'ar': {
        'h1': 'سياسة الخصوصية — downsocial Video Downloader HD',
        'date': 'آخر تحديث: 3 أكتوبر 2026',
        'intro': 'في downsocial.net، خصوصية المستخدم هي أولويتنا القصوى. توضح هذه السياسة معايير حماية البيانات عند التنزيل من يوتيوب، تيك توك، إنستغرام، فيسبوك، سناب شات وثريدز.',
        's1_h2': '1. إخلاء مسؤولية الأداة المستقلة',
        's1_p': 'تعمل downsocial كأداة طرف ثالث مستقلة، وليست تابعة لـ Google أو ByteDance أو Meta أو Snap Inc.',
        's2_h2': '2. انعدام جمع البيانات الشخصية',
        's2_p': 'لا نجمع أي معلومات شخصية ولا نطلب تسجيل حسابات ولا نحتفظ بسجلات التنزيل نهائياً.',
        's3_h2': '3. عدم تخزين الملفات على الخوادم',
        's3_p': 'لا نستضيف أي وسائط على خوادمنا، وتتدفق الملفات مباشرة من خوادم الأصل إلى جهازك.',
        's4_h2': '4. الأمان والتشفير العالي',
        's4_p': 'جميع الاتصالات محمية بتشفير SSL عالي الأمان بقوة 256 بت (HTTPS).',
        'faq_title': 'الأسئلة الشائعة',
        'faqs': [
            ('هل تقومون بحفظ الروابط التي أدخلها؟', 'كلا، تُحذف الروابط فور معالجتها في الذاكرة المؤقتة.'),
            ('هل يتم تخزين الفيديوهات على خوادمكم؟', 'لا، يتم التنزيل مباشرة إلى جهازك.'),
            ('هل الاتصال بموقعكم آمن ومشفر؟', 'نعم، مشفر بالكامل بتقنية SSL 256 بت.')
        ]
    },
    'pt': {
        'h1': 'Política de Privacidade — downsocial Video Downloader HD',
        'date': 'Última atualização: 3 de outubro de 2026',
        'intro': 'No downsocial.net, sua privacidade é prioridade absoluta. Conheça nossas diretrizes de proteção de dados ao usar nosso baixador gratuito.',
        's1_h2': '1. Isenção de Responsabilidade de Ferramenta Independente',
        's1_p': 'O downsocial é independente e não possui vínculo com Google, ByteDance, Meta ou Snap Inc.',
        's2_h2': '2. Zero Coleta de Dados Pessoais',
        's2_p': 'Não exigimos contas e não registramos históricos. Links são processados em memória volátil.',
        's3_h2': '3. Sem Armazenamento de Arquivos',
        's3_p': 'Não hospedamos mídias em nossos servidores; os arquivos vão direto ao seu dispositivo.',
        's4_h2': '4. Segurança e Criptografia',
        's4_p': 'Todas as conexões são protegidas com criptografia SSL de 256 bits (HTTPS).',
        'faq_title': 'Perguntas Frequentes',
        'faqs': [
            ('Vocês salvam as URLs enviadas?', 'Não, os links são descartados imediatamente após a extração.'),
            ('Os vídeos ficam salvos nos servidores?', 'Não, nenhum arquivo permanece em nossos servidores.'),
            ('A conexão é segura?', 'Sim, 100% protegida com SSL de ponta a ponta.')
        ]
    },
    'bn': {
        'h1': 'প্রাইভেসি পলিসি — downsocial ভিডিও ডাউনলোডার',
        'date': 'সর্বশেষ আপডেট: ৩ অক্টোবর, ২০২৬',
        'intro': 'downsocial.net-এ আপনার গোপনীয়তা আমাদের প্রথম অগ্রাধিকার। এই নীতিমালায় ডেটা সুরক্ষার নিয়মাবলী তুলে ধরা হয়েছে।',
        's1_h2': '১. স্বাধীন সেবা সংক্রান্ত ঘোষণা',
        's1_p': 'downsocial একটি স্বাধীন প্ল্যাটফর্ম। গুগল, বাইটড্যান্স, মেটা বা স্ন্যাপ ইনকর্পোরেটেডের সাথে কোনো আনুষ্ঠানিক সম্পর্ক নেই।',
        's2_h2': '২. কোনো ব্যক্তিগত তথ্য সংগ্রহ করা হয় না',
        's2_p': 'কোনো অ্যাকাউন্ট রেজিস্ট্রেশন বা হিস্ট্রি রাখা হয় না। লিংকগুলো শুধু মেমরিতে প্রসেস হয়।',
        's3_h2': '৩. সার্ভারে ফাইল সংরক্ষণ না করা',
        's3_p': 'আমাদের সার্ভারে কোনো ভিডিও রাখা হয় না। ফাইল সরাসরি মূল সার্ভার থেকে আপনার ডিভাইসে চলে যায়।',
        's4_h2': '৪. নিরাপত্তা ও এনক্রিপশন',
        's4_p': 'আপনার ব্রাউজার ও আমাদের সাইটের সংযোগটি ২৫৬-বিট SSL HTTPS এনক্রিপশনে সুরক্ষিত।',
        'faq_title': 'প্রায়শই জিজ্ঞাসিত প্রশ্নাবলী',
        'faqs': [
            ('আপনারা কি আমার পেস্ট করা লিংক সেভ করেন?', 'না, প্রসেস শেষ হওয়ার সাথে সাথে লিংক মুছে ফেলা হয়।'),
            ('ভিডিওগুলো কি আপনাদের সার্ভারে থাকে?', 'না, কোনো মিডিয়া ফাইল সংরক্ষণ করা হয় না।'),
            ('সংযোগটি কি নিরাপদ?', 'হ্যাঁ, শতভাগ এনক্রিপ্টেড ও নিরাপদ।')
        ]
    },
    'ru': {
        'h1': 'Политика конфиденциальности — downsocial HD',
        'date': 'Последнее обновление: 3 октября 2026 г.',
        'intro': 'На downsocial.net защита конфиденциальности пользователей является главным приоритетом. Ознакомьтесь с нашими стандартами безопасности.',
        's1_h2': '1. Независимый сервис',
        's1_p': 'downsocial действует независимо и не имеет отношения к Google, ByteDance, Meta или Snap Inc.',
        's2_h2': '2. Никакого сбора персональных данных',
        's2_p': 'Мы не требуем регистрации и не ведем логов скачиваний. Ссылки обрабатываются только в оперативной памяти.',
        's3_h2': '3. Отсутствие хранения файлов',
        's3_p': 'Файлы не хранятся на наших серверах и передаются напрямую на ваше устройство.',
        's4_h2': '4. Безопасность и шифрование',
        's4_p': 'Все сессии защищены 256-битным SSL-шифрованием (HTTPS).',
        'faq_title': 'Часто Задаваемые Вопросы',
        'faqs': [
            ('Сохраняются ли ссылки, которые я ввожу?', 'Нет, они моментально удаляются после обработки.'),
            ('Хранятся ли загруженные видео на серверах?', 'Нет, постоянное хранение полностью исключено.'),
            ('Защищено ли соединение?', 'Да, используется надежное шифрование SSL 256 бит.')
        ]
    },
    'id': {
        'h1': 'Kebijakan Privasi — downsocial Video Downloader HD',
        'date': 'Terakhir Diperbarui: 3 Oktober 2026',
        'intro': 'Di downsocial.net, privasi pengguna adalah prioritas tertinggi kami. Kebijakan ini menjelaskan perlindungan data saat Anda menggunakan layanan kami.',
        's1_h2': '1. Penafian Alat Independen',
        's1_p': 'downsocial adalah alat pihak ketiga independen tanpa afiliasi resmi dengan Google, ByteDance, Meta, atau Snap Inc.',
        's2_h2': '2. Nol Pengumpulan Data Pribadi',
        's2_p': 'Kami tidak mengumpulkan data pribadi atau riwayat unduhan. Tautan hanya diproses sementara di RAM.',
        's3_h2': '3. Tanpa Penyimpanan File',
        's3_p': 'Kami tidak menyimpan file media di server. Semua file dialirkan langsung ke perangkat Anda.',
        's4_h2': '4. Keamanan & Enkripsi',
        's4_p': 'Semua lalu lintas dilindungi enkripsi SSL 256-bit (HTTPS).',
        'faq_title': 'Pertanyaan yang Sering Diajukan',
        'faqs': [
            ('Apakah tautan yang saya masukkan dicatat?', 'Tidak, tautan langsung dibuang setelah proses selesai.'),
            ('Apakah file unduhan disimpan di server?', 'Tidak, kami tidak menyimpan file apa pun.'),
            ('Apakah koneksi saya aman?', 'Ya, terenkripsi aman dengan SSL 256-bit.')
        ]
    },
    'zh': {
        'h1': '隐私权保护政策 — downsocial 高清视频下载器',
        'date': '最近更新日期：2026 年 10 月 3 日',
        'intro': '在 downsocial.net，用户数字隐私是我们一切架构的基石。本政策详细阐述我们在解析音视频流时的安全处理准则。',
        's1_h2': '1. 独立第三方工具免责声明',
        's1_p': 'downsocial 属于完全独立的第三方云工具，与 Google、ByteDance、Meta 或 Snap Inc. 无任何资本或官方隶属关系。',
        's2_h2': '2. 零个人身份数据搜集准则',
        's2_p': '平台不设会员体系、不记录任何解析历史。用户提交的 URL 仅在内存中瞬时流转，解析完毕即刻销毁。',
        's3_h2': '3. 零服务器文件持久化存储',
        's3_p': '我们从不在服务器持久化归档任何音视频文件。所有媒体流均由官方 CDN 直接穿透传输至您的本地终端。',
        's4_h2': '4. 银行级传输加密保护',
        's4_p': '浏览器与本站间的所有通信全程受 256 位 SSL/TLS（HTTPS）强加密严密防护。',
        'faq_title': '常见问题解答 (FAQ)',
        'faqs': [
            ('你们会记录或保存我提交的视频链接吗？', '绝不会。所有解析请求均在内存瞬时执行，处理完毕即刻销毁，不留任何痕迹。'),
            ('下载的媒体文件会存放在你们的服务器上吗？', '绝对不会。文件直接从官方媒体源流转至您的本地设备。'),
            ('访问 downsocial 的连接足够安全吗？', '是的，全站标配 256 位高强度 SSL/TLS 端到端加密。')
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

# Complete 12-language TERMS dictionaries
TERMS_ALL = {
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
    'fr': {
        'h1': 'Conditions Générales d’Utilisation — downsocial',
        'date': 'Dernière mise à jour : 3 octobre 2026',
        'intro': 'En accédant à downsocial.net, vous acceptez les présentes conditions générales. Veuillez les lire attentivement.',
        's1_h2': '1. Utilisation Personnelle & Usage Équitable',
        's1_p': 'downsocial est réservé à un usage personnel, non commercial et éducatif de vidéos publiques.',
        's2_h2': '2. Propriété Intellectuelle & Marques',
        's2_p': 'Toutes les marques citées (YouTube, TikTok, Instagram, Facebook, Snapchat, Threads) appartiennent à leurs propriétaires respectifs.',
        's3_h2': '3. Utilisations Interdites',
        's3_p': 'Il est strictement interdit d’utiliser le service pour pirater du contenu privé ou redistribuer des vidéos à des fins commerciales.',
        's4_h2': '4. Limite de Responsabilité',
        's4_p': 'Le service est fourni en l’état. Aucun fichier n’est conservé sur nos serveurs.',
        'faq_title': 'Foire Aux Questions',
        'faqs': [
            ('Puis-je télécharger des vidéos pour mon usage personnel ?', 'Oui, la sauvegarde de vidéos publiques pour un usage privé et éducatif relève du fair-use.'),
            ('Êtes-vous affilié aux réseaux sociaux ?', 'Non, downsocial est un outil indépendant.')
        ]
    },
    'de': {
        'h1': 'Allgemeine Geschäftsbedingungen — downsocial',
        'date': 'Zuletzt aktualisiert: 3. Oktober 2026',
        'intro': 'Mit der Nutzung von downsocial.net stimmen Sie diesen Nutzungsbedingungen zu.',
        's1_h2': '1. Zulässige Persönliche Nutzung',
        's1_p': 'downsocial dient ausschließlich dem privaten, nicht-kommerziellen Zweck zum Offline-Anschauen öffentlich zugänglicher Videos.',
        's2_h2': '2. Urheberrecht und Markenzeichen',
        's2_p': 'Alle genannten Markennamen gehören ihren jeweiligen Eigentümern.',
        's3_h2': '3. Unzulässige Nutzung',
        's3_p': 'Die kommerzielle Weiterverbreitung oder das Umgehen von Schutzmechanismen ist untersagt.',
        's4_h2': '4. Haftungsbeschränkung',
        's4_p': 'Die Bereitstellung erfolgt ohne Gewähr als rein technischer Streaming-Proxy.',
        'faq_title': 'Häufig Gestellte Fragen',
        'faqs': [
            ('Darf ich Videos für den Privatgebrauch speichern?', 'Ja, die private Archivierung öffentlicher Videos ist zulässig.'),
            ('Besteht eine Partnerschaft mit Plattformen?', 'Nein, downsocial ist ein unabhängiges Hilfswerkzeug.')
        ]
    },
    'hi': {
        'h1': 'नियम एवं शर्तें — डाउनसोशल वीडियो डाउनलोडर',
        'date': 'अंतिम अपडेट: 3 अक्टूबर 2026',
        'intro': 'downsocial.net का उपयोग करके आप इन नियमों और शर्तों से सहमत होते हैं। कृपया इन्हें ध्यान से पढ़ें।',
        's1_h2': '1. व्यक्तिगत एवं उचित उपयोग',
        's1_p': 'डाउनसोशल केवल सार्वजनिक वीडियो के व्यक्तिगत और गैर-व्यावसायिक ऑफ़लाइन देखने के लिए है।',
        's2_h2': '2. कॉपीराइट अस्वीकरण',
        's2_p': 'सभी ट्रेडमार्क (YouTube, TikTok, Instagram, Facebook, Snapchat, Threads) उनके संबंधित स्वामियों की संपत्ति हैं।',
        's3_h2': '3. प्रतिबंधित उपयोग',
        's3_p': 'व्यावसायिक पुनर्वितरण या निजी खातों की सुरक्षा को बायपास करने का प्रयास पूर्णतः प्रतिबंधित है।',
        's4_h2': '4. दायित्व की सीमा',
        's4_p': 'सेवा बिना किसी वारंटी के प्रदान की जाती है। हम सर्वर पर कोई मीडिया फ़ाइल संग्रहीत नहीं करते हैं।',
        'faq_title': 'अक्सर पूछे जाने वाले प्रश्न',
        'faqs': [
            ('क्या व्यक्तिगत उपयोग के लिए वीडियो डाउनलोड करना कानूनी है?', 'हाँ, व्यक्तिगत अध्ययन या ऑफ़लाइन देखने के लिए सार्वजनिक वीडियो सुरक्षित करना वैध है।'),
            ('क्या डाउनसोशल किसी सोशल नेटवर्क से जुड़ा है?', 'नहीं, यह पूरी तरह से एक स्वतंत्र टूल है।')
        ]
    },
    'ar': {
        'h1': 'الشروط والأحكام — downsocial Video Downloader',
        'date': 'آخر تحديث: 3 أكتوبر 2026',
        'intro': 'باستخدامك لموقع downsocial.net، فإنك توافق على الالتزام بهذه الشروط والأحكام.',
        's1_h2': '1. الاستخدام الشخصي المسموح والاستخدام العادل',
        's1_p': 'downsocial مخصص للاستخدام الشخصي وغير التجاري لمشاهدة مقاطع الفيديو العامة في وضع عدم الاتصال.',
        's2_h2': '2. إخلاء مسؤولية حقوق النشر والعلامات التجارية',
        's2_p': 'جميع العلامات التجارية وأسماء المنتجات هي ملك لأصحابها المعنيين دون أي علاقة رسمية مع الموقع.',
        's3_h2': '3. الاستخدامات المحظورة',
        's3_p': 'يُحظر تماماً استخدام الموقع لإعادة التوزيع التجاري أو محاولة تجاوز القيود المفروضة على الحسابات الخاصة.',
        's4_h2': '4. حدود المسؤولية',
        's4_p': 'تُقدم الخدمة "كما هي" دون ضمانات إضافية، حيث لا يخزن الموقع أي ملفات وسائط على خوادمه.',
        'faq_title': 'الأسئلة الشائعة',
        'faqs': [
            ('هل يجوز تنزيل مقاطع الفيديو للاستخدام الشخصي؟', 'نعم، حفظ الفيديوهات العامة لأغراض شخصية وتعليمية يُعد استخداماً عادلاً.'),
            ('هل موقع downsocial تابع لأي شبكة اجتماعية؟', 'لا، نحن أداة تقنية وسيطة مستقلة تماماً.')
        ]
    },
    'pt': {
        'h1': 'Termos e Condições — downsocial Video Downloader',
        'date': 'Última atualização: 3 de outubro de 2026',
        'intro': 'Ao acessar e utilizar o downsocial.net, você concorda com estes Termos e Condições.',
        's1_h2': '1. Uso Pessoal e Uso Justo',
        's1_p': 'O downsocial destina-se ao uso pessoal e não comercial para visualização offline de vídeos públicos.',
        's2_h2': '2. Direitos Autorais e Marcas',
        's2_p': 'Todas as marcas registradas pertencem aos seus respectivos proprietários.',
        's3_h2': '3. Usos Proibidos',
        's3_p': 'É expressamente proibido redistribuir mídias comercialmente sem permissão.',
        's4_h2': '4. Limitação de Responsabilidade',
        's4_p': 'O serviço é fornecido no estado em que se encontra, sem retenção de arquivos.',
        'faq_title': 'Perguntas Frequentes',
        'faqs': [
            ('Posso baixar vídeos para uso pessoal?', 'Sim, salvar vídeos públicos para fins de estudo ou arquivo pessoal é considerado uso justo.'),
            ('O site tem vínculo com as redes sociais?', 'Não, é uma ferramenta técnica independente.')
        ]
    },
    'bn': {
        'h1': 'নিয়ম ও শর্তাবলী — downsocial ভিডিও ডাউনলোডার',
        'date': 'সর্বশেষ আপডেট: ৩ অক্টোবর, ২০২৬',
        'intro': 'downsocial.net ব্যবহার করার মাধ্যমে আপনি এই নিয়ম ও শর্তাবলীতে সম্মত হচ্ছেন।',
        's1_h2': '১. ব্যক্তিগত ও ন্যায্য ব্যবহার',
        's1_p': 'downsocial শুধুমাত্র ব্যক্তিগত, অবাণিজ্যিক এবং অফলাইনে পাবলিক ভিডিও দেখার জন্য তৈরি।',
        's2_h2': '২. কপিরাইট ও ট্রেডমার্ক সংক্রান্ত ঘোষণা',
        's2_p': 'সকল ট্রেডমার্ক তাদের নিজ নিজ প্রতিষ্ঠানের সম্পত্তি।',
        's3_h2': '৩. নিষিদ্ধ ব্যবহার',
        's3_p': 'অনুমতি ছাড়া বাণিজ্যিক পুনর্বিতরণ বা ব্যক্তিগত অ্যাকাউন্টের সীমাবদ্ধতা লঙ্ঘন করা সম্পূর্ণ নিষিদ্ধ।',
        's4_h2': '৪. দায়বদ্ধতার সীমাবদ্ধতা',
        's4_p': 'সার্ভিসটি একটি ট্রানজিয়েন্ট প্রক্সি হিসেবে কোনো অতিরিক্ত ওয়ারেন্টি ছাড়া প্রদান করা হয়।',
        'faq_title': 'প্রায়শই জিজ্ঞাসিত প্রশ্নাবলী',
        'faqs': [
            ('আমি কি ব্যক্তিগত ব্যবহারের জন্য ভিডিও ডাউনলোড করতে পারি?', 'হ্যাঁ, ব্যক্তিগত শিক্ষা বা আর্কাইভের জন্য পাবলিক ভিডিও সংরক্ষণ করা বৈধ।'),
            ('ডাউনসোশ্যাল কি কোনো সামাজিক মাধ্যমের সাথে যুক্ত?', 'না, এটি সম্পূর্ণ স্বতন্ত্র একটি টুল।')
        ]
    },
    'ru': {
        'h1': 'Условия использования — downsocial HD',
        'date': 'Последнее обновление: 3 октября 2026 г.',
        'intro': 'Используя сервис downsocial.net, вы соглашаетесь с настоящими Условиями использования.',
        's1_h2': '1. Разрешенное личное использование',
        's1_p': 'downsocial предназначен исключительно для личного и некоммерческого офлайн-просмотра публичных видео.',
        's2_h2': '2. Авторские права и товарные знаки',
        's2_p': 'Все товарные знаки принадлежат их законным правообладателям.',
        's3_h2': '3. Запрещенное использование',
        's3_p': 'Запрещено коммерческое распространение и обход ограничений закрытых аккаунтов.',
        's4_h2': '4. Ограничение ответственности',
        's4_p': 'Сервис предоставляется по принципу «как есть» без хранения файлов на серверах.',
        'faq_title': 'Часто Задаваемые Вопросы',
        'faqs': [
            ('Можно ли скачивать видео для личного просмотра?', 'Да, сохранение общедоступных видео для личных целей считается добросовестным использованием.'),
            ('Связан ли downsocial с социальными сетями?', 'Нет, это полностью независимый инструмент.')
        ]
    },
    'id': {
        'h1': 'Syarat & Ketentuan — downsocial Video Downloader',
        'date': 'Terakhir Diperbarui: 3 Oktober 2026',
        'intro': 'Dengan mengakses dan menggunakan downsocial.net, Anda menyetujui Syarat dan Ketentuan ini.',
        's1_h2': '1. Penggunaan Pribadi yang Diizinkan',
        's1_p': 'downsocial ditujukan untuk penggunaan pribadi dan non-komersial guna menonton video publik secara luring.',
        's2_h2': '2. Penafian Hak Cipta & Merek Dagang',
        's2_p': 'Semua merek dagang adalah milik sah dari masing-masing pemegang hak.',
        's3_h2': '3. Penggunaan yang Dilarang',
        's3_p': 'Dilarang keras menyebarluaskan kembali media secara komersial tanpa izin.',
        's4_h2': '4. Batasan Tanggung Jawab',
        's4_p': 'Layanan disediakan sebagaimana adanya sebagai perantara teknis tanpa penyimpanan data.',
        'faq_title': 'Pertanyaan yang Sering Diajukan',
        'faqs': [
            ('Bolehkah saya mengunduh video untuk keperluan pribadi?', 'Ya, menyimpan video publik untuk keperluan belajar atau arsip pribadi diperbolehkan.'),
            ('Apakah downsocial terafiliasi dengan media sosial?', 'Tidak, downsocial adalah utilitas independen.')
        ]
    },
    'zh': {
        'h1': '用户服务协议与使用条款 — downsocial',
        'date': '最近更新日期：2026 年 10 月 3 日',
        'intro': '当您访问并使用 downsocial.net 平台时，即代表您完全理解并同意遵守以下使用条款。',
        's1_h2': '1. 仅限个人合法合理使用原则',
        's1_p': 'downsocial 仅限用于个人非商业性质的离线观看与公开内容合理研学，用户须对所下载内容的合规性承担法律责任。',
        's2_h2': '2. 知识产权与商标权属归属声明',
        's2_p': '本站提及的所有平台商标（包括 YouTube、TikTok、Instagram、Facebook、Snapchat、Threads）均归其法定主体所有。',
        's3_h2': '3. 明确禁止之使用行为',
        's3_p': '严禁将本平台用于商业转售、批量盗版抓取，或企图恶意绕过私密账户的权限壁垒。',
        's4_h2': '4. 免责声明与责任范围限制',
        's4_p': '本服务按“现状”提供，不承担任何附加保证。平台不托管任何音视频源文件，仅提供瞬时流转支持。',
        'faq_title': '常见问题解答 (FAQ)',
        'faqs': [
            ('我可以为了个人离线观看保存受版权保护的公开视频吗？', '可以。在合理使用原则（Fair Use）下，保存公开视频供个人学术研究或非商业离线备忘是合法的。'),
            ('downsocial 是否隶属于任何社交媒体公司？', '否。downsocial 是由技术极客构建的完全独立的第三方开源协议代理工具。')
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

def generate_static_pages_data():
    pages_data = {
        'about': {},
        'features': {},
        'contact': {},
        'privacy': {},
        'terms': {}
    }

    for lang in LANGS:
        # About
        abt = ABOUT[lang]
        html_abt = render_about_html(abt)
        pages_data['about'][lang] = {
            'content': html_abt,
            'pageHtml': html_abt
        }

        # Features
        feat = FEATURES_ALL[lang]
        html_feat = render_features_html(feat)
        pages_data['features'][lang] = {
            'content': html_feat,
            'pageHtml': html_feat
        }

        # Contact
        cnt = CONTACT_ALL[lang]
        html_cnt = render_contact_html(cnt)
        pages_data['contact'][lang] = {
            'content': html_cnt,
            'pageHtml': html_cnt
        }

        # Privacy
        prv = PRIVACY_ALL[lang]
        html_prv = render_privacy_html(prv)
        pages_data['privacy'][lang] = {
            'content': html_prv,
            'pageHtml': html_prv
        }

        # Terms
        trm = TERMS_ALL[lang]
        html_trm = render_terms_html(trm)
        pages_data['terms'][lang] = {
            'content': html_trm,
            'pageHtml': html_trm
        }

    return pages_data

if __name__ == '__main__':
    data = generate_static_pages_data()
    with open('scratch/data_static_pages.py', 'w', encoding='utf-8') as f:
        f.write('# scratch/data_static_pages.py\n')
        f.write('# Complete, unshortened HTML for all 5 static pages across all 12 languages\n\n')
        f.write('STATIC_PAGES = ' + repr(data) + '\n')
    print("scratch/data_static_pages.py generated successfully for all 12 languages!")
