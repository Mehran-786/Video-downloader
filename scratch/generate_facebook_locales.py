import json
import os

locales_dir = r"c:\my folder\Pictures\Desktop\downsocial\frontend\facebook-downloader\locales"
en_path = os.path.join(locales_dir, "en.json")

with open(en_path, "r", encoding="utf-8") as f:
    en_data = json.load(f)

# Seed phrases and metadata per language
LANG_INFO = {
    "es": {
        "name": "Español",
        "seed": "descargar videos de Facebook",
        "indexTitle": "Descargar Videos de Facebook: Reels y Videos en HD Gratis",
        "indexDesc": "Descargar videos de Facebook gratis en HD MP4 o MP3. Pega el enlace de cualquier video, Reel o Watch y guárdalo en segundos sin registrarte.",
        "indexKeywords": "descargar videos de facebook, descargar video facebook, bajar videos de facebook, descargar reels facebook, facebook a mp3, guardar video facebook hd",
        "mainTitle": "Descargar Videos de Facebook",
        "tagline": "Pega cualquier enlace de video, Reel o Watch de Facebook y guárdalo en HD MP4 o MP3. Gratis y sin iniciar sesión.",
        "placeholder": "Pega el enlace de video, Reel o Watch de Facebook aquí...",
        "processBtn": "Descargar Video",
        "readyTitle": "¡Listo para Descargar!",
        "infoText": "Elige tu calidad preferida abajo.",
        "f1Title": "Compatible con Cualquier Enlace",
        "f1Desc": "Videos, Reels, Watch y enlaces cortos fb.watch. Pega y listo.",
        "f2Title": "Video HD MP4 o Audio MP3",
        "f2Desc": "Elige MP4 en HD o normal, o extrae el sonido en MP3.",
        "f3Title": "Sin Registro, Sin App, Sin Marcas",
        "f3Desc": "Sin instalar nada y sin pedir tu contraseña de Facebook.",
        "howToTitle": "Cómo Descargar Videos de Facebook en 4 Pasos",
        "faqTitle": "Preguntas Frecuentes sobre Facebook Downloader",
        "dir": "ltr"
    },
    "fr": {
        "name": "Français",
        "seed": "télécharger vidéo Facebook",
        "indexTitle": "Télécharger Vidéo Facebook: Reels et Vidéos en HD Gratuit",
        "indexDesc": "Télécharger une vidéo Facebook gratuitement en HD MP4 ou MP3. Collez le lien d'une vidéo, Reel ou Watch et enregistrez-le en quelques secondes.",
        "indexKeywords": "télécharger vidéo facebook, telecharger video facebook, enregistrer video facebook, telecharger reels facebook, facebook en mp3, video facebook hd",
        "mainTitle": "Télécharger Vidéo Facebook",
        "tagline": "Collez n'importe quel lien de vidéo, Reel ou Watch Facebook et enregistrez-le en HD MP4 ou MP3. Gratuit, sans connexion.",
        "placeholder": "Collez le lien de la vidéo, du Reel ou du Watch Facebook ici...",
        "processBtn": "Télécharger la Vidéo",
        "readyTitle": "Prêt pour le Téléchargement !",
        "infoText": "Choisissez votre qualité ci-dessous.",
        "f1Title": "Compatible avec Tous les Liens",
        "f1Desc": "Vidéos, Reels, Watch et liens courts fb.watch. Collez et téléchargez.",
        "f2Title": "Vidéo HD MP4 ou Audio MP3",
        "f2Desc": "Choisissez MP4 HD ou Normal, ou extrayez le son en MP3.",
        "f3Title": "Sans Inscription, Sans App, Sans Filigrane",
        "f3Desc": "Rien à installer et aucun mot de passe Facebook requis.",
        "howToTitle": "Comment Télécharger une Vidéo Facebook en 4 Étapes",
        "faqTitle": "FAQ Téléchargeur de Vidéos Facebook",
        "dir": "ltr"
    },
    "de": {
        "name": "Deutsch",
        "seed": "Facebook Video herunterladen",
        "indexTitle": "Facebook Video herunterladen: Reels & Videos in HD Gratis",
        "indexDesc": "Kostenlos Facebook Videos herunterladen als HD MP4 oder MP3. Link einfügen und Facebook Reels, Watch & Videos ohne Login sofort speichern.",
        "indexKeywords": "facebook video herunterladen, facebook video download, facebook reels download, facebook to mp3, facebook video speichern, download facebook video hd",
        "mainTitle": "Facebook Video Downloader",
        "tagline": "Fügen Sie einen beliebigen Facebook-Video-, Reel- oder Watch-Link ein und speichern Sie ihn in HD MP4 oder MP3. Kostenlos ohne Login.",
        "placeholder": "Fügen Sie hier Ihren Facebook-Video-, Reel- oder Watch-Link ein...",
        "processBtn": "Video Herunterladen",
        "readyTitle": "Bereit zum Herunterladen!",
        "infoText": "Wählen Sie unten Ihre bevorzugte Qualität.",
        "f1Title": "Funktioniert mit jedem Facebook-Link",
        "f1Desc": "Videos, Reels, Watch und fb.watch Kurzlinks. Einfügen, klicken, fertig.",
        "f2Title": "HD MP4 oder MP3 Audio",
        "f2Desc": "Wählen Sie HD oder Normal MP4, oder extrahieren Sie den Ton als MP3.",
        "f3Title": "Ohne Login, Ohne App, Ohne Wasserzeichen",
        "f3Desc": "Nichts zu installieren und kein Facebook-Passwort erforderlich.",
        "howToTitle": "Facebook Video herunterladen in 4 Schritten",
        "faqTitle": "Facebook Video Downloader FAQ",
        "dir": "ltr"
    },
    "hi": {
        "name": "हिन्दी",
        "seed": "फेसबुक वीडियो डाउनलोड",
        "indexTitle": "फेसबुक वीडियो डाउनलोड: HD MP4 और MP3 में मुफ्त सेव करें",
        "indexDesc": "मुफ्त फेसबुक वीडियो डाउनलोडर। फेसबुक वीडियो, रील्स या वॉच लिंक पेस्ट करें और HD MP4 या MP3 में तुरंत सेव करें। बिना लॉगिन, बिना वॉटरमार्क।",
        "indexKeywords": "फेसबुक वीडियो डाउनलोड, facebook video download, facebook reel download, download facebook video, fb video download, facebook to mp3",
        "mainTitle": "फेसबुक वीडियो डाउनलोडर",
        "tagline": "कोई भी फेसबुक वीडियो, रील्स या वॉच लिंक पेस्ट करें और HD MP4 या MP3 में सेव करें। बिल्कुल मुफ्त, बिना लॉगिन।",
        "placeholder": "अपना फेसबुक वीडियो, रील्स या वॉच लिंक यहाँ पेस्ट करें...",
        "processBtn": "वीडियो डाउनलोड करें",
        "readyTitle": "डाउनलोड के लिए तैयार!",
        "infoText": "नीचे अपनी पसंदीदा क्वालिटी चुनें।",
        "f1Title": "सभी फेसबुक लिंक समर्थित",
        "f1Desc": "वीडियो, रील्स, वॉच और fb.watch शॉर्ट लिंक। पेस्ट करें और सेव करें।",
        "f2Title": "HD MP4 या MP3 ऑडियो",
        "f2Desc": "HD या नॉर्मल MP4 चुनें, या सीधे MP3 ऑडियो निकालें।",
        "f3Title": "बिना लॉगिन, बिना ऐप, बिना वॉटरमार्क",
        "f3Desc": "कुछ भी इंस्टॉल करने की ज़रूरत नहीं, कभी कोई पासवर्ड नहीं मांगा जाता।",
        "howToTitle": "फेसबुक वीडियो 4 आसान चरणों में कैसे डाउनलोड करें",
        "faqTitle": "फेसबुक वीडियो डाउनलोडर अक्सर पूछे जाने वाले सवाल",
        "dir": "ltr"
    },
    "ar": {
        "name": "العربية",
        "seed": "تحميل فيديو من فيسبوك",
        "indexTitle": "تحميل فيديو من فيسبوك: تنزيل ريلز وفيديوهات HD مجاناً",
        "indexDesc": "تحميل فيديو من فيسبوك مجاناً بجودة HD MP4 أو MP3. الصق رابط أي فيديو أو ريلز أو واتش واحفظه في ثوانٍ بدون تسجيل دخول وبدون علامة مائية.",
        "indexKeywords": "تحميل فيديو من فيسبوك, تنزيل فيديو فيسبوك, تحميل ريلز فيسبوك, فيسبوك الى mp3, حفظ فيديو فيسبوك, download facebook video hd",
        "mainTitle": "برنامج تحميل فيديو من فيسبوك",
        "tagline": "الصق أي رابط فيديو أو ريلز أو واتش من فيسبوك واحفظه بجودة HD MP4 أو MP3 مجاناً وبدون تسجيل دخول.",
        "placeholder": "الصق رابط فيديو فيسبوك أو الريلز هنا...",
        "processBtn": "تحميل الفيديو",
        "readyTitle": "جاهز للتحميل!",
        "infoText": "اختر الجودة المطلوبة أدناه.",
        "f1Title": "يدعم جميع روابط فيسبوك",
        "f1Desc": "فيديوهات، ريلز، واتش وروابط fb.watch القصيرة بنقرة واحدة.",
        "f2Title": "فيديو HD MP4 أو صوت MP3",
        "f2Desc": "اختر MP4 بجودة عالية أو عادية، أو استخرج الصوت بصيغة MP3.",
        "f3Title": "بدون تسجيل، بدون تطبيق، بدون علامة مائية",
        "f3Desc": "لا يتطلب تثبيت أي برامج ولا نطلب كلمة مرور فيسبوك إطلاقاً.",
        "howToTitle": "كيفية تحميل فيديو من فيسبوك في 4 خطوات",
        "faqTitle": "الأسئلة الشائعة حول تحميل فيديوهات فيسبوك",
        "dir": "rtl"
    },
    "pt": {
        "name": "Português",
        "seed": "baixar vídeo do Facebook",
        "indexTitle": "Baixar Vídeo do Facebook: Salvar Reels e Vídeos HD Grátis",
        "indexDesc": "Baixar vídeo do Facebook grátis em HD MP4 ou MP3. Cole o link de qualquer vídeo, Reel ou Watch e salve em segundos sem login e sem marca d'água.",
        "indexKeywords": "baixar vídeo do facebook, baixar video facebook, baixar reels facebook, facebook para mp3, salvar video do facebook, download video facebook hd",
        "mainTitle": "Baixar Vídeo do Facebook",
        "tagline": "Cole qualquer link de vídeo, Reel ou Watch do Facebook e salve em HD MP4 ou MP3. Grátis e sem login.",
        "placeholder": "Cole o link do vídeo, Reel ou Watch do Facebook aqui...",
        "processBtn": "Baixar Vídeo",
        "readyTitle": "Pronto para Baixar!",
        "infoText": "Escolha sua qualidade preferida abaixo.",
        "f1Title": "Compatível com Todos os Links",
        "f1Desc": "Vídeos, Reels, Watch e links curtos fb.watch. Cole e pronto.",
        "f2Title": "Vídeo HD MP4 ou Áudio MP3",
        "f2Desc": "Escolha MP4 HD ou Normal, ou extraia o som em MP3.",
        "f3Title": "Sem Login, Sem App, Sem Marca d'Água",
        "f3Desc": "Nada para instalar e sem pedir sua senha do Facebook.",
        "howToTitle": "Como Baixar Vídeos do Facebook em 4 Passos",
        "faqTitle": "Perguntas Frequentes sobre o Facebook Downloader",
        "dir": "ltr"
    },
    "bn": {
        "name": "বাংলা",
        "seed": "ফেসবুক ভিডিও ডাউনলোড",
        "indexTitle": "ফেসবুক ভিডিও ডাউনলোড: HD MP4 ও MP3 তে সেভ করুন",
        "indexDesc": "ফ্রি ফেসবুক ভিডিও ডাউনলোডার। ফেসবুক ভিডিও, রিলস বা ওয়াচ লিঙ্ক পেস্ট করে HD MP4 বা MP3 তে সেভ করুন। কোনো লগইন ও ওয়াটারমার্ক ছাড়া।",
        "indexKeywords": "ফেসবুক ভিডিও ডাউনলোড, facebook video download, facebook reel download, fb video download, download facebook video, facebook to mp3",
        "mainTitle": "ফেসবুক ভিডিও ডাউনলোডার",
        "tagline": "যেকোনো পাবলিক ফেসবুক ভিডিও, রিলস বা ওয়াচ লিঙ্ক পেস্ট করে HD MP4 বা MP3 তে সেভ করুন। সম্পূর্ণ ফ্রি।",
        "placeholder": "ফেসবুক ভিডিও বা রিলস লিঙ্ক এখানে পেস্ট করুন...",
        "processBtn": "ভিডিও ডাউনলোড করুন",
        "readyTitle": "ডাউনলোডের জন্য প্রস্তুত!",
        "infoText": "নিচে আপনার পছন্দের কোয়ালিটি নির্বাচন করুন।",
        "f1Title": "সব ফেসবুক লিঙ্কে কার্যকর",
        "f1Desc": "ভিডিও, রিলস, ওয়াচ এবং fb.watch লিঙ্ক সহজেই ডাউনলোড করুন।",
        "f2Title": "HD MP4 বা MP3 অডিও",
        "f2Desc": "HD বা সাধারণ MP4 নির্বাচন করুন, অথবা সরাসরি MP3 অডিও সংগ্রহ করুন।",
        "f3Title": "লগইন ছাড়া, অ্যাপ ছাড়া, ওয়াটারমার্কহীন",
        "f3Desc": "কোনো অ্যাপ ইন্সটল বা পাসওয়ার্ডের প্রয়োজন নেই।",
        "howToTitle": "৪টি সহজ ধাপে ফেসবুক ভিডিও ডাউনলোড করার নিয়ম",
        "faqTitle": "ফেসবুক ভিডিও ডাউনলোডার সাধারণ প্রশ্নোত্তর",
        "dir": "ltr"
    },
    "ru": {
        "name": "Русский",
        "seed": "скачать видео с Facebook",
        "indexTitle": "Скачать видео с Facebook: Reels и видео в HD бесплатно",
        "indexDesc": "Бесплатный загрузчик видео с Facebook в HD MP4 или MP3. Вставьте ссылку на видео, Reels или Watch и скачайте без водяных знаков и без регистрации.",
        "indexKeywords": "скачать видео с facebook, скачать видео фейсбук, скачать reels facebook, фейсбук в mp3, скачать видео с фб, сохранить видео facebook hd",
        "mainTitle": "Скачать видео с Facebook",
        "tagline": "Вставьте ссылку на видео, Reel или Watch с Facebook и сохраните в HD MP4 или MP3. Бесплатно и без входа.",
        "placeholder": "Вставьте ссылку на видео или Reel Facebook сюда...",
        "processBtn": "Скачать видео",
        "readyTitle": "Готово к скачиванию!",
        "infoText": "Выберите желаемое качество ниже.",
        "f1Title": "Поддержка любых ссылок Facebook",
        "f1Desc": "Видео, Reels, Watch и короткие ссылки fb.watch. Вставьте и готово.",
        "f2Title": "HD MP4 или MP3 аудио",
        "f2Desc": "Выберите HD или обычный MP4, либо извлеките звук в формате MP3.",
        "f3Title": "Без входа, без приложений, без водяных знаков",
        "f3Desc": "Не нужно ничего устанавливать и указывать пароль от Facebook.",
        "howToTitle": "Как скачать видео с Facebook за 4 шага",
        "faqTitle": "Часто задаваемые вопросы о загрузчике Facebook",
        "dir": "ltr"
    },
    "id": {
        "name": "Bahasa Indonesia",
        "seed": "download video Facebook",
        "indexTitle": "Download Video Facebook: Simpan Reels & Video HD Gratis",
        "indexDesc": "Download video Facebook gratis kualitas HD MP4 atau MP3. Tempel link video, Reels, atau Watch dan simpan cepat tanpa login dan tanpa watermark.",
        "indexKeywords": "download video facebook, download video fb, unduh video facebook, download reels facebook, konversi facebook ke mp3, simpan video facebook hd",
        "mainTitle": "Download Video Facebook",
        "tagline": "Tempel tautan video, Reel, atau Watch Facebook dan simpan dalam format HD MP4 atau MP3. Gratis tanpa login.",
        "placeholder": "Tempel tautan video, Reel, atau Watch Facebook di sini...",
        "processBtn": "Download Video",
        "readyTitle": "Siap Diunduh!",
        "infoText": "Pilih kualitas yang Anda inginkan di bawah.",
        "f1Title": "Mendukung Semua Tautan Facebook",
        "f1Desc": "Video, Reels, Watch, dan tautan pendek fb.watch. Tempel dan selesai.",
        "f2Title": "Video HD MP4 atau Audio MP3",
        "f2Desc": "Pilih MP4 HD atau Normal, atau ekstrak suara menjadi MP3.",
        "f3Title": "Tanpa Login, Tanpa Aplikasi, Tanpa Watermark",
        "f3Desc": "Tidak perlu instalasi aplikasi dan tanpa meminta kata sandi Facebook.",
        "howToTitle": "Cara Download Video Facebook dalam 4 Langkah",
        "faqTitle": "FAQ Pengunduh Video Facebook",
        "dir": "ltr"
    },
    "zh": {
        "name": "中文",
        "seed": "Facebook视频下载",
        "indexTitle": "Facebook视频下载器：免费保存FB视频和Reels高清MP4",
        "indexDesc": "免费Facebook视频下载工具。粘贴任何公开的Facebook视频、Reels或Watch链接，几秒内即可下载为高清MP4或MP3。无需登录，无水印。",
        "indexKeywords": "Facebook视频下载, 下载facebook视频, fb视频下载, facebook reels下载, facebook转mp3, 保存facebook视频高清",
        "mainTitle": "Facebook视频下载器",
        "tagline": "粘贴任何公开的Facebook视频、Reel或Watch链接，保存为高清MP4或MP3。免费且无需登录。",
        "placeholder": "在此处粘贴Facebook视频、Reel或Watch链接...",
        "processBtn": "下载视频",
        "readyTitle": "准备下载！",
        "infoText": "请在下方选择所需品质。",
        "f1Title": "支持所有Facebook链接格式",
        "f1Desc": "视频、Reels、Watch以及fb.watch短链接，粘贴即下。",
        "f2Title": "高清MP4视频或MP3音频",
        "f2Desc": "选择高清或标准MP4，或将声音提取为MP3格式。",
        "f3Title": "无需登录、无需软件、无水印",
        "f3Desc": "无需安装任何应用程序，绝不索要您的Facebook密码。",
        "howToTitle": "如何分4步下载Facebook视频",
        "faqTitle": "Facebook视频下载器常见问题",
        "dir": "ltr"
    },
    "ur": {
        "name": "اردو",
        "seed": "فیس بک ویڈیو ڈاؤنلوڈ",
        "indexTitle": "فیس بک ویڈیو ڈاؤنلوڈ: ریلز اور ویڈیوز HD MP4 میں مفت",
        "indexDesc": "مفت فیس بک ویڈیو ڈاؤنلوڈر۔ کوئی بھی فیس بک ویڈیو، ریلز یا واچ لنک پیسٹ کریں اور سیکنڈوں میں HD MP4 یا MP3 میں محفوظ کریں۔ بغیر لاگ ان اور واٹر مارک۔",
        "indexKeywords": "فیس بک ویڈیو ڈاؤنلوڈ, facebook video download, fb video download, download facebook video, facebook reel download, facebook to mp3 urdu",
        "mainTitle": "فیس بک ویڈیو ڈاؤنلوڈر",
        "tagline": "کوئی بھی پبلک فیس بک ویڈیو، ریلز یا واچ لنک پیسٹ کریں اور HD MP4 یا MP3 میں محفوظ کریں۔ بالکل مفت اور بغیر لاگ ان۔",
        "placeholder": "اپنا فیس بک ویڈیو، ریلز یا واچ لنک یہاں پیسٹ کریں...",
        "processBtn": "ویڈیو ڈاؤنلوڈ کریں",
        "readyTitle": "ڈاؤنلوڈ کے لیے تیار!",
        "infoText": "نیچے اپنی پسندیدہ کوالٹی منتخب کریں۔",
        "f1Title": "ہر قسم کے فیس بک لنک پر کارآمد",
        "f1Desc": "ویڈیوز، ریلز، واچ اور fb.watch لنکس۔ لنک پیسٹ کریں اور حاصل کریں۔",
        "f2Title": "HD MP4 یا MP3 آڈیو",
        "f2Desc": "HD یا نارمل MP4 کا انتخاب کریں، یا براہ راست MP3 آڈیو نکالیں۔",
        "f3Title": "بغیر لاگ ان، بغیر ایپ، بغیر واٹر مارک",
        "f3Desc": "کچھ بھی انسٹال کرنے کی ضرورت نہیں، نہ ہی فیس بک پاس ورڈ درکار ہے۔",
        "howToTitle": "فیس بک ویڈیو 4 آسان مراحل میں ڈاؤنلوڈ کرنے کا طریقہ",
        "faqTitle": "فیس بک ویڈیو ڈاؤنلوڈر عمومی سوالات",
        "dir": "rtl"
    }
}

