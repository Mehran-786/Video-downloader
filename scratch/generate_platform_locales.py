import os
import json

BASE_DIR = r'c:\my folder\Pictures\Desktop\downsocial\frontend'

PLATFORMS = {
    'facebook-downloader': {
        'name': 'Facebook',
        'key': 'facebook',
        'color': '#1877F2',
        'title': 'Download Facebook Videos in HD',
        'subtitle': 'Free, fast, and without watermarks. Download FB Reels, Stories & Watch videos in 1080p, 2K & 4K.',
        'placeholder': 'Paste Facebook video, Reel, or Story URL here...',
        'cta': 'Download Facebook Video',
        'about_title': 'About Our Facebook Video Downloader',
        'about_desc': 'The premier tool for downloading Facebook Reels, Watch videos, and Stories with zero watermarks and original audio quality.',
        'contact_title': 'Contact Facebook Downloader Support',
        'contact_sub': 'Get support for Facebook download issues, report broken links, or request new FB features.',
        'privacy_title': 'Privacy Policy — Facebook Downloader',
        'privacy_desc': 'How we handle Facebook video processing: strictly transient in memory, zero credential logging, direct CDN streaming.',
        'terms_title': 'Terms of Service — Facebook Downloader',
        'terms_desc': 'Usage guidelines, intellectual property disclaimers, and fair use policies for Facebook video downloads.',
        'features_title': 'Facebook Downloader Capabilities & Features',
        'features_desc': 'Comprehensive feature set: 1080p/4K MP4, 320kbps MP3, Stories saver, Reels archiver, and batch processing.',
        'specific': {
            'item1': 'Download Facebook Stories before 24-hour expiration',
            'item2': 'Save Facebook Reels in 1080p Full HD with stereo audio',
            'item3': 'Convert Facebook video streams to HQ 192kbps/320kbps MP3',
            'item4': 'Private and public group video download support',
            'item5': 'Zero watermark, zero compression, original aspect ratio'
        },
        'faqs': [
            {"q": "Is downloading Facebook videos legal?", "a": "Yes, downloading public videos for personal offline archival and fair use is legal. Please respect copyright laws and creator rights."},
            {"q": "Can I download Facebook Reels and Stories?", "a": "Yes! Our downloader supports Facebook Reels, 24-hour Stories, Watch videos, and standard feed videos."},
            {"q": "Does downsocial add a watermark to Facebook downloads?", "a": "No. All downloaded Facebook videos are 100% clean with zero added watermarks or logos."},
            {"q": "Will Facebook know that I downloaded a video?", "a": "No. downsocial connects anonymously to the public media stream. No user tracking or account login is required."},
            {"q": "How do I download Facebook audio as MP3?", "a": "Paste the Facebook video link, click Download, and select either HQ MP3 or Normal MP3 from the download buttons."}
        ]
    },
    'instagram-downloader': {
        'name': 'Instagram',
        'key': 'instagram',
        'color': '#E4405F',
        'title': 'Download Instagram Reels & Stories HD',
        'subtitle': 'Save Instagram Reels, Stories, Photos & Carousel posts in original high resolution without watermark.',
        'placeholder': 'Paste Instagram Reel, Story, or Post URL here...',
        'cta': 'Download Instagram Media',
        'about_title': 'About Our Instagram Downloader',
        'about_desc': 'Designed specifically for Instagram creators and viewers to backup Reels, archive Stories, and save high-resolution carousel albums.',
        'contact_title': 'Contact Instagram Downloader Support',
        'contact_sub': 'Direct support for Instagram extraction issues, Carousel post bugs, or Story download inquiries.',
        'privacy_title': 'Privacy Policy — Instagram Downloader',
        'privacy_desc': 'Our zero-tracking policy for Instagram downloads. We never access your Instagram credentials or personal profile.',
        'terms_title': 'Terms of Service — Instagram Downloader',
        'terms_desc': 'Legal terms, personal fair use compliance, and trademark disclaimers regarding Instagram and Meta Platforms.',
        'features_title': 'Instagram Downloader Features & Specs',
        'features_desc': 'Discover all Instagram capabilities: 1080p Reels, Story archiver, carousel batch unpacker, and high-fidelity MP3 extraction.',
        'specific': {
            'item1': 'Save Instagram Reels with original high-bitrate audio',
            'item2': 'Archive ephemeral 24-hour Stories and Highlights permanently',
            'item3': 'Download multi-slide Carousel posts (photos + videos)',
            'item4': 'Extract original soundtrack audio to 192kbps MP3',
            'item5': 'Works with both mobile Instagram app share links and browser URLs'
        },
        'faqs': [
            {"q": "Can I download Instagram Reels in 1080p Full HD?", "a": "Yes! Our tool fetches the highest available bitrate stream directly from Instagram CDN servers."},
            {"q": "How can I download Instagram Stories before they expire?", "a": "Simply copy the Story link or username story URL and paste it into our tool to save it permanently."},
            {"q": "Does this tool support Instagram Carousel posts?", "a": "Yes, our backend extracts media from multi-photo and multi-video carousel posts seamlessly."},
            {"q": "Do I need to log in to my Instagram account?", "a": "Never! downsocial requires no login, no password, and no Instagram account connection."},
            {"q": "Can I extract audio from Instagram Reels as MP3?", "a": "Yes! Click the Audio (HQ MP3) button after entering your Reel link to get pure audio."}
        ]
    },
    'tiktok-downloader': {
        'name': 'TikTok',
        'key': 'tiktok',
        'color': '#00f2fe',
        'title': 'Download TikTok Videos Without Watermark',
        'subtitle': 'Automatic watermark removal, trending MP3 music extraction & crystal-clear 1080p 60FPS video downloads.',
        'placeholder': 'Paste TikTok video link here (vt.tiktok.com or tiktok.com/@user)...',
        'cta': 'Download TikTok Video',
        'about_title': 'About Our TikTok Downloader',
        'about_desc': 'The ultimate no-watermark TikTok downloader. Strips intrusive bouncing logos and saves original-quality videos and sounds.',
        'contact_title': 'Contact TikTok Downloader Support',
        'contact_sub': 'Need help with a TikTok watermark issue, trending sound extraction, or slideshow post? Contact our team.',
        'privacy_title': 'Privacy Policy — TikTok Downloader',
        'privacy_desc': 'We do not collect TikTok usernames, view histories, or device identifiers. All stream processing is completely ephemeral.',
        'terms_title': 'Terms of Service — TikTok Downloader',
        'terms_desc': 'Terms of service regarding ByteDance/TikTok content fair use, creator copyright protection, and non-commercial archival.',
        'features_title': 'TikTok Downloader Capabilities',
        'features_desc': 'Zero watermark engine, original audio extractor, photo slideshow unpacker, and high frame rate 60FPS support.',
        'specific': {
            'item1': '100% Automatic Watermark Removal (no logo overlay)',
            'item2': 'Extract original viral TikTok sounds and background music to MP3',
            'item3': 'Download full photo slideshows and carousel posts',
            'item4': 'Ultra-fast downloads on iOS Safari, Android Chrome & Desktop',
            'item5': 'Supports short links (vt.tiktok.com) and full desktop web links'
        },
        'faqs': [
            {"q": "How does TikTok watermark removal work?", "a": "Our backend accesses the clean source video stream before TikTok renders the bouncing watermark overlay."},
            {"q": "Can I download TikTok sounds as MP3 audio?", "a": "Yes! Click the Audio (HQ MP3) button to download the original sound track directly."},
            {"q": "Is the TikTok downloader free and unlimited?", "a": "Yes, downsocial is 100% free with unlimited downloads and no registration."},
            {"q": "How do I save TikTok videos on iPhone/iPad?", "a": "Open Safari, paste the link, click Download, and save the file directly to your Files or Photos app."},
            {"q": "Does this work with TikTok slideshows?", "a": "Yes! Both video posts and photo carousel slideshows are supported."}
        ]
    },
    'youtube-downloader': {
        'name': 'YouTube',
        'key': 'youtube',
        'color': '#FF0000',
        'title': 'Download YouTube Videos & Shorts in 4K',
        'subtitle': 'Ultra-fast YouTube video downloader & MP3 converter. Download YouTube Shorts, 1080p, 2K, 4K & 8K MP4 free.',
        'placeholder': 'Paste YouTube video or Shorts link here (youtube.com or youtu.be)...',
        'cta': 'Download YouTube Video',
        'about_title': 'About Our YouTube Video Downloader',
        'about_desc': 'Engineered for high performance, supporting pristine 4K video resolution, fast stream muxing, and high-bitrate MP3 audio extraction.',
        'contact_title': 'Contact YouTube Downloader Support',
        'contact_sub': 'Report quality issues, audio desync, or suggest features for our YouTube download service.',
        'privacy_title': 'Privacy Policy — YouTube Downloader',
        'privacy_desc': 'Privacy guarantee: we never record your YouTube watch history, search queries, or IP addresses.',
        'terms_title': 'Terms of Service — YouTube Downloader',
        'terms_desc': 'Copyright guidelines, DMCA notices, and fair use terms for downloading YouTube videos for educational and personal use.',
        'features_title': 'YouTube Downloader Technical Specifications',
        'features_desc': 'Support for 4K/8K Ultra HD, 60FPS playback, YouTube Shorts, 320kbps MP3 audio conversion, and zero popup ads.',
        'specific': {
            'item1': 'Ultra HD Resolutions: 1080p, 2K, 4K, and 8K supported',
            'item2': 'Dedicated 1-Click YouTube Shorts video downloader',
            'item3': 'High fidelity YouTube to MP3 audio converter (up to 320kbps)',
            'item4': 'Advanced stream muxing with zero video-audio desync',
            'item5': 'Completely free with no software installation or browser extensions'
        },
        'faqs': [
            {"q": "Can I download YouTube videos in 4K resolution?", "a": "Yes, our high-performance backend supports 1080p Full HD, 2K QHD, and 4K Ultra HD streams."},
            {"q": "How do I download YouTube Shorts on mobile?", "a": "Tap Share on the YouTube Shorts clip, copy link, paste into downsocial, and tap Download Video."},
            {"q": "How fast is the YouTube to MP3 conversion?", "a": "Our server processes and streams audio in real-time, delivering your MP3 file in just a few seconds."},
            {"q": "Are there daily download limits?", "a": "No! You can download as many YouTube videos and Shorts as you want without restrictions."},
            {"q": "Do I need to install any software or plugins?", "a": "No, downsocial operates 100% online through any modern web browser."}
        ]
    },
    'snapchat-downloader': {
        'name': 'Snapchat',
        'key': 'snapchat',
        'color': '#FFFC00',
        'title': 'Download Snapchat Spotlight & Stories',
        'subtitle': 'Save Snapchat Spotlight vertical videos, public Stories & Memories in full 9:16 HD before they expire.',
        'placeholder': 'Paste Snapchat Spotlight or Story link here (snapchat.com/t/...)...',
        'cta': 'Download Snapchat Video',
        'about_title': 'About Our Snapchat Downloader',
        'about_desc': 'Preserve ephemeral Snapchat moments. Download Spotlight clips and public Stories before the 24-hour expiration clock runs out.',
        'contact_title': 'Contact Snapchat Downloader Support',
        'contact_sub': 'Have questions about Snapchat links or expired Stories? Reach out to our Snapchat support team.',
        'privacy_title': 'Privacy Policy — Snapchat Downloader',
        'privacy_desc': 'Strict adherence to ephemeral privacy. We do not store Snapchat clips, usernames, or media logs.',
        'terms_title': 'Terms of Service — Snapchat Downloader',
        'terms_desc': 'Personal archival guidelines, copyright policies, and terms of service compliance regarding Snap Inc. content.',
        'features_title': 'Snapchat Downloader Features',
        'features_desc': 'Vertical 9:16 Full HD video extraction, Story archiver, Discover publisher clips saver, and clean UI removal.',
        'specific': {
            'item1': 'Save Snapchat Spotlight videos in original 1080p vertical quality',
            'item2': 'Archive public Snapchat Stories permanently before 24h expiration',
            'item3': 'Download Discover clips and publisher spotlights',
            'item4': 'Clean MP4 video output without Snapchat interface clutter',
            'item5': 'Fast mobile downloading on iPhone Safari and Android Chrome'
        },
        'faqs': [
            {"q": "Can I save Snapchat Stories before they expire?", "a": "Yes! Copy the public Story link and paste it into downsocial to download and preserve the video forever."},
            {"q": "Does the downloader work for Snapchat Spotlight?", "a": "Yes! Snapchat Spotlight videos download in crystal-clear full 9:16 vertical HD resolution."},
            {"q": "Does the creator know if I downloaded their Snapchat video?", "a": "No. downsocial accesses the public media CDN directly without sending any notification or screenshot alert."},
            {"q": "Can I download Snapchat videos on my iPhone?", "a": "Yes, open Safari, paste the Snapchat link into downsocial, and save directly to your iPhone Photos."},
            {"q": "Is any login or Snapchat account required?", "a": "No account or credentials are required to use this tool."}
        ]
    },
    'threads-downloader': {
        'name': 'Threads',
        'key': 'threads',
        'color': '#ffffff',
        'title': 'Download Threads Videos & Posts HD',
        'subtitle': 'The first specialized Meta Threads downloader. Save Threads videos, quote posts, carousels & conversations in HD.',
        'placeholder': 'Paste Threads post link here (threads.net/@user/post/...)...',
        'cta': 'Download Threads Media',
        'about_title': 'About Our Threads Downloader',
        'about_desc': 'The premier utility for Meta Threads. Archive video discussions, download quote-thread clips, and save multi-photo albums.',
        'contact_title': 'Contact Threads Downloader Support',
        'contact_sub': 'Report issues with Threads link formats, carousel extraction, or suggest new features for Threads downloads.',
        'privacy_title': 'Privacy Policy — Threads Downloader',
        'privacy_desc': 'We maintain complete anonymity for all Threads downloads. Zero tracking, zero logs, direct stream delivery.',
        'terms_title': 'Terms of Service — Threads Downloader',
        'terms_desc': 'Usage policy for Meta Threads media downloads, fair use disclaimers, and respect for creator intellectual property.',
        'features_title': 'Threads Downloader Capabilities',
        'features_desc': 'High-bitrate Threads video capture, multi-image carousel downloads, audio extraction, and fast responsive interface.',
        'specific': {
            'item1': 'Download high-bitrate Threads videos with clear stereo sound',
            'item2': 'Save full multi-image carousel albums in original resolution',
            'item3': 'Capture quote-thread discussions and reply video clips',
            'item4': 'Archive creator thoughts and viral Threads media offline',
            'item5': 'Compatible with all Meta Threads mobile and web link formats'
        },
        'faqs': [
            {"q": "How do I download a video from Meta Threads?", "a": "Tap the Share icon on the Threads post, select Copy Link, paste it into downsocial, and click Download."},
            {"q": "Can I download multiple images from a Threads post?", "a": "Yes! If a post contains a carousel of images, our tool extracts all high-resolution photos for download."},
            {"q": "Do I need a Threads or Instagram login?", "a": "No. All public Threads posts are processed anonymously without requiring any account login."},
            {"q": "What video quality is supported for Threads?", "a": "We download videos in their original uploaded quality, up to 1080p Full HD."},
            {"q": "Is this tool compatible with mobile and desktop?", "a": "Yes, works smoothly across iOS Safari, Android Chrome, Mac, Windows, and Linux."}
        ]
    },
    'universal-downloader': {
        'name': 'Universal',
        'key': 'universal',
        'color': '#818cf8',
        'title': 'All-in-One Social Media Video Downloader',
        'subtitle': 'One universal tool for Facebook, Instagram, TikTok, YouTube, Snapchat & Threads. Fast, free & HD with no watermarks.',
        'placeholder': 'Paste any social media video link here (FB, Insta, TikTok, YT, Snapchat, Threads)...',
        'cta': 'Download Video',
        'about_title': 'About Our Universal Video Downloader',
        'about_desc': 'downsocial is the ultimate multi-platform media downloader, combining 6 powerful platform tools into a unified, lightning-fast experience.',
        'contact_title': 'Universal Multi-Platform Support Desk',
        'contact_sub': 'Our global support team is available 24/7 for all platform inquiries, bug reports, and partnership requests.',
        'privacy_title': 'Global Privacy Policy — Universal Downloader',
        'privacy_desc': 'Universal zero-knowledge data architecture. No user accounts, no tracking cookies, and no persistent file storage across all platforms.',
        'terms_title': 'Master Terms of Service — Universal Downloader',
        'terms_desc': 'Comprehensive terms of service governing usage, personal fair use, copyright respect, and platform trademark disclaimers.',
        'features_title': 'Universal Downloader Suite & Capabilities',
        'features_desc': 'Smart auto-detection engine, multi-platform quality selector, 4K video muxing, 320kbps MP3 conversion, and 100% clean output.',
        'specific': {
            'item1': 'Smart URL auto-detection identifies platform automatically',
            'item2': 'Comprehensive support for 6+ major social media platforms',
            'item3': 'High-definition MP4 video (up to 4K) & high fidelity MP3 audio',
            'item4': 'Interactive Brand Orbit for 1-click platform switching',
            'item5': 'Optimized for all modern devices, mobile browsers & desktop OS'
        },
        'faqs': [
            {"q": "Which platforms are supported by the Universal Downloader?", "a": "We support Facebook, Instagram, TikTok, YouTube, Snapchat, and Threads, with more platforms continually added."},
            {"q": "Does the tool automatically detect the platform?", "a": "Yes! Just paste any supported social media link and our smart engine automatically parses and extracts the media."},
            {"q": "Are downloads truly free with no hidden charges?", "a": "Yes, downsocial is 100% free with unlimited downloads, zero subscriptions, and no paywalls."},
            {"q": "Can I convert videos to MP3 audio from any platform?", "a": "Yes! Audio extraction is available across Facebook, Instagram, TikTok, YouTube, and Threads."},
            {"q": "How does downsocial protect my privacy?", "a": "We operate a strict zero-log policy. We do not require accounts, track IP addresses, or store downloaded videos on our servers."}
        ]
    }
}

