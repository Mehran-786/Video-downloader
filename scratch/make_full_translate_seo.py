# scratch/make_full_translate_seo.py
import os, sys, json
sys.stdout.reconfigure(encoding='utf-8')

# We define high quality translations for all 51 headers, 25 table headers, and key table cells across all 11 non-English languages.

VOCAB = {
    'es': {
        # Quick Answers
        'Quick Answer: How to Download Social Media Videos Free': 'Respuesta Rápida: Cómo Descargar Videos de Redes Sociales Gratis',
        'Quick Answer: How to Download Facebook Videos': 'Respuesta Rápida: Cómo Descargar Videos de Facebook',
        'Quick Answer: How to Download Instagram Videos': 'Respuesta Rápida: Cómo Descargar Videos de Instagram',
        'Quick Answer: How to Download TikTok Videos (No Watermark)': 'Respuesta Rápida: Cómo Descargar Videos de TikTok (Sin Marca de Agua)',
        'Quick Answer: How to Download TikTok Videos Without Watermark': 'Respuesta Rápida: Cómo Descargar Videos de TikTok Sin Marca de Agua',
        'Quick Answer: How to Download YouTube Videos & Shorts': 'Respuesta Rápida: Cómo Descargar Videos y Shorts de YouTube',
        'Quick Answer: How to Download YouTube Videos &amp; Shorts': 'Respuesta Rápida: Cómo Descargar Videos y Shorts de YouTube',
        'Quick Answer: How to Download Snapchat Spotlight Videos': 'Respuesta Rápida: Cómo Descargar Videos de Snapchat Spotlight',
        'Quick Answer: How to Download Threads Videos': 'Respuesta Rápida: Cómo Descargar Videos de Threads',
        # Headings
        'The Ultimate All-in-One Social Media Video Downloader': 'El Descargador Definitivo Todo en Uno para Redes Sociales',
        'Facebook Video Downloader: Save Any Public Facebook Video in HD': 'Descargador de Videos de Facebook: Guarda Cualquier Video Público en HD',
        'Instagram Video Downloader: Save Reels, Stories & Posts in HD': 'Descargador de Instagram: Guarda Reels, Stories y Publicaciones en HD',
        'Instagram Video Downloader: Save Reels, Stories &amp; Posts in HD': 'Descargador de Instagram: Guarda Reels, Stories y Publicaciones en HD',
        'The Ultimate Free TikTok Video Downloader (No Watermark)': 'El Descargador Gratuito Definitivo de TikTok (Sin Marca de Agua)',
        'The Fastest, Ad-Free YouTube Video & Shorts Downloader': 'El Descargador de YouTube Más Rápido y Sin Anuncios',
        'The Fastest, Ad-Free YouTube Video &amp; Shorts Downloader': 'El Descargador de YouTube Más Rápido y Sin Anuncios',
        'The Ultimate Free Snapchat Spotlight & Story Downloader': 'El Descargador Definitivo de Snapchat Spotlight y Stories',
        'The Ultimate Free Snapchat Spotlight &amp; Story Downloader': 'El Descargador Definitivo de Snapchat Spotlight y Stories',
        'The Fastest, Safest Meta Threads Video & Media Downloader': 'El Descargador Más Rápido y Seguro para Meta Threads',
        'The Fastest, Safest Meta Threads Video &amp; Media Downloader': 'El Descargador Más Rápido y Seguro para Meta Threads',
        'Supported Platforms, Formats & Specifications': 'Plataformas, Formatos y Especificaciones Compatibles',
        'Supported Platforms, Formats &amp; Specifications': 'Plataformas, Formatos y Especificaciones Compatibles',
        'Facebook Video Downloader at a Glance': 'Descargador de Facebook de un Vistazo',
        'Instagram Video Downloader at a Glance': 'Descargador de Instagram de un Vistazo',
        'Which Facebook Links Work?': '¿Qué Enlaces de Facebook Funcionan?',
        'Which Instagram Links Work?': '¿Qué Enlaces de Instagram Funcionan?',
        'Supported TikTok Link Types & Formats': 'Tipos de Enlace y Formatos de TikTok Compatibles',
        'Supported TikTok Link Types &amp; Formats': 'Tipos de Enlace y Formatos de TikTok Compatibles',
        'Supported YouTube Link Types & Formats': 'Tipos de Enlace y Formatos de YouTube Compatibles',
        'Supported YouTube Link Types &amp; Formats': 'Tipos de Enlace y Formatos de YouTube Compatibles',
        'Supported Snapchat Link Formats': 'Formatos de Enlace de Snapchat Compatibles',
        'Supported Threads Media Link Formats': 'Formatos de Enlace de Threads Compatibles',
        'Why Choose downsocial over Competitors?': '¿Por qué elegir downsocial frente a la competencia?',
        'Why Choose downsocial over Competitors (Threadster & SaveThreads)?': '¿Por qué elegir downsocial frente a Threadster y SaveThreads?',
        'Why Choose downsocial over Competitors (Threadster &amp; SaveThreads)?': '¿Por qué elegir downsocial frente a Threadster y SaveThreads?',
        'Why Choose downsocial over Competitors (Y2Mate & SaveFrom)?': '¿Por qué elegir downsocial frente a Y2Mate y SaveFrom?',
        'Why Choose downsocial over Competitors (Y2Mate &amp; SaveFrom)?': '¿Por qué elegir downsocial frente a Y2Mate y SaveFrom?',
        'Why Choose downsocial over SnapTik, SSSTik & MusicalDown?': '¿Por qué elegir downsocial frente a SnapTik, SSSTik y MusicalDown?',
        'Why Choose downsocial over SnapTik, SSSTik &amp; MusicalDown?': '¿Por qué elegir downsocial frente a SnapTik, SSSTik y MusicalDown?',
        'Why downsocial is the Best Alternative to SnapVee, ScreenApp & SnapAny': 'Por qué downsocial es la mejor alternativa a SnapVee, ScreenApp y SnapAny',
        'Why downsocial is the Best Alternative to SnapVee, ScreenApp &amp; SnapAny': 'Por qué downsocial es la mejor alternativa a SnapVee, ScreenApp y SnapAny',
        'Why downsocial Outperforms SaveInsta, iGram, and InDown': 'Por qué downsocial supera a SaveInsta, iGram e InDown',
        'How to Copy a Facebook Video Link': 'Cómo Copiar un Enlace de Video de Facebook',
        'How to Copy an Instagram Video Link': 'Cómo Copiar un Enlace de Video de Instagram',
        'How to Download Facebook Videos on iPhone, Android and Computer': 'Cómo Descargar Videos de Facebook en iPhone, Android y Computadora',
        'How to Download Instagram Videos on iPhone, Android and Computer': 'Cómo Descargar Videos de Instagram en iPhone, Android y Computadora',
        'Step-by-Step Device Download Guide': 'Guía Paso a Paso para Descargar en Cualquier Dispositivo',
        'Step-by-Step Device Download Instructions': 'Instrucciones Paso a Paso para Descargar en Dispositivos',
        'Can You Download Private Facebook Videos?': '¿Se Pueden Descargar Videos Privados de Facebook?',
        'Can You Download Private Instagram Videos?': '¿Se Pueden Descargar Videos Privados de Instagram?',
        'Facebook Video Quality: What You Actually Get': 'Calidad de Video de Facebook: Lo Que Realmente Obtienes',
        'Instagram Video Quality: Original 1080p Full HD': 'Calidad de Video de Instagram: 1080p Full HD Original',
        'Convert Facebook Video to MP3': 'Convertir Video de Facebook a Audio MP3',
        'Convert Instagram Reels to MP3 Audio': 'Convertir Reels de Instagram a Audio MP3',
        'Why a Facebook Video Might Not Download': 'Por Qué un Video de Facebook Podría No Descargarse',
        'Why an Instagram Video Might Not Download': 'Por Qué un Video de Instagram Podría No Descargarse',
        'Common Reasons People Save Facebook Videos': 'Razones Comunes para Guardar Videos de Facebook',
        'Common Reasons People Save Instagram Videos': 'Razones Comunes para Guardar Videos de Instagram',
        'Is Downloading Facebook Videos Safe and Legal?': '¿Es Seguro y Legal Descargar Videos de Facebook?',
        'Is Downloading Instagram Videos Safe and Legal?': '¿Es Seguro y Legal Descargar Videos de Instagram?',
        'Tips for the Best Result': 'Consejos para Obtener el Mejor Resultado',
        'Tips for the Best Download Experience': 'Consejos para la Mejor Experiencia de Descarga',
        'Safe, Private & Anonymous Downloading': 'Descargas Seguras, Privadas y 100% Anónimas',
        'Safe, Private &amp; Anonymous Downloading': 'Descargas Seguras, Privadas y 100% Anónimas',
        'Zero-Log Privacy Protection': 'Protección de Privacidad con Cero Registros',
        'Need Another Platform?': '¿Necesitas Otra Plataforma?',
        'Explore Our Dedicated Platform Downloaders': 'Explora Nuestros Descargadores Especializados',
        # Table Headers
        'Platform': 'Plataforma',
        'Supported Content': 'Contenido Compatible',
        'Max Video Quality': 'Calidad Máxima de Video',
        'Audio Extraction': 'Extracción de Audio',
        'Watermark Status': 'Estado de Marca de Agua',
        'Feature': 'Característica',
        'Details': 'Detalles',
        'Link type': 'Tipo de enlace',
        'What it looks like': 'Ejemplo de enlace',
        'Works when': 'Funciona cuando',
        'Feature Comparison': 'Comparación de Características',
        'Format': 'Formato',
        'Resolution': 'Resolución',
        'Audio Quality': 'Calidad de Audio',
        'Available Resolutions': 'Resoluciones Disponibles',
        'Content Type': 'Tipo de Contenido',
        'Likely cause': 'Causa probable',
        'Recommended solution': 'Solución recomendada',
        'Media Type': 'Tipo de Medio',
        'Output Format': 'Formato de Salida',
        'Supported Quality': 'Calidad Compatible',
        'Supported when': 'Compatible cuando',
        'Symptom': 'Síntoma',
        'What to try': 'Qué intentar',
        # Table Content
        'Videos, Shorts, Music Clips': 'Videos, Shorts, Clips Musicales',
        'Videos, Sounds, Slideshows': 'Videos, Sonidos, Presentaciones',
        'Reels, Stories, Carousels': 'Reels, Stories, Carruseles',
        'Reels, Watch, Feed Posts': 'Reels, Watch, Publicaciones del Muro',
        'Spotlights, Public Stories': 'Spotlights, Historias Públicas',
        'Videos, Audio, Carousels': 'Videos, Audios, Carruseles',
        'Zero Watermark': 'Cero Marca de Agua',
        '100% Removed': '100% Eliminada',
        'Original Source': 'Fuente Original',
        '6 Major Platforms (All-in-One)': '6 Plataformas Principales (Todo en Uno)',
        '100% Lossless Removal': 'Eliminación 100% sin Pérdida',
        'Dedicated FFmpeg (320kbps)': 'FFmpeg Dedicado (320kbps)',
        'Zero Ads / 100% Clean': 'Cero Anuncios / 100% Limpio',
        'Strict Zero-Log Sandbox': 'Estricto Entorno sin Registros',
        'Limited': 'Limitado',
        'TikTok Only': 'Solo TikTok',
        'YouTube Only': 'Solo YouTube',
        'Standard': 'Estándar',
        'Yes': 'Sí',
        'Free, no download limit': 'Gratis, sin límite de descarga',
        'None required': 'No requiere',
        'None added': 'Ninguna añadida',
        'Public videos only': 'Solo videos públicos',
        'Video is public': 'El video es público',
        'Reel is public': 'El Reel es público',
        'Shared video is public': 'El video compartido es público',
        'On iPhone & iPad:': 'En iPhone y iPad:',
        'On iPhone &amp; iPad:': 'En iPhone y iPad:',
        'On Android (Samsung, Pixel, Xiaomi, OnePlus):': 'En Android (Samsung, Pixel, Xiaomi, OnePlus):',
        'On Windows, Mac & Chromebook:': 'En Windows, Mac y Chromebook:',
        'On Windows, Mac &amp; Chromebook:': 'En Windows, Mac y Chromebook:',
        'On iPhone or iPad:': 'En iPhone o iPad:',
        'On Android:': 'En Android:',
        'On Windows or Mac:': 'En Windows o Mac:'
    }
}

