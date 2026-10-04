# scratch/build_all_locales.py
import json, os, sys
sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import data_common_seo as common_mod
import data_seo_static as seo_mod
import data_static_pages as static_mod
import build_platforms_data as plat_mod
import translate_seo_articles as translate_mod


LANGUAGES = common_mod.LANGUAGES
PLATFORMS = ['index', 'facebook', 'instagram', 'tiktok', 'youtube', 'snapchat', 'threads', 'private']

DEST_DIRS = [
    r'c:\my folder\Pictures\Desktop\downsocial\frontend\locales',
    r'c:\my folder\Pictures\Desktop\downsocial\frontend\shared\locales',
    r'c:\my folder\Pictures\Desktop\downsocial\frontend\facebook-downloader\locales',
    r'c:\my folder\Pictures\Desktop\downsocial\frontend\instagram-downloader\locales',
    r'c:\my folder\Pictures\Desktop\downsocial\frontend\tiktok-downloader\locales',
    r'c:\my folder\Pictures\Desktop\downsocial\frontend\youtube-downloader\locales',
    r'c:\my folder\Pictures\Desktop\downsocial\frontend\snapchat-downloader\locales',
    r'c:\my folder\Pictures\Desktop\downsocial\frontend\threads-downloader\locales',
    r'c:\my folder\Pictures\Desktop\downsocial\frontend\universal-downloader\locales',
    r'c:\my folder\Pictures\Desktop\downsocial\frontend\private-downloader\locales'
]

# Ensure all target directories exist
for d in DEST_DIRS:
    os.makedirs(d, exist_ok=True)

def generate_features_html(lang):
    title_map = {
        'en': ('Platform Features & Technical Specifications', 'Comprehensive breakdown of codecs, stream extraction capabilities, and quality metrics.'),
        'es': ('Características de la Plataforma y Especificaciones Técnicas', 'Detalle completo de códecs, capacidades de extracción de streams y métricas de calidad.'),
        'fr': ('Fonctionnalités de la Plateforme & Spécifications Techniques', 'Détail complet des codecs, capacités d’extraction et métriques de qualité.'),
        'de': ('Plattformfunktionen & Technische Spezifikationen', 'Detaillierte Übersicht über Codecs, Stream-Extraktion und Qualitätsmetriken.'),
        'hi': ('प्लेटफ़ॉर्म विशेषताएं और तकनीकी विनिर्देश', 'कोडेक, स्ट्रीम एक्सट्रैक्शन क्षमताओं और गुणवत्ता मानकों का पूरा विवरण।'),
        'ar': ('مميزات المنصة والمواصفات الفنية', 'تفاصيل شاملة عن برامج الترميز وقدرات استخراج التدفق ومعايير الجودة.'),
        'pt': ('Recursos da Plataforma e Especificações Técnicas', 'Detalhamento completo de codecs, recursos de extração e padrões de qualidade.'),
        'bn': ('প্ল্যাটফর্মের বৈশিষ্ট্য ও প্রযুক্তিগত স্পেসিফিকেশন', 'কোডেক, মিডিয়া এক্সট্র্যাকশন সুবিধা এবং গুণমানের বিশদ বিবরণ।'),
        'ru': ('Возможности платформы и технические спецификации', 'Полный обзор кодеков, параметров захвата потока и стандартов качества.'),
        'id': ('Fitur Platform & Spesifikasi Teknis', 'Rincian lengkap codec, kemampuan ekstraksi aliran media, dan standar kualitas.'),
        'zh': ('平台核心功能架构与技术规格白皮书', '全面剖析音视频编解码协议、流媒体直链嗅探能力与端到端传输质量标准。'),
        'ur': ('پلیٹ فارم کی خصوصیات اور تکنیکی وضاحتیں', 'کوڈیک، اسٹریم نکالنے کی صلاحیتوں اور کوالٹی کے معیارات کی تفصیلی تفصیل۔'),
        'it': ('Funzionalità della Piattaforma e Specifiche Tecniche', 'Dettaglio completo dei codec, delle capacità di estrazione dei flussi e degli standard qualitativi.')
    }
    t, intro = title_map.get(lang, title_map['en'])
    return f"""<h1>{t}</h1>
<p class="article-intro">{intro}</p>
<h2>1. 1080p, 2K & 4K Ultra HD MP4 Direct Video Capture</h2>
<p>downsocial integrates directly with high-performance edge CDN infrastructure across Facebook, Instagram, TikTok, YouTube, Snapchat, and Meta Threads to retrieve original media manifests without re-compression.</p>
<h2>2. Studio-Grade 320kbps MP3 Audio Transcoding</h2>
<p>Extract speech, background tracks, and viral music clips in genuine 320kbps/192kbps MP3 format using real-time server-side FFmpeg pipelines.</p>
<h2>3. 100% Automated Watermark Removal</h2>
<p>Our proprietary parsing engine detects clean source streams before floating or bouncing watermarks are overlaid.</p>
<h2>4. Multi-Media Post & Carousel Unpacking</h2>
<p>Full support for unpacking multi-slide Instagram carousel posts, Threads photo collections, and TikTok slideshows with one click.</p>
<h2>5. Zero-Knowledge Privacy Architecture</h2>
<p>Zero account registration, zero credential caching, and zero persistent file storage. 100% SSL-encrypted HTTPS transmission.</p>"""