# Generate 11 localized JSON files mirroring en_data structure exactly
for lang, info in LANG_INFO.items():
    lang_data = json.loads(json.dumps(en_data)) # deep copy
    
    # 1. Update SEO block
    lang_data["seo"]["indexTitle"] = info["indexTitle"]
    lang_data["seo"]["indexDesc"] = info["indexDesc"]
    lang_data["seo"]["indexKeywords"] = info["indexKeywords"]
    
    # Localize other SEO titles with language name
    lang_data["seo"]["aboutTitle"] = f"{info['mainTitle']} | downsocial ({info['name']})"
    lang_data["seo"]["contactTitle"] = f"Support - {info['mainTitle']} | downsocial"
    lang_data["seo"]["privacyTitle"] = f"Privacy Policy - {info['mainTitle']} | downsocial"
    lang_data["seo"]["termsTitle"] = f"Terms - {info['mainTitle']} | downsocial"
    
    # 2. Update common
    lang_data["common"]["langBtn"] = info["name"]
    lang_data["common"]["homeBtn"] = "Home" if info["dir"] == "ltr" else "ہوم"
    
    # 3. Update index hero & features
    lang_data["index"]["mainTitle"] = info["mainTitle"]
    lang_data["index"]["tagline"] = info["tagline"]
    lang_data["index"]["placeholder"] = info["placeholder"]
    lang_data["index"]["processBtn"] = info["processBtn"]
    lang_data["index"]["readyTitle"] = info["readyTitle"]
    lang_data["index"]["infoText"] = info["infoText"]
    
    lang_data["index"]["f1Title"] = info["f1Title"]
    lang_data["index"]["f1Desc"] = info["f1Desc"]
    lang_data["index"]["f2Title"] = info["f2Title"]
    lang_data["index"]["f2Desc"] = info["f2Desc"]
    lang_data["index"]["f3Title"] = info["f3Title"]
    lang_data["index"]["f3Desc"] = info["f3Desc"]
    
    lang_data["index"]["howToSectionTitle"] = info["howToTitle"]
    lang_data["index"]["faqTitle"] = info["faqTitle"]
    
    # Save file
    target_file = os.path.join(locales_dir, f"{lang}.json")
    with open(target_file, "w", encoding="utf-8") as out_f:
        json.dump(lang_data, out_f, ensure_ascii=False, indent=2)
    print(f"Generated {lang}.json successfully.")

print("All 11 locale files created.")
