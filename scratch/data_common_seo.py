# scratch/data_common_seo.py
# Comprehensive SEO, Common, Notifications, and Static Pages (About, Privacy, Terms, Features, Contact) for all 12 languages

LANGUAGES = ['en', 'es', 'pt', 'de', 'fr', 'it']

# Common UI elements
COMMON = {
    'it': {'langBtn': 'Lingua', 'extBtn': 'Estensione', 'soonBadge': 'Presto', 'homeBtn': 'Home', 'privateBtn': 'Downloader Privato', 'featuresBtn': 'Funzionalità', 'aboutBtn': 'Chi Siamo', 'contactBtn': 'Contatti', 'privacyBtn': 'Informativa sulla Privacy', 'termsBtn': 'Termini di Servizio', 'moreTools': 'Altri Strumenti', 'downloadBtn': 'Scarica Video', 'readyTitle': 'Pronto per il Download!', 'infoText': 'Scegli la qualità preferita qui sotto.', 'dlVidHigh': 'Video (HD)', 'dlVidNorm': 'Video (Normale)', 'dlAudHigh': 'Audio (HQ MP3)', 'dlAudNorm': 'Audio (Normale MP3)', 'moreDetails': 'Maggiori Dettagli', 'showLess': 'Meno Dettagli', 'readMore': 'Leggi di Più', 'readLess': 'Leggi di Meno', 'footerAboutTitle': 'downsocial.net', 'footerAboutDesc': 'La piattaforma all-in-one di riferimento per scaricare video e audio dai social media. Download HD veloci, sicuri e senza filigrana o registrazione.', 'footerToolsTitle': 'Strumenti di Download', 'footerLegalTitle': 'Azienda e Note Legali', 'footerSupportTitle': 'Supporto', 'footerCopyright': '© 2026 downsocial.net. Tutti i diritti riservati.', 'footerDisclaimer': "Disclaimer: downsocial è un'utilità tecnica indipendente e non è affiliata, approvata o sponsorizzata da Meta, Facebook, Instagram, TikTok, ByteDance, YouTube, Google, Snapchat, Snap Inc. o Threads. Tutti i marchi appartengono ai rispettivi proprietari.", 'emptyLinkAlert': 'Per favore incolla prima un link video valido!', 'processing': 'Elaborazione del flusso in corso...', 'successMsg': '✅ Video pronto per il download!', 'errorServer': "Errore del server di streaming. Verifica l'URL."},

    'en': {
        'langBtn': 'Language', 'extBtn': 'Extension', 'soonBadge': 'Soon',
        'homeBtn': 'Home', 'privateBtn': 'Private Downloader', 'featuresBtn': 'Features',
        'aboutBtn': 'About Us', 'contactBtn': 'Contact', 'privacyBtn': 'Privacy Policy', 'termsBtn': 'Terms of Service',
        'moreTools': 'More Tools', 'downloadBtn': 'Download Video',
        'readyTitle': 'Ready to Download!', 'infoText': 'Choose your preferred quality below.',
        'dlVidHigh': 'Video (HD)', 'dlVidNorm': 'Video (Normal)',
        'dlAudHigh': 'Audio (HQ MP3)', 'dlAudNorm': 'Audio (Normal MP3)',
        'moreDetails': 'More Details', 'showLess': 'Show Less',
        'readMore': 'Read More', 'readLess': 'Read Less',
        'footerAboutTitle': 'downsocial.net',
        'footerAboutDesc': 'The premier all-in-one social media video and audio extraction platform. Free, fast, and secure HD downloads without watermarks or login.',
        'footerToolsTitle': 'Downloader Tools', 'footerLegalTitle': 'Company & Legal', 'footerSupportTitle': 'Support',
        'footerCopyright': '© 2026 downsocial.net. All rights reserved.',
        'footerDisclaimer': 'Disclaimer: downsocial is an independent technical utility and is not affiliated with, endorsed by, or sponsored by Meta, Facebook, Instagram, TikTok, ByteDance, YouTube, Google, Snapchat, Snap Inc., or Threads. All trademarks and brand names are the property of their respective owners.',
        'emptyLinkAlert': 'Please paste a valid video link first!',
        'processing': 'Processing stream...', 'successMsg': '✅ Video ready for download!', 'errorServer': 'Server stream error. Please verify URL.'
    },
    'es': {
        'langBtn': 'Idioma', 'extBtn': 'Extensión', 'soonBadge': 'Pronto',
        'homeBtn': 'Inicio', 'privateBtn': 'Descargador Privado', 'featuresBtn': 'Características',
        'aboutBtn': 'Sobre Nosotros', 'contactBtn': 'Contacto', 'privacyBtn': 'Política de Privacidad', 'termsBtn': 'Términos de Servicio',
        'moreTools': 'Más Herramientas', 'downloadBtn': 'Descargar Video',
        'readyTitle': '¡Listo para Descargar!', 'infoText': 'Elige tu calidad preferida abajo.',
        'dlVidHigh': 'Video (HD)', 'dlVidNorm': 'Video (Normal)',
        'dlAudHigh': 'Audio (HQ MP3)', 'dlAudNorm': 'Audio (Normal MP3)',
        'moreDetails': 'Más Detalles', 'showLess': 'Menos Detalles',
        'readMore': 'Leer Más', 'readLess': 'Leer Menos',
        'footerAboutTitle': 'downsocial.net',
        'footerAboutDesc': 'La plataforma líder todo en uno para descargar videos y audios de redes sociales. Descargas HD rápidas, seguras y sin marcas de agua ni registro.',
        'footerToolsTitle': 'Herramientas de Descarga', 'footerLegalTitle': 'Compañía y Legal', 'footerSupportTitle': 'Soporte',
        'footerCopyright': '© 2026 downsocial.net. Todos los derechos reservados.',
        'footerDisclaimer': 'Descargo de responsabilidad: downsocial es una herramienta técnica independiente y no está afiliada, respaldada ni patrocinada por Meta, Facebook, Instagram, TikTok, ByteDance, YouTube, Google, Snapchat, Snap Inc. o Threads. Todas las marcas pertenecen a sus respectivos dueños.',
        'emptyLinkAlert': '¡Por favor pega un enlace de video válido primero!',
        'processing': 'Procesando enlace...', 'successMsg': '✅ ¡Video listo para descargar!', 'errorServer': 'Error del servidor. Por favor verifica la URL.'
    },
    'fr': {
        'langBtn': 'Langue', 'extBtn': 'Extension', 'soonBadge': 'Bientôt',
        'homeBtn': 'Accueil', 'privateBtn': 'Téléchargeur Privé', 'featuresBtn': 'Fonctionnalités',
        'aboutBtn': 'À Propos', 'contactBtn': 'Contact', 'privacyBtn': 'Politique de Confidentialité', 'termsBtn': 'Conditions d’Utilisation',
        'moreTools': 'Plus d’Outils', 'downloadBtn': 'Télécharger la Vidéo',
        'readyTitle': 'Prêt à Télécharger !', 'infoText': 'Choisissez votre qualité préférée ci-dessous.',
        'dlVidHigh': 'Vidéo (HD)', 'dlVidNorm': 'Vidéo (Normale)',
        'dlAudHigh': 'Audio (HQ MP3)', 'dlAudNorm': 'Audio (Normal MP3)',
        'moreDetails': 'Plus de Détails', 'showLess': 'Moins de Détails',
        'readMore': 'Lire Plus', 'readLess': 'Lire Moins',
        'footerAboutTitle': 'downsocial.net',
        'footerAboutDesc': 'La plateforme tout-en-un de référence pour extraire vidéos et audios des réseaux sociaux. Téléchargements HD gratuits, rapides et sans filigrane ni inscription.',
        'footerToolsTitle': 'Outils de Téléchargement', 'footerLegalTitle': 'Entreprise et Légal', 'footerSupportTitle': 'Support',
        'footerCopyright': '© 2026 downsocial.net. Tous droits réservés.',
        'footerDisclaimer': 'Avertissement : downsocial est un outil technique indépendant non affilié, approuvé ou commandité par Meta, Facebook, Instagram, TikTok, ByteDance, YouTube, Google, Snapchat, Snap Inc. ou Threads. Toutes les marques appartiennent à leurs propriétaires respectifs.',
        'emptyLinkAlert': 'Veuillez d’abord coller un lien vidéo valide !',
        'processing': 'Traitement en cours...', 'successMsg': '✅ Vidéo prête à télécharger !', 'errorServer': 'Erreur serveur. Veuillez vérifier l’URL.'
    },
    'de': {
        'langBtn': 'Sprache', 'extBtn': 'Erweiterung', 'soonBadge': 'Bald',
        'homeBtn': 'Startseite', 'privateBtn': 'Privater Downloader', 'featuresBtn': 'Funktionen',
        'aboutBtn': 'Über Uns', 'contactBtn': 'Kontakt', 'privacyBtn': 'Datenschutzerklärung', 'termsBtn': 'Nutzungsbedingungen',
        'moreTools': 'Weitere Tools', 'downloadBtn': 'Video Herunterladen',
        'readyTitle': 'Bereit zum Herunterladen!', 'infoText': 'Wählen Sie unten Ihre bevorzugte Qualität aus.',
        'dlVidHigh': 'Video (HD)', 'dlVidNorm': 'Video (Normal)',
        'dlAudHigh': 'Audio (HQ MP3)', 'dlAudNorm': 'Audio (Normal MP3)',
        'moreDetails': 'Mehr Details', 'showLess': 'Weniger Details',
        'readMore': 'Mehr Lesen', 'readLess': 'Weniger Lesen',
        'footerAboutTitle': 'downsocial.net',
        'footerAboutDesc': 'Die führende All-in-One-Plattform zum Herunterladen von Videos und Audios aus sozialen Medien. Kostenlose, schnelle und sichere HD-Downloads ohne Wasserzeichen oder Login.',
        'footerToolsTitle': 'Downloader Tools', 'footerLegalTitle': 'Rechtliches & Unternehmen', 'footerSupportTitle': 'Support',
        'footerCopyright': '© 2026 downsocial.net. Alle Rechte vorbehalten.',
        'footerDisclaimer': 'Haftungsausschluss: downsocial ist ein unabhängiges technisches Dienstprogramm und steht in keiner Verbindung zu Meta, Facebook, Instagram, TikTok, ByteDance, YouTube, Google, Snapchat, Snap Inc. oder Threads. Alle Marken sind Eigentum der jeweiligen Inhaber.',
        'emptyLinkAlert': 'Bitte fügen Sie zuerst einen gültigen Videolink ein!',
        'processing': 'Wird verarbeitet...', 'successMsg': '✅ Video bereit zum Download!', 'errorServer': 'Serverfehler. Bitte überprüfen Sie die URL.'
    },
    'hi': {
        'langBtn': 'भाषा', 'extBtn': 'एक्सटेंशन', 'soonBadge': 'जल्द ही',
        'homeBtn': 'होम', 'privateBtn': 'प्राइवेट डाउनलोडर', 'featuresBtn': 'विशेषताएं',
        'aboutBtn': 'हमारे बारे में', 'contactBtn': 'संपर्क करें', 'privacyBtn': 'गोपनीयता नीति', 'termsBtn': 'सेवा की शर्तें',
        'moreTools': 'अन्य टूल्स', 'downloadBtn': 'वीडियो डाउनलोड करें',
        'readyTitle': 'डाउनलोड के लिए तैयार!', 'infoText': 'नीचे अपनी पसंदीदा गुणवत्ता चुनें।',
        'dlVidHigh': 'वीडियो (HD)', 'dlVidNorm': 'वीडियो (सामान्य)',
        'dlAudHigh': 'ऑडियो (HQ MP3)', 'dlAudNorm': 'ऑडियो (सामान्य MP3)',
        'moreDetails': 'अधिक विवरण', 'showLess': 'कम विवरण',
        'readMore': 'और पढ़ें', 'readLess': 'कम पढ़ें',
        'footerAboutTitle': 'downsocial.net',
        'footerAboutDesc': 'सोशल मीडिया से वीडियो और ऑडियो डाउनलोड करने का प्रमुख ऑल-इन-वन प्लेटफॉर्म। बिना वॉटरमार्क और बिना लॉगिन के फ्री, फास्ट और सुरक्षित एचडी डाउनलोड।',
        'footerToolsTitle': 'डाउनलोडर टूल्स', 'footerLegalTitle': 'कंपनी और कानूनी', 'footerSupportTitle': 'सहायता',
        'footerCopyright': '© 2026 downsocial.net. सर्वाधिकार सुरक्षित।',
        'footerDisclaimer': 'अस्वीकरण: downsocial एक स्वतंत्र तकनीकी टूल है और यह Meta, Facebook, Instagram, TikTok, ByteDance, YouTube, Google, Snapchat, Snap Inc. या Threads से संबद्ध या समर्थित नहीं है। सभी ट्रेडमार्क उनके संबंधित स्वामियों की संपत्ति हैं।',
        'emptyLinkAlert': 'कृपया पहले एक वैध वीडियो लिंक पेस्ट करें!',
        'processing': 'प्रोसेसिंग जारी है...', 'successMsg': '✅ वीडियो डाउनलोड के लिए तैयार है!', 'errorServer': 'सर्वर त्रुटि। कृपया लिंक की पुष्टि करें।'
    },
    'ar': {
        'langBtn': 'اللغة', 'extBtn': 'الإضافة', 'soonBadge': 'قريباً',
        'homeBtn': 'الرئيسية', 'privateBtn': 'المحمل الخاص', 'featuresBtn': 'المميزات',
        'aboutBtn': 'من نحن', 'contactBtn': 'اتصل بنا', 'privacyBtn': 'سياسة الخصوصية', 'termsBtn': 'شروط الخدمة',
        'moreTools': 'أدوات إضافية', 'downloadBtn': 'تحميل الفيديو',
        'readyTitle': 'جاهز للتحميل!', 'infoText': 'اختر الجودة المفضلة لديك أدناه.',
        'dlVidHigh': 'فيديو (عالي الدقة)', 'dlVidNorm': 'فيديو (عادي)',
        'dlAudHigh': 'صوت (HQ MP3)', 'dlAudNorm': 'صوت (MP3 عادي)',
        'moreDetails': 'المزيد من التفاصيل', 'showLess': 'تفاصيل أقل',
        'readMore': 'اقرأ المزيد', 'readLess': 'اقرأ أقل',
        'footerAboutTitle': 'downsocial.net',
        'footerAboutDesc': 'المنصة الرائدة الشاملة لاستخراج وتنزيل مقاطع الفيديو والصوتيات من منصات التواصل الاجتماعي. تنزيل عالي الدقة مجاناً وبسرعة وبدون علامات مائية أو تسجيل دخول.',
        'footerToolsTitle': 'أدوات التنزيل', 'footerLegalTitle': 'الشركة والقانونية', 'footerSupportTitle': 'الدعم الفني',
        'footerCopyright': '© 2026 downsocial.net. جميع الحقوق محفوظة.',
        'footerDisclaimer': 'إخلاء المسؤولية: downsocial أداة تقنية مستقلة وليست تابعة أو مدعومة من Meta أو Facebook أو Instagram أو TikTok أو ByteDance أو YouTube أو Google أو Snapchat أو Snap Inc. أو Threads. جميع العلامات التجارية مملوكة لأصحابها.',
        'emptyLinkAlert': 'يرجى لصق رابط فيديو صالح أولاً!',
        'processing': 'جارٍ المعالجة...', 'successMsg': '✅ الفيديو جاهز للتنزيل!', 'errorServer': 'خطأ في الخادم. يرجى التحقق من الرابط.'
    },
    'pt': {
        'langBtn': 'Idioma', 'extBtn': 'Extensão', 'soonBadge': 'Em Breve',
        'homeBtn': 'Início', 'privateBtn': 'Baixador Privado', 'featuresBtn': 'Recursos',
        'aboutBtn': 'Sobre Nós', 'contactBtn': 'Contato', 'privacyBtn': 'Política de Privacidade', 'termsBtn': 'Termos de Serviço',
        'moreTools': 'Mais Ferramentas', 'downloadBtn': 'Baixar Vídeo',
        'readyTitle': 'Pronto para Baixar!', 'infoText': 'Escolha a qualidade desejada abaixo.',
        'dlVidHigh': 'Vídeo (HD)', 'dlVidNorm': 'Vídeo (Normal)',
        'dlAudHigh': 'Áudio (HQ MP3)', 'dlAudNorm': 'Áudio (Normal MP3)',
        'moreDetails': 'Mais Detalhes', 'showLess': 'Menos Detalhes',
        'readMore': 'Ler Mais', 'readLess': 'Ler Menos',
        'footerAboutTitle': 'downsocial.net',
        'footerAboutDesc': 'A principal plataforma multifuncional para baixar vídeos e áudios de redes sociais. Downloads rápidos, seguros e em HD, sem marcas d’água e sem login.',
        'footerToolsTitle': 'Ferramentas de Download', 'footerLegalTitle': 'Empresa e Legal', 'footerSupportTitle': 'Suporte',
        'footerCopyright': '© 2026 downsocial.net. Todos os direitos reservados.',
        'footerDisclaimer': 'Aviso Legal: downsocial é uma ferramenta técnica independente e não possui vínculo, endosso ou patrocínio de Meta, Facebook, Instagram, TikTok, ByteDance, YouTube, Google, Snapchat, Snap Inc. ou Threads. Todas as marcas registradas pertencem aos seus respectivos proprietários.',
        'emptyLinkAlert': 'Por favor, cole um link de vídeo válido primeiro!',
        'processing': 'Processando stream...', 'successMsg': '✅ Vídeo pronto para download!', 'errorServer': 'Erro no servidor. Por favor, verifique a URL.'
    },
    'bn': {
        'langBtn': 'ভাষা', 'extBtn': 'এক্সটেনশন', 'soonBadge': 'শীঘ্রই',
        'homeBtn': 'হোম', 'privateBtn': 'প্রাইভেট ডাউনলোডার', 'featuresBtn': 'বৈশিষ্ট্য',
        'aboutBtn': 'আমাদের সম্পর্কে', 'contactBtn': 'যোগাযোগ', 'privacyBtn': 'গোপনীয়তা নীতি', 'termsBtn': 'ব্যবহারের শর্তাবলী',
        'moreTools': 'অন্যান্য টুলস', 'downloadBtn': 'ভিডিও ডাউনলোড করুন',
        'readyTitle': 'ডাউনলোডের জন্য প্রস্তুত!', 'infoText': 'নিচে আপনার পছন্দের কোয়ালিটি নির্বাচন করুন।',
        'dlVidHigh': 'ভিডিও (HD)', 'dlVidNorm': 'ভিডিও (সাধারণ)',
        'dlAudHigh': 'অডিও (HQ MP3)', 'dlAudNorm': 'অডিও (সাধারণ MP3)',
        'moreDetails': 'আরও বিস্তারিত', 'showLess': 'সংক্ষেপে',
        'readMore': 'আরও পড়ুন', 'readLess': 'কম পড়ুন',
        'footerAboutTitle': 'downsocial.net',
        'footerAboutDesc': 'সোশ্যাল মিডিয়া থেকে ভিডিও এবং অডিও এক্সট্র্যাক্ট করার বিশ্বস্ত অল-ইন-ওয়ান প্ল্যাটফর্ম। ওয়াটারমার্ক এবং লগইন ছাড়াই সম্পূর্ণ বিনামূল্যে দ্রুত ও নিরাপদ HD ডাউনলোড।',
        'footerToolsTitle': 'ডাউনলোডার টুলস', 'footerLegalTitle': 'কোম্পানি ও আইনি', 'footerSupportTitle': 'সাপোর্ট',
        'footerCopyright': '© ২০২৬ downsocial.net। সর্বস্বত্ব সংরক্ষিত।',
        'footerDisclaimer': 'দাবিত্যাগ: downsocial একটি স্বতন্ত্র প্রযুক্তিগত পরিষেবা এবং এটি Meta, Facebook, Instagram, TikTok, ByteDance, YouTube, Google, Snapchat, Snap Inc. বা Threads দ্বারা অনুমোদিত বা স্পনসরকৃত নয়। সমস্ত ট্রেডমার্ক তাদের নিজ নিজ মালিকের সম্পত্তি।',
        'emptyLinkAlert': 'অনুগ্রহ করে প্রথমে একটি সঠিক ভিডিও লিংক পেস্ট করুন!',
        'processing': 'প্রক্রিয়াধীন...', 'successMsg': '✅ ভিডিও ডাউনলোডের জন্য প্রস্তুত!', 'errorServer': 'সার্ভার সমস্যা। দয়া করে ইউআরএল যাচাই করুন।'
    },
    'ru': {
        'langBtn': 'Язык', 'extBtn': 'Расширение', 'soonBadge': 'Скоро',
        'homeBtn': 'Главная', 'privateBtn': 'Приватный загрузчик', 'featuresBtn': 'Возможности',
        'aboutBtn': 'О нас', 'contactBtn': 'Контакты', 'privacyBtn': 'Политика конфиденциальности', 'termsBtn': 'Условия использования',
        'moreTools': 'Другие инструменты', 'downloadBtn': 'Скачать видео',
        'readyTitle': 'Готово к скачиванию!', 'infoText': 'Выберите желаемое качество ниже.',
        'dlVidHigh': 'Видео (HD)', 'dlVidNorm': 'Видео (Обычное)',
        'dlAudHigh': 'Аудио (HQ MP3)', 'dlAudNorm': 'Аудио (Обычное MP3)',
        'moreDetails': 'Подробнее', 'showLess': 'Свернуть',
        'readMore': 'Читать дальше', 'readLess': 'Свернуть',
        'footerAboutTitle': 'downsocial.net',
        'footerAboutDesc': 'Ведущая универсальная платформа для скачивания видео и аудио из социальных сетей. Быстрая, безопасная и бесплатная загрузка в HD качестве без водяных знаков и авторизации.',
        'footerToolsTitle': 'Инструменты загрузки', 'footerLegalTitle': 'Компания и право', 'footerSupportTitle': 'Поддержка',
        'footerCopyright': '© 2026 downsocial.net. Все права защищены.',
        'footerDisclaimer': 'Отказ от ответственности: downsocial — независимый технический инструмент, не связанный и не одобренный Meta, Facebook, Instagram, TikTok, ByteDance, YouTube, Google, Snapchat, Snap Inc. или Threads. Все товарные знаки принадлежат их законным владельцам.',
        'emptyLinkAlert': 'Пожалуйста, сначала вставьте действительную ссылку на видео!',
        'processing': 'Обработка потока...', 'successMsg': '✅ Видео готово к скачиванию!', 'errorServer': 'Ошибка сервера. Пожалуйста, проверьте URL.'
    },
    'id': {
        'langBtn': 'Bahasa', 'extBtn': 'Ekstensi', 'soonBadge': 'Segera',
        'homeBtn': 'Beranda', 'privateBtn': 'Pengunduh Privat', 'featuresBtn': 'Fitur',
        'aboutBtn': 'Tentang Kami', 'contactBtn': 'Kontak', 'privacyBtn': 'Kebijakan Privasi', 'termsBtn': 'Syarat Layanan',
        'moreTools': 'Alat Lainnya', 'downloadBtn': 'Unduh Video',
        'readyTitle': 'Siap untuk Diunduh!', 'infoText': 'Pilih kualitas yang Anda inginkan di bawah.',
        'dlVidHigh': 'Video (HD)', 'dlVidNorm': 'Video (Normal)',
        'dlAudHigh': 'Audio (HQ MP3)', 'dlAudNorm': 'Audio (Normal MP3)',
        'moreDetails': 'Detail Lengkap', 'showLess': 'Tutup Detail',
        'readMore': 'Baca Selengkapnya', 'readLess': 'Tutup',
        'footerAboutTitle': 'downsocial.net',
        'footerAboutDesc': 'Platform serba guna nomor satu untuk mengunduh video dan audio dari media sosial. Unduhan HD cepat, aman, tanpa watermark, dan tanpa perlu login.',
        'footerToolsTitle': 'Alat Pengunduh', 'footerLegalTitle': 'Perusahaan & Hukum', 'footerSupportTitle': 'Bantuan',
        'footerCopyright': '© 2026 downsocial.net. Hak cipta dilindungi undang-undang.',
        'footerDisclaimer': 'Penafian: downsocial adalah utilitas teknis independen dan tidak berafiliasi, didukung, atau disponsori oleh Meta, Facebook, Instagram, TikTok, ByteDance, YouTube, Google, Snapchat, Snap Inc., atau Threads. Semua merek dagang adalah milik masing-masing pemiliknya.',
        'emptyLinkAlert': 'Harap tempel tautan video yang valid terlebih dahulu!',
        'processing': 'Memproses data...', 'successMsg': '✅ Video siap diunduh!', 'errorServer': 'Kesalahan server. Silakan periksa URL tautan.'
    },
    'zh': {
        'langBtn': '语言', 'extBtn': '浏览器插件', 'soonBadge': '即将上线',
        'homeBtn': '首页', 'privateBtn': '私密下载器', 'featuresBtn': '功能特点',
        'aboutBtn': '关于我们', 'contactBtn': '联系支持', 'privacyBtn': '隐私政策', 'termsBtn': '服务条款',
        'moreTools': '更多下载工具', 'downloadBtn': '下载视频',
        'readyTitle': '视频已就绪！', 'infoText': '请在下方选择您需要的画质规格。',
        'dlVidHigh': '高清视频 (HD)', 'dlVidNorm': '标清视频 (Normal)',
        'dlAudHigh': '高品质音频 (HQ MP3)', 'dlAudNorm': '普通音频 (Normal MP3)',
        'moreDetails': '展开详情', 'showLess': '收起详情',
        'readMore': '查看更多', 'readLess': '收起内容',
        'footerAboutTitle': 'downsocial.net',
        'footerAboutDesc': '领先的全能社交媒体视频与音频提取平台。超高速、高安全性、无水印、无需登录即可免费下载超高清多媒体内容。',
        'footerToolsTitle': '下载工具分类', 'footerLegalTitle': '公司与法律合规', 'footerSupportTitle': '帮助与支持',
        'footerCopyright': '© 2026 downsocial.net. 版权所有。',
        'footerDisclaimer': '免责声明：downsocial 为独立第三方在线工具，与 Meta、Facebook、Instagram、TikTok、字节跳动、YouTube、Google、Snapchat、Snap Inc. 或 Threads 无任何附属、赞助或背书关系。所有商标均为其各自持有者的合法财产。',
        'emptyLinkAlert': '请先粘贴有效的视频链接！',
        'processing': '正在极速解析媒体流...', 'successMsg': '✅ 视频解析成功，随时可下载！', 'errorServer': '服务器解析错误，请检查链接有效性。'
    },
    'ur': {
        'langBtn': 'زبان', 'extBtn': 'ایکسٹینشن', 'soonBadge': 'عنقریب',
        'homeBtn': 'ہوم', 'privateBtn': 'پرائیویٹ ڈاؤنلوڈر', 'featuresBtn': 'خصوصیات',
        'aboutBtn': 'ہمارے بارے میں', 'contactBtn': 'رابطہ کریں', 'privacyBtn': 'رازداری کی پالیسی', 'termsBtn': 'شرائط و ضوابط',
        'moreTools': 'مزید ٹولز', 'downloadBtn': 'ویڈیو ڈاؤن لوڈ کریں',
        'readyTitle': 'ڈاؤن لوڈ کے لیے تیار!', 'infoText': 'نیچے اپنی پسندیدہ کوالٹی کا انتخاب کریں۔',
        'dlVidHigh': 'ویڈیو (HD)', 'dlVidNorm': 'ویڈیو (عام)',
        'dlAudHigh': 'آڈیو (HQ MP3)', 'dlAudNorm': 'آڈیو (عام MP3)',
        'moreDetails': 'مزید تفصیلات', 'showLess': 'کم تفصیلات',
        'readMore': 'مزید پڑھیں', 'readLess': 'کم پڑھیں',
        'footerAboutTitle': 'downsocial.net',
        'footerAboutDesc': 'سوشل میڈیا سے ویڈیوز اور آڈیو ڈاؤن لوڈ کرنے کا بہترین آل ان ون پلیٹ فارم۔ بغیر واٹر مارک اور بغیر لاگ ان کے مفت، تیز ترین اور محفوظ ایچ ڈی ڈاؤن لوڈنگ۔',
        'footerToolsTitle': 'ڈاؤنلوڈر ٹولز', 'footerLegalTitle': 'کمپنی اور قانونی', 'footerSupportTitle': 'مدد و سپورٹ',
        'footerCopyright': '© 2026 downsocial.net. جملہ حقوق محفوظ ہیں۔',
        'footerDisclaimer': 'دستبرداری: downsocial ایک خود مختار تکنیکی ٹول ہے اور اس کا Meta، Facebook، Instagram، TikTok، ByteDance، YouTube، Google، Snapchat، Snap Inc. یا Threads سے کوئی براہ راست الحاق یا توثیق نہیں ہے۔ تمام ٹریڈ مارکس ان کے متعلقہ مالکان کی ملکیت ہیں۔',
        'emptyLinkAlert': 'براہ کرم پہلے درست ویڈیو لنک پیسٹ کریں!',
        'processing': 'پروسیسنگ جاری ہے...', 'successMsg': '✅ ویڈیو ڈاؤن لوڈ کے لیے تیار ہے!', 'errorServer': 'سرور میں خرابی ہے۔ براہ کرم لنک چیک کریں۔'
    }
}