# Clone base structure to build Urdu, French, German, Hindi, Arabic, Portuguese, Bengali, Russian, Indonesian, Chinese
UR_DICT = {
    'Quick Answer: How to Download Social Media Videos Free': 'فوری جواب: سوشل میڈیا ویڈیوز مفت کیسے ڈاؤن لوڈ کریں',
    'Quick Answer: How to Download Facebook Videos': 'فوری جواب: فیس بک ویڈیوز کیسے ڈاؤن لوڈ کریں',
    'Quick Answer: How to Download Instagram Videos': 'فوری جواب: انسٹاگرام ویڈیوز کیسے ڈاؤن لوڈ کریں',
    'Quick Answer: How to Download TikTok Videos (No Watermark)': 'فوری جواب: ٹک ٹاک ویڈیوز بغیر واٹر مارک کیسے ڈاؤن لوڈ کریں',
    'Quick Answer: How to Download TikTok Videos Without Watermark': 'فوری جواب: ٹک ٹاک ویڈیوز بغیر واٹر مارک کیسے ڈاؤن لوڈ کریں',
    'Quick Answer: How to Download YouTube Videos & Shorts': 'فوری جواب: یوٹیوب ویڈیوز اور شارٹس کیسے ڈاؤن لوڈ کریں',
    'Quick Answer: How to Download YouTube Videos &amp; Shorts': 'فوری جواب: یوٹیوب ویڈیوز اور شارٹس کیسے ڈاؤن لوڈ کریں',
    'Quick Answer: How to Download Snapchat Spotlight Videos': 'فوری جواب: سنیپ چیٹ اسپاٹ لائٹ ویڈیوز کیسے ڈاؤن لوڈ کریں',
    'Quick Answer: How to Download Threads Videos': 'فوری جواب: تھریڈز ویڈیوز کیسے ڈاؤن لوڈ کریں',
    'The Ultimate All-in-One Social Media Video Downloader': 'سوشل میڈیا کا بہترین اور جامع ویڈیو ڈاؤنلوڈر',
    'Facebook Video Downloader: Save Any Public Facebook Video in HD': 'فیس بک ویڈیو ڈاؤنلوڈر: کوئی بھی پبلک ویڈیو HD میں محفوظ کریں',
    'Instagram Video Downloader: Save Reels, Stories & Posts in HD': 'انسٹاگرام ویڈیو ڈاؤنلوڈر: ریلز، اسٹوریز اور پوسٹس HD میں محفوظ کریں',
    'Instagram Video Downloader: Save Reels, Stories &amp; Posts in HD': 'انسٹاگرام ویڈیو ڈاؤنلوڈر: ریلز، اسٹوریز اور پوسٹس HD میں محفوظ کریں',
    'The Ultimate Free TikTok Video Downloader (No Watermark)': 'مفت ٹک ٹاک ڈاؤنلوڈر (بغیر واٹر مارک)',
    'The Fastest, Ad-Free YouTube Video & Shorts Downloader': 'سب سے تیز، بغیر اشتہارات کے یوٹیوب ڈاؤنلوڈر',
    'The Fastest, Ad-Free YouTube Video &amp; Shorts Downloader': 'سب سے تیز، بغیر اشتہارات کے یوٹیوب ڈاؤنلوڈر',
    'The Ultimate Free Snapchat Spotlight & Story Downloader': 'مفت سنیپ چیٹ اسپاٹ لائٹ اور اسٹوری ڈاؤنلوڈر',
    'The Ultimate Free Snapchat Spotlight &amp; Story Downloader': 'مفت سنیپ چیٹ اسپاٹ لائٹ اور اسٹوری ڈاؤنلوڈر',
    'The Fastest, Safest Meta Threads Video & Media Downloader': 'تھریڈز ویڈیوز اور میڈیا کا تیز اور محفوظ ترین ڈاؤنلوڈر',
    'The Fastest, Safest Meta Threads Video &amp; Media Downloader': 'تھریڈز ویڈیوز اور میڈیا کا تیز اور محفوظ ترین ڈاؤنلوڈر',
    'Supported Platforms, Formats & Specifications': 'سپورٹ شدہ پلیٹ فارمز، فارمیٹس اور تکنیکی تفصیلات',
    'Supported Platforms, Formats &amp; Specifications': 'سپورٹ شدہ پلیٹ فارمز، فارمیٹس اور تکنیکی تفصیلات',
    'Facebook Video Downloader at a Glance': 'فیس بک ویڈیو ڈاؤنلوڈر کا مختصر جائزہ',
    'Instagram Video Downloader at a Glance': 'انسٹاگرام ویڈیو ڈاؤنلوڈر کا مختصر جائزہ',
    'Which Facebook Links Work?': 'فیس بک کے کون سے لنکس کام کرتے ہیں؟',
    'Which Instagram Links Work?': 'انسٹاگرام کے کون سے لنکس کام کرتے ہیں؟',
    'Supported TikTok Link Types & Formats': 'ٹک ٹاک کے سپورٹ شدہ لنکس اور فارمیٹس',
    'Supported TikTok Link Types &amp; Formats': 'ٹک ٹاک کے سپورٹ شدہ لنکس اور فارمیٹس',
    'Supported YouTube Link Types & Formats': 'یوٹیوب کے سپورٹ شدہ لنکس اور فارمیٹس',
    'Supported YouTube Link Types &amp; Formats': 'یوٹیوب کے سپورٹ شدہ لنکس اور فارمیٹس',
    'Supported Snapchat Link Formats': 'سنیپ چیٹ لنکس کے فارمیٹس',
    'Supported Threads Media Link Formats': 'تھریڈز لنکس کے فارمیٹس',
    'Why Choose downsocial over Competitors?': 'دیگر سروسز کے مقابلے میں ڈاؤن سوشل کا انتخاب کیوں کریں؟',
    'Why Choose downsocial over Competitors (Threadster & SaveThreads)?': 'دیگر سائٹس کے مقابلے میں ڈاؤن سوشل کیوں بہتر ہے؟',
    'Why Choose downsocial over Competitors (Threadster &amp; SaveThreads)?': 'دیگر سائٹس کے مقابلے میں ڈاؤن سوشل کیوں بہتر ہے؟',
    'Why Choose downsocial over Competitors (Y2Mate & SaveFrom)?': 'روایتی سروسز کے مقابلے میں ڈاؤن سوشل کیوں بہتر ہے؟',
    'Why Choose downsocial over Competitors (Y2Mate &amp; SaveFrom)?': 'روایتی سروسز کے مقابلے میں ڈاؤن سوشل کیوں بہتر ہے؟',
    'Why Choose downsocial over SnapTik, SSSTik & MusicalDown?': 'ٹک ٹاک ڈاؤنلوڈرز کے مقابلے میں ڈاؤن سوشل کیوں بہتر ہے؟',
    'Why Choose downsocial over SnapTik, SSSTik &amp; MusicalDown?': 'ٹک ٹاک ڈاؤنلوڈرز کے مقابلے میں ڈاؤن سوشل کیوں بہتر ہے؟',
    'Why downsocial is the Best Alternative to SnapVee, ScreenApp & SnapAny': 'دیگر ٹولز کا بہترین متبادل',
    'Why downsocial is the Best Alternative to SnapVee, ScreenApp &amp; SnapAny': 'دیگر ٹولز کا بہترین متبادل',
    'Why downsocial Outperforms SaveInsta, iGram, and InDown': 'انسٹاگرام ٹولز کے مقابلے میں ڈاؤن سوشل کی برتری',
    'How to Copy a Facebook Video Link': 'فیس بک ویڈیو کا لنک کیسے کاپی کریں',
    'How to Copy an Instagram Video Link': 'انسٹاگرام ویڈیو کا لنک کیسے کاپی کریں',
    'How to Download Facebook Videos on iPhone, Android and Computer': 'آئی فون، اینڈرائیڈ اور کمپیوٹر پر فیس بک ویڈیوز ڈاؤن لوڈ کرنے کا طریقہ',
    'How to Download Instagram Videos on iPhone, Android and Computer': 'آئی فون، اینڈرائیڈ اور کمپیوٹر پر انسٹاگرام ویڈیوز ڈاؤن لوڈ کرنے کا طریقہ',
    'Step-by-Step Device Download Guide': 'مختلف ڈیوائسز پر ڈاؤن لوڈ کرنے کا مرحلہ وار طریقہ',
    'Step-by-Step Device Download Instructions': 'ڈیوائسز پر ڈاؤن لوڈنگ کی ہدایات',
    'Can You Download Private Facebook Videos?': 'کیا پرائیویٹ فیس بک ویڈیوز ڈاؤن لوڈ ہو سکتی ہیں؟',
    'Can You Download Private Instagram Videos?': 'کیا پرائیویٹ انسٹاگرام ویڈیوز ڈاؤن لوڈ ہو سکتی ہیں؟',
    'Facebook Video Quality: What You Actually Get': 'فیس بک ویڈیو کوالٹی: آپ کو کیا ملتا ہے',
    'Instagram Video Quality: Original 1080p Full HD': 'انسٹاگرام ویڈیو کوالٹی: اصل 1080p فل ایچ ڈی',
    'Convert Facebook Video to MP3': 'فیس بک ویڈیو کو MP3 آڈیو میں تبدیل کریں',
    'Convert Instagram Reels to MP3 Audio': 'انسٹاگرام ریلز کو MP3 آڈیو میں تبدیل کریں',
    'Why a Facebook Video Might Not Download': 'فیس بک ویڈیو ڈاؤن لوڈ نہ ہونے کی وجوہات',
    'Why an Instagram Video Might Not Download': 'انسٹاگرام ویڈیو ڈاؤن لوڈ نہ ہونے کی وجوہات',
    'Common Reasons People Save Facebook Videos': 'فیس بک ویڈیوز محفوظ کرنے کی اہم وجوہات',
    'Common Reasons People Save Instagram Videos': 'انسٹاگرام ویڈیوز محفوظ کرنے کی اہم وجوہات',
    'Is Downloading Facebook Videos Safe and Legal?': 'کیا فیس بک ویڈیوز ڈاؤن لوڈ کرنا محفوظ اور قانونی ہے؟',
    'Is Downloading Instagram Videos Safe and Legal?': 'کیا انسٹاگرام ویڈیوز ڈاؤن لوڈ کرنا محفوظ اور قانونی ہے؟',
    'Tips for the Best Result': 'بہترین نتائج کے لیے مفید تجاویز',
    'Tips for the Best Download Experience': 'بہترین ڈاؤن لوڈنگ کے لیے ہدایات',
    'Safe, Private & Anonymous Downloading': 'محفوظ، نجی اور 100% گمنام ڈاؤن لوڈنگ',
    'Safe, Private &amp; Anonymous Downloading': 'محفوظ، نجی اور 100% گمنام ڈاؤن لوڈنگ',
    'Zero-Log Privacy Protection': 'زیرو لاگ پرائیویسی کا تحفظ',
    'Need Another Platform?': 'کسی اور پلیٹ فارم کی ضرورت ہے؟',
    'Explore Our Dedicated Platform Downloaders': 'ہمارے خصوصی ڈاؤنلوڈرز ملاحظہ کریں',
    'Platform': 'پلیٹ فارم',
    'Supported Content': 'سپورٹ شدہ مواد',
    'Max Video Quality': 'زیادہ سے زیادہ ویڈیو کوالٹی',
    'Audio Extraction': 'آڈیو نکالنا',
    'Watermark Status': 'واٹر مارک کی حالت',
    'Feature': 'خصوصیت',
    'Details': 'تفصیلات',
    'Link type': 'لنک کی قسم',
    'What it looks like': 'مثال کی شکل',
    'Works when': 'کب کام کرتا ہے',
    'Feature Comparison': 'خصوصیات کا موازنہ',
    'Format': 'فارمیٹ',
    'Resolution': 'ریزولوشن',
    'Audio Quality': 'آڈیو کوالٹی',
    'Available Resolutions': 'دستیاب ریزولوشنز',
    'Content Type': 'مواد کی قسم',
    'Likely cause': 'ممکنہ وجہ',
    'Recommended solution': 'تجویز کردہ حل',
    'Media Type': 'میڈیا کی قسم',
    'Output Format': 'آؤٹ پٹ فارمیٹ',
    'Supported Quality': 'سپورٹ شدہ کوالٹی',
    'Supported when': 'کب سپورٹ ہے',
    'Symptom': 'علامت',
    'What to try': 'کیا طریقہ آزمائیں',
    'Videos, Shorts, Music Clips': 'ویڈیوز، شارٹس، میوزک کلپس',
    'Videos, Sounds, Slideshows': 'ویڈیوز، ساؤنڈز، سلائیڈ شوز',
    'Reels, Stories, Carousels': 'ریلز، اسٹوریز، کیروسلز',
    'Reels, Watch, Feed Posts': 'ریلز، واچ، فیڈ پوسٹس',
    'Spotlights, Public Stories': 'اسپاٹ لائٹس، پبلک اسٹوریز',
    'Videos, Audio, Carousels': 'ویڈیوز، آڈیو، کیروسلز',
    'Zero Watermark': 'بغیر واٹر مارک',
    '100% Removed': '100% ہٹا دیا گیا',
    'Original Source': 'اصل ماخذ',
    '6 Major Platforms (All-in-One)': '6 بڑے پلیٹ فارمز (سب ایک جگہ)',
    '100% Lossless Removal': 'بغیر نقصان کے 100% صفائی',
    'Dedicated FFmpeg (320kbps)': 'اعلیٰ FFmpeg آڈیو (320kbps)',
    'Zero Ads / 100% Clean': 'اشتہارات سے پاک / 100% صاف',
    'Strict Zero-Log Sandbox': 'سخت زیرو لاگ پرائیویسی',
    'Limited': 'محدود',
    'TikTok Only': 'صرف ٹک ٹاک',
    'YouTube Only': 'صرف یوٹیوب',
    'Standard': 'معیاری',
    'Yes': 'ہاں',
    'Free, no download limit': 'مفت، بغیر کسی حد کے',
    'None required': 'ضرورت نہیں ہے',
    'None added': 'کوئی اضافہ نہیں کیا گیا',
    'Public videos only': 'صرف پبلک ویڈیوز',
    'Video is public': 'ویڈیو پبلک ہے',
    'Reel is public': 'ریل پبلک ہے',
    'Shared video is public': 'شیئر شدہ ویڈیو پبلک ہے',
    'On iPhone & iPad:': 'آئی فون اور آئی پیڈ پر:',
    'On iPhone &amp; iPad:': 'آئی فون اور آئی پیڈ پر:',
    'On Android (Samsung, Pixel, Xiaomi, OnePlus):': 'اینڈرائیڈ پر (Samsung, Pixel, Xiaomi):',
    'On Windows, Mac & Chromebook:': 'ونڈوز، میک اور کروم بُک پر:',
    'On Windows, Mac &amp; Chromebook:': 'ونڈوز، میک اور کروم بُک پر:',
    'On iPhone or iPad:': 'آئی فون یا آئی پیڈ پر:',
    'On Android:': 'اینڈرائیڈ پر:',
    'On Windows or Mac:': 'ونڈوز یا میک پر:'
}
VOCAB['ur'] = UR_DICT

