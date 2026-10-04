import json
import os

shared_locales_dir = r'c:\my folder\Pictures\Desktop\downsocial\frontend\shared\locales'

# German (de.json) base
de_data = {
  "seo": {
    "indexTitle": "Video Downloader HD — Videos kostenlos herunterladen von Facebook, Instagram, TikTok & YouTube",
    "indexDesc": "Schneller, sicherer All-in-One HD Video Downloader für Facebook, Instagram, TikTok, YouTube, Snapchat & Threads. Ohne Wasserzeichen und ohne Anmeldung.",
    "indexKeywords": "video downloader, video herunterladen, facebook video downloader, instagram video downloader, tiktok downloader ohne wasserzeichen, youtube video downloader, snapchat video downloader",
    "aboutTitle": "Über uns - Video Downloader HD | Schnell, sicher & kostenlos",
    "aboutDesc": "Erfahren Sie mehr über unsere Mission für den besten Video Downloader im Web.",
    "privacyTitle": "Datenschutzerklärung - Video Downloader HD | Sicher & Privat",
    "privacyDesc": "Unsere Datenschutzrichtlinien für maximale Anonymität und Schutz Ihrer Daten.",
    "termsTitle": "Nutzungsbedingungen - Video Downloader HD | Urheberrecht & Richtlinien",
    "termsDesc": "Rechtliche Hinweise und Nutzungsbedingungen für unseren Video Downloader."
  },
  "common": {
    "langBtn": "Sprache",
    "extBtn": "Erweiterung",
    "soonBadge": "Bald",
    "homeBtn": "Startseite",
    "footerAbout": "Über uns",
    "footerContact": "Kontakt",
    "footerPrivacy": "Datenschutz",
    "footerTerms": "Bedingungen",
    "copyright": "&copy; 2026 downsocial.net. Alle Rechte vorbehalten.",
    "emptyLinkAlert": "Bitte fügen Sie zuerst einen Link ein!",
    "processing": "Verarbeitung läuft...",
    "successMsg": "✅ Bereit!",
    "errorServer": "Serverfehler aufgetreten."
  },
  "notifications": {
    "header": "Benachrichtigungen",
    "newBadge": "1 Neu",
    "extTitle": "Browser-Erweiterung kommt bald! 🚀",
    "time": "Gerade eben",
    "content1": "Die offizielle Browser-Erweiterung für 1-Klick-Downloads befindet sich in Entwicklung.",
    "content2": "Direkter Download auf Facebook, Instagram, TikTok und YouTube ohne Copy & Paste.",
    "content3": "In Kürze verfügbar für Chrome, Firefox und Edge."
  },
  "index": {
    "mainTitle": "Video Downloader",
    "tagline": "Videos, Reels, Shorts & Stories in HD & MP3 herunterladen",
    "placeholder": "Link hier einfügen (Facebook, Instagram, TikTok, YouTube, Threads, Snapchat)...",
    "processBtn": "Video herunterladen",
    "readyTitle": "Bereit zum Herunterladen!",
    "infoText": "Wählen Sie Ihre bevorzugte Qualität.",
    "dlVidHigh": "Video (HD)",
    "dlVidNorm": "Video (Normal)",
    "dlAudHigh": "Audio (HQ MP3)",
    "dlAudNorm": "Audio (Normal MP3)",
    "f1Title": "Blitzschnell",
    "f1Desc": "Sofortige Konvertierung und direkter High-Speed-Download ohne Wartezeit.",
    "moreDetails": "Mehr Details",
    "showLess": "Weniger anzeigen",
    "f2Title": "100% Sicher",
    "f2Desc": "Keine Speicherung, keine Logs und keine Registrierung erforderlich.",
    "f3Title": "All-in-One HD",
    "f3Desc": "Unterstützt Facebook, Instagram, TikTok, YouTube, Snapchat und Threads.",
    "howToSectionTitle": "So einfach funktioniert's",
    "faqTitle": "Häufig gestellte Fragen (FAQ)"
  }
}

