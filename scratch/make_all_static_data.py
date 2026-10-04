# scratch/make_all_static_data.py
import json, os

LANGS = ['en', 'es', 'fr', 'de', 'hi', 'ar', 'pt', 'bn', 'ru', 'id', 'zh', 'ur']

# --- DICTIONARIES FOR STATIC PAGES ---

# 1. ABOUT
ABOUT = {
    'en': {
        'h1': 'About downsocial — Free All-in-One Video & Audio Downloader',
        'intro': 'Welcome to downsocial.net. We built this platform with one straightforward mission: give everyone a fast, secure, and effortless way to download videos, reels, shorts, and MP3 audio from Facebook, Instagram, TikTok, YouTube, Snapchat, and Threads — without watermarks, without sign-ups, and 100% free.',
        'm_h2': 'Our Mission',
        'm_p': 'We believe that saving publicly available videos for offline learning, travel, content analysis, and personal memories should be simple and private. Traditional downloaders are riddled with deceptive pop-up ads, malware threats, forced software installations, or severe video compression. downsocial completely reimagines media downloading with a pristine, instantaneous browser-based experience.',
        'arch_h2': 'Multi-Platform Architectural Support',
        'arch_intro': 'downsocial eliminates the need to jump between multiple disjointed websites. One single search box parses and handles direct media stream extraction across all top platforms:',
        'bullets': [
            ('Facebook:', 'Reels, public Feed videos, Watch episodes, and Stories in 1080p Full HD.'),
            ('Instagram:', 'High-bitrate Reels, IGTV videos, high-res carousel albums, and 24-hour Stories.'),
            ('TikTok:', '100% clean video downloads stripped of bouncing watermarks, plus trending audio extraction.'),
            ('YouTube:', 'Full 1080p, 2K, and 4K Ultra HD video clips, plus YouTube Shorts and high-fidelity 320kbps MP3 audio.'),
            ('Snapchat:', 'Spotlight vertical videos and public Stories saved before expiration.'),
            ('Meta Threads:', 'Crisp video discussions, photo albums, and voice notes.')
        ],
        'priv_h2': 'Zero Tracking & Total Privacy',
        'priv_p': 'We operate on a zero-knowledge technical architecture. No account registration, no cookies tracking your downloads, and no media files stored on our servers. Your downloads remain 100% private, anonymous, and encrypted.',
        'faq_title': 'Frequently Asked Questions',
        'faqs': [
            ('Is downsocial really free?', 'Yes, downsocial is 100% free with unlimited downloads and no hidden subscription fees.'),
            ('Do I need an account to download videos?', 'No account registration or login is required. You can download videos immediately and anonymously.'),
            ('Which platforms are supported?', 'downsocial supports video and audio downloads from YouTube, TikTok (no watermark), Instagram Reels, Facebook, Snapchat, and Threads.'),
            ('Does downsocial store or keep my downloaded videos?', 'No. We operate on a zero-knowledge architecture and do not host, store, or archive any downloaded media on our servers.')
        ]
    },
    'es': {
        'h1': 'Sobre downsocial — Descargador Gratuito Todo en Uno de Videos y Audios',
        'intro': 'Bienvenido a downsocial.net. Desarrollamos esta plataforma con una misión clara: ofrecer a todos una forma rápida, segura y sencilla de descargar videos, reels, shorts y audios MP3 de Facebook, Instagram, TikTok, YouTube, Snapchat y Threads — sin marcas de agua, sin registros y 100% gratis.',
        'm_h2': 'Nuestra Misión',
        'm_p': 'Creemos que guardar videos públicos para el aprendizaje sin conexión, viajes, archivo personal y recuerdos debe ser accesible y seguro. La mayoría de los descargadores tradicionales están saturados de anuncios invasivos, enlaces engañosos o software innecesario. downsocial elimina todas esas barreras con una interfaz limpia y veloz basada en la nube.',
        'arch_h2': 'Soporte Multiplataforma Completo',
        'arch_intro': 'Con downsocial no necesitas múltiples páginas web. Una única barra inteligente procesa y extrae enlaces de los mejores sitios:',
        'bullets': [
            ('Facebook:', 'Reels, videos de Watch, historias y videos de publicaciones en 1080p Full HD.'),
            ('Instagram:', 'Reels en alta tasa de bits, carruseles de fotos y videos, y Stories de 24 horas.'),
            ('TikTok:', 'Videos limpios sin la molesta marca de agua que rebota, además de audio MP3 original.'),
            ('YouTube:', 'Videos en 1080p, 2K y 4K UHD, Shorts virales y conversión a MP3 de 320kbps.'),
            ('Snapchat:', 'Videos verticales de Spotlight y Stories públicas antes de que desaparezcan.'),
            ('Threads:', 'Videos de conversaciones, notas de voz y carruseles fotográficos.')
        ],
        'priv_h2': 'Privacidad Absoluta y Cero Registros',
        'priv_p': 'Operamos bajo una arquitectura estricta sin registro de datos. No solicitamos contraseñas, no guardamos cookies de rastreo y no almacenamos archivos multimedia en nuestros servidores. Todo se procesa de forma transitoria en memoria con cifrado SSL.',
        'faq_title': 'Preguntas Frecuentes',
        'faqs': [
            ('¿downsocial es realmente gratuito?', 'Sí, downsocial es 100% gratis con descargas ilimitadas y sin costos ocultos de suscripción.'),
            ('¿Necesito una cuenta para descargar videos?', 'No se requiere registrarse ni iniciar sesión. Puedes descargar videos de forma inmediata y anónima.'),
            ('¿Qué plataformas son compatibles?', 'downsocial admite descargas de YouTube, TikTok (sin marcas de agua), Instagram Reels, Facebook, Snapchat y Threads.'),
            ('¿downsocial almacena copias de los videos descargados?', 'No. Operamos con arquitectura de conocimiento cero y no alojamos ni archivamos archivos en nuestros servidores.')
        ]
    },
    'fr': {
        'h1': 'À Propos de downsocial — Téléchargeur Vidéo & Audio Tout-en-Un Gratuit',
        'intro': 'Bienvenue sur downsocial.net. Notre mission est simple et claire : offrir à chacun une méthode rapide, sécurisée et fluide pour télécharger des vidéos, reels, shorts et MP3 depuis Facebook, Instagram, TikTok, YouTube, Snapchat et Threads — sans filigrane, sans inscription et 100% gratuit.',
        'm_h2': 'Notre Mission',
        'm_p': 'Sauvegarder des vidéos publiques pour une utilisation hors ligne ou pour des souvenirs personnels doit être simple et privé. downsocial élimine les publicités intrusives et les logiciels tiers grâce à un outil ultra-rapide fonctionnant directement dans votre navigateur.',
        'arch_h2': 'Compatibilité Multi-Plateforme Complète',
        'arch_intro': 'Un seul outil remplace tous vos anciens téléchargeurs dispersés :',
        'bullets': [
            ('Facebook :', 'Reels, vidéos Watch et Stories en 1080p Full HD.'),
            ('Instagram :', 'Reels, albums carrousels multi-photos et Stories éphémères.'),
            ('TikTok :', 'Téléchargement sans filigrane et extraction de bande-son MP3 320 kbps.'),
            ('YouTube :', 'Qualité 1080p, 2K, 4K UHD, YouTube Shorts et conversion MP3 studio.'),
            ('Snapchat :', 'Clips Spotlight 9:16 et Stories publiques avant expiration.'),
            ('Threads :', 'Vidéos, notes vocales et albums photo de Meta Threads.')
        ],
        'priv_h2': 'Confidentialité Totale et Zéro Enregistrement',
        'priv_p': 'Aucune création de compte, aucun cookie de pistage, aucun fichier stocké sur nos serveurs. Vos téléchargements sont strictement privés, éphémères et chiffrés via HTTPS 256 bits.',
        'faq_title': 'Foire Aux Questions',
        'faqs': [
            ('Est-ce que downsocial est réellement gratuit ?', 'Oui, downsocial est 100% gratuit avec des téléchargements illimités et sans aucun frais caché.'),
            ('Faut-il créer un compte pour télécharger ?', 'Aucune inscription ni connexion requise. Téléchargez immédiatement et anonymement.'),
            ('Quelles plateformes sont prises en charge ?', 'downsocial prend en charge YouTube, TikTok (sans filigrane), Instagram Reels, Facebook, Snapchat et Threads.'),
            ('Conservez-vous une copie de mes téléchargements ?', 'Non. Aucun média n’est stocké sur nos serveurs. Tout est traité en mémoire vive de manière éphémère.')
        ]
    },
    'de': {
        'h1': 'Über downsocial — Kostenloser All-in-One Video- & Audio-Downloader',
        'intro': 'Willkommen bei downsocial.net. Wir haben diese Plattform mit einer klaren Mission entwickelt: Jedem Nutzer eine schnelle, sichere und mühelose Möglichkeit zu bieten, Videos, Reels, Shorts und MP3-Dateien von Facebook, Instagram, TikTok, YouTube, Snapchat und Threads herunterzuladen – ohne Wasserzeichen, ohne Registrierung und 100% kostenlos.',
        'm_h2': 'Unsere Mission',
        'm_p': 'Das Speichern öffentlich zugänglicher Videos für das Offline-Lernen oder private Archive sollte einfach und datenschutzfreundlich sein. downsocial bietet eine saubere, werbefreie und leistungsstarke Weboberfläche ohne lästige Software-Installationen.',
        'arch_h2': 'Umfassende Multiplattform-Unterstützung',
        'arch_intro': 'Ein einziges Eingabefeld erkennt automatisch die jeweilige Plattform und verarbeitet den Stream:',
        'bullets': [
            ('Facebook:', 'Reels, Watch-Videos und 24h-Storys in 1080p Full HD.'),
            ('Instagram:', 'Reels, Karussell-Posts mit mehreren Bildern und Storys in Originalauflösung.'),
            ('TikTok:', 'Videos ohne störendes Wasserzeichen sowie virale Musik im MP3-Format.'),
            ('YouTube:', '1080p, 2K und 4K UHD Videos, YouTube Shorts und 320kbps MP3-Audio.'),
            ('Snapchat:', 'Spotlight-Clips im 9:16-Format und öffentliche Storys.'),
            ('Threads:', 'Videos, Sprachnachrichten und Fotobeiträge aus Meta Threads.')
        ],
        'priv_h2': 'Datenschutz & Null-Protokollierung',
        'priv_p': 'Wir arbeiten nach dem Zero-Knowledge-Prinzip: Keine Benutzerkonten, keine Tracking-Cookies und keine dauerhafte Speicherung von Dateien auf unseren Servern. Ihre Daten bleiben zu 100% geschützt.',
        'faq_title': 'Häufig Gestellte Fragen',
        'faqs': [
            ('Ist downsocial wirklich kostenlos?', 'Ja, downsocial ist zu 100% kostenlos mit unbegrenzten Downloads ohne versteckte Abogebühren.'),
            ('Benötige ich ein Benutzerkonto?', 'Nein, es ist keine Registrierung und kein Login erforderlich. Alle Downloads erfolgen anonym.'),
            ('Welche Plattformen werden unterstützt?', 'downsocial unterstützt YouTube, TikTok (ohne Wasserzeichen), Instagram Reels, Facebook, Snapchat und Threads.'),
            ('Werden heruntergeladene Videos gespeichert?', 'Nein. Es werden niemals Mediendateien auf unseren Servern gespeichert oder zwischengespeichert.')
        ]
    },
    'hi': {
        'h1': 'downsocial के बारे में — मुफ़्त ऑल-इन-वन वीडियो और ऑडियो डाउनलोडर',
        'intro': 'downsocial.net में आपका स्वागत है। हमारा उद्देश्य बिल्कुल स्पष्ट है: सभी उपयोगकर्ताओं को फेसबुक, इंस्टाग्राम, टिकटॉक, यूट्यूब, स्नैपचैट और थ्रेड्स से बिना वॉटरमार्क, बिना किसी लॉगिन और 100% फ्री में वीडियो, रील्स, शॉर्ट्स और MP3 डाउनलोड करने की सबसे तेज़ और सुरक्षित सुविधा प्रदान करना।',
        'm_h2': 'हमारा मिशन',
        'm_p': 'हमारा मानना है कि व्यक्तिगत अध्ययन, यात्रा या व्यक्तिगत यादों के लिए सार्वजनिक वीडियो सहेजना आसान और सुरक्षित होना चाहिए। अधिकांश डाउनलोडर अत्यधिक विज्ञापनों और वायरस के खतरों से भरे होते हैं। downsocial एक स्वच्छ और विश्वसनीय अनुभव प्रदान करता है।',
        'arch_h2': 'मल्टी-प्लेटफ़ॉर्म सपोर्ट',
        'arch_intro': 'downsocial सभी प्रमुख सोशल मीडिया नेटवर्क का समर्थन करता है:',
        'bullets': [
            ('Facebook:', 'रील्स, वॉच वीडियो और 24 घंटे की स्टोरीज 1080p Full HD में।'),
            ('Instagram:', 'रील्स, मल्टी-फोटो कैरोसेल और स्टोरीज बिना किसी वॉटरमार्क के।'),
            ('TikTok:', 'बिना लोगो या वॉटरमार्क के मूल वीडियो और 320kbps MP3 ऑडियो।'),
            ('YouTube:', '1080p, 2K, 4K UHD वीडियो, शॉर्ट्स और हाई-क्वालिटी MP3 कन्वर्जन।'),
            ('Snapchat:', 'स्पॉटलाइट वर्टिकल क्लिप्स और पब्लिक स्टोरीज।'),
            ('Threads:', 'मेटा थ्रेड्स वीडियो, वॉयस नोट्स और तस्वीरें।')
        ],
        'priv_h2': 'पूर्ण गोपनीयता और सुरक्षा',
        'priv_p': 'हम आपकी गोपनीयता का पूरा सम्मान करते हैं। कोई खाता बनाने की आवश्यकता नहीं है, कोई ट्रैकिंग कुकीज़ नहीं हैं और हमारे सर्वर पर कोई वीडियो फ़ाइल स्टोर नहीं होती है।',
        'faq_title': 'अक्सर पूछे जाने वाले प्रश्न',
        'faqs': [
            ('क्या downsocial सचमुच मुफ़्त है?', 'हाँ, downsocial असीमित डाउनलोड के साथ 100% मुफ़्त है।'),
            ('क्या वीडियो डाउनलोड करने के लिए अकाउंट चाहिए?', 'नहीं, किसी रजिस्ट्रेशन या लॉग-इन की आवश्यकता नहीं है।'),
            ('कौन से प्लेटफ़ॉर्म समर्थित हैं?', 'YouTube, TikTok, Instagram Reels, Facebook, Snapchat और Threads समर्थित हैं।'),
            ('क्या downsocial डाउनलोड किए गए वीडियो स्टोर करता है?', 'नहीं, हम सर्वर पर कोई भी वीडियो या मीडिया स्टोर नहीं करते हैं।')
        ]
    },
    'ar': {
        'h1': 'من نحن — downsocial.net محمل الفيديوهات والصوتيات الشامل المجاني',
        'intro': 'مرحباً بكم في downsocial.net. قمنا بإنشاء هذه المنصة بهدف واحد وواضح: تمكين الجميع من تنزيل مقاطع الفيديو، الريلز، الشورتس، والصوتيات بصيغة MP3 من فيسبوك، إنستغرام، تيك توك، يوتيوب، سناب شات، وثريدز — بدون علامة مائية، بدون تسجيل وبشكل مجاني 100%.',
        'm_h2': 'مهمتنا',
        'm_p': 'نؤمن بأن حفظ مقاطع الفيديو العامة للتعلم في وضع عدم الاتصال أو الأرشفة الشخصية يجب أن يكون بسيطاً وآمناً وخالياً من التعقيدات. تتفوق منصة downsocial على المواقع التقليدية المليئة بالإعلانات المزعجة بتوفير تجربة سريعة ونقية وآمنة تعتمد على السحابة مباشرة عبر متصفحك.',
        'arch_h2': 'دعم هندسي شامل لكافة المنصات',
        'arch_intro': 'تقضي منصة downsocial على الحاجة للتنقل بين مواقع متعددة. مربع بحث ذكي واحد يتولى استخراج الوسائط من جميع المنصات:',
        'bullets': [
            ('فيسبوك:', 'مقاطع ريلز، فيديوهات Watch، والقصص بدقة 1080p Full HD عالية الوضوح.'),
            ('إنستغرام:', 'ريلز بمعدل بت عالي، ألبومات الصور المتعددة، والقصص اليومية.'),
            ('تيك توك:', 'تنزيل نقي 100% بدون علامة مائية مع إمكانية استخراج الصوتيات الأصلية.'),
            ('يوتيوب:', 'فيديوهات بدقة 1080p و 2K و 4K Ultra HD بالإضافة إلى YouTube Shorts وصوت 320kbps MP3.'),
            ('سناب شات:', 'مقاطع أضواء سبوتلايت والقصص العامة قبل انتهائها.'),
            ('ميتا ثريدز:', 'فيديوهات النقاشات الحوارية، ألبومات الصور والملاحظات الصوتية.')
        ],
        'priv_h2': 'خصوصية مطلقة وبدون أي سجلات تتبع',
        'priv_p': 'نعمل وفق بنية تقنية تعتمد على انعدام المعرفة التامة. لا نطلب إنشاء حساب، ولا نستخدم ملفات تتبع الارتباط، ولا نحتفظ بأي ملفات وسائط على خوادمنا نهائياً.',
        'faq_title': 'الأسئلة الشائعة',
        'faqs': [
            ('هل موقع downsocial مجاني بالفعل؟', 'نعم، موقع downsocial مجاني 100% مع تنزيلات غير محدودة وبدون أي رسوم خفية.'),
            ('هل أحتاج إلى إنشاء حساب لتنزيل الفيديوهات؟', 'لا، لا يلزم أي تسجيل حساب أو تسجيل دخول. يمكنك التنزيل فوراً وبشكل مجهول.'),
            ('ما هي المنصات المدعومة؟', 'يدعم downsocial تنزيل الفيديو والصوت من يوتيوب، تيك توك (بدون علامة مائية)، إنستغرام ريلز، فيسبوك، سناب شات، وثريدز.'),
            ('هل يحتفظ downsocial بنسخ من الفيديوهات المحملة؟', 'كلا. نحن نعمل وفق بنية انعدام المعرفة ولا نستضيف أو نخزن أي وسائط على خوادمنا نهائياً.')
        ]
    },
    'pt': {
        'h1': 'Sobre downsocial — Baixador Gratuito Tudo-em-Um de Vídeos e Áudios',
        'intro': 'Bem-vindo ao downsocial.net. Desenvolvemos esta plataforma com uma missão direta: oferecer a todos uma maneira rápida, segura e sem esforço de baixar vídeos, reels, shorts e áudios MP3 do Facebook, Instagram, TikTok, YouTube, Snapchat e Threads — sem marcas d’água, sem cadastros e 100% gratuito.',
        'm_h2': 'Nossa Missão',
        'm_p': 'Acreditamos que salvar vídeos públicos para aprendizado offline ou lembranças deve ser simples e privado. O downsocial elimina todas as barreiras com uma ferramenta moderna que roda direto no navegador.',
        'arch_h2': 'Suporte Multiplataforma Completo',
        'arch_intro': 'Uma única barra de pesquisa processa e extrai mídias dos principais canais sociais:',
        'bullets': [
            ('Facebook:', 'Reels, vídeos do Watch, stories e posts em 1080p Full HD.'),
            ('Instagram:', 'Reels de alta taxa de bits, carrosséis de fotos e Stories.'),
            ('TikTok:', 'Vídeos sem a marca d’água flutuante e áudio MP3 original.'),
            ('YouTube:', 'Vídeos em 1080p, 2K e 4K UHD, Shorts e conversão para MP3 a 320kbps.'),
            ('Snapchat:', 'Vídeos do Spotlight e stories públicas antes de expirarem.'),
            ('Threads:', 'Vídeos, mensagens de áudio e álbuns de fotos do Meta Threads.')
        ],
        'priv_h2': 'Privacidade Rigorosa e Zero Registros',
        'priv_p': 'Operamos com arquitetura de conhecimento zero. Sem contas, sem cookies invasivos e sem mídias armazenadas em nossos servidores. Tudo é criptografado com SSL de 256 bits.',
        'faq_title': 'Perguntas Frequentes',
        'faqs': [
            ('O downsocial é realmente gratuito?', 'Sim, 100% gratuito com downloads ilimitados sem taxas ocultas.'),
            ('Preciso criar uma conta para baixar vídeos?', 'Não, nenhum cadastro é necessário. Você faz downloads de forma anônima e instantânea.'),
            ('Quais plataformas são suportadas?', 'Suportamos YouTube, TikTok (sem marca d’água), Instagram Reels, Facebook, Snapchat e Threads.'),
            ('O downsocial armazena meus vídeos baixados?', 'Não. Não mantemos nem armazenamos nenhum arquivo de mídia em nossos servidores.')
        ]
    },
    'bn': {
        'h1': 'downsocial সম্পর্কে — সম্পূর্ণ ফ্রি অল-ইন-ওয়ান ভিডিও ও অডিও ডাউনলোডার',
        'intro': 'downsocial.net-এ আপনাকে স্বাগতম। আমাদের লক্ষ্য অত্যন্ত স্পষ্ট: ফেসবুক, ইনস্টাগ্রাম, টিকটক, ইউটিউব, স্ন্যাপচ্যাট ও থ্রেডস থেকে ওয়াটারমার্ক ছাড়া, কোনো রেজিস্ট্রেশন ব্যতিরেকে এবং সম্পূর্ণ বিনামূল্যে দ্রুততম উপায়ে ভিডিও ও MP3 ডাউনলোড করার সুযোগ প্রদান করা।',
        'm_h2': 'আমাদের মিশন',
        'm_p': 'আমরা বিশ্বাস করি অফলাইন স্টাডি বা ব্যক্তিগত স্মৃতির জন্য পাবলিক ভিডিও সংরক্ষণ করা সহজ এবং নিরাপদ হওয়া উচিত। downsocial যেকোনো বিরক্তিকর বিজ্ঞাপন ছাড়াই একটি পরিষ্কার ও সুপারফাস্ট ব্রাউজারভিত্তিক অভিজ্ঞতা উপহার দেয়।',
        'arch_h2': 'মাল্টি-প্ল্যাটফর্ম আর্কিটেকচারাল সাপোর্ট',
        'arch_intro': 'একাধিক ওয়েবসাইটে ঘোরার কোনো প্রয়োজন নেই। একটি সার্চ বার থেকেই সব প্ল্যাটফর্ম প্রসেস হয়:',
        'bullets': [
            ('Facebook:', 'রিলস, ওয়াচ ভিডিও ও স্টোরিজ ১০৮০p Full HD কোয়ালিটিতে।'),
            ('Instagram:', 'উচ্চ বিটরেটের রিলস, ক্যারোসেল অ্যালবাম এবং ২৪ ঘণ্টার স্টোরিজ।'),
            ('TikTok:', 'ওয়াটারমার্ক ও লোগো ছাড়া মূল ভিডিও এবং ৩২০kbps MP3 অডিও।'),
            ('YouTube:', '১০৮০p, ২K ও ৪K UHD ভিডিও, শর্টস এবং হাই-কোয়ালিটি MP3 অডিও।'),
            ('Snapchat:', 'স্পটলাইট ভিডিও এবং পাবলিক স্টোরিজ এক্সপায়ার হওয়ার আগেই ডাউনলোড।'),
            ('Meta Threads:', 'থ্রেডস ভিডিও, ভয়েস নোটস এবং ফটো অ্যালবাম।')
        ],
        'priv_h2': 'সম্পূর্ণ গোপনীয়তা ও জিরো ট্র্যাকিং',
        'priv_p': 'আমরা জিরো-নলেজ আর্কিটেকচারে কাজ করি। কোনো লগইন তথ্য বা মিডিয়া ফাইল আমাদের সার্ভারে জমা রাখা হয় না।',
        'faq_title': 'প্রায়শই জিজ্ঞাসিত প্রশ্নাবলী (FAQ)',
        'faqs': [
            ('downsocial কি সত্যি সম্পূর্ণ বিনামূল্যে ব্যবহারযোগ্য?', 'হ্যাঁ, এটি সীমাহীন ডাউনলোডের জন্য শতভাগ ফ্রি।'),
            ('ভিডিও ডাউনলোড করার জন্য কি অ্যাকাউন্ট খুলতে হবে?', 'না, কোনো অ্যাকাউন্ট বা লগইন করার প্রয়োজন নেই।'),
            ('কোন কোন প্ল্যাটফর্ম সমর্থিত?', 'ইউটিউব, টিকটক (ওয়াটারমার্ক ছাড়া), ইনস্টাগ্রাম রিলস, ফেসবুক, স্ন্যাপচ্যাট এবং থ্রেডস।'),
            ('downsocial কি ডাউনলোড করা ভিডিও সংরক্ষণ করে?', 'না, আমাদের সার্ভারে কোনো ফাইল সংরক্ষণ করা হয় না।')
        ]
    },
    'ru': {
        'h1': 'О сервисе downsocial — Бесплатный универсальный загрузчик видео и аудио',
        'intro': 'Добро пожаловать на downsocial.net. Наша цель проста: предоставить каждому быстрый, безопасный и удобный способ скачивать видео, рилс, шортс и аудио MP3 с YouTube, TikTok, Instagram, Facebook, Snapchat и Threads — без водяных знаков, без регистрации и 100% бесплатно.',
        'm_h2': 'Наша Миссия',
        'm_p': 'Мы убеждены, что сохранение общедоступных видеороликов для офлайн-просмотра или личного архива должно быть простым и конфиденциальным. downsocial избавляет от навязчивой рекламы и подозрительных программ благодаря чистому и быстрому браузерному сервису.',
        'arch_h2': 'Комплексная кроссплатформенная поддержка',
        'arch_intro': 'Вам больше не нужны десятки разных сайтов. Одно поле поиска мгновенно извлекает медиапотоки с ведущих платформ:',
        'bullets': [
            ('Facebook:', 'Рилс, видео Watch, истории и посты в разрешении 1080p Full HD.'),
            ('Instagram:', 'Рилс с высоким битрейтом, фотокарусели и 24-часовые истории.'),
            ('TikTok:', 'Чистые видео без водяных знаков и извлечение трендовых аудиодорожек.'),
            ('YouTube:', 'Видеоклипы в 1080p, 2K и 4K Ultra HD, YouTube Shorts и MP3 320 кбит/с.'),
            ('Snapchat:', 'Вертикальные клипы Spotlight и публичные истории до их удаления.'),
            ('Meta Threads:', 'Видеодискуссии, фотогалереи и голосовые заметки.')
        ],
        'priv_h2': 'Полная конфиденциальность и нулевое логирование',
        'priv_p': 'Мы строго соблюдаем архитектуру нулевого разглашения. Никакой регистрации аккаунтов, никаких файлов cookie и никакого сохранения файлов на серверах. Все сессии защищены 256-битным SSL-шифрованием.',
        'faq_title': 'Часто Задаваемые Вопросы',
        'faqs': [
            ('Сервис downsocial действительно бесплатен?', 'Да, downsocial на 100% бесплатен без скрытых подписок и ограничений.'),
            ('Нужна ли регистрация для скачивания?', 'Регистрация или вход в систему не требуются. Все загрузки анонимны.'),
            ('Какие платформы поддерживаются?', 'Поддерживаются YouTube, TikTok (без водяных знаков), Instagram Reels, Facebook, Snapchat и Threads.'),
            ('Хранит ли downsocial загруженные видео?', 'Нет. Мы не храним и не архивируем медиафайлы на своих серверах.')
        ]
    },
    'id': {
        'h1': 'Tentang downsocial — Pengunduh Video & Audio All-in-One Gratis',
        'intro': 'Selamat datang di downsocial.net. Kami merancang platform ini dengan misi jelas: memberi semua orang cara cepat, aman, dan mudah untuk mengunduh video, reels, shorts, dan audio MP3 dari YouTube, TikTok, Instagram, Facebook, Snapchat, dan Threads — tanpa watermark, tanpa daftar akun, dan 100% gratis.',
        'm_h2': 'Misi Kami',
        'm_p': 'Menyimpan video publik untuk belajar luring atau arsip pribadi haruslah praktis dan privat. downsocial menghadirkan antarmuka bersih tanpa iklan menyesatkan langsung dari peramban web Anda.',
        'arch_h2': 'Dukungan Arsitektur Multi-Platform',
        'arch_intro': 'Tidak perlu membuka banyak situs terpisah. Cukup satu kolom pencarian cerdas untuk memproses tautan dari berbagai jaringan populer:',
        'bullets': [
            ('Facebook:', 'Reels, video Watch, dan Stories dalam kualitas 1080p Full HD.'),
            ('Instagram:', 'Reels beresolusi tinggi, album foto karosel, dan Stories 24 jam.'),
            ('TikTok:', 'Video bersih tanpa watermark melompat dan ekstraksi audio MP3 320kbps.'),
            ('YouTube:', 'Video 1080p, 2K, 4K UHD, YouTube Shorts, dan audio MP3 studio.'),
            ('Snapchat:', 'Video vertikal Spotlight dan Stories publik sebelum kedaluwarsa.'),
            ('Meta Threads:', 'Video diskusi, album foto, dan pesan audio.')
        ],
        'priv_h2': 'Privasi Penuh & Nol Pencatatan',
        'priv_p': 'Kami menerapkan sistem zero-knowledge. Tanpa pendaftaran, tanpa pelacakan riwayat unduhan, dan tanpa menyimpan file di server. Semua unduhan terenkripsi aman.',
        'faq_title': 'Pertanyaan yang Sering Diajukan',
        'faqs': [
            ('Apakah downsocial benar-benar gratis?', 'Ya, downsocial 100% gratis dengan unduhan tanpa batas.'),
            ('Apakah saya perlu mendaftar akun?', 'Tidak perlu registrasi atau login. Anda dapat mengunduh secara anonim.'),
            ('Platform apa saja yang didukung?', 'Mendukung YouTube, TikTok (tanpa watermark), Instagram Reels, Facebook, Snapchat, dan Threads.'),
            ('Apakah downsocial menyimpan file yang diunduh?', 'Tidak. Kami tidak pernah menyimpan file media di server kami.')
        ]
    },
    'zh': {
        'h1': '关于 downsocial — 免费全能社交媒体视频与音频极速下载器',
        'intro': '欢迎访问 downsocial.net。我们打造该平台的初衷清晰纯粹：为全球用户提供快捷、安全、零门槛的音视频下载方案，轻松解析 YouTube、TikTok、Instagram、Facebook、Snapchat 与 Threads 的视频、Reels、Shorts 与 MP3 音频——去除水印、无需注册，且永久 100% 免费。',
        'm_h2': '我们的使命',
        'm_p': '为离线学习、旅行通勤与个人数字归档保存公开视频应当是一件简单且兼顾隐私的事。传统下载工具充斥着欺诈性弹窗、强制安装第三方软件或画质劣化等问题。downsocial 依托云端直连协议，打造真正纯净高效的原生网页下载体验。',
        'arch_h2': '全平台专业架构支持',
        'arch_intro': '告别在不同站点间频繁切换的繁琐体验，单个输入框直达主流平台媒体流捕获：',
        'bullets': [
            ('Facebook：', '1080p 全高清 Reels、公开动态视频、Watch 专区剧集及 Stories 快拍。'),
            ('Instagram：', '超清高码率 Reels、多图相册轮播（Carousel）及 24 小时快拍。'),
            ('TikTok：', '100% 自动剥离浮动水印与用户标贴，同步提取 320kbps 热门背景音乐。'),
            ('YouTube：', '最高支持 1080p、2K、4K 原画质解析，支持 Shorts 极速下载及高保真 MP3 转码。'),
            ('Snapchat：', 'Spotlight 9:16 竖版视频与公开故事，在时效过期前无痕保存。'),
            ('Meta Threads：', '高清讨论视频、多图动态相册及原声语音留言。')
        ],
        'priv_h2': '零数据驻留与极致隐私防护',
        'priv_p': '我们严格恪守“零知识（Zero-Knowledge）”安全准则。不设用户注册系统、不使用追踪性 Cookie、更不在服务器端持久化存储任何媒体文件。全流程采用 256 位 SSL 强加密保护。',
        'faq_title': '常见问题解答 (FAQ)',
        'faqs': [
            ('downsocial 真的完全免费吗？', '是的，downsocial 永久 100% 免费，无任何隐形收费或每日次数限制。'),
            ('下载视频需要注册或登录账户吗？', '完全不需要。无需提供任何个人信息，即开即用，全面保护匿名性。'),
            ('目前支持哪些社交媒体平台？', '全面支持 YouTube、TikTok（无水印）、Instagram Reels、Facebook、Snapchat 与 Threads。'),
            ('downsocial 会在服务器保存我下载的文件吗？', '绝不会。所有媒体流均由官方 CDN 直连您的浏览器，服务器不留存任何副本。')
        ]
    },
    'ur': {
        'h1': 'ڈاؤن سوشل کے بارے میں — مفت آل اِن ون ویڈیو اور آڈیو ڈاؤنلوڈر',
        'intro': 'downsocial.net پر خوش آمدید۔ ہمارا مشن بالکل واضح اور شفاف ہے: فیس بک، انسٹاگرام، ٹک ٹاک، یوٹیوب، سنیپ چیٹ اور تھریڈز سے ویڈیوز، ریلز، شارٹس اور MP3 آڈیو ڈاؤن لوڈ کرنے کی تیز ترین، محفوظ ترین اور بغیر واٹر مارک مکمل مفت سہولت فراہم کرنا۔',
        'm_h2': 'ہمارا مشن',
        'm_p': 'ہمارا ماننا ہے کہ تعلیمی مقاصد، سفر یا ذاتی یادوں کے لیے پبلک ویڈیوز کو محفوظ کرنا آسان اور پرائیویٹ ہونا چاہیے۔ روایتی ڈاؤنلوڈرز میں دھوکہ دہی والے اشتہارات اور وائرسز بھرے ہوتے ہیں۔ ڈاؤن سوشل ایک صاف شفاف اور محفوظ براؤزر ٹول مہیا کرتا ہے۔',
        'arch_h2': 'ملٹی پلیٹ فارم سپورٹ',
        'arch_intro': 'مختلف ویب سائٹس پر جانے کی کوئی ضرورت نہیں۔ ایک ہی سرچ باکس تمام بڑی سوشل میڈیا سروسز کو سپورٹ کرتا ہے:',
        'bullets': [
            ('Facebook:', 'ریلز، واچ ویڈیوز اور 24 گھنٹے کی اسٹوریز 1080p Full HD میں۔'),
            ('Instagram:', 'ہائی بٹ ریٹ ریلز، کیروسل فوٹو البمز اور اسٹوریز بغیر واٹر مارک کے۔'),
            ('TikTok:', 'واٹر مارک کے بغیر صاف شفاف ویڈیوز اور 320kbps MP3 آڈیو۔'),
            ('YouTube:', '1080p، 2K اور 4K UHD ویڈیوز، یوٹیوب شارٹس اور بہترین MP3 آڈیو۔'),
            ('Snapchat:', 'اسپاٹ لائٹ ویڈیوز اور پبلک اسٹوریز ختم ہونے سے پہلے ڈاؤن لوڈ کریں۔'),
            ('Meta Threads:', 'تھریڈز ویڈیوز، وائس نوٹس اور فوٹو البمز۔')
        ],
        'priv_h2': 'مکمل رازداری اور زیرو لاگ پالیسی',
        'priv_p': 'ہم آپ کی رازداری کا مکمل احترام کرتے ہیں۔ نہ کوئی اکاؤنٹ بنانے کی ضرورت ہے، نہ کوکیز ٹریک کی جاتی ہیں اور نہ ہی ہمارے سرور پر کوئی ویڈیو فائل محفوظ ہوتی ہے۔',
        'faq_title': 'اکثر پوچھے جانے والے سوالات (FAQ)',
        'faqs': [
            ('کیا ڈاؤن سوشل واقعی مکمل مفت ہے؟', 'جی ہاں، ڈاؤن سوشل لامحدود ڈاؤن لوڈنگ کے ساتھ 100% مفت ہے اور کوئی پوشیدہ فیس نہیں ہے۔'),
            ('کیا ویڈیو ڈاؤن لوڈ کرنے کے لیے اکاؤنٹ بنانا ضروری ہے؟', 'نہیں، کسی رجسٹریشن یا لاگ ان کی بالکل ضرورت نہیں ہے۔ آپ فوری طور پر گمنام طریقے سے ڈاؤن لوڈ کر سکتے ہیں۔'),
            ('کون سے پلیٹ فارمز سپورٹڈ ہیں؟', 'یوٹیوب، ٹک ٹاک (بغیر واٹر مارک)، انسٹاگرام ریلز، فیس بک، سنیپ چیٹ اور تھریڈز۔'),
            ('کیا ڈاؤن سوشل ڈاؤن لوڈ کی گئی ویڈیوز اپنے پاس محفوظ رکھتا ہے؟', 'ہرگز نہیں۔ ہم زیرو نالج پالیسی پر عمل کرتے ہیں اور سرور پر کوئی فائل محفوظ نہیں کرتے۔')
        ]
    }
}

def render_about_html(t):
    bullets_html = ''.join([f'<li><strong>{b[0]}</strong> {b[1]}</li>' for b in t['bullets']])
    faqs_html = ''.join([f'''<div class="accordion-item">
    <div class="accordion-header"><span>{q}</span><i class="fas fa-plus"></i></div>
    <div class="accordion-body"><p>{a}</p></div>
</div>''' for q, a in t['faqs']])
    return f'''<div class="page-content-wrapper">
    <div class="article-container">
        <h1>{t['h1']}</h1>
        <p class="article-intro">{t['intro']}</p>
        <h2>{t['m_h2']}</h2>
        <p>{t['m_p']}</p>
        <h2>{t['arch_h2']}</h2>
        <p>{t['arch_intro']}</p>
        <ul>{bullets_html}</ul>
        <h2>{t['priv_h2']}</h2>
        <p>{t['priv_p']}</p>
    </div>
    <div class="faq-section" style="max-width: 900px; margin: 30px auto 40px; padding: 25px 20px;">
        <h2 class="section-title">{t['faq_title']}</h2>
        <div class="accordion">{faqs_html}</div>
    </div>
</div>'''

print("About template compiled.")