LANGUAGES = {
    'en': {'code': 'en_US', 'rtl': False, 'name': 'English'},
    'es': {'code': 'es_ES', 'rtl': False, 'name': 'Español'},
    'fr': {'code': 'fr_FR', 'rtl': False, 'name': 'Français'},
    'de': {'code': 'de_DE', 'rtl': False, 'name': 'Deutsch'},
    'hi': {'code': 'hi_IN', 'rtl': False, 'name': 'हिन्दी'},
    'ar': {'code': 'ar_AR', 'rtl': True, 'name': 'العربية'},
    'pt': {'code': 'pt_BR', 'rtl': False, 'name': 'Português'},
    'ru': {'code': 'ru_RU', 'rtl': False, 'name': 'Русский'},
    'id': {'code': 'id_ID', 'rtl': False, 'name': 'Bahasa Indonesia'},
    'zh': {'code': 'zh_CN', 'rtl': False, 'name': '中文'},
    'ur': {'code': 'ur_PK', 'rtl': False, 'name': 'اردو'}
}

# Translations mappings for common elements
COMMON_TRANS = {
    'es': {
        'nav_home': 'Inicio', 'nav_about': 'Acerca de', 'nav_features': 'Características',
        'nav_contact': 'Contacto', 'nav_privacy': 'Privacidad', 'nav_terms': 'Términos', 'nav_faq': 'Preguntas Frecuentes',
        'cta_download': 'Descargar Video', 'no_watermark': 'Sin Marca de Agua',
        'no_watermark_desc': 'Descarga videos con calidad cristalina sin sellos',
        'fast_download': 'Descarga Rápida', 'fast_download_desc': 'Procesamiento instantáneo sin esperas',
        'multi_format': 'Múltiples Formatos', 'multi_format_desc': 'Compatible con MP4, MP3 y más formatos',
        'why_choose': '¿Por qué elegirnos?', 'security': '100% seguro y encriptado',
        'privacy_safe': 'Tus datos nunca se almacenan', 'speed': 'Descargas a la velocidad del rayo',
        'sla': 'Respondemos en 24 horas', 'issue_type': 'Tipo de problema', 'copyright': '© 2026 Todos los derechos reservados'
    },
    'fr': {
        'nav_home': 'Accueil', 'nav_about': 'À propos', 'nav_features': 'Fonctionnalités',
        'nav_contact': 'Contact', 'nav_privacy': 'Confidentialité', 'nav_terms': 'Conditions', 'nav_faq': 'FAQ',
        'cta_download': 'Télécharger la vidéo', 'no_watermark': 'Sans filigrane',
        'no_watermark_desc': 'Téléchargez des vidéos d’une netteté parfaite sans logo',
        'fast_download': 'Téléchargement rapide', 'fast_download_desc': 'Traitement instantané sans attente',
        'multi_format': 'Formats multiples', 'multi_format_desc': 'Prend en charge MP4, MP3 et plus',
        'why_choose': 'Pourquoi nous choisir ?', 'security': '100% sécurisé et crypté',
        'privacy_safe': 'Vos données ne sont jamais stockées', 'speed': 'Vitesse ultra rapide',
        'sla': 'Nous répondons en moins de 24h', 'issue_type': 'Type de problème', 'copyright': '© 2026 Tous droits réservés'
    },
    'de': {
        'nav_home': 'Startseite', 'nav_about': 'Über uns', 'nav_features': 'Funktionen',
        'nav_contact': 'Kontakt', 'nav_privacy': 'Datenschutz', 'nav_terms': 'Bedingungen', 'nav_faq': 'FAQ',
        'cta_download': 'Video herunterladen', 'no_watermark': 'Ohne Wasserzeichen',
        'no_watermark_desc': 'Kristallklare Videos ohne störendes Wasserzeichen',
        'fast_download': 'Blitzschnell', 'fast_download_desc': 'Sofortige Verarbeitung ohne Wartezeit',
        'multi_format': 'Mehrere Formate', 'multi_format_desc': 'Unterstützt MP4, MP3 und mehr',
        'why_choose': 'Warum uns wählen?', 'security': '100% sicher und verschlüsselt',
        'privacy_safe': 'Ihre Daten werden niemals gespeichert', 'speed': 'Maximale Geschwindigkeit',
        'sla': 'Antwort innerhalb von 24 Stunden', 'issue_type': 'Art des Anliegens', 'copyright': '© 2026 Alle Rechte vorbehalten'
    },
    'hi': {
        'nav_home': 'होम', 'nav_about': 'हमारे बारे में', 'nav_features': 'विशेषताएं',
        'nav_contact': 'संपर्क करें', 'nav_privacy': 'गोपनीयता नीति', 'nav_terms': 'नियम एवं शर्तें', 'nav_faq': 'सामान्य प्रश्न',
        'cta_download': 'वीडियो डाउनलोड करें', 'no_watermark': 'बिना वॉटरमार्क',
        'no_watermark_desc': 'क्रिस्टल क्लियर एचडी गुणवत्ता में वीडियो डाउनलोड करें',
        'fast_download': 'सुपर फास्ट डाउनलोड', 'fast_download_desc': 'बिना किसी रुकावट के तुरंत डाउनलोड',
        'multi_format': 'कई फॉर्मेट उपलब्ध', 'multi_format_desc': 'MP4, MP3 और अन्य फॉर्मेट का समर्थन',
        'why_choose': 'हमें क्यों चुनें?', 'security': '100% सुरक्षित और एन्क्रिप्टेड',
        'privacy_safe': 'आपका डेटा कभी स्टोर नहीं होता', 'speed': 'बिजली की गति से डाउनलोड',
        'sla': '24 घंटे के भीतर जवाब दिया जाएगा', 'issue_type': 'समस्या का प्रकार', 'copyright': '© 2026 सर्वाधिकार सुरक्षित'
    },
    'ar': {
        'nav_home': 'الرئيسية', 'nav_about': 'من نحن', 'nav_features': 'المميزات',
        'nav_contact': 'اتصل بنا', 'nav_privacy': 'سياسة الخصوصية', 'nav_terms': 'شروط الخدمة', 'nav_faq': 'الأسئلة الشائعة',
        'cta_download': 'تحميل الفيديو', 'no_watermark': 'بدون علامة مائية',
        'no_watermark_desc': 'قم بتحميل مقاطع الفيديو بجودة فائقة بدون شعارات',
        'fast_download': 'تحميل فائق السرعة', 'fast_download_desc': 'معالجة فورية بدون أي انتظار',
        'multi_format': 'صيغ متعددة', 'multi_format_desc': 'يدعم MP4 و MP3 والعديد من الصيغ',
        'why_choose': 'لماذا تختارنا؟', 'security': 'آمن ومشفّر بنسبة 100%',
        'privacy_safe': 'بياناتك لا يتم تخزينها أبداً', 'speed': 'سرعة تحميل فائقة',
        'sla': 'الرد في غضون 24 ساعة', 'issue_type': 'نوع المشكلة', 'copyright': '© 2026 جميع الحقوق محفوظة'
    },
    'pt': {
        'nav_home': 'Início', 'nav_about': 'Sobre nós', 'nav_features': 'Recursos',
        'nav_contact': 'Contato', 'nav_privacy': 'Privacidade', 'nav_terms': 'Termos', 'nav_faq': 'Perguntas Frequentes',
        'cta_download': 'Baixar Vídeo', 'no_watermark': 'Sem Marca d’Água',
        'no_watermark_desc': 'Baixe vídeos com qualidade cristalina sem marcas',
        'fast_download': 'Download Rápido', 'fast_download_desc': 'Processamento instantâneo sem esperas',
        'multi_format': 'Múltiplos Formatos', 'multi_format_desc': 'Suporte a MP4, MP3 e muito mais',
        'why_choose': 'Por que nos escolher?', 'security': '100% seguro e criptografado',
        'privacy_safe': 'Seus dados nunca são armazenados', 'speed': 'Downloads extremamente rápidos',
        'sla': 'Respondemos em até 24 horas', 'issue_type': 'Tipo de problema', 'copyright': '© 2026 Todos os direitos reservados'
    },
    'ru': {
        'nav_home': 'Главная', 'nav_about': 'О сервисе', 'nav_features': 'Возможности',
        'nav_contact': 'Контакты', 'nav_privacy': 'Конфиденциальность', 'nav_terms': 'Условия', 'nav_faq': 'Частые вопросы',
        'cta_download': 'Скачать видео', 'no_watermark': 'Без водяных знаков',
        'no_watermark_desc': 'Скачивайте видео в оригинальном качестве без логотипов',
        'fast_download': 'Быстрая загрузка', 'fast_download_desc': 'Мгновенная обработка без ожидания',
        'multi_format': 'Различные форматы', 'multi_format_desc': 'Поддержка MP4, MP3 и других форматов',
        'why_choose': 'Почему выбирают нас?', 'security': '100% безопасно и зашифровано',
        'privacy_safe': 'Ваши данные никогда не сохраняются', 'speed': 'Молниеносная скорость',
        'sla': 'Ответ в течение 24 часов', 'issue_type': 'Тип вопроса', 'copyright': '© 2026 Все права защищены'
    },
    'id': {
        'nav_home': 'Beranda', 'nav_about': 'Tentang Kami', 'nav_features': 'Fitur',
        'nav_contact': 'Kontak', 'nav_privacy': 'Privasi', 'nav_terms': 'Syarat & Ketentuan', 'nav_faq': 'Tanya Jawab',
        'cta_download': 'Unduh Video', 'no_watermark': 'Tanpa Watermark',
        'no_watermark_desc': 'Unduh video jernih berkualitas tinggi tanpa tanda air',
        'fast_download': 'Unduhan Cepat', 'fast_download_desc': 'Proses instan tanpa menunggu lama',
        'multi_format': 'Banyak Format', 'multi_format_desc': 'Mendukung MP4, MP3 dan format lainnya',
        'why_choose': 'Mengapa Memilih Kami?', 'security': '100% aman dan terenkripsi',
        'privacy_safe': 'Data Anda tidak pernah disimpan', 'speed': 'Kecepatan secepat kilat',
        'sla': 'Kami merespon dalam 24 jam', 'issue_type': 'Jenis kendala', 'copyright': '© 2026 Hak cipta dilindungi'
    },
    'zh': {
        'nav_home': '首页', 'nav_about': '关于我们', 'nav_features': '功能特点',
        'nav_contact': '联系我们', 'nav_privacy': '隐私政策', 'nav_terms': '使用条款', 'nav_faq': '常见问题',
        'cta_download': '下载视频', 'no_watermark': '无水印下载',
        'no_watermark_desc': '高清原画质下载，去除所有多余水印',
        'fast_download': '超快下载', 'fast_download_desc': '瞬时解析处理，无需长时间等待',
        'multi_format': '多种格式支持', 'multi_format_desc': '完美支持 MP4、MP3 等主流音视频格式',
        'why_choose': '为什么选择我们？', 'security': '100% 安全且高强度加密',
        'privacy_safe': '从不保存任何个人隐私数据', 'speed': '极速直链下载',
        'sla': '我们将在24小时内回复您', 'issue_type': '问题类型', 'copyright': '© 2026 版权所有'
    },
    'ur': {
        'nav_home': 'ہوم', 'nav_about': 'ہمارے بارے میں', 'nav_features': 'خصوصیات',
        'nav_contact': 'رابطہ کریں', 'nav_privacy': 'پرائیویسی پالیسی', 'nav_terms': 'شرائط و ضوابط', 'nav_faq': 'عام سوالات',
        'cta_download': 'ویڈیو ڈاؤن لوڈ کریں', 'no_watermark': 'بغیر واٹر مارک',
        'no_watermark_desc': 'کرسٹل کلیئر ایچ ڈی کوالٹی میں بغیر کسی لوگو کے ڈاؤن لوڈ کریں',
        'fast_download': 'تیز ترین ڈاؤن لوڈ', 'fast_download_desc': 'بغیر کسی تاخیر کے فوری پروسیسنگ',
        'multi_format': 'متعدد فارمیٹس', 'multi_format_desc': 'MP4 اور MP3 فارمیٹس کی مکمل سپورٹ',
        'why_choose': 'ہمیں کیوں منتخب کریں؟', 'security': '100% محفوظ اور انکرپٹڈ',
        'privacy_safe': 'آپ کا ڈیٹا کبھی اسٹور نہیں کیا جاتا', 'speed': 'بجلی کی رفتار سے ڈاؤن لوڈنگ',
        'sla': 'ہم 24 گھنٹوں کے اندر جواب دیتے ہیں', 'issue_type': 'مسئلے کی قسم', 'copyright': '© 2026 جملہ حقوق محفوظ ہیں'
    }
}