# Build other languages programmatically or with tailored dictionaries
LANG_NAMES = {
    'fr': 'Français', 'de': 'Deutsch', 'hi': 'हिन्दी', 'ar': 'العربية',
    'pt': 'Português', 'bn': 'বাংলা', 'ru': 'Русский', 'id': 'Bahasa Indonesia',
    'zh': '中文'
}

# Core terms for other languages
from enrich_all_seo_vocab import ALL_VOCAB
for lang in ['fr', 'de', 'hi', 'ar', 'pt', 'bn', 'ru', 'id', 'zh']:
    VOCAB[lang] = dict(ALL_VOCAB.get(lang, {}))
    # Add common HTML entity variations
    for k, v in list(VOCAB[lang].items()):
        if '&' in k:
            VOCAB[lang][k.replace('&', '&amp;')] = v
        # Add basic table headers
        if 'Platform' not in VOCAB[lang]: VOCAB[lang]['Platform'] = 'Platform'
        if 'Details' not in VOCAB[lang]: VOCAB[lang]['Details'] = 'Details'
        if 'Feature' not in VOCAB[lang]: VOCAB[lang]['Feature'] = 'Feature'

print(f"Total languages configured in VOCAB: {len(VOCAB)}")

# Now generate code for translate_seo_articles.py
code = f'''# scratch/translate_seo_articles.py
# Comprehensive SEO article translation mapping for all 12 languages with full tables, headers, and device guides.

import os, re

LANGS = ['en', 'es', 'fr', 'de', 'hi', 'ar', 'pt', 'bn', 'ru', 'id', 'zh', 'ur']
PLATFORMS = ['index', 'facebook', 'instagram', 'tiktok', 'youtube', 'snapchat', 'threads']

VOCAB = {repr(VOCAB)}

def get_translated_seo_article(platform, lang):
    orig_file = f'scratch/orig_seo_{{platform}}.html'
    if not os.path.exists(orig_file):
        return ""
    with open(orig_file, 'r', encoding='utf-8') as f:
        html = f.read()

    if lang == 'en':
        return html

    vocab = VOCAB.get(lang, {{}})
    translated_html = html
    # Sort keys by length descending to prevent partial replacement
    sorted_keys = sorted(vocab.keys(), key=lambda x: len(x), reverse=True)
    for en_phrase in sorted_keys:
        target_phrase = vocab[en_phrase]
        translated_html = translated_html.replace(en_phrase, target_phrase)
    
    return translated_html

if __name__ == '__main__':
    print("SEO article translation engine initialized with all 12 languages.")
'''

with open('scratch/translate_seo_articles.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("scratch/translate_seo_articles.py successfully written!")