def generate_contact_html(lang):
    title_map = {
        'en': ('Contact Support & Help Desk', 'We are here to assist with link extraction inquiries, broken URL reports, and partnerships.'),
        'es': ('Contacto y Centro de Ayuda', 'Estamos aquí para asistirte con reportes de enlaces caídos, dudas y sugerencias.'),
        'fr': ('Contact & Centre d’Assistance', 'Notre équipe est à votre disposition pour vous aider et recevoir vos signalements de liens.'),
        'de': ('Kontakt & Hilfe-Center', 'Wir helfen Ihnen gerne bei Fragen, Fehlermeldungen und Feedback weiter.'),
        'hi': ('संपर्क और सहायता केंद्र', 'हम लिंक एक्सट्रैक्शन से संबंधित प्रश्नों और बग रिपोर्ट में आपकी सहायता के लिए तैयार हैं।'),
        'ar': ('اتصل بالدعم الفني ومركز المساعدة', 'فريقنا متاح للإجابة على استفساراتكم والتعامل مع الإبلاغ عن الروابط المتعطلة.'),
        'pt': ('Contato e Central de Ajuda', 'Estamos à disposição para ajudar com dúvidas, relatórios de links e sugestões.'),
        'bn': ('যোগাযোগ ও সহায়তা কেন্দ্র', 'যেকোনো সমস্যা, অকার্যকর লিংক বা প্রশ্নের জন্য আমাদের সাপোর্ট টিম সর্বদা প্রস্তুত।'),
        'ru': ('Контакты и служба поддержки', 'Мы готовы помочь с решением проблем со скачиванием и ответить на любые вопросы.'),
        'id': ('Hubungi Kami & Pusat Bantuan', 'Kami siap membantu menyelesaikan kendala unduhan dan menerima laporan tautan rusak.'),
        'zh': ('联系我们与全球在线技术支持', '7×24 小时竭诚为您排查失效链接、解答流媒体解析疑问及处理商务合作。'),
        'ur': ('رابطہ اور ہیلپ ڈیسک', 'ہم لنک نکالنے کے مسائل، خراب یو آر ایل اور سوالات کے حل کے لیے حاضر ہیں۔'),
        'it': ('Contatti e Assistenza Clienti', 'Siamo a tua completa disposizione per aiutarti con link non funzionanti, domande e collaborazioni.')
    }
    t, intro = title_map.get(lang, title_map['en'])
    return f"""<h1>{t}</h1>
<p class="article-intro">{intro}</p>
<h2>Customer Support & Technical Inquiries</h2>
<p>If you experience an issue downloading a specific social media video, or have feedback on our tools, please reach out to our dedicated support desk:</p>
<ul>
    <li><strong>Email:</strong> support@downsocial.net</li>
    <li><strong>Response SLA:</strong> Within 24 hours guaranteed</li>
    <li><strong>Operating Hours:</strong> 24/7 Global Availability</li>
</ul>
<h2>Reporting a Broken URL</h2>
<p>When reporting a broken media link, please include:</p>
<ol>
    <li>The exact public URL from Facebook, Instagram, TikTok, YouTube, Snapchat, or Threads</li>
    <li>Your browser and device (e.g. Safari on iOS, Chrome on Android, Windows 11)</li>
    <li>The exact error message displayed (if any)</li>
</ol>
<h2>DMCA & Copyright Compliance</h2>
<p>downsocial operates strictly as a transient stream proxy and does not host media files. For intellectual property inquiries or link restrictions, contact <strong>dmca@downsocial.net</strong>.</p>"""