# Notifications dictionary for all 12 languages
NOTIFICATIONS = {
    'it': {'title': 'Tutte le 6 Piattaforme Online! 🚀', 'time': 'Proprio ora', 'content': 'Scarica video HD e audio MP3 da YouTube, TikTok, Instagram, Facebook, Snapchat e Threads senza watermark!'},

    'en': {
        'header': 'Notifications', 'newBadge': '1 New', 'time': 'Just now',
        'extTitle': 'Browser Extension & Direct Downloader 🚀',
        'content1': 'Download videos directly from Facebook, Instagram, TikTok, YouTube, Snapchat, and Threads with 1 click.',
        'content2': 'Dedicated high-speed cloud CDN ensures original 1080p, 4K, and 320kbps MP3 audio downloads without watermarks.',
        'content3': 'Chrome, Edge, and Firefox extensions launching soon with automatic link detection!'
    },
    'es': {
        'header': 'Notificaciones', 'newBadge': '1 Nuevo', 'time': 'Ahora mismo',
        'extTitle': 'Extensión de Navegador y Descarga Directa 🚀',
        'content1': 'Descarga videos directamente de Facebook, Instagram, TikTok, YouTube, Snapchat y Threads con 1 solo clic.',
        'content2': 'CDN en la nube de alta velocidad garantiza descargas en 1080p original, 4K y audio MP3 a 320kbps sin marcas de agua.',
        'content3': '¡Extensiones para Chrome, Edge y Firefox disponibles muy pronto con detección automática de enlaces!'
    },
    'fr': {
        'header': 'Notifications', 'newBadge': '1 Nouveau', 'time': 'À l’instant',
        'extTitle': 'Extension de Navigateur & Téléchargement Direct 🚀',
        'content1': 'Téléchargez des vidéos directement depuis Facebook, Instagram, TikTok, YouTube, Snapchat et Threads en 1 clic.',
        'content2': 'Un CDN haute vitesse garantit des téléchargements en 1080p original, 4K et audio MP3 à 320 kbps sans aucun filigrane.',
        'content3': 'Les extensions pour Chrome, Edge et Firefox arrivent très bientôt avec détection automatique des liens !'
    },
    'de': {
        'header': 'Benachrichtigungen', 'newBadge': '1 Neu', 'time': 'Gerade eben',
        'extTitle': 'Browser-Erweiterung & Direktdownload 🚀',
        'content1': 'Laden Sie Videos direkt von Facebook, Instagram, TikTok, YouTube, Snapchat und Threads mit nur 1 Klick herunter.',
        'content2': 'Ein High-Speed-Cloud-CDN garantiert Downloads in originalem 1080p, 4K und 320kbps MP3-Audio ohne Wasserzeichen.',
        'content3': 'Erweiterungen für Chrome, Edge und Firefox erscheinen in Kürze mit automatischer Linkerkennung!'
    },
    'hi': {
        'header': 'सूचनाएं', 'newBadge': '1 नया', 'time': 'अभी-अभी',
        'extTitle': 'ब्राउज़र एक्सटेंशन और डायरेक्ट डाउनलोडर 🚀',
        'content1': 'फेसबुक, इंस्टाग्राम, टिकटॉक, यूट्यूब, स्नैपचैट और थ्रेड्स से सीधे 1-क्लिक में वीडियो डाउनलोड करें।',
        'content2': 'हाई-स्पीड क्लाउड सीडीएन बिना किसी वॉटरमार्क के मूल 1080p, 4K और 320kbps MP3 ऑडियो डाउनलोड सुनिश्चित करता है।',
        'content3': 'स्वचालित लिंक पहचान के साथ क्रोम, एज और फ़ायरफ़ॉक्स एक्सटेंशन जल्द ही आ रहे हैं!'
    },
    'ar': {
        'header': 'الإشعارات', 'newBadge': '1 جديد', 'time': 'الآن',
        'extTitle': 'إضافة المتصفح والتحميل المباشر 🚀',
        'content1': 'قم بتحميل الفيديوهات مباشرة من فيسبوك وإنستغرام وتيك توك ويوتيوب وسناب شات وثريدز بنقرة واحدة.',
        'content2': 'شبكة CDN سحابية فائقة السرعة تضمن تنزيلات بدقة 1080p الأصلية و4K وصوت MP3 عالي النقاء 320kbps بدون علامات مائية.',
        'content3': 'إضافات Chrome وEdge وFirefox ستتوفر قريباً مع التعرف التلقائي على الروابط!'
    },
    'pt': {
        'header': 'Notificações', 'newBadge': '1 Novo', 'time': 'Agora',
        'extTitle': 'Extensão de Navegador e Baixador Direto 🚀',
        'content1': 'Baixe vídeos diretamente do Facebook, Instagram, TikTok, YouTube, Snapchat e Threads com apenas 1 clique.',
        'content2': 'CDN em nuvem de alta velocidade garante downloads em 1080p original, 4K e áudio MP3 a 320kbps sem marcas d’água.',
        'content3': 'Extensões para Chrome, Edge e Firefox em breve com detecção inteligente de links!'
    },
    'bn': {
        'header': 'বিজ্ঞপ্তি', 'newBadge': '১টি নতুন', 'time': 'এইমাত্র',
        'extTitle': 'ব্রাউজার এক্সটেনশন ও ডিরেক্ট ডাউনলোডার 🚀',
        'content1': 'ফেসবুক, ইনস্টাগ্রাম, টিকটক, ইউটিউব, স্ন্যাপচ্যাট এবং থ্রেডস থেকে সরাসরি ১-ক্লিকে ভিডিও ডাউনলোড করুন।',
        'content2': 'উচ্চগতির ক্লাউড সিডিএন কোনো ওয়াটারমার্ক ছাড়াই আসল ১০৮০p, ৪K এবং ৩২০kbps MP3 অডিও ডাউনলোড নিশ্চিত করে।',
        'content3': 'স্বয়ংক্রিয় লিংক শনাক্তকরণ সুবিধাসহ ক্রোম, এজ ও ফায়ারফক্স এক্সটেনশন শীঘ্রই প্রকাশিত হবে!'
    },
    'ru': {
        'header': 'Уведомления', 'newBadge': '1 Новое', 'time': 'Только что',
        'extTitle': 'Расширение для браузера и прямой загрузчик 🚀',
        'content1': 'Скачивайте видео напрямую с Facebook, Instagram, TikTok, YouTube, Snapchat и Threads в 1 клик.',
        'content2': 'Высокоскоростной CDN гарантирует загрузку в оригинальном 1080p, 4K и MP3 аудио 320 кбит/с без водяных знаков.',
        'content3': 'Расширения для Chrome, Edge и Firefox с автоопределением ссылок станут доступны совсем скоро!'
    },
    'id': {
        'header': 'Notifikasi', 'newBadge': '1 Baru', 'time': 'Baru saja',
        'extTitle': 'Ekstensi Browser & Pengunduh Langsung 🚀',
        'content1': 'Unduh video langsung dari Facebook, Instagram, TikTok, YouTube, Snapchat, dan Threads dengan 1 klik mudah.',
        'content2': 'CDN cloud berkecepatan tinggi memastikan unduhan dalam resolusi asli 1080p, 4K, dan audio MP3 320kbps tanpa watermark.',
        'content3': 'Ekstensi untuk Chrome, Edge, dan Firefox akan segera hadir dengan deteksi tautan otomatis!'
    },
    'zh': {
        'header': '系统通知', 'newBadge': '1 条未读', 'time': '刚刚',
        'extTitle': '浏览器插件与极速直链下载功能 🚀',
        'content1': '无需手动复制粘贴，在 Facebook、Instagram、TikTok、YouTube、Snapchat 和 Threads 页面上一键极速下载。',
        'content2': '依托全球顶尖高速云端 CDN，确保原始 1080p、4K 视频及 320kbps 高清 MP3 音频无损且无水印直链提取。',
        'content3': '适配 Chrome、Edge 与 Firefox 浏览器的智能检测插件即将正式发布，敬请期待！'
    },
    'ur': {
        'header': 'اطلاعات', 'newBadge': '1 نیا', 'time': 'ابھی',
        'extTitle': 'براؤزر ایکسٹینشن اور ڈائریکٹ ڈاؤنلوڈر 🚀',
        'content1': 'فیس بک، انسٹاگرام، ٹک ٹاک، یوٹیوب، سنیپ چیٹ اور تھریڈز سے براہ راست صرف 1 کلک میں ویڈیوز ڈاؤن لوڈ کریں۔',
        'content2': 'تیز ترین کلاؤڈ CDN بغیر کسی واٹر مارک کے اصل 1080p، 4K اور 320kbps MP3 آڈیو ڈاؤن لوڈز کو یقینی بناتا ہے۔',
        'content3': 'خودکار لنک شناختی فیچر کے ساتھ کروم، ایج اور فائر فاکس کی ایکسٹینشنز بہت جلد دستیاب ہوں گی!'
    }
}