# Urdu (ur.json) base
ur_data = {
  "seo": {
    "indexTitle": "ویڈیو ڈاؤنلوڈر ایچ ڈی — فیس بک، انسٹاگرام، ٹک ٹاک، یوٹیوب سے مفت ویڈیوز ڈاؤن لوڈ کریں",
    "indexDesc": "فیس بک، انسٹاگرام، ٹک ٹاک، یوٹیوب، اسنیپ چیٹ اور تھریڈز کے لیے تیز ترین اور محفوظ ویڈیو ڈاؤنلوڈر۔ واٹر مارک اور لاگ ان کے بغیر ایچ ڈی ویڈیوز حاصل کریں۔",
    "indexKeywords": "video downloader, download video, facebook video downloader, instagram reel download, tiktok download no watermark, youtube video download mp4 mp3",
    "aboutTitle": "ہمارے بارے میں - ویڈیو ڈاؤنلوڈر ایچ ڈی",
    "aboutDesc": "ہمارے محفوظ اور مفت سوشل میڈیا ویڈیو ڈاؤنلوڈر ٹول کے بارے میں تفصیلات۔",
    "privacyTitle": "پرائیویسی پالیسی - ڈاؤن سوشل",
    "privacyDesc": "ہماری زیرو لاگ اور پرائیویسی پروٹیکشن پالیسی پڑھیں۔",
    "termsTitle": "شرائط و ضوابط - ڈاؤن سوشل",
    "termsDesc": "ویڈیو ڈاؤنلوڈر کے منصفانہ اور قانونی استعمال کی شرائط۔"
  },
  "common": {
    "langBtn": "زبان (Language)",
    "extBtn": "ایکسٹینشن",
    "soonBadge": "جلد",
    "homeBtn": "ہوم",
    "footerAbout": "ہمارے بارے میں",
    "footerContact": "رابطہ کریں",
    "footerPrivacy": "پرائیویسی پالیسی",
    "footerTerms": "شرائط و ضوابط",
    "copyright": "&copy; 2026 downsocial.net. جملہ حقوق محفوظ ہیں۔",
    "emptyLinkAlert": "براہ کرم پہلے ویڈیو کا لنک پیسٹ کریں!",
    "processing": "پروسیسنگ جاری ہے...",
    "successMsg": "✅ ویڈیو تیار ہے!",
    "errorServer": "سرور سے رابطہ نہ ہو سکا۔"
  },
  "notifications": {
    "header": "اطلاعات (Notifications)",
    "newBadge": "1 نیا",
    "extTitle": "براؤزر ایکسٹینشن جلد آرہی ہے! 🚀",
    "time": "ابھی ابھی",
    "content1": "ہماری آفیشل ڈاؤن سوشل براؤزر ایکسٹینشن پر کام جاری ہے!",
    "content2": "ویڈیوز کے نیچے 1-کلک ڈاؤن لوڈ بٹن کے ساتھ آسانی سے ویڈیوز سیو کریں۔",
    "content3": "کروم، فائر فاکس اور ایج براؤزرز پر بہت جلد دستیاب ہوگی۔"
  },
  "index": {
    "mainTitle": "سوشل میڈیا ویڈیو ڈاؤنلوڈر",
    "tagline": "فیس بک، انسٹاگرام، ٹک ٹاک، یوٹیوب اور تھریڈز سے ایچ ڈی ویڈیوز اور ایم پی 3 آڈیو مفت ڈاؤن لوڈ کریں",
    "placeholder": "ویڈیو کا لنک یہاں پیسٹ کریں (Facebook, Instagram, TikTok, YouTube, Threads)...",
    "processBtn": "ویڈیو ڈاؤن لوڈ کریں",
    "readyTitle": "ڈاؤن لوڈ کے لیے تیار ہے!",
    "infoText": "اپنی پسندیدہ کوالٹی کا انتخاب کریں:",
    "dlVidHigh": "ویڈیو (HD)",
    "dlVidNorm": "ویڈیو (Normal)",
    "dlAudHigh": "آڈیو (HQ MP3)",
    "dlAudNorm": "آڈیو (Normal MP3)",
    "f1Title": "انتہائی تیز رفتار",
    "f1Desc": "بغیر کسی تاخیر کے فوری پروسیسنگ اور ہائی اسپیڈ ڈاؤن لوڈنگ۔",
    "moreDetails": "مزید تفصیلات",
    "showLess": "کم دکھائیں",
    "f2Title": "محفوظ اور نجی",
    "f2Desc": "نہ کسی لاگ ان کی ضرورت ہے اور نہ ہی آپ کا ڈیٹا محفوظ کیا جاتا ہے۔",
    "f3Title": "تمام پلیٹ فارمز کے لیے",
    "f3Desc": "فیس بک • انسٹاگرام • ٹک ٹاک • یوٹیوب • اسنیپ چیٹ • تھریڈز",
    "howToSectionTitle": "ڈاؤن لوڈ کرنے کا طریقہ",
    "faqTitle": "اکثر پوچھے جانے والے سوالات (FAQ)"
  }
}

with open(os.path.join(shared_locales_dir, 'de.json'), 'w', encoding='utf-8') as f:
    json.dump(de_data, f, ensure_ascii=False, indent=2)

with open(os.path.join(shared_locales_dir, 'ur.json'), 'w', encoding='utf-8') as f:
    json.dump(ur_data, f, ensure_ascii=False, indent=2)

print("Created de.json and ur.json in shared/locales!")