for lang in LANGUAGES:
    print(f"Building complete locale for: {lang}...")
    locale_data = {}

    # 1. SEO
    seo_dict = {}
    for p in ['index', 'facebook', 'instagram', 'tiktok', 'youtube', 'snapchat', 'threads', 'private', 'about', 'features', 'contact', 'privacy', 'terms']:
        t = seo_mod.SEO_TITLES.get(p, {}).get(lang, seo_mod.SEO_TITLES.get(p, {}).get('en', 'downsocial'))
        d = seo_mod.SEO_DESCS.get(p, {}).get(lang, seo_mod.SEO_DESCS.get(p, {}).get('en', 'downsocial video downloader'))
        kw = f"{p} video downloader, download {p} video, downsocial {p}, free video downloader"
        seo_dict[f"{p}Title"] = t
        seo_dict[f"{p}Desc"] = d
        seo_dict[f"{p}Keywords"] = kw
        seo_dict[f"{p}OgTitle"] = t
        seo_dict[f"{p}OgDesc"] = d
    locale_data['seo'] = seo_dict

    # 2. Common
    locale_data['common'] = common_mod.COMMON[lang]

    # 3. Notifications
    locale_data['notifications'] = common_mod.NOTIFICATIONS[lang]

    # 4. Platforms (index, facebook, instagram, tiktok, youtube, snapchat, threads, private)
    for p in PLATFORMS:
        p_data = plat_mod.get_platform_data(p, lang)
        if p == 'index':
            # Add backwards compatible keys for index
            p_data['mainTitle'] = p_data['title']
            p_data['processBtn'] = p_data['downloadBtn']
            p_data['f1Title'] = p_data['features'][0]['title']
            p_data['f1Desc'] = p_data['features'][0]['desc']
            p_data['f1Content'] = f"<h4><i class=\"{p_data['features'][0]['blogIcon']}\"></i> {p_data['features'][0]['blogTitle']}</h4><p>{p_data['features'][0]['blogP1']}</p><p>{p_data['features'][0]['blogP2']}</p>"
            p_data['f2Title'] = p_data['features'][1]['title']
            p_data['f2Desc'] = p_data['features'][1]['desc']
            p_data['f2Content'] = f"<h4><i class=\"{p_data['features'][1]['blogIcon']}\"></i> {p_data['features'][1]['blogTitle']}</h4><p>{p_data['features'][1]['blogP1']}</p><p>{p_data['features'][1]['blogP2']}</p>"
            p_data['f3Title'] = p_data['features'][2]['title']
            p_data['f3Desc'] = p_data['features'][2]['desc']
            p_data['f3Content'] = f"<h4><i class=\"{p_data['features'][2]['blogIcon']}\"></i> {p_data['features'][2]['blogTitle']}</h4><p>{p_data['features'][2]['blogP1']}</p><p>{p_data['features'][2]['blogP2']}</p>"
            p_data['howToSectionTitle'] = p_data['howToTitle']
            # Build howToContent html
            ht_html = ""
            for st in p_data['howToSteps']:
                ht_html += f"<h3>{st['title']}</h3><p>{st['desc']}</p><ul class=\"how-to-list\"><li><i class=\"fas fa-check\"></i> {st['bullet']}</li></ul>"
            p_data['howToContent'] = ht_html
            # Build howToHiddenContent html
            hth_html = ""
            for st in p_data['howToHidden']:
                hth_html += f"<h3>{st['title']}</h3><p>{st['desc']}</p><ul class=\"how-to-list\">"
                for b in st['bullets']:
                    hth_html += f"<li><i class=\"fas fa-check\"></i> {b}</li>"
                hth_html += f"</ul><p class=\"pro-tip\">{st['tip']}</p>"
            p_data['howToHiddenContent'] = hth_html
            p_data['readMoreBtn'] = common_mod.COMMON[lang]['readMore']
            p_data['readLessBtn'] = common_mod.COMMON[lang]['readLess']
            p_data['faqTitle'] = p_data['faqsTitle']
        
        # Override seoArticle with the rich table SEO article (100% original tables preserved in English, translated in others)
        if p in ['index', 'facebook', 'instagram', 'tiktok', 'youtube', 'snapchat', 'threads']:
            p_data['seoArticle'] = translate_mod.get_translated_seo_article(p, lang)
            
        locale_data[p] = p_data

    # 5. Static Pages (Full HTML including FAQ accordions, feature cards, and tables)
    for sp in ['about', 'features', 'contact', 'privacy', 'terms']:
        locale_data[sp] = static_mod.STATIC_PAGES[sp][lang]

    # Save to all target directory paths
    json_str = json.dumps(locale_data, ensure_ascii=False, indent=2)
    for d in DEST_DIRS:
        fpath = os.path.join(d, f"{lang}.json")
        with open(fpath, "w", encoding="utf-8") as fp:
            fp.write(json_str)

print("All 12 locales built and saved across all platform directories successfully!")
