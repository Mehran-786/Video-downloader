# scratch/enrich_all_static_languages.py
# Provides full 12-language dictionaries for FEATURES, CONTACT, PRIVACY, TERMS so zero English remains!

FEATURES_ALL = {
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
    'fr': {
        'h1': 'Fonctionnalités et Spécifications Techniques',
        'intro': 'Une vue d’ensemble détaillée de notre architecture cloud, de la vitesse d’encodage et des formats pris en charge.',
        'core_h2': 'Fonctionnalités Principales & Points Forts',
        'cards': [
            ('fas fa-globe', '6 Plateformes en un Seul Outil', 'Support complet pour YouTube, TikTok, Instagram, Facebook, Snapchat et Threads.'),
            ('fas fa-tv', 'Ultra HD 4K & 1080p', 'Téléchargements sans perte en Full HD, 2K et 4K avec les couleurs d’origine.'),
            ('fas fa-magic', 'Suppression de Filigrane TikTok', 'Extraction 100% propre sans le logo TikTok rebondissant.'),
            ('fas fa-music', 'Conversion MP3 en Temps Réel', 'Moteur audio FFmpeg intégré extrayant du MP3 haute fidélité 320 kbps.'),
            ('fas fa-shield-alt', 'Zéro Pubs, Zéro Pop-ups, Zéro Logs', 'Interface épurée sans publicité intrusive et respect absolu de la vie privée.'),
            ('fas fa-bolt', 'Streaming CDN Instantané', 'Téléchargement direct et ultrarapide depuis les serveurs officiels.')
        ],
        'tech_h2': 'Spécifications Techniques Détaillées',
        'specs_cols': ('Attribut', 'Norme et Capacité'),
        'specs_rows': [
            ('Réseaux Pris en Charge', 'YouTube, TikTok, Instagram, Facebook, Snapchat, Meta Threads'),
            ('Formats Vidéo', 'MP4 (4K, 2K, 1080p Full HD, 720p HD)'),
            ('Formats Audio', 'MP3 Audio (192 kbps / 320 kbps Qualité Studio via FFmpeg)'),
            ('Filigrane', '100% Automatique et sans filigrane'),
            ('Carrousels Multi-Photos', 'Déballage complet des albums photos et diaporamas'),
            ('Compatibilité', 'Multiplateforme : Safari, Chrome, Firefox, Edge'),
            ('Authentification', 'Aucune inscription ni mot de passe requis')
        ],
        'comp_h2': 'Comparaison Directe avec les Autres Outils',
        'comp_p': 'Découvrez les avantages de downsocial face aux téléchargeurs traditionnels :',
        'comp_cols': ('Critère', 'downsocial.net', 'Téléchargeurs Classiques (SaveFrom, SnapTik, Y2Mate)'),
        'comp_rows': [
            ('Couverture Plateformes', 'Tout-en-Un (6 Plateformes)', 'Fragmenté / Une seule plateforme'),
            ('Gestion du Filigrane', '100% Propre et sans marque', 'Filigrane visible / Inconstant'),
            ('Sécurité et Publicités', 'Sûr et Propre (Zéro Pop-up)', 'Publicités agressives et trompeuses'),
            ('Qualité Audio', 'MP3 Studio 320 kbps', 'Basse qualité ou absent'),
            ('Compte Requis', 'Aucun (100% Anonyme)', 'Exige une inscription ou un logiciel')
        ]
    },
    'de': {
        'h1': 'Plattform-Features und Technische Spezifikationen',
        'intro': 'Umfassender Überblick über unsere Cloud-Transkodierungsarchitektur und alle unterstützten Medienformate.',
        'core_h2': 'Kernkompetenzen & Highlights',
        'cards': [
            ('fas fa-globe', '6 Plattformen in Einem Tool', 'Vollständige Unterstützung für YouTube, TikTok, Instagram, Facebook, Snapchat und Threads.'),
            ('fas fa-tv', '4K & 1080p Ultra HD', 'Verlustfreie Downloads in 1080p, 2K und 4K mit brillanten Farben.'),
            ('fas fa-magic', 'Wasserzeichenfreie TikTok-Videos', 'Automatisches Entfernen von TikTok-Wasserzeichen und Benutzernamen.'),
            ('fas fa-music', 'Echtzeit-MP3-Konvertierung', 'Integrierte FFmpeg-Audio-Engine für kristallklares 320kbps MP3-Audio.'),
            ('fas fa-shield-alt', 'Keine Werbung, Popups & Logs', 'Saubere Weboberfläche ohne trügerische Banner und ohne Datenprotokolle.'),
            ('fas fa-bolt', 'Direktes CDN-Streaming', 'Highspeed-Proxies ermöglichen sofortige Downloads ohne Wartezeiten.')
        ],
        'tech_h2': 'Detaillierte Technische Spezifikationen',
        'specs_cols': ('Spezifikationsattribut', 'Fähigkeit und Standard'),
        'specs_rows': [
            ('Unterstützte Netzwerke', 'YouTube, TikTok, Instagram, Facebook, Snapchat, Meta Threads'),
            ('Videoformate', 'MP4 (4K, 2K, 1080p Full HD, 720p HD)'),
            ('Audioformate', 'MP3-Audio (192 kbps / 320 kbps Studioqualität)'),
            ('Wasserzeichen-Entfernung', '100% automatische saubere Extraktion'),
            ('Karussell-Beiträge', 'Vollständige Extraktion von Foto- und Videokarussells'),
            ('Kompatibilität', 'Plattformübergreifend: Safari, Chrome, Firefox, Edge'),
            ('Kontoerfordernis', 'Keine Registrierung oder Installation notwendig')
        ],
        'comp_h2': 'Vergleich mit Anderen Downloadern',
        'comp_p': 'So schneidet downsocial im direkten Vergleich ab:',
        'comp_cols': ('Kriterium', 'downsocial.net', 'Herkömmliche Downloader (SaveFrom, SnapTik, Y2Mate)'),
        'comp_rows': [
            ('Plattformabdeckung', 'All-in-One (6 Netzwerke)', 'Nur einzelne Netzwerke'),
            ('Wasserzeichen', '100% sauber ohne Logo', 'Oft mit störenden Logos'),
            ('Werbung & Sicherheit', 'Sauber & Sicher (Keine Popups)', 'Aggressive Werbebanner und Risiken'),
            ('Audioqualität', '320kbps Studio-MP3', 'Geringe Qualität oder fehlt'),
            ('Benutzerkonto', 'Keines (100% anonym)', 'Verlangt Login oder App-Installation')
        ]
    },
    'hi': {
        'h1': 'डाउनसोशल की विशेषताएं और तकनीकी विनिर्देश',
        'intro': 'डाउनसोशल के आधुनिक क्लाउड आर्किटेक्चर, सुपरफास्ट ट्रांसकोडिंग और समर्थित मीडिया प्रारूपों का संपूर्ण विवरण।',
        'core_h2': 'प्रमुख क्षमताएं और मुख्य विशेषताएं',
        'cards': [
            ('fas fa-globe', '6 प्लेटफ़ॉर्म एक ही टूल में', 'YouTube, TikTok, Instagram, Facebook, Snapchat और Threads के लिए एकीकृत समाधान।'),
            ('fas fa-tv', '4K और 1080p अल्ट्रा एचडी', 'मूल गुणवत्ता, रंगों और स्पष्टता के साथ 1080p, 2K और 4K वीडियो डाउनलोड करें।'),
            ('fas fa-magic', 'बिना वॉटरमार्क टिकटॉक वीडियो', 'सर्वर द्वारा टिकटॉक का लोगो और यूजरनेम स्वतः हटाकर साफ वीडियो प्रदान किया जाता है।'),
            ('fas fa-music', 'रीयल-टाइम 320kbps MP3 ऑडियो', 'FFmpeg ऑडियो इंजन वीडियो से 320kbps तक का उच्च गुणवत्ता वाला MP3 निकालता है।'),
            ('fas fa-shield-alt', 'विज्ञापन, पॉपअप और लॉग्स से मुक्त', 'बिना किसी भ्रामक विज्ञापन और वायरस के सुरक्षित व निजी ब्राउज़िंग अनुभव।'),
            ('fas fa-bolt', 'त्वरित सीडीएन स्ट्रीमिंग', 'तेज गति वाले सर्वर बिना किसी कतार के तुरंत वीडियो डाउनलोड करते हैं।')
        ],
        'tech_h2': 'विस्तृत तकनीकी विनिर्देश',
        'specs_cols': ('विशेषता', 'मानक और क्षमता'),
        'specs_rows': [
            ('समर्थित नेटवर्क', 'YouTube, TikTok, Instagram, Facebook, Snapchat, Meta Threads'),
            ('वीडियो प्रारूप', 'MP4 (4K, 2K, 1080p Full HD, 720p HD)'),
            ('ऑडियो प्रारूप', 'MP3 ऑडियो (192 kbps / 320 kbps स्टूडियो गुणवत्ता)'),
            ('वॉटरमार्क हटाना', '100% स्वचालित और स्वच्छ निष्कर्षण'),
            ('मल्टी-मीडिया पोस्ट्स', 'इंस्टाग्राम और थ्रेड्स के फोटो कैरोसेल की पूरी सुविधा'),
            ('प्लेटफ़ॉर्म संगतता', 'आईफोन (Safari), एंड्रॉइड (Chrome), विंडोज और मैक'),
            ('लॉगिन आवश्यकता', 'कोई खाता या पासवर्ड आवश्यक नहीं')
        ],
        'comp_h2': 'पारंपरिक डाउनलोडर्स के साथ तुलना',
        'comp_p': 'देखें कि डाउनसोशल अन्य डाउनलोडर्स से कैसे बेहतर है:',
        'comp_cols': ('मूल्यांकन मानदंड', 'downsocial.net', 'पारंपरिक डाउनलोडर (SaveFrom, SnapTik, Y2Mate)'),
        'comp_rows': [
            ('प्लेटफ़ॉर्म कवरेज', 'ऑल-इन-वन (6 प्लेटफ़ॉर्म)', 'अलग-अलग / केवल एक प्लेटफ़ॉर्म'),
            ('वॉटरमार्क हैंडलिंग', '100% बिना वॉटरमार्क', 'वॉटरमार्क रह जाता है'),
            ('सुरक्षा और विज्ञापन', 'सुरक्षित और विज्ञापन-मुक्त', 'अत्यधिक विज्ञापन और वायरस का खतरा'),
            ('ऑडियो निष्कर्षण', '320kbps स्टूडियो MP3', 'कम गुणवत्ता या अनुपलब्ध'),
            ('अकाउंट की आवश्यकता', 'कोई नहीं (100% अनाम)', 'सॉफ़्टवेयर या लॉगिन की मांग')
        ]
    },
    'ar': {
        'h1': 'ميزات المنصة والمواصفات التقنية',
        'intro': 'نظرة شاملة على بنيتنا السحابية المتقدمة، وسرعة استخراج الوسائط، والتنسيقات المدعومة عبر جميع شبكات التواصل.',
        'core_h2': 'القدرات الأساسية والميزات البارزة',
        'cards': [
            ('fas fa-globe', '6 منصات في أداة واحدة', 'دعم شامل ليوتيوب، تيك توك، إنستغرام، فيسبوك، سناب شات، وثريدز.'),
            ('fas fa-tv', 'فائق الوضوح 4K و 1080p', 'تنزيل مقاطع الفيديو بأعلى دقة أصلية دون ضغط أو تقليل للألوان.'),
            ('fas fa-magic', 'إزالة العلامة المائية بدون فقدان جودة', 'إزالة تلقائية لشعار تيك توك للحصول على فيديو نقي وجاهز للمشاركة.'),
            ('fas fa-music', 'تحويل فوري إلى MP3 عالي الدقة', 'محرك FFmpeg مدمج لاستخراج الصوتيات بنقاء 320kbps استوديو.'),
            ('fas fa-shield-alt', 'بدون إعلانات أو نوافذ منبثقة أو سجلات', 'واجهة نظيفة وخالية من الإعلانات المزعجة وحماية تامة لبياناتك.'),
            ('fas fa-bolt', 'بث مباشر وسريع عبر CDN', 'اتصال مباشر بخوادم التوصيل السحابي بدون أي فترات انتظار.')
        ],
        'tech_h2': 'المواصفات التقنية الدقيقة',
        'specs_cols': ('خاصية المواصفات', 'المعيار والقدرة'),
        'specs_rows': [
            ('الشبكات المدعومة', 'يوتيوب، تيك توك، إنستغرام، فيسبوك، سناب شات، ميتا ثريدز'),
            ('تنسيقات الفيديو', 'MP4 (4K 2160p, 2K 1440p, 1080p Full HD, 720p HD)'),
            ('تنسيقات الصوت', 'صوت MP3 (192 kbps / 320 kbps استوديو)'),
            ('إزالة العلامة المائية', 'استخراج نقي 100% بدون أي شعارات مائية'),
            ('ألبومات الصور والوسائط', 'فك وتنزيل كامل لألبومات الصور المتعددة في إنستغرام وثريدز'),
            ('التوافقية', 'متوافق مع آيفون (سفاري)، أندرويد (كروم)، ماك وويندوز'),
            ('متطلبات الدخول', 'لا يلزم أي تسجيل دخول أو تثبيت برامج')
        ],
        'comp_h2': 'المقارنة المباشرة مع الخدمات التقليدية',
        'comp_p': 'تعرف على تفوق downsocial على المواقع القديمة:',
        'comp_cols': ('معيار التقييم', 'downsocial.net', 'المحملات التقليدية (SaveFrom, SnapTik, Y2Mate)'),
        'comp_rows': [
            ('تغطية المنصات', 'شامل الكل (6 منصات كبرى)', 'منصة واحدة فقط أو مجزأة'),
            ('معالجة العلامة المائية', 'نقي 100% وبدون علامات', 'يترك علامة مائية أحياناً'),
            ('الأمان والإعلانات', 'نظيف وآمن (بدون منبثقات)', 'إعلانات خادعة ونوافذ خطرة'),
            ('استخراج الصوت', 'صوت MP3 نقي 320kbps', 'جودة منخفضة 128kbps أو غير مدعوم'),
            ('طلب الحساب', 'لا يوجد (مجهول 100%)', 'يطلب تسجيل أو تثبيت برامج')
        ]
    },
    'pt': {
        'h1': 'Recursos da Plataforma e Especificações Técnicas',
        'intro': 'Visão abrangente sobre nossa arquitetura em nuvem, desempenho de transcodificação e formatos suportados.',
        'core_h2': 'Capacidades Principais e Destaques',
        'cards': [
            ('fas fa-globe', '6 Plataformas em Uma Ferramenta', 'Suporte para YouTube, TikTok, Instagram, Facebook, Snapchat e Threads.'),
            ('fas fa-tv', 'Ultra HD 4K e 1080p', 'Downloads nítidos em 1080p, 2K e 4K com fidelidade visual absoluta.'),
            ('fas fa-magic', 'Remoção de Marca d’Água sem Perda', 'Vídeos do TikTok limpos e sem o logotipo flutuante.'),
            ('fas fa-music', 'Conversão para MP3 em Tempo Real', 'Motor FFmpeg extrai faixas de áudio cristalinas em 320kbps.'),
            ('fas fa-shield-alt', 'Zero Anúncios, Popups e Logs', 'Interface limpa, moderna e com total respeito à sua privacidade.'),
            ('fas fa-bolt', 'Streaming CDN Instantâneo', 'Servidores de alta velocidade entregam seus arquivos sem espera.')
        ],
        'tech_h2': 'Especificações Técnicas Detalhadas',
        'specs_cols': ('Atributo', 'Padrão e Capacidade'),
        'specs_rows': [
            ('Redes Sociais', 'YouTube, TikTok, Instagram, Facebook, Snapchat, Meta Threads'),
            ('Formatos de Vídeo', 'MP4 (4K, 2K, 1080p Full HD, 720p HD)'),
            ('Formatos de Áudio', 'MP3 Audio (192 kbps / 320 kbps Qualidade de Estúdio)'),
            ('Marca d’Água', '100% Automático e Sem Marcas'),
            ('Álbuns e Carrosséis', 'Descompactação de carrosséis de fotos do Instagram e Threads'),
            ('Compatibilidade', 'Multiplataforma: Safari, Chrome, Firefox, Edge'),
            ('Autenticação', 'Sem necessidade de login, senha ou extensões')
        ],
        'comp_h2': 'Comparação Direta com Alternativas',
        'comp_p': 'Veja por que o downsocial supera os baixadores tradicionais:',
        'comp_cols': ('Critério', 'downsocial.net', 'Baixadores Convencionais (SaveFrom, SnapTik, Y2Mate)'),
        'comp_rows': [
            ('Cobertura', 'Tudo-em-Um (6 Plataformas)', 'Fragmentado / Apenas uma'),
            ('Marcas d’Água', '100% Limpo e sem logo', 'Deixa marcas d’água'),
            ('Segurança e Anúncios', 'Limpo e Seguro (Sem Popups)', 'Anúncios agressivos e invasivos'),
            ('Extração de Áudio', 'MP3 de Estúdio 320kbps', 'Baixa qualidade ou indisponível'),
            ('Conta de Usuário', 'Nenhuma (100% Anônimo)', 'Exige cadastro ou programas')
        ]
    },
    'bn': {
        'h1': 'প্ল্যাটফর্মের ফিচার এবং টেকনিক্যাল স্পেসিফিকেশন',
        'intro': 'আমাদের ক্লাউড ট্রান্সকোডিং আর্কিটেকচার, দ্রুত ডাউনলোড পারফরম্যান্স এবং সমর্থিত সমস্ত ফরম্যাটের বিস্তারিত ওভারভিউ।',
        'core_h2': 'মূল বৈশিষ্ট্য ও হাইলাইটস',
        'cards': [
            ('fas fa-globe', 'একটি টুলে ৬টি প্ল্যাটফর্ম', 'ইউটিউব, টিকটক, ইনস্টাগ্রাম, ফেসবুক, স্ন্যাপচ্যাট এবং থ্রেডসের জন্য সমন্বিত প্ল্যাটফর্ম।'),
            ('fas fa-tv', '৪K ও ১০৮০p আল্ট্রা HD', '১০৮০p, ২K ও ৪K রেজোলিউশনে আসল কালার ও ক্ল্যারিটি সহ ভিডিও ডাউনলোড।'),
            ('fas fa-magic', 'ওয়াটারমার্কহীন টিকটক ভিডিও', 'টিকটকের লোগো এবং ইউজারনেম স্বয়ংক্রিয়ভাবে রিমুভ করে সম্পূর্ণ ফ্রেশ ভিডিও প্রদান।'),
            ('fas fa-music', 'রিয়েল-টাইম ৩২০kbps MP3', 'ইনবিল্ট FFmpeg ইঞ্জিন যে কোনো ভিডিও থেকে স্টুডিও কোয়ালিটি ৩২০kbps MP3 তৈরি করে।'),
            ('fas fa-shield-alt', 'বিজ্ঞাপন, পপ-আপ ও লগ মুক্ত', 'কোনো বিভ্রান্তিকর বিজ্ঞাপন বা ভাইরাস নেই, সম্পূর্ণ সুরক্ষিত ও প্রাইভেট।'),
            ('fas fa-bolt', 'দ্রুততম সিডিএন স্ট্রিমিং', 'হাই-স্পিড সার্ভার প্রক্সি নিমেষেই ফাইল ডাউনলোড সম্পন্ন করে।')
        ],
        'tech_h2': 'বিস্তারিত প্রযুক্তিগত স্পেসিফিকেশন',
        'specs_cols': ('বৈশিষ্ট্য', 'মান এবং সক্ষমতা'),
        'specs_rows': [
            ('সমর্থিত নেটওয়ার্ক', 'ইউটিউব, টিকটক, ইনস্টাগ্রাম, ফেসবুক, স্ন্যাপচ্যাট, মেটা থ্রেডস'),
            ('ভিডিও ফরম্যাট', 'MP4 (4K, 2K, 1080p Full HD, 720p HD)'),
            ('অডিও ফরম্যাট', 'MP3 Audio (192 kbps / 320 kbps স্টুডিও কোয়ালিটি)'),
            ('ওয়াটারমার্ক রিমুভাল', '১০০% অটোমেটিক ও ক্লিন এক্সট্রাকশন'),
            ('ক্যারোসেল ও অ্যালবাম', 'ইনস্টাগ্রাম ও থ্রেডসের মাল্টিপল ফটো ক্যারোসেল সাপোর্ট'),
            ('ডিভাইস সাপোর্ট', 'আইফোন (Safari), অ্যান্ড্রয়েড (Chrome), ম্যাক এবং উইন্ডোজ'),
            ('লগইন রিকোয়ারমেন্ট', 'কোনো অ্যাকাউন্ট বা সফটওয়্যার ইন্সটলেশনের প্রয়োজন নেই')
        ],
        'comp_h2': 'অন্যান্য ডাউনলোডারদের সাথে তুলনা',
        'comp_p': 'কেন ডাউনসোশ্যাল অন্যান্য সার্ভিস থেকে বহুগুণে সেরা:',
        'comp_cols': ('মূল্যায়নের মাপকাঠি', 'downsocial.net', 'গতানুগতিক ডাউনলোডার (SaveFrom, SnapTik, Y2Mate)'),
        'comp_rows': [
            ('প্ল্যাটফর্ম কভারেজ', 'অল-ইন-ওয়ান (৬টি প্ল্যাটফর্ম)', 'আলাদা আলাদা অথবা একটি মাত্র সাইট'),
            ('ওয়াটারমার্ক', '১০০% ক্লিন ও ওয়াটারমার্কহীন', 'অনেক সময় ওয়াটারমার্ক থেকে যায়'),
            ('নিরাপত্তা ও বিজ্ঞাপন', 'নিরাপদ (জিরো পপ-আপ)', 'বিরক্তিকর ও ক্ষতিকর পপ-আপ বিজ্ঞাপন'),
            ('অডিও কোয়ালিটি', '৩২০kbps স্টুডিও MP3', 'কম কোয়ালিটি অথবা অনুপস্থিত'),
            ('অ্যাকাউন্টের প্রয়োজনীয়তা', 'কোনোটিই নয় (১০০% অজ্ঞাতনামা)', 'অ্যাকাউন্ট বা অ্যাপ ইন্সটল করতে বলে')
        ]
    },
    'ru': {
        'h1': 'Функции платформы и технические характеристики',
        'intro': 'Подробный обзор специализированной облачной архитектуры, скорости конвертации и поддерживаемых медиаформатов.',
        'core_h2': 'Ключевые возможности и преимущества',
        'cards': [
            ('fas fa-globe', '6 платформ в одном инструменте', 'Полная поддержка YouTube, TikTok, Instagram, Facebook, Snapchat и Threads.'),
            ('fas fa-tv', '4K и 1080p Ultra HD', 'Загрузка кристально чистых видео в Full HD, 2K и 4K с сохранением цветов оригинала.'),
            ('fas fa-magic', 'Удаление водяных знаков TikTok', 'Автоматическое удаление логотипа TikTok на сервере без потери качества.'),
            ('fas fa-music', 'Мгновенная конвертация в MP3', 'Встроенный аудиодвижок FFmpeg извлекает чистый звук студийного качества 320 кбит/с.'),
            ('fas fa-shield-alt', 'Без рекламы, всплывающих окон и логов', 'Чистый веб-интерфейс без опасных редиректов и с абсолютной анонимностью.'),
            ('fas fa-bolt', 'Прямой CDN-стриминг', 'Высокоскоростные серверные прокси отдают файлы напрямую без очередей.')
        ],
        'tech_h2': 'Подробные технические спецификации',
        'specs_cols': ('Параметр', 'Стандарт и возможности'),
        'specs_rows': [
            ('Поддерживаемые сети', 'YouTube, TikTok, Instagram, Facebook, Snapchat, Meta Threads'),
            ('Форматы видео', 'MP4 (4K, 2K, 1080p Full HD, 720p HD)'),
            ('Форматы аудио', 'MP3 Audio (192 кбит/с / 320 кбит/с студийное качество)'),
            ('Водяные знаки', '100% автоматическое удаление логотипов'),
            ('Фотокарусели', 'Полная распаковка альбомов Instagram и постов Threads'),
            ('Совместимость', 'Кроссплатформенно: Safari, Chrome, Firefox, Edge'),
            ('Авторизация', 'Никакой регистрации и паролей не требуется')
        ],
        'comp_h2': 'Сравнение с аналогами',
        'comp_p': 'Преимущества downsocial перед устаревшими сервисами:',
        'comp_cols': ('Критерий', 'downsocial.net', 'Обычные загрузчики (SaveFrom, SnapTik, Y2Mate)'),
        'comp_rows': [
            ('Охват платформ', 'Все в одном (6 сетей)', 'Только одна или две сети'),
            ('Водяные знаки', '100% чистые видео', 'Часто оставляет логотипы'),
            ('Безопасность', 'Безопасно и чисто (без попапов)', 'Агрессивные всплывающие баннеры'),
            ('Качество аудио', 'Студийный MP3 320 кбит/с', 'Низкое качество 128 кбит/с'),
            ('Аккаунт', 'Не требуется (100% анонимно)', 'Требует логин или установку софта')
        ]
    },
    'id': {
        'h1': 'Fitur Platform & Spesifikasi Teknis',
        'intro': 'Ulasan komprehensif mengenai arsitektur cloud cerdas, kecepatan transkoding, dan format media yang didukung.',
        'core_h2': 'Kemampuan Utama & Keunggulan',
        'cards': [
            ('fas fa-globe', '6 Platform dalam Satu Alat', 'Mendukung YouTube, TikTok, Instagram, Facebook, Snapchat, dan Threads secara terpadu.'),
            ('fas fa-tv', 'Ultra HD 4K & 1080p', 'Unduh video Full HD, 2K, dan 4K dengan ketajaman warna asli dari kreator.'),
            ('fas fa-magic', 'Bebas Watermark TikTok', 'Penghapusan logo dan username TikTok otomatis di server tanpa kompresi.'),
            ('fas fa-music', 'Konversi MP3 Real-Time', 'Mesin audio FFmpeg terintegrasi menghasilkan audio MP3 jernih 320kbps.'),
            ('fas fa-shield-alt', 'Tanpa Iklan, Pop-up & Log', 'Antarmuka modern tanpa banner jebakan dan perlindungan privasi ketat.'),
            ('fas fa-bolt', 'Streaming CDN Cepat', 'Server proxy berkecepatan tinggi mengirimkan file langsung tanpa jeda antrean.')
        ],
        'tech_h2': 'Spesifikasi Teknis Lengkap',
        'specs_cols': ('Atribut Spesifikasi', 'Kemampuan & Standar'),
        'specs_rows': [
            ('Jaringan yang Didukung', 'YouTube, TikTok, Instagram, Facebook, Snapchat, Meta Threads'),
            ('Format Video', 'MP4 (4K, 2K, 1080p Full HD, 720p HD)'),
            ('Format Audio', 'Audio MP3 (192 kbps / 320 kbps Kualitas Studio)'),
            ('Watermark', 'Ekstraksi 100% Bersih dan Otomatis'),
            ('Postingan Karosel', 'Bongkar semua slide foto Instagram dan Threads'),
            ('Kompatibilitas', 'Multi-platform: Safari, Chrome, Firefox, Edge'),
            ('Persyaratan Akun', 'Tidak perlu registrasi atau unduh aplikasi')
        ],
        'comp_h2': 'Perbandingan dengan Pengunduh Lain',
        'comp_p': 'Alasan downsocial lebih unggul dibanding pengunduh lawas:',
        'comp_cols': ('Kriteria Evaluasi', 'downsocial.net', 'Pengunduh Konvensional (SaveFrom, SnapTik, Y2Mate)'),
        'comp_rows': [
            ('Cakupan Platform', 'All-in-One (6 Platform)', 'Terpisah / Hanya satu platform'),
            ('Penanganan Watermark', '100% Bersih tanpa logo', 'Masih ada watermark'),
            ('Keamanan & Iklan', 'Aman (Tanpa Pop-up)', 'Banyak iklan berisiko dan pop-up'),
            ('Kualitas Audio', 'MP3 Studio 320kbps', 'Kualitas rendah atau tidak tersedia'),
            ('Akun Pengguna', 'Tidak Perlu (100% Anonim)', 'Mengharuskan daftar atau pasang aplikasi')
        ]
    },
    'zh': {
        'h1': '平台核心功能与技术规格总览',
        'intro': '深入解析 downsocial 针对全球主流社交网络的分布式云端转码架构、原画质解析标准与多媒体格式支持。',
        'core_h2': '核心技术优势与产品亮点',
        'cards': [
            ('fas fa-globe', '一站式整合 6 大主流网络', '完美整合 YouTube、TikTok、Instagram、Facebook、Snapchat 与 Threads。'),
            ('fas fa-tv', '4K 与 1080p 原画质无损直链', '直连官方媒体源，完整保留 Full HD、2K 及 4K Ultra HD 官方色彩动态。'),
            ('fas fa-magic', '100% 自动剥离 TikTok 水印', '云端算法实时剔除浮动水印和作者标贴，输出纯净原版画质短视频。'),
            ('fas fa-music', '实时工业级 MP3 音频转码', '内置 FFmpeg 高性能音频管道，瞬时抽取封装 320kbps 纯正原生音轨。'),
            ('fas fa-shield-alt', '无欺诈弹窗与零访问日志', '纯净极简界面，无恶意插件诱导，彻底落实零日志隐私标准。'),
            ('fas fa-bolt', '全球 CDN 毫秒级直连流转', '高带宽专线代理加速，免排队等待，即解析即下载。')
        ],
        'tech_h2': '全方位技术规格明细',
        'specs_cols': ('技术规格分类', '性能标准与支持范围'),
        'specs_rows': [
            ('支持社交网络', 'YouTube、TikTok、Instagram、Facebook、Snapchat、Meta Threads'),
            ('视频输出格式', 'MP4（支持 4K 2160p、2K 1440p、1080p 全高清、720p 高清）'),
            ('音频输出格式', 'MP3 原生音频（192 kbps / 320 kbps 录音室级别）'),
            ('水印清理技术', '100% 自动化去除浮动 LOGO 与尾帧署名'),
            ('多媒体图集解包', '全量解析 Instagram 与 Threads 的相册轮播图集与幻灯片'),
            ('终端环境适配', '跨平台支持：Safari (iOS/macOS)、Chrome (Android/PC)、Edge、Firefox'),
            ('访问鉴权要求', '免登录、免密码、无需安装任何第三方插件或客户端')
        ],
        'comp_h2': '主流工具横向评测对比',
        'comp_p': '对比传统下载网站，downsocial 在性能与体验上的绝对优势：',
        'comp_cols': ('评测维度', 'downsocial.net', '传统下载网站（SaveFrom、SnapTik、Y2Mate 等）'),
        'comp_rows': [
            ('平台覆盖度', '六合一全能（6 大主流平台）', '单一零散 / 频繁跳转'),
            ('水印处理效果', '100% 纯净无痕', '残留水印 / 经常失效'),
            ('安全性与广告', '纯净安全（零弹窗骚扰）', '充斥高风险欺诈弹窗与不良诱导'),
            ('音频质量', '320kbps 录音室母带级别', '低码率 128kbps 或无法分离'),
            ('账户体系依赖', '免登录（100% 匿名保护）', '强制注册登录或诱导安装外部软件')
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

print("Enriched static languages module ready.")
