# scratch/build_platforms_data.py
# High-fidelity multilingual generator for all platforms across all 12 languages

def get_platform_data(platform_id, lang):
    """
    Returns the complete dictionary for a specific platform in a given language.
    Guarantees full length, zero truncation, and authentic vocabulary.
    """
    # Platform base specs
    specs = {
        'index': {
            'it': ('Social Media Video Downloader', 'Scarica video, reel, shorts e storie da YouTube, TikTok, Instagram, Facebook, Snapchat e Threads in 1080p HD, 4K e MP3 gratis', 'Incolla qualsiasi link video (YouTube, TikTok, Instagram, Facebook, Snapchat, Threads)...', 'Scarica Video'),
            'name': 'Universal Social Media',
            'icon': 'fas fa-photo-video',
            'f1_icon': 'fas fa-bolt',
            'f2_icon': 'fas fa-shield-alt',
            'f3_icon': 'fas fa-photo-video',
        },
        'facebook': {
            'it': ('Facebook Video Downloader', 'Scarica Facebook Reels, video Watch, storie e clip di gruppi in 1080p Full HD gratis', 'Incolla qui l\'URL del video, Reel o Storia di Facebook...', 'Scarica Video da Facebook'),
            'name': 'Facebook',
            'icon': 'fab fa-facebook-f',
            'f1_icon': 'fas fa-bolt',
            'f2_icon': 'fab fa-facebook',
            'f3_icon': 'fas fa-music',
        },
        'instagram': {
            'it': ('Instagram Video Downloader', 'Scarica Instagram Reels, storie, foto e post carosello in risoluzione originale HD gratis', 'Incolla qui il link di Instagram Reel, Storia o Post...', 'Scarica Video da Instagram'),
            'name': 'Instagram',
            'icon': 'fab fa-instagram',
            'f1_icon': 'fas fa-bolt',
            'f2_icon': 'fab fa-instagram',
            'f3_icon': 'fas fa-music',
        },
        'tiktok': {
            'it': ('TikTok Video Downloader', 'Scarica video TikTok senza watermark in HD MP4 ed estrai audio MP3 a 320kbps gratis', 'Incolla qui il link del video TikTok...', 'Scarica Video da TikTok'),
            'name': 'TikTok',
            'icon': 'fab fa-tiktok',
            'f1_icon': 'fas fa-bolt',
            'f2_icon': 'fab fa-tiktok',
            'f3_icon': 'fas fa-music',
        },
        'youtube': {
            'it': ('YouTube Video Downloader', 'Scarica video e Shorts da YouTube in 1080p, 2K, 4K UHD ed estrai audio MP3 a 320kbps gratis', 'Incolla qui il link del video o Short di YouTube...', 'Scarica Video da YouTube'),
            'name': 'YouTube',
            'icon': 'fab fa-youtube',
            'f1_icon': 'fas fa-bolt',
            'f2_icon': 'fab fa-youtube',
            'f3_icon': 'fas fa-music',
        },
        'snapchat': {
            'it': ('Snapchat Video Downloader', 'Scarica video di Snapchat Spotlight e storie pubbliche in 1080p HD MP4 gratis', 'Incolla qui il link di Snapchat Spotlight o Storia...', 'Scarica Video da Snapchat'),
            'name': 'Snapchat',
            'icon': 'fab fa-snapchat-ghost',
            'f1_icon': 'fas fa-bolt',
            'f2_icon': 'fab fa-snapchat',
            'f3_icon': 'fas fa-music',
        },
        'threads': {
            'it': ('Threads Video Downloader', 'Scarica video, album fotografici e note vocali da Meta Threads in 1080p Full HD gratis', 'Incolla qui il link del post di Threads...', 'Scarica Video da Threads'),
            'name': 'Threads',
            'icon': 'fab fa-threads',
            'f1_icon': 'fas fa-bolt',
            'f2_icon': 'fab fa-threads',
            'f3_icon': 'fas fa-microphone',
        },
        'private': {
            'it': ('Downloader Video Privato', 'Scarica video protetti e privati da qualsiasi piattaforma incollando il codice sorgente', 'Incolla qui il codice sorgente della pagina web...', 'Estrai Video'),
            'name': 'Private Downloader',
            'icon': 'fas fa-user-lock',
            'f1_icon': 'fas fa-lock',
            'f2_icon': 'fas fa-shield-virus',
            'f3_icon': 'fas fa-code',
        }
    }

    # Titles & Taglines in 12 languages
    TITLES = {
        'index': {
            'en': ('Social Media Video Downloader', 'Download Videos, Reels, Shorts & Stories from YouTube, TikTok, Instagram, Facebook, Snapchat & Threads in 1080p HD, 4K & MP3 Free', 'Paste any video link (YouTube, TikTok, Instagram, Facebook, Snapchat, Threads)...', 'Download Video'),
            'es': ('Descargador de Videos de Redes Sociales', 'Descarga videos, reels, shorts y stories de YouTube, TikTok, Instagram, Facebook, Snapchat y Threads en 1080p HD, 4K y MP3 gratis', 'Pega cualquier enlace de video (YouTube, TikTok, Instagram, Facebook, Snapchat, Threads)...', 'Descargar Video'),
            'fr': ('Téléchargeur de Vidéos Réseaux Sociaux', 'Téléchargez vidéos, reels, shorts et stories depuis YouTube, TikTok, Instagram, Facebook, Snapchat et Threads en 1080p HD, 4K et MP3', 'Collez n’importe quel lien vidéo (YouTube, TikTok, Instagram, Facebook, Snapchat, Threads)...', 'Télécharger la Vidéo'),
            'de': ('Social Media Video Downloader', 'Laden Sie Videos, Reels, Shorts und Storys von YouTube, TikTok, Instagram, Facebook, Snapchat und Threads in 1080p HD, 4K und MP3 kostenlos herunter', 'Beliebigen Videolink hier einfügen (YouTube, TikTok, Instagram, Facebook, Snapchat, Threads)...', 'Video Herunterladen'),
            'hi': ('सोशल मीडिया वीडियो डाउनलोडर', 'यूट्यूब, टिकटॉक, इंस्टाग्राम, फेसबुक, स्नैपचैट और थ्रेड्स से 1080p HD, 4K और MP3 में वीडियो, रील्स, शॉर्ट्स और स्टोरीज मुफ्त डाउनलोड करें', 'कोई भी वीडियो लिंक यहां पेस्ट करें (YouTube, TikTok, Instagram, Facebook, Snapchat, Threads)...', 'वीडियो डाउनलोड करें'),
            'ar': ('محمل فيديوهات وسائل التواصل الاجتماعي', 'قم بتنزيل الفيديوهات والريلز والشورتس والقصص من يوتيوب وتيك توك وإنستغرام وفيسبوك وسناب شات وثريدز بدقة 1080p و 4K وصوت MP3 مجاناً', 'الصق أي رابط فيديو هنا (YouTube, TikTok, Instagram, Facebook, Snapchat, Threads)...', 'تحميل الفيديو'),
            'pt': ('Baixador de Vídeos de Redes Sociais', 'Baixe vídeos, reels, shorts e stories do YouTube, TikTok, Instagram, Facebook, Snapchat e Threads em 1080p HD, 4K e MP3 grátis', 'Cole qualquer link de vídeo aqui (YouTube, TikTok, Instagram, Facebook, Snapchat, Threads)...', 'Baixar Vídeo'),
            'bn': ('সোশ্যাল মিডিয়া ভিডিও ডাউনলোডার', 'ইউটিউব, টিকটক, ইনস্টাগ্রাম, ফেসবুক, স্ন্যাপচ্যাট ও থ্রেডস থেকে ১০৮০p HD, ৪K ও MP3 ফরম্যাটে ভিডিও ও রিলস সম্পূর্ণ ফ্রিতে ডাউনলোড করুন', 'যেকোনো ভিডিও লিংক এখানে পেস্ট করুন (YouTube, TikTok, Instagram, Facebook, Snapchat, Threads)...', 'ভিডিও ডাউনলোড করুন'),
            'ru': ('Загрузчик видео из социальных сетей', 'Скачивайте видео, рилс, шортс и истории с YouTube, TikTok, Instagram, Facebook, Snapchat и Threads в 1080p HD, 4K и MP3 бесплатно', 'Вставьте любую ссылку на видео (YouTube, TikTok, Instagram, Facebook, Snapchat, Threads)...', 'Скачать видео'),
            'id': ('Pengunduh Video Media Sosial', 'Unduh video, reels, shorts & story dari YouTube, TikTok, Instagram, Facebook, Snapchat, dan Threads dalam resolusi 1080p HD, 4K & MP3 gratis', 'Tempel tautan video apa pun di sini (YouTube, TikTok, Instagram, Facebook, Snapchat, Threads)...', 'Unduh Video'),
            'zh': ('全能社交媒体视频下载器', '免费极速解析下载 YouTube、TikTok、Instagram、Facebook、Snapchat 与 Threads 的高清视频、Reels、Shorts 与 320kbps MP3 音乐', '在此粘贴任意社交媒体视频链接 (YouTube, TikTok, Instagram, Facebook, Snapchat, Threads)...', '下载视频'),
            'ur': ('سوشل میڈیا ویڈیو ڈاؤنلوڈر', 'یوٹیوب، ٹک ٹاک، انسٹاگرام، فیس بک، سنیپ چیٹ اور تھریڈز سے 1080p HD، 4K اور MP3 میں ویڈیوز، ریلز اور شارٹس مفت ڈاؤن لوڈ کریں', 'کسی بھی ویڈیو کا لنک یہاں پیسٹ کریں (YouTube, TikTok, Instagram, Facebook, Snapchat, Threads)...', 'ویڈیو ڈاؤن لوڈ کریں')
        },
        'facebook': {
            'en': ('Facebook Video Downloader', 'Download Facebook Reels, Watch Videos, Stories & Group Clips in 1080p Full HD Free', 'Paste Facebook video, Reel, or Story URL here (facebook.com/watch/?v=...)...', 'Download Facebook Video'),
            'es': ('Descargador de Videos de Facebook', 'Descarga Facebook Reels, videos de Watch, Stories y clips de grupos en 1080p Full HD gratis', 'Pega la URL de Facebook video, Reel o Story aquí...', 'Descargar Video de Facebook'),
            'fr': ('Téléchargeur de Vidéos Facebook', 'Téléchargez Facebook Reels, vidéos Watch, Stories et clips en 1080p Full HD gratuitement', 'Collez l’URL de la vidéo, Reel ou Story Facebook ici...', 'Télécharger Vidéo Facebook'),
            'de': ('Facebook Video Downloader', 'Laden Sie Facebook Reels, Watch-Videos, Storys und Gruppenclips in 1080p Full HD kostenlos herunter', 'Facebook Video-, Reel- oder Story-URL hier einfügen...', 'Facebook Video Herunterladen'),
            'hi': ('फेसबुक वीडियो डाउनलोडर', 'फेसबुक रील्स, वॉच वीडियो, स्टोरीज और ग्रुप क्लिप्स 1080p फुल एचडी में मुफ्त डाउनलोड करें', 'फेसबुक वीडियो, रील या स्टोरी लिंक यहां पेस्ट करें...', 'फेसबुक वीडियो डाउनलोड करें'),
            'ar': ('محمل فيديوهات فيسبوك', 'تنزيل مقاطع ريلز وفيديوهات وستوري فيسبوك بدقة 1080p Full HD مجاناً وبدون علامات مائية', 'الصق رابط فيديو أو ريلز أو ستوري فيسبوك هنا...', 'تحميل فيديو فيسبوك'),
            'pt': ('Baixador de Vídeos do Facebook', 'Baixe Reels do Facebook, vídeos do Watch, Stories e clipes de grupos em 1080p Full HD grátis', 'Cole o link de vídeo, Reel ou Story do Facebook aqui...', 'Baixar Vídeo do Facebook'),
            'bn': ('ফেসবুক ভিডিও ডাউনলোডার', 'ফেসবুক রিলস, ওয়াচ ভিডিও, স্টোরিজ ও ক্লিপ ১০৮০p ফুল HD কোয়ালিটিতে বিনামূল্যে ডাউনলোড করুন', 'ফেসবুক ভিডিও, রিল বা স্টোরি লিংক এখানে পেস্ট করুন...', 'ফেসবুক ভিডিও ডাউনলোড করুন'),
            'ru': ('Загрузчик видео Facebook', 'Скачивайте рилс Facebook, видео Watch, истории и клипы в качестве 1080p Full HD бесплатно', 'Вставьте ссылку на видео, рилс или историю Facebook здесь...', 'Скачать видео Facebook'),
            'id': ('Pengunduh Video Facebook', 'Unduh Facebook Reels, video Watch, Story, dan klip grup dalam 1080p Full HD gratis', 'Tempel URL video, Reel, atau Story Facebook di sini...', 'Unduh Video Facebook'),
            'zh': ('Facebook 视频高清下载器', '免费下载 Facebook Reels 短剧、Watch 专区视频、快拍 Stories 及公开小组高清视频（1080p 原画）', '在此粘贴 Facebook 视频、Reel 或 Story 链接...', '下载 Facebook 视频'),
            'ur': ('فیس بک ویڈیو ڈاؤنلوڈر', 'فیس بک ریلز، واچ ویڈیوز، اسٹوریز اور گروپ کلپس کو 1080p فل ایچ ڈی میں مفت ڈاؤن لوڈ کریں', 'فیس بک ویڈیو، ریل یا اسٹوری کا لنک یہاں پیسٹ کریں...', 'فیس بک ویڈیو ڈاؤن لوڈ کریں')
        },
        'instagram': {
            'en': ('Instagram Video Downloader', 'Download Instagram Reels, Stories, Photos & Carousel Posts in Original HD Resolution Free', 'Paste Instagram Reel, Story, or Post link here (instagram.com/reel/...)...', 'Download Instagram Video'),
            'es': ('Descargador de Instagram', 'Descarga Instagram Reels, Stories, Fotos y Carruseles en resolución original HD gratis', 'Pega el enlace de Instagram Reel, Story o Publicación aquí...', 'Descargar Video de Instagram'),
            'fr': ('Téléchargeur de Vidéos Instagram', 'Téléchargez Reels, Stories, Photos et Carrousels Instagram en HD originale gratuitement', 'Collez le lien Instagram Reel, Story ou Publication ici...', 'Télécharger Vidéo Instagram'),
            'de': ('Instagram Video Downloader', 'Laden Sie Instagram Reels, Storys, Fotos und Karussell-Beiträge in Original-HD kostenlos herunter', 'Instagram Reel-, Story- oder Beitragslink hier einfügen...', 'Instagram Video Herunterladen'),
            'hi': ('इंस्टाग्राम वीडियो डाउनलोडर', 'इंस्टाग्राम रील्स, स्टोरीज, फोटोज और कैरोसेल मूल HD रिज़ॉल्यूशन में मुफ्त डाउनलोड करें', 'इंस्टाग्राम रील, स्टोरी या पोस्ट लिंक यहां पेस्ट करें...', 'इंस्टाग्राम वीडियो डाउनलोड करें'),
            'ar': ('محمل فيديوهات إنستغرام', 'تنزيل مقاطع ريلز وقصص وصور ومنشورات الكاروسيل من إنستغرام بدقتها الأصلية العالية مجاناً', 'الصق رابط ريلز أو ستوري أو منشور إنستغرام هنا...', 'تحميل فيديو إنستغرام'),
            'pt': ('Baixador do Instagram', 'Baixe Reels, Stories, Fotos e Carrosséis do Instagram na resolução original em HD grátis', 'Cole o link de Reel, Story ou Publicação do Instagram aqui...', 'Baixar Vídeo do Instagram'),
            'bn': ('ইনস্টাগ্রাম ভিডিও ডাউনলোডার', 'ইনস্টাগ্রাম রিলস, স্টোরিজ, ছবি ও ক্যারোসেল পোস্ট আসল HD রেজোলিউশনে ফ্রিতে ডাউনলোড করুন', 'ইনস্টাগ্রাম রিল, স্টোরি বা পোস্ট লিংক এখানে পেস্ট করুন...', 'ইনস্টাগ্রাম ভিডিও ডাউনলোড করুন'),
            'ru': ('Загрузчик видео Instagram', 'Скачивайте рилс, истории, фото и карусели Instagram в оригинальном качестве HD бесплатно', 'Вставьте ссылку на рилс, историю или пост Instagram здесь...', 'Скачать видео Instagram'),
            'id': ('Pengunduh Video Instagram', 'Unduh Instagram Reels, Story, Foto, dan Postingan Korsel dalam resolusi asli HD gratis', 'Tempel tautan Instagram Reel, Story, atau Postingan di sini...', 'Unduh Video Instagram'),
            'zh': 'Instagram 视频下载器', # Will format in tuple
            'ur': ('انسٹاگرام ویڈیو ڈاؤنلوڈر', 'انسٹاگرام ریلز، اسٹوریز، تصاویر اور کیروسل پوسٹس کو اصل HD ریزولوشن میں مفت ڈاؤن لوڈ کریں', 'انسٹاگرام ریل، اسٹوری یا پوسٹ کا لنک یہاں پیسٹ کریں...', 'انسٹاگرام ویڈیو ڈاؤن لوڈ کریں')
        },
        'tiktok': {
            'en': ('TikTok Video Downloader', 'Download TikTok Videos Without Watermark in HD MP4 & Extract 320kbps MP3 Audio Free', 'Paste TikTok video link here (vt.tiktok.com or tiktok.com/@user)...', 'Download TikTok Video'),
            'es': ('Descargador de Videos de TikTok', 'Descarga videos de TikTok sin marca de agua en HD MP4 y extrae audio MP3 a 320kbps gratis', 'Pega el enlace de video de TikTok aquí...', 'Descargar Video de TikTok'),
            'fr': ('Téléchargeur de Vidéos TikTok', 'Téléchargez des vidéos TikTok sans filigrane en HD MP4 et extrayez l’audio MP3 320 kbps', 'Collez le lien de la vidéo TikTok ici...', 'Télécharger Vidéo TikTok'),
            'de': ('TikTok Video Downloader', 'Laden Sie TikTok-Videos ohne Wasserzeichen in HD MP4 herunter und extrahieren Sie 320kbps MP3', 'TikTok-Videolink hier einfügen...', 'TikTok Video Herunterladen'),
            'hi': ('टिकटॉक वीडियो डाउनलोडर', 'बिना वॉटरमार्क के HD MP4 में टिकटॉक वीडियो डाउनलोड करें और 320kbps MP3 ऑडियो निकालें', 'टिकटॉक वीडियो लिंक यहां पेस्ट करें...', 'टिकटॉक वीडियो डाउनलोड करें'),
            'ar': ('محمل فيديوهات تيك توك', 'تنزيل مقاطع تيك توك بدون علامة مائية بدقة HD MP4 واستخراج الصوتيات MP3 بنقاء 320kbps', 'الصق رابط فيديو تيك توك هنا...', 'تحميل فيديو تيك توك'),
            'pt': ('Baixador de Vídeos do TikTok', 'Baixe vídeos do TikTok sem marca d’água em HD MP4 e extraia áudio MP3 de 320kbps grátis', 'Cole o link do vídeo do TikTok aqui...', 'Baixar Vídeo do TikTok'),
            'bn': ('টিকটক ভিডিও ডাউনলোডার', 'কোনো ওয়াটারমার্ক ছাড়া টিকটক ভিডিও HD MP4-এ ডাউনলোড এবং ৩২০kbps MP3 অডিও সেভ করুন', 'টিকটক ভিডিও লিংক এখানে পেস্ট করুন...', 'টিকটক ভিডিও ডাউনলোড করুন'),
            'ru': ('Загрузчик видео TikTok', 'Скачивайте видео из TikTok без водяных знаков в HD MP4 и извлекайте MP3 аудио 320 кбит/с', 'Вставьте ссылку на видео TikTok здесь...', 'Скачать видео TikTok'),
            'id': ('Pengunduh Video TikTok', 'Unduh video TikTok tanpa watermark dalam HD MP4 & ekstrak audio MP3 320kbps gratis', 'Tempel tautan video TikTok di sini...', 'Unduh Video TikTok'),
            'zh': ('TikTok 无水印视频下载器', '超清解析去除 TikTok 浮动水印，一键下载原画 MP4 视频与 320kbps 高保真 MP3 音乐伴奏', '在此粘贴 TikTok 视频链接 (vt.tiktok.com 或 tiktok.com/@user)...', '下载 TikTok 视频'),
            'ur': ('ٹک ٹاک ویڈیو ڈاؤنلوڈر', 'بغیر واٹر مارک کے ٹک ٹاک ویڈیوز HD MP4 میں ڈاؤن لوڈ کریں اور 320kbps MP3 آڈیو حاصل کریں', 'ٹک ٹاک ویڈیو کا لنک یہاں پیسٹ کریں...', 'ٹک ٹاک ویڈیو ڈاؤن لوڈ کریں')
        },
        'youtube': {
            'en': ('YouTube Video Downloader & Shorts', 'Download YouTube Videos, Shorts & Playlists in 1080p, 2K, 4K UHD & 320kbps MP3 Free', 'Paste YouTube video or Shorts link here (youtube.com or youtu.be)...', 'Download YouTube Video'),
            'es': ('Descargador de YouTube y Shorts', 'Descarga videos de YouTube, Shorts y listas en 1080p, 2K, 4K UHD y MP3 a 320kbps gratis', 'Pega el enlace de video de YouTube o Shorts aquí...', 'Descargar Video de YouTube'),
            'fr': ('Téléchargeur de Vidéos YouTube & Shorts', 'Téléchargez des vidéos YouTube, Shorts et playlists en 1080p, 2K, 4K UHD et MP3 320 kbps', 'Collez le lien de la vidéo YouTube ou Shorts ici...', 'Télécharger Vidéo YouTube'),
            'de': ('YouTube Video Downloader & Shorts', 'Laden Sie YouTube-Videos, Shorts & Playlists in 1080p, 2K, 4K UHD und 320kbps MP3 kostenlos herunter', 'YouTube Video- oder Shorts-Link hier einfügen...', 'YouTube Video Herunterladen'),
            'hi': ('यूट्यूब वीडियो डाउनलोडर और शॉर्ट्स', 'यूट्यूब वीडियो, शॉर्ट्स और प्लेलिस्ट 1080p, 2K, 4K UHD और 320kbps MP3 में मुफ्त डाउनलोड करें', 'यूट्यूब वीडियो या शॉर्ट्स लिंक यहां पेस्ट करें...', 'यूट्यूब वीडियो डाउनलोड करें'),
            'ar': ('محمل فيديوهات يوتيوب والشورتس', 'تنزيل مقاطع يوتيوب وشورتس بدقة 1080p و 2K و 4K Ultra HD وتحويلها إلى MP3 نقي 320kbps', 'الصق رابط فيديو يوتيوب أو شورتس هنا...', 'تحميل فيديو يوتيوب'),
            'pt': ('Baixador do YouTube e Shorts', 'Baixe vídeos do YouTube, Shorts e playlists em 1080p, 2K, 4K UHD e MP3 de 320kbps grátis', 'Cole o link de vídeo do YouTube ou Shorts aqui...', 'Baixar Vídeo do YouTube'),
            'bn': ('ইউটিউব ভিডিও ও শর্টস ডাউনলোডার', 'ইউটিউব ভিডিও, শর্টস ও প্লেলিস্ট ১০৮০p, ২K, ৪K UHD এবং ৩২০kbps MP3 ফরম্যাটে ফ্রিতে ডাউনলোড করুন', 'ইউটিউব ভিডিও বা শর্টস লিংক এখানে পেস্ট করুন...', 'ইউটিউব ভিডিও ডাউনলোড করুন'),
            'ru': ('Загрузчик видео с YouTube и Shorts', 'Скачивайте видео с YouTube, Shorts и плейлисты в 1080p, 2K, 4K UHD и MP3 320 кбит/с бесплатно', 'Вставьте ссылку на видео или Shorts с YouTube здесь...', 'Скачать видео YouTube'),
            'id': ('Pengunduh Video YouTube & Shorts', 'Unduh video YouTube, Shorts, dan daftar putar dalam 1080p, 2K, 4K UHD & MP3 320kbps gratis', 'Tempel tautan video atau Shorts YouTube di sini...', 'Unduh Video YouTube'),
            'zh': ('YouTube 视频与 Shorts 下载器', '快速解析 YouTube 视频与 Shorts 短片，支持 1080p、2K、4K 超清音画合流与 320kbps MP3 音频转码', '在此粘贴 YouTube 视频或 Shorts 链接 (youtube.com 或 youtu.be)...', '下载 YouTube 视频'),
            'ur': ('یوٹیوب ویڈیو اور شارٹس ڈاؤنلوڈر', 'یوٹیوب ویڈیوز، شارٹس اور پلے لسٹس کو 1080p، 2K، 4K UHD اور 320kbps MP3 میں مفت ڈاؤن لوڈ کریں', 'یوٹیوب ویڈیو یا شارٹس کا لنک یہاں پیسٹ کریں...', 'یوٹیوب ویڈیو ڈاؤن لوڈ کریں')
        },
        'snapchat': {
            'en': ('Snapchat Video Downloader', 'Download Snapchat Spotlight Videos & Public Stories in 9:16 Full HD MP4 Free', 'Paste Snapchat Spotlight or Story link here (snapchat.com/t/...)...', 'Download Snapchat Video'),
            'es': ('Descargador de Snapchat', 'Descarga videos de Snapchat Spotlight y Stories públicas en vertical 9:16 Full HD gratis', 'Pega el enlace de Snapchat Spotlight o Story aquí...', 'Descargar Video de Snapchat'),
            'fr': ('Téléchargeur de Vidéos Snapchat', 'Téléchargez des vidéos Snapchat Spotlight et Stories publiques en 9:16 Full HD gratuit', 'Collez le lien Snapchat Spotlight ou Story ici...', 'Télécharger Vidéo Snapchat'),
            'de': ('Snapchat Video Downloader', 'Laden Sie Snapchat Spotlight-Videos & öffentliche Storys im 9:16 Full HD MP4 kostenlos herunter', 'Snapchat Spotlight- oder Story-Link hier einfügen...', 'Snapchat Video Herunterladen'),
            'hi': ('स्नैपचैट वीडियो डाउनलोडर', 'स्नैपचैट स्पॉटलाइट वीडियो और सार्वजनिक कहानियाँ 9:16 फुल एचडी MP4 में मुफ्त डाउनलोड करें', 'स्नैपचैट स्पॉटलाइट या स्टोरी लिंक यहां पेस्ट करें...', 'स्नैपचैट वीडियो डाउनलोड करें'),
            'ar': ('محمل فيديوهات سناب شات', 'تنزيل مقاطع سناب شات سبوت لايت والقصص العامة بدقة 9:16 Full HD MP4 مجاناً وبدون علم الناشر', 'الصق رابط سناب شات سبوت لايت أو ستوري هنا...', 'تحميل فيديو سناب شات'),
            'pt': ('Baixador do Snapchat', 'Baixe vídeos do Snapchat Spotlight e Stories públicas em 9:16 Full HD MP4 grátis', 'Cole o link de Snapchat Spotlight ou Story aqui...', 'Baixar Vídeo do Snapchat'),
            'bn': ('স্ন্যাপচ্যাট ভিডিও ডাউনলোডার', 'স্ন্যাপচ্যাট স্পটলাইট ও পাবলিক স্টোরিজ ৯:১৬ ফুল HD MP4 কোয়ালিটিতে বিনামূল্যে ডাউনলোড করুন', 'স্ন্যাপচ্যাট স্পটলাইট বা স্টোরি লিংক এখানে পেস্ট করুন...', 'স্ন্যাপচ্যাট ভিডিও ডাউনলোড করুন'),
            'ru': ('Загрузчик видео Snapchat', 'Скачивайте ролики Snapchat Spotlight и публичные истории в формате 9:16 Full HD MP4 бесплатно', 'Вставьте ссылку на Snapchat Spotlight или историю здесь...', 'Скачать видео Snapchat'),
            'id': ('Pengunduh Video Snapchat', 'Unduh video Snapchat Spotlight dan Story publik dalam format 9:16 Full HD MP4 gratis', 'Tempel tautan Snapchat Spotlight atau Story di sini...', 'Unduh Video Snapchat'),
            'zh': ('Snapchat 视频与快拍下载器', '无水印保存 Snapchat Spotlight 竖屏短片与公开 Stories 快拍为 9:16 原画全高清 MP4 格式', '在此粘贴 Snapchat Spotlight 或 Story 链接 (snapchat.com/t/...)...', '下载 Snapchat 视频'),
            'ur': ('سنیپ چیٹ ویڈیو ڈاؤنلوڈر', 'سنیپ چیٹ اسپاٹ لائٹ ویڈیوز اور پبلک اسٹوریز کو 9:16 فل ایچ ڈی MP4 میں مفت ڈاؤن لوڈ کریں', 'سنیپ چیٹ اسپاٹ لائٹ یا اسٹوری کا لنک یہاں پیسٹ کریں...', 'سنیپ چیٹ ویڈیو ڈاؤن لوڈ کریں')
        },
        'threads': {
            'en': ('Threads Video Downloader', 'Download Meta Threads Videos, Voice Notes, Carousel Photos & Audio in 1080p Full HD Free', 'Paste your Meta Threads post link here (threads.net/@user/post/...)...', 'Download Video'),
            'es': ('Descargador de Videos de Threads', 'Descarga videos, notas de voz, fotos de carrusel y audios de Meta Threads en 1080p Full HD gratis', 'Pega el enlace de la publicación de Meta Threads aquí...', 'Descargar Video'),
            'fr': ('Téléchargeur de Vidéos Threads', 'Téléchargez vidéos, notes vocales, carrousels et audios Meta Threads en 1080p Full HD gratuit', 'Collez le lien de la publication Meta Threads ici...', 'Télécharger la Vidéo'),
            'de': ('Threads Video Downloader', 'Laden Sie Meta Threads Videos, Sprachnachrichten, Fotos und Audio in 1080p Full HD kostenlos herunter', 'Meta Threads Beitragslink hier einfügen...', 'Video Herunterladen'),
            'hi': ('थ्रेड्स वीडियो डाउनलोडर', 'मेटा थ्रेड्स वीडियो, वॉयस नोट्स, कैरोसेल फोटो और ऑडियो 1080p फुल एचडी में मुफ्त डाउनलोड करें', 'मेटा थ्रेड्स पोस्ट लिंक यहां पेस्ट करें...', 'वीडियो डाउनलोड करें'),
            'ar': ('محمل فيديوهات ثريدز', 'تنزيل مقاطع الفيديو والتسجيلات الصوتية والصور من ميتا ثريدز بجودة 1080p Full HD مجاناً', 'الصق رابط منشور ميتا ثريدز هنا...', 'تحميل الفيديو'),
            'pt': ('Baixador de Vídeos do Threads', 'Baixe vídeos, notas de voz, fotos de carrossel e áudios do Meta Threads em 1080p Full HD grátis', 'Cole o link da publicação do Meta Threads aqui...', 'Baixar Vídeo'),
            'bn': ('থ্রেডস ভিডিও ডাউনলোডার', 'মেটা থ্রেডস ভিডিও, ভয়েس নোট, ক্যারোসেল ছবি ও অডিও ১০৮০p ফুল HD কোয়ালিটিতে বিনামূল্যে ডাউনলোড করুন', 'মেটা থ্রেডস পোস্টের লিংক এখানে পেস্ট করুন...', 'ভিডিও ডাউনলোড করুন'),
            'ru': ('Загрузчик видео Threads', 'Скачивайте видео, голосовые заметки, фото-карусели и аудио из Meta Threads в 1080p Full HD бесплатно', 'Вставьте ссылку на публикацию Meta Threads здесь...', 'Скачать видео'),
            'id': ('Pengunduh Video Threads', 'Unduh video Meta Threads, rekaman suara, foto korsel, dan audio dalam 1080p Full HD gratis', 'Tempel tautan postingan Meta Threads di sini...', 'Unduh Video'),
            'zh': ('Threads 视频下载器', '高清下载 Meta Threads 话题视频、语音备忘录、图文轮播相册与无损 MP3 音频（支持 1080p 原画）', '在此粘贴 Meta Threads 帖子链接 (threads.net/@user/post/...)...', '下载视频'),
            'ur': ('تھریڈز ویڈیو ڈاؤنلوڈر', 'میٹا تھریڈز ویڈیوز، وائس نوٹس، کیروسل تصاویر اور آڈیو 1080p فل ایچ ڈی میں مفت ڈاؤن لوڈ کریں', 'میٹا تھریڈز پوسٹ کا لنک یہاں پیسٹ کریں...', 'ویڈیو ڈاؤن لوڈ کریں')
        },
        'private': {
            'en': ('Private Video Downloader', 'Download Private Instagram Reels, Facebook Closed Group Videos & Restricted Posts Safely', 'Paste the full page source code (HTML) here to extract video streams...', 'Extract Private Video'),
            'es': ('Descargador de Videos Privados', 'Descarga reels privados de Instagram, videos de grupos de Facebook y publicaciones restringidas', 'Pega el código fuente de la página completa (HTML) aquí...', 'Extraer Video Privado'),
            'fr': ('Téléchargeur de Vidéos Privées', 'Téléchargez reels Instagram privés, vidéos de groupes Facebook et publications restreintes', 'Collez le code source complet de la page (HTML) ici...', 'Extraire la Vidéo Privée'),
            'de': ('Privater Video Downloader', 'Laden Sie private Instagram Reels, geschützte Facebook-Videos und geschlossene Gruppen herunter', 'Fügen Sie den vollständigen HTML-Quelltext der Seite hier ein...', 'Privates Video Extrahieren'),
            'hi': ('प्राइवेट वीडियो डाउनलोडर', 'इंस्टाग्राम रील्स, फेसबुक प्राइवेट ग्रुप्स और प्रतिबंधित वीडियो सुरक्षित रूप से डाउनलोड करें', 'वीडियो निकालने के लिए पेज का पूरा सोर्स कोड (HTML) यहां पेस्ट करें...', 'प्राइवेट वीडियो निकालें'),
            'ar': ('محمل الفيديوهات الخاصة', 'تنزيل ريلز إنستغرام الخاصة وفيديوهات مجموعات فيسبوك المغلقة والمنشورات المقيدة بأمان', 'الصق كود مصدر الصفحة بالكامل (HTML) هنا لاستخراج الفيديو...', 'استخراج الفيديو الخاص'),
            'pt': ('Baixador de Vídeos Privados', 'Baixe reels privados do Instagram, vídeos de grupos fechados do Facebook e posts restritos', 'Cole o código-fonte completo da página (HTML) aqui...', 'Extrair Vídeo Privado'),
            'bn': ('প্রাইভেট ভিডিও ডাউনলোডার', 'ইনস্টাগ্রাম প্রাইভেট রিলস, ফেসবুক বন্ধ গ্রুপের ভিডিও ও সংরক্ষিত পোস্ট নিরাপদে ডাউনলোড করুন', 'ভিডিও লিংক বের করতে সম্পূর্ণ পেইজ সোর্স কোড (HTML) এখানে পেস্ট করুন...', 'প্রাইভেট ভিডিও এক্সট্র্যাক্ট করুন'),
            'ru': ('Загрузчик приватных видео', 'Скачивайте закрытые рилс Instagram, видео из групп Facebook и приватные публикации', 'Вставьте полный исходный код страницы (HTML) здесь...', 'Извлечь приватное видео'),
            'id': ('Pengunduh Video Privat', 'Unduh reels privat Instagram, video grup tertutup Facebook, dan postingan terbatas', 'Tempel seluruh kode sumber halaman (HTML) di sini...', 'Ekstrak Video Privat'),
            'zh': ('私密视频安全解析下载器', '基于纯前端网页源代码安全解析，提取下载已获关注授权的 Instagram 与 Facebook 私密视频', '在此粘贴包含私密视频的完整网页源代码 (HTML)...', '解析提取私密视频'),
            'ur': ('پرائیویٹ ویڈیو ڈاؤنلوڈر', 'انسٹاگرام کی پرائیویٹ ریلز، فیس بک کے بند گروپس اور محدود ویڈیوز محفوظ طریقے سے ڈاؤن لوڈ کریں', 'ویڈیو نکالنے کے لیے پیج کا مکمل سورس کوڈ (HTML) یہاں پیسٹ کریں...', 'پرائیویٹ ویڈیو حاصل کریں')
        }
    }

    # Fix Chinese tuple for instagram
    TITLES['instagram']['zh'] = ('Instagram 视频高清下载器', '免登录下载 Instagram Reels 卷轴短片、24小时快拍 Stories、超清相册与多图轮播（100% 原画质无水印）', '在此粘贴 Instagram Reel、Story 或帖子链接 (instagram.com/reel/...)...', '下载 Instagram 视频')

    # Italian TITLES entries
    TITLES['index']['it'] = ('Scaricatore di Video dai Social Network', 'Scarica video, reel, shorts e storie da YouTube, TikTok, Instagram, Facebook, Snapchat e Threads in 1080p HD, 4K e MP3 gratis', 'Incolla qualsiasi link video (YouTube, TikTok, Instagram, Facebook, Snapchat, Threads)...', 'Scarica Video')
    TITLES['facebook']['it'] = ('Scaricatore di Video da Facebook', 'Scarica Reel di Facebook, video Watch, storie e clip di gruppi in 1080p Full HD gratis', 'Incolla qui l\'URL di video, Reel o storia di Facebook...', 'Scarica Video da Facebook')
    TITLES['instagram']['it'] = ('Scaricatore di Video da Instagram', 'Scarica Reel, storie, foto e post carosello di Instagram in risoluzione originale HD gratis', 'Incolla qui il link di Reel, storia o post di Instagram...', 'Scarica Video da Instagram')
    TITLES['tiktok']['it'] = ('Scaricatore di Video da TikTok', 'Scarica video da TikTok senza watermark in HD MP4 ed estrai audio MP3 a 320 kbps gratis', 'Incolla qui il link del video di TikTok...', 'Scarica Video da TikTok')
    TITLES['youtube']['it'] = ('Scaricatore di Video da YouTube e Shorts', 'Scarica video, Shorts e playlist di YouTube in 1080p, 2K, 4K UHD e MP3 a 320 kbps gratis', 'Incolla qui il link di video o Shorts di YouTube...', 'Scarica Video da YouTube')
    TITLES['snapchat']['it'] = ('Scaricatore di Video da Snapchat', 'Scarica video Spotlight di Snapchat e storie pubbliche in formato 9:16 Full HD MP4 gratis', 'Incolla qui il link di Snapchat Spotlight o storia...', 'Scarica Video da Snapchat')
    TITLES['threads']['it'] = ('Scaricatore di Video da Threads', 'Scarica video, note vocali, foto carosello e audio da Meta Threads in 1080p Full HD gratis', 'Incolla qui il link del post di Meta Threads...', 'Scarica Video')
    TITLES['private']['it'] = ('Scaricatore di Video Privati', 'Scarica reel privati di Instagram, video di gruppi chiusi di Facebook e post protetti in sicurezza', 'Incolla qui il codice sorgente completo della pagina (HTML)...', 'Estrai Video Privato')

    p_info = TITLES.get(platform_id, TITLES['index']).get(lang, TITLES['index']['en'])
    title, tagline, placeholder, download_btn = p_info

    # 3 Features for this platform in this language
    def get_features():
        # High quality localized feature descriptions
        p_name = specs[platform_id]['name']
        f_map = {
            'it': [
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
                    'blogP2': 'Tutta l\'elaborazione avviene temporaneamente nella memoria RAM e viene cancellata al termine.'
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

            'en': [
                {
                    'title': 'Original HD & 4K Quality',
                    'desc': f'Download {p_name} media in pristine original resolution without extra compression or visual artifacts.',
                    'blogIcon': 'fas fa-film',
                    'blogTitle': f'Lossless {p_name} Stream Capture',
                    'blogP1': f'Our servers connect directly to high-speed CDN delivery points to fetch pure high-bitrate video streams.',
                    'blogP2': 'Enjoy vibrant colors, sharp frame rates, and zero quality loss across all playback devices.'
                },
                {
                    'title': 'Zero Login & 100% Private',
                    'desc': 'Download freely without providing account credentials, email addresses, or passwords.',
                    'blogIcon': 'fas fa-shield-halved',
                    'blogTitle': 'Complete Anonymity & Data Protection',
                    'blogP1': 'We respect your online privacy. No download history, session tokens, or personal identifiers are stored.',
                    'blogP2': 'Every processing request is handled ephemerally in RAM and purged immediately upon delivery.'
                },
                {
                    'title': 'Studio-Grade 320kbps MP3',
                    'desc': f'Convert and save sound clips, speech, and background music from {p_name} as genuine high-fidelity MP3 audio.',
                    'blogIcon': 'fas fa-headphones',
                    'blogTitle': 'Real-Time Audio Transcoding Engine',
                    'blogP1': 'Integrated FFmpeg pipeline converts original audio streams into crystal-clear 320kbps/192kbps MP3 files.',
                    'blogP2': 'Perfect for ringtones, podcast archives, voice notes, and offline music libraries.'
                }
            ],
            'es': [
                {
                    'title': 'Calidad Original HD y 4K',
                    'desc': f'Descarga contenido de {p_name} en resolución nativa sin compresión adicional ni pérdida de detalle.',
                    'blogIcon': 'fas fa-film',
                    'blogTitle': f'Captura Sin Pérdidas para {p_name}',
                    'blogP1': f'Nos conectamos a los puntos CDN para obtener streams limpios con la máxima tasa de bits posible.',
                    'blogP2': 'Disfruta de colores vivos y reproducción fluida en cualquier smartphone, tablet o computadora.'
                },
                {
                    'title': 'Sin Login y 100% Privado',
                    'desc': 'Descarga libremente sin compartir tus credenciales de acceso, contraseñas ni correos.',
                    'blogIcon': 'fas fa-shield-halved',
                    'blogTitle': 'Anonimato Garantizado y Cero Rastreo',
                    'blogP1': 'Respetamos tu privacidad. No guardamos registros de descargas ni identificadores personales.',
                    'blogP2': 'Todo el procesamiento se realiza en memoria RAM y se borra inmediatamente al finalizar.'
                },
                {
                    'title': 'Audio MP3 de Estudio 320kbps',
                    'desc': f'Extrae bandas sonoras, voz y pistas musicales de {p_name} directamente en formato MP3 de alta fidelidad.',
                    'blogIcon': 'fas fa-headphones',
                    'blogTitle': 'Conversión de Audio en Tiempo Real',
                    'blogP1': 'Motor integrado que transcodifica pistas de audio en archivos MP3 limpios y de alta calidad.',
                    'blogP2': 'Ideal para notas de voz, música para entrenar, podcasts y reproducción sin conexión.'
                }
            ],
            'fr': [
                {
                    'title': 'Qualité Originale HD & 4K',
                    'desc': f'Téléchargez les médias {p_name} en résolution native sans compression supplémentaire ni artefacts.',
                    'blogIcon': 'fas fa-film',
                    'blogTitle': f'Extraction Sans Perte pour {p_name}',
                    'blogP1': f'Connexion directe aux serveurs CDN pour récupérer les flux vidéo à haut débit les plus nets.',
                    'blogP2': 'Bénéficiez de couleurs éclatantes et d’une fluidité optimale sur tous vos écrans.'
                },
                {
                    'title': 'Sans Inscription & 100% Privé',
                    'desc': 'Téléchargez en toute liberté sans renseigner d’identifiants, d’e-mails ou de mots de passe.',
                    'blogIcon': 'fas fa-shield-halved',
                    'blogTitle': 'Anonymat Total & Respect de la Vie Privée',
                    'blogP1': 'Nous ne conservons aucun historique ni jeton de session. Vos téléchargements restent confidentiels.',
                    'blogP2': 'Traitement ultra-rapide en mémoire vive sans aucune persistance sur disque dur.'
                },
                {
                    'title': 'Audio MP3 Haute Définition 320 kbps',
                    'desc': f'Convertissez et extrayez la musique et les voix de {p_name} en fichiers MP3 authentiques.',
                    'blogIcon': 'fas fa-headphones',
                    'blogTitle': 'Moteur d’Extraction Audio Instantané',
                    'blogP1': 'Pipeline de transcodage de pointe produisant des fichiers MP3 purs jusqu’à 320 kbps.',
                    'blogP2': 'Parfait pour créer des sonneries, écouter hors ligne et archiver vos bandes-son favorites.'
                }
            ],
            'de': [
                {
                    'title': 'Original HD & 4K Qualität',
                    'desc': f'Laden Sie Medien von {p_name} in nativer Auflösung ohne zusätzliche Kompression herunter.',
                    'blogIcon': 'fas fa-film',
                    'blogTitle': f'Verlustfreie {p_name}-Extraktion',
                    'blogP1': f'Direkte Anbindung an High-Speed-CDN-Server für maximale Bitraten und kristallklare Bildschärfe.',
                    'blogP2': 'Genießen Sie brillante Farben und flüssige Wiedergabe auf all Ihren Endgeräten.'
                },
                {
                    'title': 'Kein Login & 100% Sicher',
                    'desc': 'Völlig ohne Registrierung, Passwörter oder persönliche Daten nutzbar.',
                    'blogIcon': 'fas fa-shield-halved',
                    'blogTitle': 'Vollständige Anonymität & Datenschutz',
                    'blogP1': 'Keine Protokollierung, keine Cookies und keine Verknüpfung mit Benutzerkonten.',
                    'blogP2': 'Alle Datenströme werden flüchtig im RAM verarbeitet und sofort wieder gelöscht.'
                },
                {
                    'title': '320kbps MP3-Audio in Studioqualität',
                    'desc': f'Speichern Sie Sprachnachrichten und Musik aus {p_name} direkt als hochwertige MP3-Dateien.',
                    'blogIcon': 'fas fa-headphones',
                    'blogTitle': 'Echtzeit-Audiotranscodierung',
                    'blogP1': 'Leistungsstarke Audio-Engine konvertiert Videoton in kristallklare MP3-Dateien mit bis zu 320 kbps.',
                    'blogP2': 'Ideal für Klingeltöne, Playlists und das ungestörte Offline-Hören unterwegs.'
                }
            ],
            'hi': [
                {
                    'title': 'मूल HD और 4K गुणवत्ता',
                    'desc': f'{p_name} से बिना किसी अतिरिक्त संपीड़न के मूल उच्च रिज़ॉल्यूशन में वीडियो डाउनलोड करें।',
                    'blogIcon': 'fas fa-film',
                    'blogTitle': f'दोषरहित {p_name} वीडियो डाउनलोड',
                    'blogP1': f'हमारा सर्वर सीधे मूल CDN से जुड़कर हाई-बिटरेट वीडियो स्ट्रीम प्राप्त करता है।',
                    'blogP2': 'सभी स्मार्टफोन, टैबलेट और कंप्यूटर पर बेहतरीन रंग और स्पष्ट फ्रेम रेट का आनंद लें।'
                },
                {
                    'title': 'बिना लॉगिन और 100% सुरक्षित',
                    'desc': 'बिना किसी पासवर्ड, ईमेल या खाता विवरण दर्ज किए पूरी तरह सुरक्षित डाउनलोड करें।',
                    'blogIcon': 'fas fa-shield-halved',
                    'blogTitle': 'पूर्ण गोपनीयता और ज़ीरो-ट्रैकिंग',
                    'blogP1': 'हम आपकी गोपनीयता का पूरा सम्मान करते हैं। कोई डाउनलोड इतिहास या व्यक्तिगत डेटा स्टोर नहीं होता।',
                    'blogP2': 'प्रत्येक अनुरोध मेमोरी में प्रोसेस होता है और डाउनलोड होते ही तुरंत हटा दिया जाता है।'
                },
                {
                    'title': 'स्टूडियो-ग्रेड 320kbps MP3 ऑडियो',
                    'desc': f'{p_name} से संगीत, आवाज और बैकग्राउंड ऑडियो को वास्तविक 320kbps MP3 में बदलें।',
                    'blogIcon': 'fas fa-headphones',
                    'blogTitle': 'रीयल-टाइम MP3 ऑडियो इंजन',
                    'blogP1': 'शक्तिशाली ऑडियो कनवर्टर किसी भी वीडियो से स्पष्ट 320kbps/192kbps MP3 फाइल निकालता है।',
                    'blogP2': 'रिंगटोन, पॉडकास्ट और ऑफलाइन म्यूजिक लाइब्रेरी के लिए एकदम सही विकल्प।'
                }
            ],
            'ar': [
                {
                    'title': 'جودة أصلية فائقة HD و 4K',
                    'desc': f'قم بتنزيل محتوى {p_name} بأعلى دقة أصلية دون أي ضغط إضافي أو تشويش في الصورة.',
                    'blogIcon': 'fas fa-film',
                    'blogTitle': f'استخراج بدون فقدان الجودة لـ {p_name}',
                    'blogP1': f'تتصل خوادمنا مباشرة بشبكات CDN الأصلية لضمان تنزيل الفيديو بأعلى معدل بت ممكن.',
                    'blogP2': 'استمتع بألوان نابضة بالحياة وتشغيل سلس تماماً على الهاتف أو الحاسوب.'
                },
                {
                    'title': 'بدون تسجيل دخول وخاص بنسبة 100%',
                    'desc': 'حمل بكل حرية وأمان دون الحاجة لإدخال أي كلمات مرور أو بريد إلكتروني أو بيانات شخصية.',
                    'blogIcon': 'fas fa-shield-halved',
                    'blogTitle': 'حماية مطلقة للخصوصية وبدون تتبع',
                    'blogP1': 'نحن نحترم خصوصيتك بالكامل. لا نقوم بتسجيل أي سجلات تنزيل أو معرّفات مستخدمين.',
                    'blogP2': 'تتم معالجة الروابط في الذاكرة العشوائية وتُحذف فوراً بعد انتهاء عملية التحميل.'
                },
                {
                    'title': 'صوت MP3 نقي بدقة استوديو 320kbps',
                    'desc': f'استخرج المقاطع الموسيقية والتسجيلات الصوتية من {p_name} بصيغة MP3 نقية وعالية الجودة.',
                    'blogIcon': 'fas fa-headphones',
                    'blogTitle': 'محرك تحويل صوتي فوري وفائق السرعة',
                    'blogP1': 'يقوم نظام التحويل بمعالجة الصوت في الوقت الفعلي وإنشاء ملفات MP3 متوافقة مع كل المشغلات.',
                    'blogP2': 'خيار مثالي للنغمات والتسجيلات الصوتية وقوائم التشغيل في وضع عدم الاتصال.'
                }
            ],
            'pt': [
                {
                    'title': 'Qualidade Original HD e 4K',
                    'desc': f'Baixe mídias do {p_name} na resolução original máxima, sem compressão extra ou perda visual.',
                    'blogIcon': 'fas fa-film',
                    'blogTitle': f'Captura de Alta Fidelidade no {p_name}',
                    'blogP1': f'Nossos servidores conectam-se diretamente às fontes oficiais de CDN para entregar streams impecáveis.',
                    'blogP2': 'Aproveite imagens nítidas e cores autênticas em todos os seus dispositivos.'
                },
                {
                    'title': 'Sem Login e 100% Anônimo',
                    'desc': 'Baixe com total liberdade sem precisar cadastrar e-mail, senhas ou vincular contas.',
                    'blogIcon': 'fas fa-shield-halved',
                    'blogTitle': 'Privacidade Blindada e Zero Logs',
                    'blogP1': 'Respeitamos sua privacidade. Nenhum histórico de download ou dado pessoal é armazenado.',
                    'blogP2': 'Todo o fluxo é processado na memória volátil e eliminado imediatamente após o término.'
                },
                {
                    'title': 'Áudio MP3 de Estúdio a 320kbps',
                    'desc': f'Converta e extraia músicas, áudios virais e vozes do {p_name} direto para MP3 cristalino.',
                    'blogIcon': 'fas fa-headphones',
                    'blogTitle': 'Motor de Áudio em Tempo Real',
                    'blogP1': 'Conversão inteligente para MP3 de até 320kbps com excelente definição acústica.',
                    'blogP2': 'Ideal para criar toques de celular, salvar podcasts e ouvir offline quando quiser.'
                }
            ],
            'bn': [
                {
                    'title': 'আসল HD ও ৪K কোয়ালিটি',
                    'desc': f'{p_name} থেকে কোনো অতিরিক্ত কম্প্রেশন ছাড়া আসল পূর্ণ রেজোলিউশনে ভিডিও ডাউনলোড করুন।',
                    'blogIcon': 'fas fa-film',
                    'blogTitle': f'লসলেস {p_name} মিডিয়া এক্সট্র্যাকশন',
                    'blogP1': f'আমাদের সার্ভার সরাসরি মূল সিডিএন-এর সাথে সংযোগ স্থাপন করে উচ্চ বিটরেটের ভিডিও প্রদান করে।',
                    'blogP2': 'যেকোনো মোবাইল বা কম্পিউটারে আসল রঙের উজ্জ্বলতা ও মসৃণ ফ্রেম রেট উপভোগ করুন।'
                },
                {
                    'title': 'লগইন ছাড়া ১০০% নিরাপদ',
                    'desc': 'কোনো পাসওয়ার্ড, ইমেল বা সামাজিক যোগাযোগ অ্যাকাউন্টের তথ্য না দিয়েই অবাধে ডাউনলোড করুন।',
                    'blogIcon': 'fas fa-shield-halved',
                    'blogTitle': 'সম্পূর্ণ গোপনীয়তা ও জিরো ট্র্যাকিং',
                    'blogP1': 'আমরা আপনার গোপনীয়তা রক্ষা করি। কোনো ডাউনলোড ইতিহাস বা ব্যক্তিগত ডেটা রেকর্ড করা হয় না।',
                    'blogP2': 'প্রতিটি লিংক তাৎক্ষণিকভাবে মেমরিতে প্রসেস হয় এবং ডাউনলোড শেষেই সম্পূর্ণ মুছে যায়।'
                },
                {
                    'title': 'স্টুডিও কোয়ালিটি ৩২০kbps MP3',
                    'desc': f'{p_name} থেকে সাউন্ড ট্র্যাক ও ভয়েস ক্লিপ সরাসরি উচ্চমানের ৩২০kbps MP3 অডিওতে রূপান্তর করুন।',
                    'blogIcon': 'fas fa-headphones',
                    'blogTitle': 'রিয়েল-টাইম অডিও কনভার্সন সিস্টেম',
                    'blogP1': 'উন্নত অডিও ইঞ্জিন ভিডিও থেকে পরিষ্কার ৩২০kbps/১৯২kbps MP3 ফাইল নিষ্কাশন করে।',
                    'blogP2': 'অফলাইনে গান শোনা, রিংটোন তৈরি এবং পডকাস্ট সংরক্ষণের জন্য উপযুক্ত।'
                }
            ],
            'ru': [
                {
                    'title': 'Оригинальное качество HD и 4K',
                    'desc': f'Скачивайте видео из {p_name} в исходном разрешении без потери резкости и артефактов.',
                    'blogIcon': 'fas fa-film',
                    'blogTitle': f'Прямой захват потока из {p_name}',
                    'blogP1': f'Наши серверы подключаются напрямую к CDN-узлам для извлечения видео с максимальным битрейтом.',
                    'blogP2': 'Наслаждайтесь сочными цветами и четким изображением на смартфоне, планшете или компьютере.'
                },
                {
                    'title': 'Без авторизации и 100% анонимно',
                    'desc': 'Скачивайте без ввода паролей, личной почты или привязки аккаунтов социальных сетей.',
                    'blogIcon': 'fas fa-shield-halved',
                    'blogTitle': 'Полная конфиденциальность и нулевой сбор данных',
                    'blogP1': 'Мы не отслеживаем активность пользователей и не храним историю скачиваний.',
                    'blogP2': 'Обработка ссылок происходит в оперативной памяти и завершается мгновенным удалением.'
                },
                {
                    'title': 'Студийный звук MP3 320 кбит/с',
                    'desc': f'Конвертируйте треки, голосовые заметки и звуковые дорожки из {p_name} в формат MP3 высокой четкости.',
                    'blogIcon': 'fas fa-headphones',
                    'blogTitle': 'Быстрое транскодирование звука',
                    'blogP1': 'Мощный встроенный аудиоконвертер извлекает чистый звук с битрейтом до 320 кбит/с.',
                    'blogP2': 'Отличное решение для создания рингтонов, подкастов и офлайн-плейлистов.'
                }
            ],
            'id': [
                {
                    'title': 'Kualitas Asli HD & 4K',
                    'desc': f'Unduh media {p_name} dalam resolusi asli tanpa kompresi berlebih atau penurunan kualitas.',
                    'blogIcon': 'fas fa-film',
                    'blogTitle': f'Ekstraksi Tanpa Penurunan Kualitas {p_name}',
                    'blogP1': f'Terhubung langsung ke CDN asal untuk mengambil aliran video dengan bitrate tertinggi.',
                    'blogP2': 'Nikmati ketajaman visual dan warna alami di semua perangkat pemutar media Anda.'
                },
                {
                    'title': 'Tanpa Login & 100% Privat',
                    'desc': 'Unduh sepuasnya tanpa perlu memasukkan kata sandi, email, atau kredensial akun.',
                    'blogIcon': 'fas fa-shield-halved',
                    'blogTitle': 'Anonimitas Penuh Tanpa Riwayat Log',
                    'blogP1': 'Privasi Anda terjaga sepenuhnya. Kami tidak mencatat histori unduhan atau data pengguna.',
                    'blogP2': 'Semua pemrosesan berlangsung sementara di memori RAM dan langsung dihapus setelah selesai.'
                },
                {
                    'title': 'Audio Studio MP3 320kbps',
                    'desc': f'Ekstrak musik, suara latar, dan klip percakapan dari {p_name} langsung ke format MP3 jernih.',
                    'blogIcon': 'fas fa-headphones',
                    'blogTitle': 'Mesin Konversi Audio Real-Time',
                    'blogP1': 'Sistem pemrosesan audio canggih menghasilkan file MP3 berkualitas tinggi hingga 320kbps.',
                    'blogP2': 'Sangat pas untuk nada dering, koleksi musik offline, dan rekaman suara penting.'
                }
            ],
            'zh': [
                {
                    'title': '原始 1080p 与 4K 超清画质',
                    'desc': f'无损提取 {p_name} 原生高分辨率媒体，杜绝任何额外二次压缩与画质失真模糊。',
                    'blogIcon': 'fas fa-film',
                    'blogTitle': f'全保真 {p_name} 流媒体直链捕获',
                    'blogP1': f'直连各大平台官方顶级 CDN 边缘加速节点，瞬时捕获未经重编码的高码率纯净视频流。',
                    'blogP2': '完美呈现色彩细腻、帧率稳定的高清画面，无论是手机还是电脑屏幕均清晰无匹。'
                },
                {
                    'title': '免登录账号且 100% 匿名安全',
                    'desc': '无需输入任何个人密码、不绑定账号凭据、不索取敏感权限，纯净直链下载。',
                    'blogIcon': 'fas fa-shield-halved',
                    'blogTitle': '零留痕隐私防御体系与去中心化设计',
                    'blogP1': '我们严守用户个人数据安全底线，不记录解析历史、不写入追踪型 Cookies。',
                    'blogP2': '所有请求均在易失性高速 RAM 内存中微秒级流转，数据提取完毕后立即彻底粉碎。'
                },
                {
                    'title': '录音室级 320kbps MP3 原声提取',
                    'desc': f'一键将 {p_name} 中的配乐旋律、热门音频与原声朗读转码提取为纯正 MP3 音乐。',
                    'blogIcon': 'fas fa-headphones',
                    'blogTitle': '毫秒级高保真音频转码引擎',
                    'blogP1': '搭载工业级实时转码架构，完美抽离独立音频轨道并生成最高 320kbps 的纯正 MP3。',
                    'blogP2': '无论用于车载播放、手机铃声制作还是离线播客收听，均可获得绝佳听觉享受。'
                }
            ],
            'ur': [
                {
                    'title': 'اصل HD اور 4K کوالٹی',
                    'desc': f'{p_name} سے بغیر کسی اضافی کمپریشن کے اصل ہائی ریزولوشن میں ویڈیوز ڈاؤن لوڈ کریں۔',
                    'blogIcon': 'fas fa-film',
                    'blogTitle': f'نقصان کے بغیر {p_name} ویڈیو ڈاؤن لوڈنگ',
                    'blogP1': f'ہمارا سرور براہ راست اصل سی ڈی این سے منسلک ہو کر ہائی بٹ ریٹ ویڈیوز فراہم کرتا ہے۔',
                    'blogP2': 'تمام اسمارٹ فونز، ٹیبلیٹس اور کمپیوٹرز پر بہترین رنگوں اور فریم ریٹ کا لطف اٹھائیں۔'
                },
                {
                    'title': 'بغیر لاگ ان اور 100% محفوظ',
                    'desc': 'کسی بھی پاس ورڈ، ای میل یا اکاؤنٹ کی تفصیلات کے بغیر مکمل طور پر محفوظ طریقے سے ڈاؤن لوڈ کریں۔',
                    'blogIcon': 'fas fa-shield-halved',
                    'blogTitle': 'مکمل رازداری اور زیرو ٹریکنگ',
                    'blogP1': 'ہم آپ کی رازداری کا مکمل احترام کرتے ہیں۔ کوئی ڈاؤن لوڈ ہسٹری محفوظ نہیں کی جاتی۔',
                    'blogP2': 'ہر درخواست میموری میں پراسیس ہوتی ہے اور ڈاؤن لوڈ ہوتے ہی فوری طور پر مٹا دی جاتی ہے۔'
                },
                {
                    'title': 'اسٹوڈیو گریڈ 320kbps MP3 آڈیو',
                    'desc': f'{p_name} سے میوزک، آواز اور بیک گراؤنڈ آڈیو کو حقیقی 320kbps MP3 میں تبدیل کریں۔',
                    'blogIcon': 'fas fa-headphones',
                    'blogTitle': 'رئیل ٹائم MP3 آڈیو انجن',
                    'blogP1': 'جدید آڈیو کنورٹر کسی بھی ویڈیو سے صاف شفاف 320kbps/192kbps MP3 فائل نکالتا ہے۔',
                    'blogP2': 'رنگ ٹونز، پوڈکاسٹ اور آف لائن میوزک کے لیے ایک بہترین انتخاب۔'
                }
            ]
        }
        return f_map.get(lang, f_map['en'])

    # How-To Guide in 12 languages
    def get_howto():
        p_name = specs[platform_id]['name']
        h_map = {
            'it': {
                'title': f'Come Scaricare Video e Audio da {p_name} Online',
                'steps': [
                    {'title': f'Passo 1: Copia il link del video da {p_name}', 'desc': f'Apri {p_name}, trova il video che desideri salvare, tocca Condividi e seleziona "Copia link".', 'bullet': 'Il link è ora salvato negli appunti del tuo dispositivo.'},
                    {'title': 'Passo 2: Incolla il link nel nostro downloader', 'desc': 'Torna su downsocial.net e incolla il link copiato nella casella in alto.', 'bullet': 'Il nostro motore individua immediatamente la piattaforma e analizza il flusso.'},
                    {'title': 'Passo 3: Fai clic su "Scarica Video"', 'desc': 'Premi il pulsante per avviare l\'analisi immediata del contenuto multimediale.', 'bullet': 'Le opzioni di qualità disponibili appariranno a schermo in pochi secondi.'},
                    {'title': 'Passo 4: Scegli il tuo formato (HD MP4 o MP3 a 320kbps)', 'desc': 'Seleziona "Video (HD)" per 1080p/4K oppure "Audio (HQ MP3)" per estrarre solo la traccia sonora.', 'bullet': 'Nessun watermark aggiunto e massima qualità originale.'}
                ],
                'hidden': [
                    {'title': 'Passo 5: Salva il file sul tuo dispositivo', 'desc': 'Il file verrà scaricato direttamente nella memoria del tuo smartphone o computer.', 'bullets': ['Android: Si salva direttamente nella cartella Download o nella Galleria.', 'iPhone/iPad: Apri i download di Safari, tocca Condividi e seleziona "Salva video".', 'PC o Mac: Il file si salva nella tua cartella Download predefinita.'], 'tip': f'Consiglio: Puoi scaricare video illimitati da {p_name} 24/7 senza alcuna restrizione.'}
                ]
            },

            'en': {
                'title': f'How to Download Videos & Audio from {p_name} Online',
                'steps': [
                    {'title': f'Step 1: Copy the {p_name} video link', 'desc': f'Open {p_name}, find the video or clip you wish to save, tap Share, and choose "Copy Link".', 'bullet': 'The exact link is now saved to your device clipboard.'},
                    {'title': 'Step 2: Paste the URL into our downloader', 'desc': 'Navigate back to downsocial.net and paste the copied link into the input field above.', 'bullet': 'Our smart engine instantly parses the URL and locates the media stream.'},
                    {'title': 'Step 3: Click "Download Video"', 'desc': 'Click the vibrant download button to initiate media analysis.', 'bullet': 'Available video resolutions and audio options appear in seconds.'},
                    {'title': 'Step 4: Select your format (HD MP4 or 320kbps MP3)', 'desc': 'Choose "Video (HD)" for pristine 1080p/4K video or "Audio (HQ MP3)" for the standalone soundtrack.', 'bullet': 'Zero watermarks and zero visual compression added.'}
                ],
                'hidden': [
                    {'title': 'Step 5: Save directly to your phone or computer', 'desc': 'Your browser will prompt you to download the file directly into your storage.', 'bullets': ['Android: File saves straight into your Downloads folder or Gallery.', 'iOS (iPhone/iPad): Open Safari Downloads, tap Share, and select "Save Video".', 'PC & Mac: File saves directly to your default browser downloads folder.'], 'tip': f'Pro Tip: You can download unlimited {p_name} videos and audios 24/7 with zero limits.'}
                ]
            },
            'es': {
                'title': f'Cómo Descargar Videos y Audios de {p_name} en Línea',
                'steps': [
                    {'title': f'Paso 1: Copia el enlace de {p_name}', 'desc': f'Abre {p_name}, busca el video que deseas guardar, toca Compartir y selecciona "Copiar Enlace".', 'bullet': 'El enlace ahora está copiado en el portapapeles de tu dispositivo.'},
                    {'title': 'Paso 2: Pega el enlace en nuestro descargador', 'desc': 'Regresa a downsocial.net y pega el enlace copiado en el campo superior.', 'bullet': 'Nuestro sistema inteligente reconoce el enlace y localiza el stream multimedia.'},
                    {'title': 'Paso 3: Haz clic en "Descargar Video"', 'desc': 'Presiona el botón de descarga para iniciar el análisis instantáneo.', 'bullet': 'Las opciones de calidad aparecerán en pantalla en cuestión de segundos.'},
                    {'title': 'Paso 4: Elige tu formato (HD MP4 o MP3 a 320kbps)', 'desc': 'Selecciona "Video (HD)" para 1080p/4K o "Audio (HQ MP3)" si solo deseas la pista sonora.', 'bullet': 'Descarga limpia, sin marcas de agua y en máxima calidad.'}
                ],
                'hidden': [
                    {'title': 'Paso 5: Guarda el archivo en tu dispositivo', 'desc': 'El navegador descargará el archivo directamente en la memoria de tu equipo.', 'bullets': ['Android: Se guarda directamente en tu Galería o carpeta Descargas.', 'iPhone/iPad: Abre las descargas de Safari, toca Compartir y presiona "Guardar Video".', 'PC o Mac: El archivo se guarda en tu carpeta predeterminada de descargas.'], 'tip': f'Consejo Pro: Puedes descargar videos ilimitados de {p_name} sin restricciones de uso.'}
                ]
            },
            'fr': {
                'title': f'Comment Télécharger des Vidéos et Audios depuis {p_name}',
                'steps': [
                    {'title': f'Étape 1 : Copiez le lien de la vidéo {p_name}', 'desc': f'Ouvrez {p_name}, trouvez la vidéo désirée, cliquez sur Partager puis sur "Copier le lien".', 'bullet': 'Le lien est maintenant copié dans votre presse-papiers.'},
                    {'title': 'Étape 2 : Collez le lien dans notre outil', 'desc': 'Revenez sur downsocial.net et collez l’URL dans le champ de saisie ci-dessus.', 'bullet': 'Notre moteur identifie automatiquement la source et prépare l’extraction.'},
                    {'title': 'Étape 3 : Cliquez sur "Télécharger la Vidéo"', 'desc': 'Appuyez sur le bouton pour lancer l’analyse du flux multimédia.', 'bullet': 'Les formats disponibles s’affichent instantanément.'},
                    {'title': 'Étape 4 : Choisissez votre format (HD MP4 ou MP3 320 kbps)', 'desc': 'Sélectionnez "Vidéo (HD)" pour une qualité 1080p/4K ou "Audio (HQ MP3)" pour la piste son.', 'bullet': 'Zéro logo, zéro filigrane et une qualité préservée.'}
                ],
                'hidden': [
                    {'title': 'Étape 5 : Enregistrez le fichier sur votre appareil', 'desc': 'Le fichier est directement transféré dans le stockage de votre smartphone ou ordinateur.', 'bullets': ['Android : Enregistré directement dans votre Galerie ou le dossier Téléchargements.', 'iPhone/iPad : Ouvrez les téléchargements Safari, touchez Partager puis "Enregistrer la vidéo".', 'PC & Mac : Le fichier se trouve dans le dossier de téléchargement habituel.'], 'tip': f'Astuce : Téléchargements illimités et 100% gratuits 24h/24 pour {p_name}.'}
                ]
            },
            'de': {
                'title': f'So laden Sie Videos & Audio von {p_name} online herunter',
                'steps': [
                    {'title': f'Schritt 1: {p_name}-Videolink kopieren', 'desc': f'Öffnen Sie {p_name}, wählen Sie das gewünschte Video aus, tippen Sie auf Teilen und dann auf "Link kopieren".', 'bullet': 'Der Link befindet sich nun in Ihrer Zwischenablage.'},
                    {'title': 'Schritt 2: Link in den Downloader einfügen', 'desc': 'Gehen Sie auf downsocial.net und fügen Sie die URL in das Suchfeld oben ein.', 'bullet': 'Unsere Engine erkennt den Link automatisch und lokalisiert die Datei.'},
                    {'title': 'Schritt 3: Auf "Video Herunterladen" klicken', 'desc': 'Klicken Sie auf den Button, um die Analyse des Streams zu starten.', 'bullet': 'Die Download-Optionen erscheinen in Sekundenschnelle auf dem Bildschirm.'},
                    {'title': 'Schritt 4: Format wählen (HD MP4 oder 320kbps MP3)', 'desc': 'Wählen Sie "Video (HD)" für maximale Schärfe oder "Audio (HQ MP3)" für die reine Musikspur.', 'bullet': 'Ohne störende Wasserzeichen und in voller Originalauflösung.'}
                ],
                'hidden': [
                    {'title': 'Schritt 5: Datei auf Ihrem Gerät speichern', 'desc': 'Die Datei wird direkt in Ihrem Speicher abgelegt.', 'bullets': ['Android: Speichert direkt in Ihrer Galerie oder im Download-Ordner.', 'iPhone/iPad: In Safari-Downloads auf Teilen tippen und "Video sichern" wählen.', 'PC & Mac: Die Datei landet in Ihrem Standard-Downloadordner.'], 'tip': f'Profi-Tipp: Sie können unbegrenzt viele {p_name}-Videos kostenlos herunterladen.'}
                ]
            },
            'hi': [
                # Will build cleanly
            ],
            'ar': [
                # Will build cleanly
            ],
            'pt': [
                # Will build cleanly
            ],
            'bn': [
                # Will build cleanly
            ],
            'ru': [
                # Will build cleanly
            ],
            'id': [
                # Will build cleanly
            ],
            'zh': [
                # Will build cleanly
            ],
            'ur': [
                # Will build cleanly
            ]
        }
        # Provide rich universal translations for the remaining languages
        if lang == 'hi':
            return {
                'title': f'{p_name} से ऑनलाइन वीडियो और ऑडियो डाउनलोड कैसे करें',
                'steps': [
                    {'title': f'चरण 1: {p_name} वीडियो का लिंक कॉपी करें', 'desc': f'{p_name} खोलें, जो वीडियो आप सहेजना चाहते हैं उसे खोजें, शेयर पर टैप करें और "लिंक कॉपी करें" चुनें।', 'bullet': 'लिंक अब आपके डिवाइस के क्लिपबोर्ड पर कॉपी हो गया है।'},
                    {'title': 'चरण 2: लिंक को हमारे डाउनलोडर में पेस्ट करें', 'desc': 'downsocial.net पर आएं और कॉपी किए गए लिंक को ऊपर दिए गए बॉक्स में पेस्ट करें।', 'bullet': 'हमारा टूल तुरंत लिंक की पहचान कर लेता है।'},
                    {'title': 'चरण 3: "वीडियो डाउनलोड करें" पर क्लिक करें', 'desc': 'वीडियो का विश्लेषण शुरू करने के लिए डाउनलोड बटन पर क्लिक करें।', 'bullet': 'उपलब्ध गुणवत्ता विकल्प तुरंत स्क्रीन पर दिखाई देंगे।'},
                    {'title': 'चरण 4: अपना फॉर्मेट चुनें (HD MP4 या 320kbps MP3)', 'desc': 'पूर्ण वीडियो के लिए "वीडियो (HD)" या केवल संगीत के लिए "ऑडियो (HQ MP3)" चुनें।', 'bullet': 'बिना किसी वॉटरमार्क के मूल उच्च गुणवत्ता में डाउनलोड।'}
                ],
                'hidden': [
                    {'title': 'चरण 5: वीडियो सीधे अपने डिवाइस में सेव करें', 'desc': 'फ़ाइल सीधे आपके फोन या कंप्यूटर के स्टोरेज में डाउनलोड हो जाएगी।', 'bullets': ['एंड्रॉइड: फ़ाइल सीधे आपकी गैलरी या डाउनलोड फ़ोल्डर में सहेजी जाती है।', 'iPhone/iPad: सफ़ारी डाउनलोड में जाएं, शेयर पर टैप करें और "Save Video" चुनें।', 'कंप्यूटर: फ़ाइल आपके डिफ़ॉल्ट डाउनलोड फ़ोल्डर में सहेजी जाती है।'], 'tip': f'सुझाव: आप {p_name} से बिना किसी सीमा के असीमित वीडियो डाउनलोड कर सकते हैं।'}
                ]
            }
        elif lang == 'ar':
            return {
                'title': f'كيفية تنزيل مقاطع الفيديو والصوتيات من {p_name} أونلاين',
                'steps': [
                    {'title': f'الخطوة 1: انسخ رابط فيديو {p_name}', 'desc': f'افتح {p_name}، واختر الفيديو المطلوب، ثم اضغط على زر المشاركة واختر "نسخ الرابط".', 'bullet': 'تم نسخ الرابط الآن في حافظة جهازك بنجاح.'},
                    {'title': 'الخطوة 2: الصق الرابط في مربع البحث أعلاه', 'desc': 'عد إلى موقع downsocial.net والصق الرابط في المكان المخصص بالأعلى.', 'bullet': 'يتعرف نظامنا الذكي على الفيديو ومساره في أجزاء من الثانية.'},
                    {'title': 'الخطوة 3: اضغط على زر "تحميل الفيديو"', 'desc': 'انقر على زر التنزيل لبدء فحص خيارات الجودة المتاحة.', 'bullet': 'ستظهر أمامك خيارات الفيديو والصوت المناسبة فوراً.'},
                    {'title': 'الخطوة 4: اختر الصيغة المناسبة (HD MP4 أو 320kbps MP3)', 'desc': 'اختر "فيديو عالي الدقة" لمشاهدة الفيديو بالكامل أو "صوت MP3" للاستماع فقط.', 'bullet': 'تنزيل نظيف وخالٍ تماماً من العلامات المائية المزعجة.'}
                ],
                'hidden': [
                    {'title': 'الخطوة 5: احفظ الملف مباشرة في ذاكرة جهازك', 'desc': 'يبدأ التنزيل الفوري وتُحفظ الوسائط مباشرة في مجلد التنزيلات بجهازك.', 'bullets': ['أندرويد: يُحفظ الفيديو مباشرة في المعرض (Gallery) أو التنزيلات.', 'آيفون/آيباد: افتح تنزيلات Safari، اضغط على مشاركة واختر "Save Video".', 'الحاسوب: يُحفظ الملف مباشرة في مجلد التنزيلات الافتراضي لديك.'], 'tip': f'ملاحظة: يمكنك تنزيل عدد غير محدود من فيديوهات {p_name} مجاناً طوال اليوم.'}
                ]
            }
        elif lang == 'pt':
            return {
                'title': f'Como Baixar Vídeos e Áudios do {p_name} Online',
                'steps': [
                    {'title': f'Passo 1: Copie o link do vídeo no {p_name}', 'desc': f'Abra o {p_name}, localize o vídeo que deseja salvar, clique em Compartilhar e selecione "Copiar Link".', 'bullet': 'O endereço da mídia já está na sua área de transferência.'},
                    {'title': 'Passo 2: Cole o link no campo de busca acima', 'desc': 'Acesse downsocial.net e insira a URL copiada no campo principal do topo.', 'bullet': 'Nosso sistema localiza imediatamente o fluxo de mídia correspondente.'},
                    {'title': 'Passo 3: Clique em "Baixar Vídeo"', 'desc': 'Pressione o botão para liberar as resoluções e opções de áudio disponíveis.', 'bullet': 'Os botões de formato serão exibidos em poucos segundos.'},
                    {'title': 'Passo 4: Escolha o formato (HD MP4 ou MP3 a 320kbps)', 'desc': 'Opte por "Vídeo (HD)" para imagem nítida ou "Áudio (HQ MP3)" para a trilha sonora.', 'bullet': 'Sem logos indesejados e mantendo a taxa de bits nativa.'}
                ],
                'hidden': [
                    {'title': 'Passo 5: Salve o arquivo em seu celular ou PC', 'desc': 'O download será concluído e gravado direto no armazenamento do seu dispositivo.', 'bullets': ['Android: O arquivo vai direto para a Galeria ou pasta Downloads.', 'iPhone/iPad: No Safari, toque na lista de downloads, selecione Compartilhar e "Salvar Vídeo".', 'Computador: O vídeo é salvo na sua pasta padrão de downloads.'], 'tip': f'Dica: Baixe quantos vídeos e músicas do {p_name} quiser, sem limite de uso.'}
                ]
            }
        elif lang == 'bn':
            return {
                'title': f'কীভাবে {p_name} থেকে ভিডিও এবং অডিও ডাউনলোড করবেন',
                'steps': [
                    {'title': f'ধাপ ১: {p_name} ভিডিও লিংক কপি করুন', 'desc': f'{p_name} ওপেন করে পছন্দের ভিডিওটিতে যান, শেয়ার বাটনে চাপ দিন এবং "Copy Link" নির্বাচন করুন।', 'bullet': 'লিংকটি আপনার ডিভাইসের ক্লিপবোর্ডে কপি হয়ে গেছে।'},
                    {'title': 'ধাপ ২: আমাদের ওয়েবসাইটে লিংকটি পেস্ট করুন', 'desc': 'downsocial.net-এ ফিরে এসে উপরের সার্চ বক্সে লিংকটি পেস্ট করে দিন।', 'bullet': 'আমাদের বুদ্ধিমান সিস্টেম মুহূর্তের মধ্যে লিংকটি শনাক্ত করে ফেলে।'},
                    {'title': 'ধাপ ৩: "ভিডিও ডাউনলোড করুন" বাটনে ক্লিক করুন', 'desc': 'ভিডিওর গুণমান ও অপশন দেখতে ডাউনলোড বাটনে ক্লিক করুন।', 'bullet': 'কয়েক সেকেন্ডের মধ্যেই ডাউনলোডের বোতামগুলো পর্দায় চলে আসবে।'},
                    {'title': 'ধাপ ৪: আপনার পছন্দের ফরম্যাট বেছে নিন (HD MP4 বা ৩২০kbps MP3)', 'desc': 'পূর্ণ ভিডিওর জন্য "ভিডিও (HD)" অথবা সাউন্ডট্র্যাকের জন্য "অডিও (HQ MP3)" চাপুন।', 'bullet': 'কোনো ওয়াটারমার্ক ছাড়া সম্পূর্ণ আসল রেজোলিউশনে সেভ হবে।'}
                ],
                'hidden': [
                    {'title': 'ধাপ ৫: সরাসরি আপনার ডিভাইসে ফাইলটি সেভ করুন', 'desc': 'ফাইলটি কোনো ঝামেলা ছাড়াই আপনার ফোন বা পিসির ড্রাইভে সেভ হয়ে যাবে।', 'bullets': ['অ্যান্ড্রয়েড: ফাইলটি সরাসরি আপনার গ্যালারি বা ডাউনলোড ফোল্ডারে পাওয়া যাবে।', 'আইফোন/আইপ্যাড: সাফারি ডাউনলোডে গিয়ে শেয়ার আইকনে চাপ দিয়ে "Save Video" চাপুন।', 'কম্পিউটার: ব্রাউজারের নিজস্ব ডাউনলোড ডিরেক্টরিতে ফাইলটি জমা হবে।'], 'tip': f'টিপস: আপনি প্রতিদিন যত খুশি তত {p_name} ভিডিও ও গান সম্পূর্ণ বিনামূল্যে নামাতে পারবেন।'}
                ]
            }
        elif lang == 'ru':
            return {
                'title': f'Как скачать видео и аудио из {p_name} онлайн',
                'steps': [
                    {'title': f'Шаг 1: Скопируйте ссылку на видео в {p_name}', 'desc': f'Откройте {p_name}, найдите нужное видео, нажмите «Поделиться» и выберите «Копировать ссылку».', 'bullet': 'Ссылка успешно скопирована в буфер обмена.'},
                    {'title': 'Шаг 2: Вставьте ссылку в поле загрузчика', 'desc': 'Перейдите на downsocial.net и вставьте ссылку в поисковую строку выше.', 'bullet': 'Система моментально найдет источник видеопотока.'},
                    {'title': 'Шаг 3: Нажмите кнопку «Скачать видео»', 'desc': 'Нажмите кнопку для мгновенного анализа форматов и разрешений.', 'bullet': 'Доступные форматы загрузки появятся на экране за пару секунд.'},
                    {'title': 'Шаг 4: Выберите формат (HD MP4 или MP3 320 кбит/с)', 'desc': 'Выберите «Видео (HD)» для качества 1080p/4K или «Аудио (HQ MP3)» для музыки.', 'bullet': 'Файл будет загружен без водяных знаков и логотипов.'}
                ],
                'hidden': [
                    {'title': 'Шаг 5: Сохраните файл на смартфон или ПК', 'desc': 'Видео сохранится непосредственно в память вашего устройства.', 'bullets': ['Android: Файл попадает сразу в Галерею или папку «Загрузки».', 'iPhone/iPad: В Safari откройте список загрузок, нажмите «Поделиться» и «Сохранить видео».', 'Компьютер: Файл сохранится в стандартную папку загрузок браузера.'], 'tip': f'Совет: Количество скачиваний видео и музыки из {p_name} ничем не ограничено.'}
                ]
            }
        elif lang == 'id':
            return {
                'title': f'Cara Mengunduh Video & Audio dari {p_name} Secara Online',
                'steps': [
                    {'title': f'Langkah 1: Salin tautan video {p_name}', 'desc': f'Buka {p_name}, temukan video yang ingin disimpan, pilih opsi Bagikan lalu klik "Salin Tautan".', 'bullet': 'Tautan kini tersimpan di papan klip perangkat Anda.'},
                    {'title': 'Langkah 2: Tempel tautan pada kolom di atas', 'desc': 'Kembali ke downsocial.net dan tempel tautan pada bilah pencarian.', 'bullet': 'Sistem otomatis memeriksa tautan dan menyiapkan media.'},
                    {'title': 'Langkah 3: Klik tombol "Unduh Video"', 'desc': 'Tekan tombol unduh untuk melihat pilihan resolusi video dan audio.', 'bullet': 'Opsi format akan muncul dalam hitungan detik.'},
                    {'title': 'Langkah 4: Pilih format yang diinginkan (HD MP4 atau MP3 320kbps)', 'desc': 'Pilih "Video (HD)" untuk visual tajam atau "Audio (HQ MP3)" untuk trek suara saja.', 'bullet': 'Hasil bersih tanpa tanda air dan mempertahankan kejernihan asli.'}
                ],
                'hidden': [
                    {'title': 'Langkah 5: Simpan file ke perangkat Anda', 'desc': 'File akan diunduh dan tersimpan ke penyimpanan lokal Anda.', 'bullets': ['Android: Tersimpan langsung di Galeri atau folder Unduhan Anda.', 'iPhone/iPad: Buka unduhan Safari, tekan ikon Bagikan lalu pilih "Simpan Video".', 'PC & Mac: File tersimpan di folder unduhan default peramban Anda.'], 'tip': f'Tips Pro: Unduh video dan audio dari {p_name} sepuasnya tanpa batasan kuota harian.'}
                ]
            }
        elif lang == 'zh':
            return {
                'title': f'如何在线高速下载 {p_name} 高清视频与提取 MP3 原声',
                'steps': [
                    {'title': f'步骤 1：复制 {p_name} 目标多媒体链接', 'desc': f'打开 {p_name} 客户端或网页端，找到想保存的内容，点击“分享”并选择“复制链接”。', 'bullet': '该媒体的唯一网络链接已安全存入您的剪贴板中。'},
                    {'title': '步骤 2：将链接粘贴至上方解析搜索框', 'desc': '返回 downsocial.net 首页，将刚才复制的链接完整粘贴在顶部的输入框中。', 'bullet': '本站智能路由引擎将毫秒级匹配解析该平台的官方媒体流节点。'},
                    {'title': '步骤 3：点击“下载视频”按钮启动解析', 'desc': '轻触醒目的下载按钮，服务器将实时探测源端所支持的最高分辨率和音频规格。', 'bullet': '数秒内即可在下方调出专属的多画质下载按钮。'},
                    {'title': '步骤 4：选取理想规格（1080p/4K MP4 或 320kbps MP3）', 'desc': '需要完整画面请选“高清视频 (HD)”，若仅需背景原声则选“高品质音频 (HQ MP3)”。', 'bullet': '100% 保留原生超清画质与纯净立体声，杜绝任何水印。'}
                ],
                'hidden': [
                    {'title': '步骤 5：直接保存至您的手机相册或电脑磁盘', 'desc': '文件将通过超高速通道直接保存至本地硬件介质中。', 'bullets': ['Android 安卓设备：下载后直接保存在“下载内容”或系统“相册/相册集”中。', 'iOS 苹果设备：Safari 下载完成后轻点分享图标，选择“存储视频”即可存入照片 App。', 'Windows / Mac 电脑：自动保存在您浏览器的默认下载文件目录中。'], 'tip': f'进阶技巧：本站提供全年 365 天无限制免费解析，随心提取任意 {p_name} 媒体。'}
                ]
            }
        elif lang == 'ur':
            return {
                'title': f'{p_name} سے آن لائن ویڈیوز اور آڈیو ڈاؤن لوڈ کرنے کا طریقہ',
                'steps': [
                    {'title': f'مرحلہ 1: {p_name} ویڈیو کا لنک کاپی کریں', 'desc': f'{p_name} ایپ کھولیں، اپنی پسندیدہ ویڈیو تلاش کریں، شیئر پر کلک کریں اور "Copy Link" منتخب کریں۔', 'bullet': 'ویڈیو کا لنک آپ کے فون کے کلپ بورڈ میں محفوظ ہو چکا ہے۔'},
                    {'title': 'مرحلہ 2: لنک کو ہمارے ڈاؤنلوڈر میں پیسٹ کریں', 'desc': 'downsocial.net پر واپس آئیں اور اوپر موجود باکس میں کاپی کیا ہوا لنک پیسٹ کریں۔', 'bullet': 'ہماری ویب سائٹ سیکنڈوں میں لنک کی تصدیق کر لیتی ہے۔'},
                    {'title': 'مرحلہ 3: "ویڈیو ڈاؤن لوڈ کریں" کے بٹن پر کلک کریں', 'desc': 'ڈاؤن لوڈ کے بٹن پر کلک کریں تاکہ ویڈیو کا جائزہ لیا جا سکے۔', 'bullet': 'کچھ ہی سیکنڈ میں تمام دستیاب کوالٹی آپشنز سامنے آ جائیں گے۔'},
                    {'title': 'مرحلہ 4: اپنا فارمیٹ منتخب کریں (HD MP4 یا 320kbps MP3)', 'desc': 'مکمل ویڈیو کے لیے "ویڈیو (HD)" یا صرف آواز کے لیے "آڈیو (HQ MP3)" منتخب کریں۔', 'bullet': 'بغیر کسی واٹر مارک یا لوگو کے اصل کوالٹی میں ڈاؤن لوڈنگ۔'}
                ],
                'hidden': [
                    {'title': 'مرحلہ 5: ویڈیو کو اپنے فون یا کمپیوٹر میں محفوظ کریں', 'desc': 'فائل براہ راست آپ کے موبائل یا کمپیوٹر میں محفوظ ہو جائے گی۔', 'bullets': ['اینڈرائیڈ: فائل سیدھی آپ کی گیلری یا ڈاؤن لوڈز فولڈر میں محفوظ ہوتی ہے۔', 'آئی فون: سفاری میں ڈاؤن لوڈ کے بعد شیئر پر ٹیپ کریں اور "Save Video" منتخب کریں۔', 'کمپیوٹر: فائل خودکار طور پر آپ کے ڈاؤن لوڈز فولڈر میں محفوظ ہو جاتی ہے۔'], 'tip': f'مشورہ: آپ بغیر کسی حد اور فیس کے {p_name} سے جتنی چاہیں ویڈیوز ڈاؤن لوڈ کر سکتے ہیں۔'}
                ]
            }
        return h_map.get(lang, h_map['en'])

    # FAQs in 12 languages
    def get_faqs():
        p_name = specs[platform_id]['name']
        faq_sets = {
            'it': [
                {'q': f'Scaricare video da {p_name} è sicuro e legale?', 'a': f'Sì, salvare video pubblici da {p_name} per uso personale offline e studio è sicuro e ampiamente consentito.'},
                {'q': f'Il video scaricato avrà filigrane o loghi aggiunti?', 'a': f'Assolutamente no! downsocial estrae il video originale direttamente dal CDN senza inserire alcun logo.'},
                {'q': f'Posso convertire i video di {p_name} in file audio MP3?', 'a': f'Certamente! Incolla il link e seleziona "Audio (HQ MP3)" per ottenere un file MP3 puro fino a 320kbps.'},
                {'q': f'Devo installare qualche programma o app sul dispositivo?', 'a': f'Non occorre installare nulla. downsocial funziona direttamente in qualsiasi browser moderno.'},
                {'q': f'L\'autore del video saprà che l\'ho scaricato?', 'a': f'No. L\'elaborazione è totalmente anonima e non invia alcuna notifica o avviso al creatore del video.'},
                {'q': f'Esiste un limite al numero di download giornalieri?', 'a': f'Nessun limite! Puoi scaricare tutti i video e gli audio che desideri in modo gratuito e illimitato.'}
            ],

            'en': [
                {'q': f'Is downloading videos from {p_name} legal and safe?', 'a': f'Yes. Downloading public media from {p_name} for personal offline viewing and educational fair use is 100% legal. downsocial uses SSL encryption and zero tracking.'},
                {'q': f'Will downloaded {p_name} videos have a watermark or logo?', 'a': f'No! downsocial extracts the original clean stream directly from the CDN. There are zero watermarks, logos, or overlay stamps added.'},
                {'q': f'Can I convert {p_name} videos into MP3 audio files?', 'a': f'Yes! Simply paste your {p_name} link and click "Audio (HQ MP3)". Our built-in FFmpeg transcoders extract crystal-clear 320kbps/192kbps MP3 files.'},
                {'q': f'Do I need to install any software or mobile app?', 'a': f'No installation is required. downsocial operates 100% online through your browser on iPhone, Android, Mac, Windows, and Linux.'},
                {'q': f'Does the creator of the {p_name} video know that I saved it?', 'a': f'No. Because downsocial accesses public CDN delivery streams anonymously, the creator receives zero notifications, alerts, or screenshot warnings.'},
                {'q': f'Are there download limits or daily caps?', 'a': f'No! downsocial offers 100% free, unlimited downloads without subscriptions, registrations, or throttling.'}
            ],
            'es': [
                {'q': f'¿Es legal y seguro descargar videos de {p_name}?', 'a': f'Sí. Guardar videos públicos de {p_name} para uso personal y archivo privado sin fines de lucro es legal y completamente seguro con downsocial.'},
                {'q': f'¿Los videos descargados de {p_name} tienen marca de agua?', 'a': f'¡No! downsocial obtiene el archivo original directo del servidor de origen, garantizando una descarga limpia sin sellos ni logotipos añadidos.'},
                {'q': f'¿Puedo convertir videos de {p_name} a formato MP3?', 'a': f'¡Por supuesto! Pega tu enlace y presiona "Audio (HQ MP3)" para obtener archivos de audio limpios y en alta tasa de bits.'},
                {'q': f'¿Necesito instalar algún programa o aplicación en mi celular?', 'a': f'No necesitas instalar nada. downsocial funciona totalmente en la nube desde cualquier navegador web moderno.'},
                {'q': f'¿El autor del video de {p_name} sabrá que lo descargué?', 'a': f'No. La descarga se procesa de forma anónima sin avisar al creador ni enviar alertas de captura de pantalla.'},
                {'q': f'¿Existe algún límite diario de descargas?', 'a': f'¡Ninguno! Puedes descargar tantos videos y canciones de {p_name} como desees sin ningún tipo de costo.'}
            ],
            'fr': [
                {'q': f'Est-il légal et sûr de télécharger des vidéos {p_name} ?', 'a': f'Oui. Télécharger des vidéos publiques de {p_name} pour une consultation hors ligne personnelle et équitable est légal et entièrement sécurisé.'},
                {'q': f'Les vidéos téléchargées ont-elles un filigrane ou un logo ?', 'a': f'Non ! downsocial récupère le fichier source propre sans jamais ajouter de filigrane, de logo ou de tampon publicitaire.'},
                {'q': f'Puis-je convertir les vidéos {p_name} en MP3 ?', 'a': f'Oui ! Collez le lien et cliquez sur "Audio (HQ MP3)" pour extraire une piste son d’une netteté irréprochable jusqu’à 320 kbps.'},
                {'q': f'Faut-il installer un logiciel ou une application ?', 'a': f'Aucune installation n’est requise. Le service s’exécute entièrement dans votre navigateur sur smartphone, tablette ou ordinateur.'},
                {'q': f'Le créateur de la vidéo {p_name} est-il prévenu ?', 'a': f'Non. L’accès au flux est anonyme et ne déclenche aucune notification ni avertissement pour le compte d’origine.'},
                {'q': f'Y a-t-il des limites ou un quota quotidien ?', 'a': f'Non, aucun quota ! downsocial est 100% gratuit et illimité, sans abonnement ni frais cachés.'}
            ],
            'de': [
                {'q': f'Ist das Herunterladen von {p_name}-Videos legal und sicher?', 'a': f'Ja. Das Herunterladen öffentlicher Videos von {p_name} für den privaten Gebrauch und die Offline-Archivierung ist vollkommen legal und sicher.'},
                {'q': f'Haben die heruntergeladenen Videos ein Wasserzeichen?', 'a': f'Nein! downsocial ruft den sauberen Originalstream direkt ab, ohne zusätzliche Wasserzeichen oder störende Einblendungen.'},
                {'q': f'Kann ich {p_name}-Videos als MP3-Audio speichern?', 'a': f'Ja! Fügen Sie den Link ein und klicken Sie auf "Audio (HQ MP3)", um die Tonspur in brillanter 320kbps-Qualität zu speichern.'},
                {'q': f'Muss ich eine zusätzliche App oder Software installieren?', 'a': f'Nein. downsocial funktioniert zu 100% online im Webbrowser auf Smartphones, Tablets und PCs.'},
                {'q': f'Erfährt der Ersteller von dem Download?', 'a': f'Nein. Der Abruf erfolgt völlig anonym ohne Benachrichtigungen oder Screenshot-Meldungen an das Profil.'},
                {'q': f'Gibt es ein tägliches Download-Limit?', 'a': f'Nein! Sie können unbegrenzt viele Videos und Audiodateien von {p_name} kostenlos herunterladen.'}
            ],
            'hi': [
                {'q': f'क्या {p_name} से वीडियो डाउनलोड करना कानूनी और सुरक्षित है?', 'a': f'हाँ, व्यक्तिगत और गैर-व्यावसायिक उपयोग के लिए सार्वजनिक वीडियो डाउनलोड करना पूरी तरह से सुरक्षित और वैध है।'},
                {'q': f'क्या डाउनलोड किए गए वीडियो में कोई वॉटरमार्क होगा?', 'a': f'बिल्कुल नहीं! downsocial सीधे मूल CDN से वीडियो लेता है, इसलिए इसमें कोई भी अतिरिक्त लोगो या वॉटरमार्क नहीं होता।'},
                {'q': f'क्या मैं {p_name} वीडियो को MP3 ऑडियो में बदल सकता हूँ?', 'a': f'हाँ! बस अपना लिंक पेस्ट करें और "ऑडियो (HQ MP3)" पर क्लिक करें। आपको तुरंत 320kbps MP3 ऑडियो फाइल मिल जाएगी।'},
                {'q': f'क्या मुझे कोई ऐप या सॉफ्टवेयर इंस्टॉल करना होगा?', 'a': f'नहीं, किसी ऐप की जरूरत नहीं है। यह वेबसाइट मोबाइल और कंप्यूटर के किसी भी ब्राउज़र में सीधे काम करती है।'},
                {'q': f'क्या वीडियो क्रिएटर को पता चलेगा कि मैंने वीडियो डाउनलोड किया है?', 'a': f'नहीं, यह प्रक्रिया पूरी तरह से गोपनीय है और क्रिएटर को कोई सूचना नहीं भेजी जाती है।'},
                {'q': f'क्या डाउनलोड करने की कोई दैनिक सीमा है?', 'a': f'नहीं! downsocial पूरी तरह से मुफ़्त है और आप जितने चाहें उतने वीडियो डाउनलोड कर सकते हैं।'}
            ],
            'ar': [
                {'q': f'هل تنزيل مقاطع الفيديو من {p_name} قانوني وآمن؟', 'a': f'نعم، تنزيل مقاطع الفيديو العامة من {p_name} للاستخدام الشخصي العادل وغير التجاري آمن وقانوني بنسبة 100%.'},
                {'q': f'هل تحتوي مقاطع الفيديو المحملة على علامات مائية أو شعارات؟', 'a': f'كلا! يقوم downsocial باستخراج ملف المصدر النظيف مباشرة من السحابة دون إضافة أي علامات مائية إطلاقاً.'},
                {'q': f'هل يمكنني تحويل فيديوهات {p_name} إلى ملفات صوتية MP3؟', 'a': f'نعم بكل تأكيد! الصق الرابط واضغط على "صوت (HQ MP3)" لتحميل ملف صوتي عالي النقاء 320kbps.'},
                {'q': f'هل يلزم تثبيت أي برامج أو تطبيقات خارجية؟', 'a': f'لا يلزم تثبيت أي شيء. تعمل الأداة بشكل كامل عبر متصفح الويب في هواتف آيفون وأندرويد وأجهزة الكمبيوتر.'},
                {'q': f'هل يعلم صاحب الفيديو أنني قمت بتحميله؟', 'a': f'كلا، يتم التنزيل بشكل مجهول وآمن تماماً دون إرسال أي إشعار أو تنبيه للناشر.'},
                {'q': f'هل توجد أي حدود يومية للتنزيل؟', 'a': f'لا توجد أي قيود! يمكنك تنزيل عدد لا نهائي من الفيديوهات والصوتيات مجاناً دون اشتراكات.'}
            ],
            'pt': [
                {'q': f'É seguro e permitido baixar vídeos do {p_name}?', 'a': f'Sim. Baixar conteúdos públicos do {p_name} para arquivamento pessoal e uso justo não comercial é seguro e plenamente aceito.'},
                {'q': f'Os vídeos baixados do {p_name} vêm com marca d’água?', 'a': f'Não! O downsocial extrai o arquivo fonte limpo diretamente dos servidores oficiais, sem marcas d’água ou carimbos adicionados.'},
                {'q': f'Consigo converter vídeos do {p_name} para MP3?', 'a': f'Com certeza! Cole o link e clique em "Áudio (HQ MP3)" para salvar o arquivo de som com taxa de até 320kbps.'},
                {'q': f'Preciso instalar algum software ou app no celular?', 'a': f'Não é necessário instalar nada. O downsocial funciona diretamente em navegadores como Chrome, Safari e Edge.'},
                {'q': f'O autor do vídeo fica sabendo que eu baixei?', 'a': f'Não. A solicitação é feita de modo 100% anônimo pelo servidor, sem gerar notificações para o perfil de origem.'},
                {'q': f'Existe algum limite de downloads diários?', 'a': f'Não há limites! Você pode baixar quantos vídeos e músicas quiser, de forma ilimitada e gratuita.'}
            ],
            'bn': [
                {'q': f'{p_name} থেকে ভিডিও ডাউনলোড করা কি নিরাপদ ও বৈধ?', 'a': f'হ্যাঁ, ব্যক্তিগত অফলাইন সংরক্ষণ ও শিক্ষার উদ্দেশ্যে উন্মুক্ত ভিডিও ডাউনলোড করা সম্পূর্ণ নিরাপদ ও বৈধ।'},
                {'q': f'ডাউনলোড করা ভিডিওতে কি কোনো ওয়াটারমার্ক থাকবে?', 'a': f'না! downsocial সরাসরি মূল সার্ভার থেকে ভিডিও সংগ্রহ করে, তাই কোনো বাড়তি লোগো বা ওয়াটারমার্ক যুক্ত হয় না।'},
                {'q': f'আমি কি {p_name} ভিডিওকে MP3 অডিওতে রূপান্তর করতে পারি?', 'a': f'হ্যাঁ! শুধু লিংকটি পেস্ট করে "অডিও (HQ MP3)" অপশনে ক্লিক করুন এবং ৩২০kbps অডিও ফাইলটি নামিয়ে নিন।'},
                {'q': f'আমাকে কি কোনো সফটওয়্যার বা অ্যাপ ইনস্টল করতে হবে?', 'a': f'কোনো অ্যাপ বা সফটওয়্যার লাগবেনা। মোবাইল বা কম্পিউটারের ব্রাউজার থেকেই এটি সরাসরি ব্যবহারযোগ্য।'},
                {'q': f'ভিডিও নির্মাতা কি জানতে পারবেন যে আমি ভিডিওটি সেভ করেছি?', 'a': f'না, ডাউনলোডের প্রক্রিয়া সম্পূর্ণ গোপনীয় হওয়ায় নির্মাতার কাছে কোনো অ্যালার্ট বা নোটিফিকেশন যায় না।'},
                {'q': f'প্রতিদিন ডাউনলোড করার কোনো নির্দিষ্ট সীমা আছে কি?', 'a': f'না, কোনো সীমা নেই! আপনি বিনামূল্যে যত খুশি ভিডিও এবং গান ডাউনলোড করতে পারেন।'}
            ],
            'ru': [
                {'q': f'Законно и безопасно ли скачивать видео из {p_name}?', 'a': f'Да, сохранение общедоступных видеороликов из {p_name} для личного некоммерческого просмотра абсолютно законно и безопасно.'},
                {'q': f'Будет ли на видео водяной знак или логотип?', 'a': f'Нет! downsocial извлекает чистый видеопоток напрямую из CDN без добавления каких-либо логотипов.'},
                {'q': f'Можно ли конвертировать видео из {p_name} в MP3?', 'a': f'Да! Просто вставьте ссылку и нажмите «Аудио (HQ MP3)», чтобы скачать чистую аудиодорожку 320 кбит/с.'},
                {'q': f'Нужно ли устанавливать программы или расширения?', 'a': f'Установка не требуется. Сервис работает онлайн в любом браузере на телефонах и компьютерах.'},
                {'q': f'Узнает ли автор видео о том, что я его скачал?', 'a': f'Нет, загрузка происходит абсолютно анонимно, без отправки уведомлений автору публикации.'},
                {'q': f'Есть ли ограничения на количество скачиваний?', 'a': f'Никаких ограничений нет! Сервис downsocial полностью бесплатен для неограниченного использования.'}
            ],
            'id': [
                {'q': f'Apakah mengunduh video dari {p_name} aman dan legal?', 'a': f'Ya, mengunduh konten publik dari {p_name} untuk keperluan pribadi dan arsip offline sepenuhnya aman dan legal.'},
                {'q': f'Apakah video unduhan akan memiliki tanda air?', 'a': f'Tidak! downsocial mengambil sumber video murni langsung dari CDN tanpa tambahan logo atau tanda air apa pun.'},
                {'q': f'Bisakah saya mengubah video {p_name} menjadi file audio MP3?', 'a': f'Bisa! Cukup tempel tautan lalu klik tombol "Audio (HQ MP3)" untuk mengunduh audio jernih hingga 320kbps.'},
                {'q': f'Apakah saya harus memasang aplikasi tambahan?', 'a': f'Tidak perlu aplikasi apa pun. downsocial beroperasi penuh melalui peramban web di semua jenis perangkat.'},
                {'q': f'Apakah pemilik video tahu bahwa saya mengunduh kontennya?', 'a': f'Tidak. Proses unduhan berlangsung anonim tanpa mengirimkan notifikasi apa pun kepada pemilik akun.'},
                {'q': f'Apakah ada batasan jumlah unduhan harian?', 'a': f'Sama sekali tidak ada batasan! Anda bebas mengunduh media dari {p_name} sebanyak yang Anda mau secara gratis.'}
            ],
            'zh': [
                {'q': f'从 {p_name} 下载视频是否安全且合规？', 'a': f'完全安全合规。将公开共享的多媒体内容用于个人离线学习、旅行归档及非商业性合理使用受普遍支持，且本站受 SSL 安全防护。'},
                {'q': f'下载后的 {p_name} 视频是否包含平台水印或多余 Logo？', 'a': f'绝无任何水印！downsocial 直接从源端 CDN 抽取干净的原始媒体流，呈现 100% 纯净的原画视频。'},
                {'q': f'能否将 {p_name} 视频独立转码提取为 MP3 音频文件？', 'a': f'当然支持！只需粘贴链接并点击“高品质音频 (HQ MP3)”，即可毫秒级转码并获取最高 320kbps 的纯正 MP3。'},
                {'q': f'是否需要额外安装第三方应用或浏览器插件？', 'a': f'完全无需安装任何应用或客户端。支持在 iPhone、安卓手机、Mac 与 PC 浏览器的原生环境中即开即用。'},
                {'q': f'{p_name} 原作者会察觉或收到视频被保存的系统通知吗？', 'a': f'绝不会。解析请求由服务端直接与公共媒体流节点握手，全程高度匿名，绝不向原作者发送提醒或截图警告。'},
                {'q': f'平台每日是否有解析频次或下载额度限制？', 'a': f'绝无任何限制！downsocial 面向全球互联网用户永久提供 100% 免费、不限次数的高速解析服务。'}
            ],
            'ur': [
                {'q': f'کیا {p_name} سے ویڈیو ڈاؤن لوڈ کرنا قانونی اور محفوظ ہے؟', 'a': f'جی ہاں، ذاتی اور غیر تجارتی مقاصد کے لیے پبلک ویڈیوز محفوظ کرنا مکمل طور پر قانونی اور محفوظ ہے۔'},
                {'q': f'کیا ڈاؤن لوڈ کی گئی ویڈیو پر کوئی واٹر مارک یا لوگو ہوگا؟', 'a': f'ہرگز نہیں! downsocial اصل سورس سے ویڈیو نکالتا ہے اس لیے اس پر کوئی اضافی واٹر مارک یا لوگو نہیں ہوتا۔'},
                {'q': f'کیا میں {p_name} ویڈیو کو MP3 آڈیو میں تبدیل کر سکتا ہوں؟', 'a': f'بالکل! بس لنک پیسٹ کریں اور "آڈیو (HQ MP3)" پر کلک کریں، آپ کو اعلیٰ ترین 320kbps MP3 آڈیو فائل مل جائے گی۔'},
                {'q': f'کیا مجھے کوئی ایپ یا سافٹ ویئر انسٹال کرنے کی ضرورت ہے؟', 'a': f'کسی بھی ایپ کی ضرورت نہیں۔ یہ ویب سائٹ موبائل اور کمپیوٹر کے براؤزر میں براہ راست کام کرتی ہے۔'},
                {'q': f'کیا ویڈیو بنانے والے کو پتہ چلے گا کہ میں نے ویڈیو ڈاؤن لوڈ کی ہے؟', 'a': f'نہیں، یہ عمل مکمل طور پر پوشیدہ ہے اور بنانے والے کو کوئی نوٹیفکیشن یا الرٹ نہیں جاتا۔'},
                {'q': f'کیا روزانہ ڈاؤن لوڈ کرنے کی کوئی حد مقرر ہے؟', 'a': f'کوئی حد نہیں! downsocial بالکل مفت ہے اور آپ جتنی چاہیں ویڈیوز اور آڈیوز ڈاؤن لوڈ کر سکتے ہیں۔'}
            ]
        }
        return faq_sets.get(lang, faq_sets['en'])

    # Deep SEO Technical Article in 12 languages
    def get_seo_article():
        p_name = specs[platform_id]['name']
        art_map = {
            'it': f"""<h2>Guida Completa all'Estrazione di Video e Audio da {p_name}</h2>
<p>Salvare video ad alto bitrate e tracce audio pulite da {p_name} è oggi un'esigenza fondamentale per studenti, creator e appassionati. downsocial.net offre una soluzione web moderna, rapida e priva di qualsiasi perdita qualitativa.</p>
<h3>Risoluzione 1080p, 2K e 4K Ultra HD Senza Perdita</h3>
<p>Interrogando direttamente i nodi CDN di {p_name}, la nostra piattaforma estrae flussi nativi MP4 garantendo la massima fedeltà cromatica, fluidità a 60fps e sincronizzazione audio perfetta.</p>
<h3>Transcodifica Audio MP3 Professionale a 320kbps</h3>
<p>Vuoi salvare solo la musica, una voce narrante o un memo vocale? La pipeline integrata converte la sorgente in file MP3 ad alta definizione compatibili con tutti i dispositivi.</p>
<h3>Privacy Assoluta e Architettura Zero-Knowledge</h3>
<p>Nessun account, nessun dato personale e nessun file memorizzato sui nostri server. I download sono 100% anonimi ed elaborati in memoria con crittografia SSL a 256 bit.</p>""",

            'en': f"""<h2>Comprehensive {p_name} Video & Audio Extraction Guide</h2>
<p>In modern digital media curation, saving high-bitrate video clips, ephemeral stories, and studio-grade audio tracks from {p_name} is essential for content creators, researchers, and multimedia enthusiasts. Traditional download methods frequently degrade visual fidelity through aggressive re-encoding or enforce intrusive software installations. downsocial.net introduces an advanced, clean, and lossless extraction architecture.</p>
<h3>1080p, 2K & 4K Ultra HD Stream Capture</h3>
<p>Our server-side pipeline queries the direct content delivery network (CDN) endpoints deployed by {p_name}. By extracting native MP4 video manifests without secondary compression, downsocial delivers original color reproduction, deep contrast, and crisp audio sync across all resolutions.</p>
<h3>Real-Time 320kbps MP3 Audio Transcoding</h3>
<p>Need to extract music, voice notes, speeches, or sound effects? Our integrated audio engine demuxes the container format and produces authentic high-bitrate MP3 files compatible with all desktop and mobile players.</p>
<h3>Zero-Knowledge Architecture & Privacy Protection</h3>
<p>downsocial operates strictly on ephemeral in-memory processing. We never store media files, never request user credentials, and never track download histories. Enjoy seamless, unlimited, and free media archiving anytime.</p>""",
            'es': f"""<h2>Guía Completa de Extracción de Video y Audio de {p_name}</h2>
<p>Guardar clips de video en alta tasa de bits, historias efímeras y pistas de audio de {p_name} es una necesidad diaria para creadores y usuarios de todo el mundo. downsocial.net ofrece una solución técnica limpia, rápida y sin pérdida de calidad visual.</p>
<h3>Captura en 1080p, 2K y 4K Ultra HD</h3>
<p>Nuestro sistema se conecta directamente a los servidores CDN oficiales de {p_name}, entregando streams nativos en MP4 sin compresión adicional ni marcas de agua añadidas.</p>
<h3>Conversión Instantánea a MP3 de 320kbps</h3>
<p>Extrae canciones, notas de voz o podcasts en tiempo real. Nuestro motor de audio produce archivos MP3 limpios y de alta fidelidad acústica para cualquier dispositivo.</p>
<h3>Privacidad Absoluta Sin Almacenamiento</h3>
<p>Operamos bajo una arquitectura estricta sin registro: tus enlaces se procesan en la memoria RAM y se eliminan al instante. Disfruta de descargas gratuitas e ilimitadas con total seguridad.</p>""",
            'fr': f"""<h2>Guide Complet d’Extraction Multimédia pour {p_name}</h2>
<p>Sauvegarder des vidéos haute définition et des pistes audio nettes depuis {p_name} n’a jamais été aussi simple. downsocial.net propose une technologie de pointe garantissant une qualité irréprochable sans aucune publicité invasive.</p>
<h3>Résolution 1080p, 2K et 4K Ultra HD Intacte</h3>
<p>En interrogeant directement les serveurs CDN de {p_name}, notre plateforme extrait les flux vidéo originaux au format MP4 sans dégradation de la fluidité ni altération des couleurs.</p>
<h3>Transcodage Audio MP3 Haute Définition 320 kbps</h3>
<p>Isolez facilement les bandes sonores ou les enregistrements vocaux. Le convertisseur intégré génère des fichiers MP3 purs compatibles avec tous vos lecteurs multimédias.</p>
<h3>Sécurité Maximale et Zéro Donnée Enregistrée</h3>
<p>Aucun compte requis, aucun historique conservé, aucun fichier stocké sur nos serveurs. Vos téléchargements sont strictement confidentiels et protégés par un chiffrement SSL de bout en bout.</p>""",
            'de': f"""<h2>Umfassender Leitfaden zum Herunterladen von {p_name}</h2>
<p>Das Speichern von hochauflösenden Videoclips und erstklassigen Audiospuren von {p_name} ist mit downsocial.net so einfach wie nie zuvor. Unsere moderne Web-Infrastruktur garantiert verlustfreie Ergebnisse ohne lästige Zwischenschritte.</p>
<h3>Originalqualität in 1080p, 2K und 4K Ultra HD</h3>
<p>Durch direkten Zugriff auf die CDN-Knotenpunkte von {p_name} erhalten Sie saubere MP4-Dateien in voller Auflösung und ohne zusätzliche Einblendungen oder störende Wasserzeichen.</p>
<h3>Echtzeit-Audiokonvertierung in 320kbps MP3</h3>
<p>Extrahieren Sie Musik, Sprache und Soundeffekte sekundenschnell. Die Audio-Engine liefert unverfälschte MP3-Dateien für Ihre persönliche Musiksammlung oder den Offline-Genuss.</p>
<h3>Datenschutz nach modernsten Standards</h3>
<p>Keine Registrierung, keine Cookies, keine Speicherung von Mediendateien auf Servern. Alle Prozesse laufen flüchtig und verschlüsselt im Arbeitsspeicher ab.</p>""",
            'hi': f"""<h2>{p_name} वीडियो और ऑडियो डाउनलोड करने की संपूर्ण मार्गदर्शिका</h2>
<p>{p_name} से उच्च गुणवत्ता वाले वीडियो और ऑडियो सहेजना अब बेहद आसान है। downsocial.net बिना किसी विज्ञापन या वायरस के सीधे मूल गुणवत्ता में डाउनलोड करने की सुविधा प्रदान करता है।</p>
<h3>1080p, 2K और 4K अल्ट्रा एचडी वीडियो गुणवत्ता</h3>
<p>हमारा सिस्टम {p_name} के आधिकारिक सर्वर से सीधे वीडियो स्ट्रीम प्राप्त करता है, जिससे वीडियो के रंग और स्पष्टता बिल्कुल मूल रूप में बने रहते हैं।</p>
<h3>रीयल-टाइम 320kbps MP3 ऑडियो कन्वर्जन</h3>
<p>यदि आपको केवल संगीत या आवाज चाहिए, तो हमारा ऑडियो कनवर्टर वीडियो को तुरंत क्रिस्टल क्लियर MP3 फाइल में बदल देता है।</p>
<h3>100% गोपनीयता और सुरक्षित सेवा</h3>
<p>हम कभी भी आपकी कोई व्यक्तिगत जानकारी या डाउनलोड हिस्ट्री स्टोर नहीं करते हैं। पूरी तरह से मुफ्त और असीमित डाउनलोड का आनंद लें।</p>""",
            'ar': f"""<h2>دليل شامل لتحميل مقاطع الفيديو والصوتيات من {p_name}</h2>
<p>أصبح حفظ مقاطع الفيديو عالية الدقة والمسارات الصوتية من {p_name} أسهل وأسرع من أي وقت مضى مع downsocial.net، المنصة الرائدة في استخراج الوسائط الرقمية بأمان وبدون إعلانات مزعجة.</p>
<h3>جودة 1080p و 2K و 4K Ultra HD فائقة النقاء</h3>
<p>ترتبط أنظمتنا مباشرة بخوادم CDN الرسمية لـ {p_name}، مما يتيح لك تنزيل الفيديو بصيغة MP4 الأصلية دون ضغط إضافي أو وضع علامات مائية.</p>
<h3>تحويل فوري إلى صوتيات MP3 عالية الوضوح 320kbps</h3>
<p>يمكنك عزل الصوت والموسيقى والملاحظات الصوتية بدقة متناهية للحصول على ملفات MP3 متوافقة مع جميع مشغلات الموسيقى والهواتف.</p>
<h3>خصوصية كاملة وضمان عدم تسجيل البيانات</h3>
<p>نعمل بمعايير أمان صارمة بدون تسجيل حسابات أو تتبع أو تخزين أي ملفات وسائط على الخوادم. تمتع بتنزيل مجاني وغير محدود في أي وقت.</p>""",
            'pt': f"""<h2>Guia Completo para Download de Mídia do {p_name}</h2>
<p>Salvar vídeos com alta taxa de quadros e áudios de estúdio do {p_name} é indispensável para quem busca praticidade. O downsocial.net oferece uma arquitetura rápida, confiável e livre de marcas d’água.</p>
<h3>Captura em 1080p, 2K e 4K Ultra HD</h3>
<p>Nossos servidores estabelecem conexão direta com as redes CDN de entrega do {p_name}, entregando arquivos MP4 puros e com sincronia labial perfeita.</p>
<h3>Transcodificação para MP3 a 320kbps</h3>
<p>Extraia trilhas sonoras, vinhetas ou narrações em tempo real. O conversor integrado gera arquivos MP3 com reprodução impecável em qualquer player.</p>
<h3>Privacidade Rigorosa sem Retenção de Dados</h3>
<p>Processamento totalmente volátil na memória RAM, sem salvar mídias em disco e sem monitorar seu histórico de uso. Downloads gratuitos, ilimitados e seguros.</p>""",
            'bn': f"""<h2>{p_name} ভিডিও ও অডিও ডাউনলোডের পূর্ণাঙ্গ নির্দেশিকা</h2>
<p>{p_name} থেকে উচ্চ বিটরেটের ভিডিও ক্লিপ এবং স্টুডিও কোয়ালিটির অডিও সেভ করা এখন downsocial.net-এর মাধ্যমে অত্যন্ত সহজ ও দ্রুত। কোনো বিরক্তিকর বিজ্ঞাপন ছাড়াই আসল রেজোলিউশনে ফাইল সংগ্রহ করুন।</p>
<h3>১০৮০p, ২K ও ৪K আল্ট্রা HD রেজোলিউশন</h3>
<p>আমাদের সিস্টেম সরাসরি {p_name}-এর মূল সিডিএন সার্ভারের সাথে যুক্ত হয়ে আসল MP4 ভিডিও স্ট্রীম সরবরাহ করে, যাতে রঙের উজ্জ্বলতা শতভাগ অক্ষুণ্ণ থাকে।</p>
<h3>রিয়েল-টাইম ৩২০kbps MP3 অডিও কনভার্সন</h3>
<p>ভিডিও থেকে ব্যাকগ্রাউন্ড মিউজিক বা ভয়েস আলাদা করতে চান? আমাদের ইনবিল্ট কনভার্টার নিমেষেই হাই-কোয়ালিটি ৩২০kbps MP3 তৈরি করে দেয়।</p>
<h3>সম্পূর্ণ নিরাপত্তা ও জিরো লগ সিস্টেম</h3>
<p>কোনো অ্যাকাউন্ট বা ব্যক্তিগত তথ্য সংরক্ষণের প্রয়োজন নেই। সম্পূর্ণ সুরক্ষিত এবং আনলিমিটেড ডাউনলোডের অভিজ্ঞতা উপভোগ করুন।</p>""",
            'ru': f"""<h2>Полное руководство по скачиванию медиа из {p_name}</h2>
<p>Сохранение видео в высоком разрешении и звуковых дорожек из {p_name} стало быстрым и удобным благодаря сервису downsocial.net. Забудьте о навязчивой рекламе и сложных программах.</p>
<h3>Оригинальное разрешение 1080p, 2K и 4K Ultra HD</h3>
<p>Прямое подключение к CDN-серверам {p_name} позволяет получать оригинальные потоки MP4 без дополнительного сжатия и наложения водяных знаков.</p>
<h3>Мгновенное извлечение аудио в формате MP3 320 кбит/с</h3>
<p>Выделяйте музыку, диалоги или звуковые эффекты в один клик. Встроенный конвертер создает чистые MP3-файлы студийного качества.</p>
<h3>Конфиденциальность и безопасность</h3>
<p>Мы не требуем регистрации и не храним загруженные файлы на своих серверах. Все данные обрабатываются в оперативной памяти и моментально удаляются.</p>""",
            'id': f"""<h2>Panduan Lengkap Mengunduh Video & Audio dari {p_name}</h2>
<p>Menyimpan video beresolusi tinggi dan trek audio jernih dari {p_name} kini semakin praktis bersama downsocial.net. Nikmati pengunduhan cepat tanpa watermark dan tanpa iklan mengganggu.</p>
<h3>Kualitas Maksimal 1080p, 2K, dan 4K Ultra HD</h3>
<p>Terhubung langsung ke jaringan pengiriman konten (CDN) resmi {p_name}, menghasilkan video MP4 asli tanpa penurunan ketajaman maupun warna.</p>
<h3>Konversi Cepat ke Format MP3 320kbps</h3>
<p>Dapatkan lagu favorit atau rekaman suara secara terpisah. Sistem kami memisahkan audio menjadi file MP3 berkualitas tinggi dengan lancar.</p>
<h3>Privasi Terjamin Tanpa Penyimpanan File</h3>
<p>Sistem kami beroperasi tanpa log dan tanpa menyimpan media di server. Semua proses terenkripsi aman dan gratis tanpa batas.</p>""",
            'zh': f"""<h2>{p_name} 高清多媒体极速提取与音频转码深度指南</h2>
<p>在快节奏的移动互联网时代，离线收藏与分析来自 {p_name} 的高清视频素材、热门快拍与无损伴奏，已成为创作者与普通用户的刚需。downsocial.net 采用新一代云端直链技术，为您提供纯净、无损且免安装的高效下载体验。</p>
<h3>1080p、2K 与 4K Ultra HD 官方原画质捕获</h3>
<p>服务端底层直连 {p_name} 分布式官方 CDN 节点，直接读取原始 MP4 媒体清单（Manifest），从根源杜绝二次重编码压缩造成的边缘泛白或画质降级，100% 还原超清水准。</p>
<h3>毫秒级 320kbps 原生 MP3 音频转码抽离</h3>
<p>只需提取背景原声、名家配音或播客对白？系统内置工业级音频提取模块，瞬时分离音视频封装，生成完全兼容各类播放器的原生高保真 320kbps/192kbps MP3 文件。</p>
<h3>严守零留痕隐私法则，保障极致安全</h3>
<p>本站严格奉行“内存瞬时流转，绝不落地持久化”的安全准则。无账号体系、不储存用户文件、不搜集操作轨迹。尽享全天候无限次安全极速下载。</p>""",
            'ur': f"""<h2>{p_name} ویڈیو اور آڈیو ڈاؤن لوڈنگ کی مکمل گائیڈ</h2>
<p>{p_name} سے ہائی ڈیفینیشن ویڈیوز اور اعلیٰ ترین آڈیو محفوظ کرنا اب downsocial.net کے ساتھ انتہائی تیز اور آسان ہے۔ بغیر کسی اشتہار کے اصل کوالٹی میں ویڈیوز ڈاؤن لوڈ کریں۔</p>
<h3>1080p، 2K اور 4K الٹرا ایچ ڈی ویڈیو کوالٹی</h3>
<p>ہمارا جدید سسٹم {p_name} کے سرورز سے براہ راست ویڈیو حاصل کرتا ہے، جس سے ویڈیو کا ریزولوشن اور رنگ بالکل اصل حالت میں برقرار رہتے ہیں۔</p>
<h3>رئیل ٹائم 320kbps MP3 آڈیو کنورژن</h3>
<p>اگر آپ کو ویڈیو میں سے صرف میوزک یا آواز چاہیے تو ہمارا آڈیو انجن ویڈیو کو فوری طور پر صاف شفاف MP3 فائل میں تبدیل کر دیتا ہے۔</p>
<h3>100% رازداری اور محفوظ سروس</h3>
<p>ہم صارف کا کوئی بھی ذاتی ڈیٹا یا ڈاؤن لوڈ ہسٹری محفوظ نہیں کرتے۔ مکمل رازداری کے ساتھ مفت اور لامحدود ڈاؤن لوڈنگ کا لطف اٹھائیں۔</p>"""
        }
        return art_map.get(lang, art_map['en'])

    # Quick answer snippet for AEO / GEO
    def get_quick_answer():
        p_name = specs[platform_id]['name']
        qa_map = {
            'en': (f'Quick Answer: How to Download {p_name} Media?', f'Copy the {p_name} URL, paste it into downsocial.net, and click "Download Video" to save 1080p Full HD MP4 or 320kbps MP3 audio without watermarks in seconds.'),
            'es': (f'Respuesta Rápida: ¿Cómo descargar de {p_name}?', f'Copia el enlace de {p_name}, pégalo en downsocial.net y presiona "Descargar Video" para obtener MP4 en 1080p o MP3 a 320kbps sin marcas de agua al instante.'),
            'fr': (f'Réponse Rapide : Comment télécharger sur {p_name} ?', f'Copiez l’URL de {p_name}, collez-la sur downsocial.net et cliquez sur "Télécharger la Vidéo" pour obtenir un MP4 1080p ou un MP3 320 kbps sans filigrane.'),
            'de': (f'Kurzantwort: Wie lade ich von {p_name} herunter?', f'Kopieren Sie den {p_name}-Link, fügen Sie ihn bei downsocial.net ein und klicken Sie auf "Video Herunterladen", um 1080p MP4 oder 320kbps MP3 ohne Wasserzeichen zu speichern.'),
            'hi': (f'त्वरित उत्तर: {p_name} से वीडियो कैसे डाउनलोड करें?', f'{p_name} का लिंक कॉपी करें, downsocial.net पर पेस्ट करें और बिना वॉटरमार्क के 1080p Full HD MP4 या 320kbps MP3 तुरंत डाउनलोड करने के लिए "वीडियो डाउनलोड करें" पर क्लिक करें।'),
            'ar': (f'إجابة سريعة: كيف تقوم بالتحميل من {p_name}؟', f'انسخ رابط {p_name}، والصقه في موقع downsocial.net، واضغط على "تحميل الفيديو" لتحصل على فيديو 1080p MP4 أو صوت 320kbps MP3 فائق النقاء وبدون علامة مائية.'),
            'pt': (f'Resposta Rápida: Como baixar do {p_name}?', f'Copie o link do {p_name}, cole no downsocial.net e clique em "Baixar Vídeo" para obter arquivos em 1080p MP4 ou MP3 a 320kbps sem marcas d’água em segundos.'),
            'bn': (f'সহজ উত্তর: {p_name} থেকে কীভাবে ডাউনলোড করবেন?', f'{p_name}-এর লিংকটি কপি করে downsocial.net-এ পেস্ট করুন এবং কোনো ওয়াটারমার্ক ছাড়া ১০৮০p MP4 বা ৩২০kbps MP3 পেতে "ভিডিও ডাউনলোড করুন"-এ চাপ দিন।'),
            'ru': (f'Краткий ответ: Как скачать из {p_name}?', f'Скопируйте ссылку {p_name}, вставьте ее на downsocial.net и нажмите «Скачать видео», чтобы сохранить 1080p MP4 или MP3 320 кбит/с без водяных знаков.'),
            'id': (f'Jawaban Cepat: Cara Mengunduh dari {p_name}?', f'Salin tautan dari {p_name}, tempel di downsocial.net, lalu klik "Unduh Video" untuk menyimpan video 1080p MP4 atau audio MP3 320kbps tanpa tanda air.'),
            'zh': (f'快速解答：如何从 {p_name} 高速下载音视频？', f'复制 {p_name} 链接并粘贴至 downsocial.net，点击“下载视频”即可瞬间获得无水印 1080p 全高清 MP4 或 320kbps 纯正 MP3 音频。'),
            'ur': (f'فوری جواب: {p_name} سے ویڈیو کیسے ڈاؤن لوڈ کریں؟', f'{p_name} کا لنک کاپی کریں، downsocial.net پر پیسٹ کریں اور بغیر واٹر مارک کے 1080p MP4 یا 320kbps MP3 حاصل کرنے کے لیے "ویڈیو ڈاؤن لوڈ کریں" پر کلک کریں۔'),
            'it': (f'Risposta Rapida: Come scaricare da {p_name}?', f'Copia l\'URL di {p_name}, incollalo su downsocial.net e fai clic su "Scarica Video" per salvare video 1080p Full HD MP4 o audio MP3 a 320kbps senza filigrane in pochi secondi.')
        }
        return qa_map.get(lang, qa_map['en'])

    qa_title, qa_text = get_quick_answer()
    howto_data = get_howto()

    faq_heading = f"FAQ su {specs[platform_id]['name']}" if lang == 'it' else f"{specs[platform_id]['name']} FAQ"

    return {
        'title': title,
        'tagline': tagline,
        'placeholder': placeholder,
        'downloadBtn': download_btn,
        'features': get_features(),
        'howToTitle': howto_data['title'],
        'howToSteps': howto_data['steps'],
        'howToHidden': howto_data['hidden'],
        'faqsTitle': faq_heading,
        'faqs': get_faqs(),
        'quickAnswerTitle': qa_title,
        'quickAnswerText': qa_text,
        'seoArticle': get_seo_article()
    }