total_files_created = 0

for p_folder, p_data in PLATFORMS.items():
    locales_dir = os.path.join(BASE_DIR, p_folder, 'locales')
    os.makedirs(locales_dir, exist_ok=True)
    
    # 1. English (Base)
    en_locale = {
        "meta": {
            "platform": p_data['key'],
            "language": "en",
            "locale_code": "en_US",
            "rtl": False
        },
        "navigation": {
            "home": f"{p_data['name']} Video Downloader",
            "about": "About Our Tool",
            "features": "Features",
            "contact": "Contact Us",
            "privacy": "Privacy Policy",
            "terms": "Terms of Service",
            "faq": "FAQ"
        },
        "hero": {
            "title": p_data['title'],
            "subtitle": p_data['subtitle'],
            "cta_button": p_data['cta'],
            "placeholder": p_data['placeholder']
        },
        "features": {
            "feature_1_title": "No Watermark",
            "feature_1_desc": "Download videos with crystal clear quality and no added watermarks",
            "feature_2_title": "Fast Download",
            "feature_2_desc": "Instant real-time stream processing with zero waiting",
            "feature_3_title": "Multiple Formats",
            "feature_3_desc": "MP4 (HD/SD) and high-fidelity MP3 audio supported"
        },
        "platform_specific": p_data['specific'],
        "about": {
            "title": p_data['about_title'],
            "description": p_data['about_desc'],
            "why_choose": f"Why choose downsocial for {p_data['name']}?",
            "security": "100% secure, encrypted HTTPS transmission",
            "privacy": "Zero login required, zero tracking cookies",
            "speed": "Direct CDN streaming for blazing fast downloads"
        },
        "contact": {
            "title": p_data['contact_title'],
            "subtitle": p_data['contact_sub'],
            "email_label": f"For {p_data['name']}-specific inquiries:",
            "phone_label": "Support desk:",
            "response_time": "We respond within 24 hours guaranteed",
            "issue_type": f"Issue Type ({p_data['name']} only)"
        },
        "privacy": {
            "title": p_data['privacy_title'],
            "subtitle": p_data['privacy_desc'],
            "data_collection": f"What data we collect during {p_data['name']} downloads: Zero personal data",
            "integration": f"How we interact with {p_data['name']} CDN servers safely",
            "your_privacy": f"Your absolute privacy when saving {p_data['name']} content"
        },
        "terms": {
            "title": p_data['terms_title'],
            "subtitle": p_data['terms_desc'],
            "compliance": f"Compliance with {p_data['name']} community terms and fair use",
            "usage_rights": "Personal, non-commercial archival use guidelines",
            "liability": "Limitation of liability and copyright ownership"
        },
        "faq": {
            f"q{i+1}": item['q'] for i, item in enumerate(p_data['faqs'])
        } | {
            f"a{i+1}": item['a'] for i, item in enumerate(p_data['faqs'])
        },
        "footer": {
            "copyright": "© 2026 downsocial.net. All rights reserved.",
            "about_link": "About",
            "features_link": "Features",
            "contact_link": "Contact",
            "privacy_link": "Privacy",
            "terms_link": "Terms"
        }
    }
    
    with open(os.path.join(locales_dir, 'en.json'), 'w', encoding='utf-8') as f:
        json.dump(en_locale, f, ensure_ascii=False, indent=2)
    total_files_created += 1
    
    # 2. Generate other 10 languages
    for lang, lang_info in LANGUAGES.items():
        if lang == 'en':
            continue
        c = COMMON_TRANS.get(lang, COMMON_TRANS['es'])
        
        lang_locale = {
            "meta": {
                "platform": p_data['key'],
                "language": lang,
                "locale_code": lang_info['code'],
                "rtl": lang_info['rtl']
            },
            "navigation": {
                "home": f"{p_data['name']} {c['nav_home']}",
                "about": c['nav_about'],
                "features": c['nav_features'],
                "contact": c['nav_contact'],
                "privacy": c['nav_privacy'],
                "terms": c['nav_terms'],
                "faq": c['nav_faq']
            },
            "hero": {
                "title": f"{c['cta_download']} {p_data['name']} HD",
                "subtitle": f"{c['no_watermark']} • {c['fast_download']} • {c['multi_format']}",
                "cta_button": f"{c['cta_download']} {p_data['name']}",
                "placeholder": p_data['placeholder']
            },
            "features": {
                "feature_1_title": c['no_watermark'],
                "feature_1_desc": c['no_watermark_desc'],
                "feature_2_title": c['fast_download'],
                "feature_2_desc": c['fast_download_desc'],
                "feature_3_title": c['multi_format'],
                "feature_3_desc": c['multi_format_desc']
            },
            "platform_specific": p_data['specific'],
            "about": {
                "title": f"{c['nav_about']} — {p_data['name']}",
                "description": p_data['about_desc'],
                "why_choose": c['why_choose'],
                "security": c['security'],
                "privacy": c['privacy_safe'],
                "speed": c['speed']
            },
            "contact": {
                "title": f"{c['nav_contact']} — {p_data['name']}",
                "subtitle": p_data['contact_sub'],
                "email_label": f"Support {p_data['name']}:",
                "phone_label": "Support Desk:",
                "response_time": c['sla'],
                "issue_type": c['issue_type']
            },
            "privacy": {
                "title": f"{c['nav_privacy']} — {p_data['name']}",
                "subtitle": p_data['privacy_desc'],
                "data_collection": f"{p_data['name']}: {c['privacy_safe']}",
                "integration": c['security'],
                "your_privacy": c['privacy_safe']
            },
            "terms": {
                "title": f"{c['nav_terms']} — {p_data['name']}",
                "subtitle": p_data['terms_desc'],
                "compliance": f"{p_data['name']} Compliance & Terms",
                "usage_rights": "Fair Use & Copyright Policy",
                "liability": "Liability Limitation"
            },
            "faq": {
                f"q{i+1}": item['q'] for i, item in enumerate(p_data['faqs'])
            } | {
                f"a{i+1}": item['a'] for i, item in enumerate(p_data['faqs'])
            },
            "footer": {
                "copyright": c['copyright'],
                "about_link": c['nav_about'],
                "features_link": c['nav_features'],
                "contact_link": c['nav_contact'],
                "privacy_link": c['nav_privacy'],
                "terms_link": c['nav_terms']
            }
        }
        
        with open(os.path.join(locales_dir, f'{lang}.json'), 'w', encoding='utf-8') as f:
            json.dump(lang_locale, f, ensure_ascii=False, indent=2)
        total_files_created += 1

print(f"Successfully generated {total_files_created} platform locale JSON files across 7 platforms and 11 languages!")
