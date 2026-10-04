# scratch/enrich_remaining_seo.py
# Provides authentic Russian, Indonesian, and Bengali dictionaries for index, tiktok, snapchat, and threads.

import os

# --- INDEX ---
INDEX_RU = {
    'qa_title': 'Быстрый ответ: как скачать видео из соцсетей бесплатно',
    'qa_text': 'Чтобы скачать любое общедоступное видео с YouTube, TikTok, Instagram, Facebook, Snapchat или Threads, скопируйте ссылку (Поделиться > Копировать ссылку), вставьте ее на <strong>downsocial.net</strong>, нажмите <strong>"Скачать видео"</strong> и выберите <strong>Video (HD)</strong> или <strong>Audio (HQ MP3)</strong>. Сервис на 100% бесплатен, не требует входа или установки приложений, не содержит рекламы и сохраняет файлы на iPhone, Android и ПК.',
    'h2': 'Универсальный бесплатный загрузчик видео из всех соцсетей',
    'intro': 'Раньше для сохранения видео требовались десятки сомнительных сайтов с навязчивой рекламой. <strong>downsocial.net</strong> объединяет все популярные платформы в одном быстром веб-сервисе. Скачивайте тренды TikTok без водяных знаков, YouTube Shorts в 1080p, Reels из Instagram и видео Facebook без лишних усилий.',
    't1_h3': 'Поддерживаемые платформы, форматы и спецификации',
    't1_headers': ['Платформа', 'Поддерживаемый контент', 'Максимальное качество', 'Извлечение аудио', 'Водяной знак'],
    't1_rows': [
        ('<i class="fab fa-youtube" style="color:#ff0000; margin-right:5px;"></i> YouTube', 'Видео, Shorts, музыкальные клипы', '4K UHD / 1080p Full HD', '320 kbps MP3', 'Без водяных знаков'),
        ('<i class="fab fa-tiktok" style="color:#25F4EE; margin-right:5px;"></i> TikTok', 'Видео, звуки, фото-слайдшоу', '1080p 60fps Full HD', '320 kbps MP3', '<span class="badge-highlight">100% удален</span>'),
        ('<i class="fab fa-instagram" style="color:#E1306C; margin-right:5px;"></i> Instagram', 'Reels, Stories, карусели', '1080p Full HD', '192 kbps MP3', 'Оригинальный поток'),
        ('<i class="fab fa-facebook-f" style="color:#1877F2; margin-right:5px;"></i> Facebook', 'Reels, Watch, публикации ленты', '1080p Full HD', '192 kbps MP3', 'Оригинальный поток'),
        ('<i class="fab fa-snapchat-ghost" style="color:#FFFC00; margin-right:5px;"></i> Snapchat', 'Spotlights, открытые истории', '1080p Full HD', '320 kbps MP3', 'Без водяных знаков'),
        ('<i class="fa-brands fa-threads" style="color:#ffffff; margin-right:5px;"></i> Threads', 'Видео, аудио, карусели', '1080p Full HD', '320 kbps MP3', 'Оригинальный поток')
    ],
    'comp_h3': 'Почему стоит выбрать downsocial, а не аналоги?',
    'comp_p': 'Обычные сайты вроде SaveFrom, SnapTik и Y2Mate перегружены всплывающей рекламой и искусственно занижают скорость. downsocial работает на безопасной облачной инфраструктуре без навязчивой рекламы.',
    'comp_headers': ['Сравнение возможностей', 'downsocial.net', 'SaveFrom.net', 'SnapTik.app', 'Y2Mate.is'],
    'comp_rows': [
        ('Поддерживаемые платформы', '6 основных платформ (Все в одном)', 'Ограничено', 'Только TikTok', 'Только YouTube'),
        ('Удаление водяного знака TikTok', '100% без потери качества', 'Базовое', 'Да', 'Не применимо'),
        ('Максимальное качество видео', 'До 4K UHD и 1080p HD', '720p (HD платно)', '1080p', '1080p'),
        ('Конвертер MP3 в реальном времени', 'Выделенный FFmpeg (320kbps)', '128kbps', 'Ограничено', '192kbps'),
        ('Навязчивая реклама и всплывающие окна', 'Ноль рекламы / 100% чисто', 'Много окон', 'Агрессивная реклама', 'Много рекламы'),
        ('Конфиденциальность и безопасность', 'Строгая политика без логов', 'Отслеживание куки', 'Трекеры рекламы', 'Трекеры рекламы')
    ],
    'guide_h3': 'Пошаговая инструкция для любых устройств',
    'ios': '<strong>На iPhone и iPad:</strong> откройте Safari, перейдите на <code>downsocial.net</code>, вставьте ссылку и нажмите "Скачать видео". Выберите "Video (HD)" и подтвердите загрузку. В списке загрузок откройте файл, нажмите Поделиться и выберите <em>"Сохранить видео"</em> в Фото.',
    'android': '<strong>На Android (Samsung, Pixel, Xiaomi, Motorola):</strong> откройте Chrome, вставьте ссылку на downsocial, нажмите "Скачать видео" и выберите нужное качество. Файл сохранится в папку <code>Downloads</code> и отобразится в Галерее.',
    'pc': '<strong>На Windows, Mac и Chromebook:</strong> откройте downsocial.net в браузере, вставьте ссылку и скачайте файл в выбранном формате.',
    'priv_h3': 'Безопасное, конфиденциальное и анонимное скачивание',
    'priv_p': 'Ваша конфиденциальность — главный приоритет. downsocial придерживается политики нулевых логов. Мы не требуем учетной записи, не сохраняем историю ваших скачиваний и шифруем весь трафик по 256-битному протоколу SSL.'
}

INDEX_ID = {
    'qa_title': 'Jawaban Cepat: Cara Mengunduh Video Media Sosial Gratis',
    'qa_text': 'Untuk mengunduh video publik apa pun dari YouTube, TikTok, Instagram, Facebook, Snapchat, atau Threads, salin tautan dari aplikasi (Bagikan > Salin Tautan), tempelkan di <strong>downsocial.net</strong>, klik <strong>"Download Video"</strong> dan pilih <strong>Video (HD)</strong> atau <strong>Audio (HQ MP3)</strong>. Layanan ini 100% gratis, tanpa login atau instalasi aplikasi, bebas iklan, dan berfungsi di iPhone, Android, serta PC.',
    'h2': 'Pengunduh Video Media Sosial All-in-One Terbaik',
    'intro': 'Dahulu menyimpan video internet membutuhkan puluhan situs mencurigakan penuh iklan pop-up. <strong>downsocial.net</strong> menyatukan seluruh ekosistem media sosial dalam satu aplikasi web modern dan cepat. Baik mengunduh TikTok tanpa watermark, YouTube Shorts 1080p, Instagram Reels, atau video Facebook, downsocial menyelesaikannya dengan mudah.',
    't1_h3': 'Platform, Format & Spesifikasi yang Didukung',
    't1_headers': ['Platform', 'Konten yang Didukung', 'Kualitas Video Maks', 'Ekstraksi Audio', 'Status Watermark'],
    't1_rows': [
        ('<i class="fab fa-youtube" style="color:#ff0000; margin-right:5px;"></i> YouTube', 'Video, Shorts, Klip Musik', '4K UHD / 1080p Full HD', '320 kbps MP3', 'Bebas Watermark'),
        ('<i class="fab fa-tiktok" style="color:#25F4EE; margin-right:5px;"></i> TikTok', 'Video, Suara, Slideshow Foto', '1080p 60fps Full HD', '320 kbps MP3', '<span class="badge-highlight">100% Dihapus</span>'),
        ('<i class="fab fa-instagram" style="color:#E1306C; margin-right:5px;"></i> Instagram', 'Reels, Stories, Carousel', '1080p Full HD', '192 kbps MP3', 'Sumber Asli'),
        ('<i class="fab fa-facebook-f" style="color:#1877F2; margin-right:5px;"></i> Facebook', 'Reels, Watch, Postingan Feed', '1080p Full HD', '192 kbps MP3', 'Sumber Asli'),
        ('<i class="fab fa-snapchat-ghost" style="color:#FFFC00; margin-right:5px;"></i> Snapchat', 'Spotlights, Cerita Publik', '1080p Full HD', '320 kbps MP3', 'Bebas Watermark'),
        ('<i class="fa-brands fa-threads" style="color:#ffffff; margin-right:5px;"></i> Threads', 'Video, Audio, Carousel', '1080p Full HD', '320 kbps MP3', 'Sumber Asli')
    ],
    'comp_h3': 'Mengapa Memilih downsocial Dibandingkan Pesaing?',
    'comp_p': 'Situs web lawas seperti SaveFrom, SnapTik, dan Y2Mate membebani pengguna dengan pop-up berbahaya dan kecepatan lambat. downsocial berjalan pada infrastruktur cloud yang aman tanpa iklan invasif.',
    'comp_headers': ['Perbandingan Fitur', 'downsocial.net', 'SaveFrom.net', 'SnapTik.app', 'Y2Mate.is'],
    'comp_rows': [
        ('Platform yang Didukung', '6 Platform Utama (All-in-One)', 'Terbatas', 'Hanya TikTok', 'Hanya YouTube'),
        ('Penghapusan Watermark TikTok', '100% Tanpa Kehilangan Kualitas', 'Standar', 'Ya', 'N/A'),
        ('Kualitas Video Maksimal', 'Hingga 4K UHD & 1080p HD', '720p (HD Berbayar)', '1080p', '1080p'),
        ('Konverter MP3 Real-Time', 'FFmpeg Khusus (320kbps)', '128kbps', 'Terbatas', '192kbps'),
        ('Iklan Pop-up Mengganggu', 'Nol Iklan / 100% Bersih', 'Banyak Pop-up', 'Iklan Agresif', 'Banyak Iklan'),
        ('Privasi & Keamanan', 'Lingkungan Tanpa Log Ketat', 'Lacak Cookie/IP', 'Pelacak Iklan', 'Pelacak Iklan')
    ],
    'guide_h3': 'Panduan Mengunduh Langkah Demi Langkah di Berbagai Perangkat',
    'ios': '<strong>Di iPhone dan iPad:</strong> Buka Safari, akses <code>downsocial.net</code>, tempel tautan dan ketuk "Download Video". Pilih "Video (HD)" dan konfirmasi unduhan. Buka file di Safari, ketuk Bagikan dan pilih <em>"Simpan Video"</em> untuk menyimpannya ke Foto.',
    'android': '<strong>Di Android (Samsung, Pixel, Xiaomi, Motorola):</strong> Buka Chrome, tempel tautan di downsocial, ketuk "Download Video" dan pilih format yang diinginkan. File langsung tersimpan di folder <code>Downloads</code> dan muncul di Galeri ponsel Anda.',
    'pc': '<strong>Di Windows, Mac dan Chromebook:</strong> Buka downsocial.net di peramban apa pun, tempel tautan dan klik "Download Video" untuk menyimpannya langsung ke komputer.',
    'priv_h3': 'Pengunduhan Aman, Privat & 100% Anonim',
    'priv_p': 'Privasi Anda terjamin. downsocial beroperasi dengan kebijakan tanpa pencatatan log (zero-log). Kami tidak meminta akun pengguna, tidak pernah menyimpan kata sandi, dan melindungi transmisi dengan enkripsi SSL 256-bit.'
}

INDEX_BN = {
    'qa_title': 'সহজ উত্তর: কীভাবে ফ্রিতে সোশ্যাল মিডিয়া ভিডিও ডাউনলোড করবেন',
    'qa_text': 'ইউটিউব, টিকটক, ইনস্টাগ্রাম, ফেসবুক, স্ন্যাপচ্যাট বা থ্রেডস থেকে যেকোনো পাবলিক ভিডিও ডাউনলোড করতে অ্যাপ থেকে লিংক কপি করুন (Share > Copy link), <strong>downsocial.net</strong> এ পেস্ট করুন, <strong>"Download Video"</strong> বাটনে ক্লিক করুন এবং <strong>Video (HD)</strong> বা <strong>Audio (HQ MP3)</strong> বেছে নিন। এটি ১০০% ফ্রি, কোনো অ্যাকাউন্ট বা অ্যাপ লাগবে না, বিজ্ঞাপনমুক্ত এবং iPhone, Android ও PC-তে কাজ করে।',
    'h2': 'সোশ্যাল মিডিয়ার সেরা অল-ইন-ওয়ান ভিডিও ডাউনলোডার',
    'intro': 'পূর্বে ভিডিও সেভ করতে গেলে নানা অনিরাপদ ও বিজ্ঞাপনে ভরা সাইটে যেতে হতো। <strong>downsocial.net</strong> সকল সোশ্যাল মিডিয়াকে একটি দ্রুত ও আধুনিক ওয়েব টুলে একীভূত করেছে। ওয়াটারমার্ক ছাড়া টিকটক, ১০৮০p ইউটিউব শর্টস, ইনস্টাগ্রাম রিলস বা ফেসবুক ভিডিও সহজেই ডাউনলোড করুন।',
    't1_h3': 'সমর্থিত প্ল্যাটফর্ম, ফরম্যাট ও স্পেসিফিকেশন',
    't1_headers': ['প্ল্যাটফর্ম', 'সমর্থিত কনটেন্ট', 'সর্বোচ্চ ভিডিও কোয়ালিটি', 'অডিও এক্সট্রাকশন', 'ওয়াটারমার্ক স্ট্যাটাস'],
    't1_rows': [
        ('<i class="fab fa-youtube" style="color:#ff0000; margin-right:5px;"></i> YouTube', 'ভিডিও, শর্টস, মিউজিক ক্লিপ', '4K UHD / 1080p Full HD', '320 kbps MP3', 'কোনো ওয়াটারমার্ক নেই'),
        ('<i class="fab fa-tiktok" style="color:#25F4EE; margin-right:5px;"></i> TikTok', 'ভিডিও, অডিও, স্লাইডশো', '1080p 60fps Full HD', '320 kbps MP3', '<span class="badge-highlight">১০০% অপসারিত</span>'),
        ('<i class="fab fa-instagram" style="color:#E1306C; margin-right:5px;"></i> Instagram', 'রিলস, স্টোরিজ, ক্যারোজেল', '1080p Full HD', '192 kbps MP3', 'আসল সোর্স'),
        ('<i class="fab fa-facebook-f" style="color:#1877F2; margin-right:5px;"></i> Facebook', 'রিলস, ওয়াচ, ফিড পোস্ট', '1080p Full HD', '192 kbps MP3', 'আসল সোর্স'),
        ('<i class="fab fa-snapchat-ghost" style="color:#FFFC00; margin-right:5px;"></i> Snapchat', 'স্পটলাইট, পাবলিক স্টোরিজ', '1080p Full HD', '320 kbps MP3', 'কোনো ওয়াটারমার্ক নেই'),
        ('<i class="fa-brands fa-threads" style="color:#ffffff; margin-right:5px;"></i> Threads', 'ভিডিও, অডিও, ক্যারোজেল', '1080p Full HD', '320 kbps MP3', 'আসল সোর্স')
    ],
    'comp_h3': 'অন্যান্য সাইটের চেয়ে downsocial কেন সেরা?',
    'comp_p': 'ঐতিহ্যবাহী সাইটগুলো প্রচুর ক্ষতিকর পপ-আপ বিজ্ঞাপন দেখায় এবং গতি কমিয়ে দেয়। downsocial কোনো বিজ্ঞাপন ছাড়াই সরাসরি উচ্চগতির ক্লাউডে কাজ করে।',
    'comp_headers': ['ফিচার তুলনা', 'downsocial.net', 'SaveFrom.net', 'SnapTik.app', 'Y2Mate.is'],
    'comp_rows': [
        ('সমর্থিত প্ল্যাটফর্ম', '৬টি প্রধান প্ল্যাটফর্ম (অল-ইন-ওয়ান)', 'সীমিত', 'শুধুমাত্র TikTok', 'শুধুমাত্র YouTube'),
        ('টিকটক ওয়াটারমার্ক রিমুভাল', '১০০% কোয়ালিটি বজায় রেখে রিমুভ', 'সাধারণ', 'হ্যাঁ', 'প্রযোজ্য নয়'),
        ('সর্বোচ্চ ভিডিও কোয়ালিটি', '4K UHD ও 1080p HD পর্যন্ত', '720p (HD পেইড)', '1080p', '1080p'),
        ('রিয়েল-টাইম MP3 কনভার্টার', 'ডেডিকেটেড FFmpeg (320kbps)', '128kbps', 'সীমিত', '192kbps'),
        ('পপ-আপ ও বিজ্ঞাপন', 'শূন্য বিজ্ঞাপন / ১০০% ক্লিন', 'প্রচুর পপ-আপ', 'আক্রমণাত্মক বিজ্ঞাপন', 'প্রচুর বিজ্ঞাপন'),
        ('নিরাপত্তা ও গোপনীয়তা', 'কঠোর জিরো-লগ পলিসি', 'কুকি ও আইপি ট্র্যাকিং', 'বিজ্ঞাপন ট্র্যাকার', 'বিজ্ঞাপন ট্র্যাকার')
    ],
    'guide_h3': 'বিভিন্ন ডিভাইসে ডাউনলোডের সহজ নিয়মাবলী',
    'ios': '<strong>iPhone ও iPad-এ:</strong> Safari খুলে <code>downsocial.net</code>-এ যান, লিংক পেস্ট করে "Download Video" চাপুন। 1080p MP4 বেছে নিন এবং ফাইলে গিয়ে Share থেকে <em>"Save Video"</em> দিন।',
    'android': '<strong>Android-এ:</strong> Chrome খুলে লিংক পেস্ট করুন এবং "Download Video" চাপুন। ফাইলটি সরাসরি আপনার Downloads ফোল্ডার ও ফোন গ্যালারিতে সেভ হবে।',
    'pc': '<strong>Windows ও Mac-এ:</strong> ব্রাউজারে downsocial.net খুলে লিংক পেস্ট করে পছন্দের ফরম্যাটে এক ক্লিকে ডাউনলোড করুন।',
    'priv_h3': 'নিরাপদ, সম্পূর্ণ প্রাইভেট ও অজ্ঞাতনামা ডাউনলোড',
    'priv_p': 'আপনার গোপনীয়তা শতভাগ সুরক্ষিত। downsocial কোনো লগ সংরক্ষণ করে না এবং আপনার ডাউনলোড তথ্য সম্পূর্ণ গোপন রাখে।'
}

# --- TIKTOK RU, ID, BN ---
TIKTOK_RU = {
    'qa_title': 'Быстрый ответ: как скачать видео из TikTok без водяного знака',
    'qa_text': 'Чтобы скачать видео из TikTok без водяного знака, откройте приложение TikTok, нажмите <strong>Поделиться > Ссылка</strong>, вставьте ссылку на <strong>downsocial.net/tiktok-downloader/</strong>, нажмите <strong>"Скачать видео"</strong> и выберите <strong>Video (HD No Watermark)</strong> или <strong>Audio (HQ MP3)</strong>. Сервис полностью бесплатен, не требует входа и сохраняет видео без логотипов на iPhone, Android и ПК.',
    'h2': 'Лучший бесплатный загрузчик видео TikTok (без водяных знаков)',
    'intro': 'TikTok — главная мировая платформа коротких видео, однако стандартная кнопка сохранения накладывает логотип с именем автора. <strong>downsocial.net</strong> извлекает исходный поток высокой четкости до наложения водяного знака, предоставляя вам чистый MP4-файл или MP3-аудиодорожку.',
    't1_h3': 'Поддерживаемые форматы ссылок TikTok',
    't1_headers': ['Тип контента', 'Пример ссылки', 'Качество', 'Формат файла'],
    't1_rows': [
        ('Видео TikTok (Без водяного знака)', 'tiktok.com/@user/video/...', '1080p Full HD (60fps)', 'MP4 без логотипа'),
        ('Короткая ссылка TikTok', 'vt.tiktok.com/... или vm.tiktok.com/...', 'Оригинальное HD', 'MP4 без логотипа'),
        ('Аудиодорожка TikTok (Звук)', 'tiktok.com/music/...', '192kbps / 320kbps', 'MP3 аудио'),
        ('Фото-слайдшоу TikTok', 'tiktok.com/@user/video/...', 'Исходное фото HD', 'Оригинальные кадры')
    ],
    'comp_h3': 'Почему downsocial превосходит SnapTik, SSSTik и MusicalDown',
    'comp_p': 'Популярные сайты вроде <em>SnapTik (snaptik.app)</em> и <em>SSSTik (ssstik.io)</em> заваливают пользователя агрессивной рекламой. downsocial предлагает мгновенную загрузку без рекламы, чистое видео 1080p и извлечение звука в MP3.',
    'comp_headers': ['Сравнение возможностей', 'downsocial.net', 'SnapTik', 'SSSTik', 'MusicalDown'],
    'comp_rows': [
        ('Удаление водяного знака', '100% чистое видео без логотипа', 'Без знака', 'Без знака', 'Без знака'),
        ('Максимальное качество видео', '1080p 60fps Full HD', '720p / 1080p', '720p', '720p'),
        ('Извлечение аудио (MP3)', '320kbps студийный MP3', '128kbps', 'Не всегда доступно', '128kbps'),
        ('Всплывающая реклама', 'Ноль рекламы / 100% чисто', 'Агрессивные всплывающие окна', 'Много рекламы', 'Навязчивая реклама'),
        ('Необходимость регистрации', 'Не требуется (Анонимно)', 'Нет', 'Нет', 'Нет')
    ],
    'guide_h3': 'Пошаговая инструкция для любых устройств',
    'ios': '<strong>На iPhone и iPad:</strong> откройте Safari, перейдите на <code>downsocial.net/tiktok-downloader/</code>, вставьте ссылку и нажмите "Скачать видео". Выберите вариант без водяного знака, откройте загруженный файл и выберите <em>"Сохранить видео"</em> в приложении Фото.',
    'android': '<strong>На Android:</strong> откройте Chrome, вставьте ссылку в downsocial и нажмите "Скачать видео". Файл без водяных знаков сохранится в папку <code>Downloads</code> и сразу появится в Галерее.',
    'pc': '<strong>На Windows, Mac и Chromebook:</strong> вставьте ссылку в браузере и сохраните видео на компьютере в один клик.',
    'priv_h3': 'Конфиденциальность и безопасность без сохранения данных',
    'priv_p': 'Мы не отслеживаем скачиваемые вами видео и не храним файлы на серверах. Все соединения защищены надежным шифрованием.'
}

TIKTOK_ID = {
    'qa_title': 'Jawaban Cepat: Cara Mengunduh Video TikTok Tanpa Watermark',
    'qa_text': 'Untuk mengunduh video TikTok apa pun tanpa tanda air, buka aplikasi TikTok, ketuk <strong>Bagikan > Salin Tautan</strong>, tempelkan URL di <strong>downsocial.net/tiktok-downloader/</strong>, klik <strong>"Download Video"</strong> dan pilih <strong>Video (HD No Watermark)</strong> atau <strong>Audio (HQ MP3)</strong>. Layanan ini 100% gratis, tanpa login atau instalasi aplikasi, dan tersimpan bersih di iPhone, Android, atau PC.',
    'h2': 'Pengunduh Video TikTok Gratis Terbaik (Tanpa Watermark)',
    'intro': 'TikTok merupakan platform video pendek terpopuler di dunia, namun tombol simpan bawaannya menempelkan logo watermark yang mengganggu. <strong>downsocial.net</strong> mengekstrak aliran video asli beresolusi tinggi sebelum watermark ditambahkan, memberi Anda file MP4 bersih atau audio MP3.',
    't1_h3': 'Format Tautan TikTok yang Didukung',
    't1_headers': ['Jenis Konten', 'Contoh Format Tautan', 'Resolusi', 'Format Output'],
    't1_rows': [
        ('Video TikTok (Bebas Watermark)', 'tiktok.com/@user/video/...', '1080p Full HD (60fps)', 'MP4 Bersih'),
        ('Tautan Pendek TikTok', 'vt.tiktok.com/... atau vm.tiktok.com/...', 'HD Asli', 'MP4 Bersih'),
        ('Audio / Suara TikTok', 'tiktok.com/music/...', '192kbps / 320kbps', 'Audio MP3'),
        ('Slideshow Foto TikTok', 'tiktok.com/@user/video/...', 'Resolusi Asli', 'Gambar / MP4')
    ],
    'comp_h3': 'Mengapa downsocial Lebih Baik dari SnapTik, SSSTik & MusicalDown',
    'comp_p': 'Alat populer seperti <em>SnapTik (snaptik.app)</em> dan <em>SSSTik (ssstik.io)</em> dipenuhi iklan pop-up yang mengganggu. downsocial memberikan unduhan berkecepatan tinggi tanpa iklan, kualitas 1080p asli, dan ekstraksi audio MP3 instan.',
    'comp_headers': ['Perbandingan Fitur', 'downsocial.net', 'SnapTik', 'SSSTik', 'MusicalDown'],
    'comp_rows': [
        ('Penghapusan Watermark', '100% Bersih Tanpa Logo', 'Bebas Watermark', 'Bebas Watermark', 'Bebas Watermark'),
        ('Kualitas Video Maksimal', '1080p 60fps Full HD', '720p / 1080p', '720p', '720p'),
        ('Ekstraksi Audio (MP3)', '320kbps Studio MP3', '128kbps', 'Tidak Tersedia', '128kbps'),
        ('Iklan Pop-up Mengganggu', 'Nol Iklan / 100% Bersih', 'Banyak Pop-up', 'Iklan Berlebihan', 'Banyak Iklan'),
        ('Perlu Akun / Pendaftaran', 'Tidak Perlu (100% Anonim)', 'Tidak', 'Tidak', 'Tidak')
    ],
    'guide_h3': 'Panduan Mengunduh Langkah demi Langkah di Semua Perangkat',
    'ios': '<strong>Di iPhone dan iPad:</strong> Buka Safari, akses <code>downsocial.net/tiktok-downloader/</code>, tempel tautan TikTok dan ketuk "Download Video". Pilih opsi tanpa watermark, buka file di Safari, ketuk Bagikan dan pilih <em>"Simpan Video"</em> untuk menyimpannya di Foto.',
    'android': '<strong>Di Android:</strong> Buka Chrome, tempel tautan di downsocial dan ketuk "Download Video". File MP4 tanpa watermark akan langsung tersimpan di folder <code>Downloads</code> dan muncul di Galeri ponsel Anda.',
    'pc': '<strong>Di Windows, Mac dan Chromebook:</strong> Tempel tautan di peramban dan simpan video ke komputer tanpa memerlukan perangkat lunak tambahan.',
    'priv_h3': 'Perlindungan Privasi Tanpa Pencatatan Log',
    'priv_p': 'Privasi Anda terjamin sepenuhnya. downsocial tidak pernah melacak riwayat unduhan Anda dan tidak menyimpan file video di server.'
}

TIKTOK_BN = {
    'qa_title': 'সহজ উত্তর: ওয়াটারমার্ক ছাড়া টিকটক ভিডিও কীভাবে ডাউনলোড করবেন',
    'qa_text': 'কোনো ওয়াটারমার্ক ছাড়া টিকটক ভিডিও সেভ করতে টিকটক অ্যাপে গিয়ে <strong>Share > Copy Link</strong> চাপুন, লিংকটি <strong>downsocial.net/tiktok-downloader/</strong> এ পেস্ট করুন, <strong>"Download Video"</strong> বাটনে ক্লিক করে <strong>Video (HD No Watermark)</strong> বা <strong>Audio (HQ MP3)</strong> নির্বাচন করুন। এটি সম্পূর্ণ বিনামূল্যে ও বিজ্ঞাপনমুক্ত।',
    'h2': 'সেরা ফ্রি টিকটক ভিডিও ডাউনলোডার (ওয়াটারমার্ক ছাড়া)',
    'intro': 'টিকটকের ডিফল্ট সেভ বাটনে লেখকের নাম ও লোগোর ওয়াটারমার্ক থাকে। <strong>downsocial.net</strong> কোনো ওয়াটারমার্ক ছাড়াই আসল ১০৮০p হাই-ডেফিনিশন ভিডিও ও MP3 মিউজিক ডাউনলোড করতে দেয়।',
    't1_h3': 'সমর্থিত টিকটক লিংক ফরম্যাট',
    't1_headers': ['কনটেন্টের ধরন', 'নমুনা লিংক', 'রেজোলিউশন', 'আউটপুট ফরম্যাট'],
    't1_rows': [
        ('টিকটক ভিডিও (ওয়াটারমার্কহীন)', 'tiktok.com/@user/video/...', '1080p Full HD (60fps)', 'ক্লিন MP4'),
        ('টিকটক শর্ট লিংক', 'vt.tiktok.com/... বা vm.tiktok.com/...', 'আসল HD', 'ক্লিন MP4'),
        ('টিকটক অডিও / ব্যাকগ্রাউন্ড সাউন্ড', 'tiktok.com/music/...', '192kbps / 320kbps', 'MP3 অডিও'),
        ('টিকটক ফটো স্লাইডশো', 'tiktok.com/@user/video/...', 'আসল কোয়ালিটি', 'ছবি / MP4')
    ],
    'comp_h3': 'SnapTik ও SSSTik এর চেয়ে downsocial কেন সেরা',
    'comp_p': 'অন্যান্য টুলগুলোতে বিরক্তিকর পপ-আপ বিজ্ঞাপন থাকে। downsocial কোনো প্রকার বিজ্ঞাপন ছাড়াই আসল ১০৮০p ভিডিও ও ৩২০kbps অডিও সরবরাহ করে।',
    'comp_headers': ['ফিচার তুলনা', 'downsocial.net', 'SnapTik', 'SSSTik', 'MusicalDown'],
    'comp_rows': [
        ('ওয়াটারমার্ক রিমুভাল', '১০০% ক্লিন লোগোহীন ভিডিও', 'লোগোহীন', 'লোগোহীন', 'লোগোহীন'),
        ('সর্বোচ্চ ভিডিও কোয়ালিটি', '1080p 60fps Full HD', '720p / 1080p', '720p', '720p'),
        ('অডিও এক্সট্রাকশন (MP3)', '320kbps স্টুডিও MP3', '128kbps', 'উপলব্ধ নয়', '128kbps'),
        ('বিরক্তিকর পপ-আপ বিজ্ঞাপন', 'শূন্য বিজ্ঞাপন / ১০০% ক্লিন', 'আক্রমণাত্মক পপ-আপ', 'অতিরিক্ত বিজ্ঞাপন', 'প্রচুর বিজ্ঞাপন'),
        ('লগইন বা রেজিস্ট্রেশন', 'কোনো লগইন লাগবে না', 'না', 'না', 'না')
    ],
    'guide_h3': 'সকল ডিভাইসে ডাউনলোডের নির্দেশিকা',
    'ios': '<strong>iPhone ও iPad-এ:</strong> Safari-তে <code>downsocial.net/tiktok-downloader/</code> খুলুন, লিংক পেস্ট করে ডাউনলোড চাপুন এবং সেভ ভিডিও দিন।',
    'android': '<strong>Android-এ:</strong> Chrome-এ পেস্ট করে ডাউনলোড চাপলেই ওয়াটারমার্ক ছাড়া ভিডিও সরাসরি গ্যালারিতে সেভ হবে।',
    'pc': '<strong>Windows ও Mac-এ:</strong> ব্রাউজারে লিংক পেস্ট করে এক ক্লিকে সেভ করুন।',
    'priv_h3': 'জিরো-লগ প্রাইভেসি প্রটেকশন',
    'priv_p': 'আমরা কোনো ডাউনলোড হিস্ট্রি বা ব্যক্তিগত ডেটা সংরক্ষণ করি না।'
}

# --- SNAPCHAT RU, ID, BN ---
SNAPCHAT_RU = {
    'qa_title': 'Быстрый ответ: как скачать видео из Snapchat Spotlight',
    'qa_text': 'Чтобы скачать видео из Snapchat Spotlight или открытую историю, откройте Snapchat, нажмите <strong>Поделиться > Скопировать ссылку</strong>, вставьте URL на <strong>downsocial.net/snapchat-downloader/</strong>, нажмите <strong>"Скачать видео"</strong> и выберите <strong>Video (HD MP4)</strong> или <strong>Audio (HQ MP3)</strong>. Сервис на 100% бесплатен, автор не получает уведомлений, водяные знаки не добавляются, а видео сохраняется на iPhone, Android или ПК.',
    'h2': 'Лучший загрузчик видео и историй из Snapchat Spotlight',
    'intro': 'Snapchat стал популярной площадкой для вирусных вертикальных видео через <strong>Snapchat Spotlight</strong>. <strong>downsocial.net</strong> предлагает самый быстрый и безопасный способ сохранять видео Spotlight и открытые истории на телефон или компьютер.',
    't1_h3': 'Поддерживаемые форматы ссылок Snapchat',
    't1_headers': ['Тип контента', 'Пример ссылки', 'Разрешение', 'Формат файла'],
    't1_rows': [
        ('Видео Snapchat Spotlight', 'snapchat.com/spotlight/W...', '1080p Full HD (60fps)', 'MP4 видео'),
        ('Публичная история автора', 'story.snapchat.com/s/...', 'Оригинальное качество', 'MP4 видео'),
        ('Звук / голос из Spotlight', 'snapchat.com/spotlight/...', '192kbps / 320kbps', 'MP3 аудио'),
        ('Короткая ссылка "Поделиться"', 'snapchat.com/t/...', 'Оригинальное качество', 'MP4 / MP3')
    ],
    'comp_h3': 'Почему downsocial — лучшая альтернатива SnapVee, ScreenApp и SnapAny',
    'comp_p': 'Устаревшие сервисы перегружены назойливой рекламой и часто выдают ошибки. downsocial обеспечивает прямую загрузку с серверов без рекламы и с мгновенной конвертацией в MP3.',
    'comp_headers': ['Сравнение возможностей', 'downsocial.net', 'SnapVee', 'SnapAny', 'ScreenApp'],
    'comp_rows': [
        ('Максимальное качество видео', '1080p 60fps Full HD', '720p', '720p', '1080p'),
        ('Аудио из Spotlight (MP3)', '320kbps HQ MP3', 'Базовое', 'Недоступно', 'Только видео'),
        ('Всплывающая реклама', 'Ноль рекламы / 100% чисто', 'Много окон', 'Частая реклама', 'Навязчивые баннеры'),
        ('Добавление водяных знаков', 'Нет (Оригинальное видео)', 'Нет', 'Знак в бесплатной версии', 'Нет'),
        ('Регистрация или аккаунт', 'Не требуется', 'Нет', 'Требует установку приложения', 'Нет')
    ],
    'guide_h3': 'Пошаговое руководство для любых устройств',
    'ios': '<strong>На iPhone и iPad:</strong> откройте Safari, перейдите на <code>downsocial.net/snapchat-downloader/</code>, вставьте ссылку и нажмите "Скачать видео". В загрузках Safari нажмите "Поделиться" и выберите <em>"Сохранить видео"</em> в Фото.',
    'android': '<strong>На Android:</strong> откройте Chrome, вставьте ссылку в downsocial и нажмите "Скачать видео". Файл сохранится в папку <code>Downloads</code> и отобразится в Галерее.',
    'pc': '<strong>На Windows, Mac и Chromebook:</strong> вставьте ссылку в браузере и сохраните видео в Full HD на компьютер.',
    'priv_h3': 'Анонимность и безопасность без сохранения логов',
    'priv_p': 'Полная анонимность: автор видео не получит уведомление о скачивании, а мы не сохраняем историю ваших запросов.'
}

SNAPCHAT_ID = {
    'qa_title': 'Jawaban Cepat: Cara Mengunduh Video Snapchat Spotlight',
    'qa_text': 'Untuk mengunduh video Snapchat Spotlight atau cerita publik, buka Snapchat, ketuk <strong>Bagikan > Salin Tautan</strong>, tempelkan URL di <strong>downsocial.net/snapchat-downloader/</strong>, klik <strong>"Download Video"</strong> dan pilih <strong>Video (HD MP4)</strong> atau <strong>Audio (HQ MP3)</strong>. Layanan ini 100% gratis, tidak memberi notifikasi ke pembuat konten, bebas watermark, dan tersimpan di iPhone atau Android.',
    'h2': 'Pengunduh Video & Cerita Snapchat Spotlight Terbaik',
    'intro': 'Snapchat telah menjadi pusat video pendek viral melalui <strong>Snapchat Spotlight</strong>. <strong>downsocial.net</strong> menyediakan utilitas tercepat dan paling aman untuk menyimpan video Spotlight dan cerita publik langsung ke ponsel atau komputer Anda.',
    't1_h3': 'Format Tautan Snapchat yang Didukung',
    't1_headers': ['Jenis Konten', 'Contoh Format Tautan', 'Resolusi', 'Format Output'],
    't1_rows': [
        ('Video Snapchat Spotlight', 'snapchat.com/spotlight/W...', '1080p Full HD (60fps)', 'Video MP4'),
        ('Cerita Publik Kreator', 'story.snapchat.com/s/...', 'Kualitas Asli', 'Video MP4'),
        ('Audio / Suara Spotlight', 'snapchat.com/spotlight/...', '192kbps / 320kbps', 'Audio MP3'),
        ('Tautan Bagikan Pendek', 'snapchat.com/t/...', 'Kualitas Asli', 'MP4 / MP3')
    ],
    'comp_h3': 'Mengapa downsocial Merupakan Alternatif Terbaik untuk SnapVee, ScreenApp & SnapAny',
    'comp_p': 'Alat lawas seperti SnapVee dan ScreenApp dipenuhi iklan pop-up yang mengganggu. downsocial memberikan unduhan langsung tanpa iklan dengan konversi instan ke MP3.',
    'comp_headers': ['Perbandingan Fitur', 'downsocial.net', 'SnapVee', 'SnapAny', 'ScreenApp'],
    'comp_rows': [
        ('Kualitas Video Maksimal', '1080p 60fps Full HD', '720p', '720p', '1080p'),
        ('Audio Spotlight (MP3)', '320kbps HQ MP3', 'Dasar', 'Tidak Tersedia', 'Hanya Video'),
        ('Iklan Pop-up Mengganggu', 'Nol Iklan / 100% Bersih', 'Banyak Pop-up', 'Iklan Sering Muncul', 'Banner Mengganggu'),
        ('Watermark Ditambahkan', 'Tidak Ada (Video Asli)', 'Tidak Ada', 'Ada Watermark di Versi Gratis', 'Tidak Ada'),
        ('Perlu Akun atau Daftar', 'Tidak Perlu Akun', 'Tidak', 'Perlu Instal Aplikasi', 'Tidak')
    ],
    'guide_h3': 'Panduan Mengunduh Langkah demi Langkah di Semua Perangkat',
    'ios': '<strong>Di iPhone dan iPad:</strong> Buka Safari, akses <code>downsocial.net/snapchat-downloader/</code>, tempel tautan Spotlight dan ketuk "Download Video". Setelah selesai, buka file di Safari dan pilih <em>"Simpan Video"</em> untuk menyimpannya di Foto.',
    'android': '<strong>Di Android:</strong> Buka Chrome, tempel tautan di downsocial dan klik "Download Video". Unduhan akan tersimpan di folder <code>Downloads</code> dan muncul di Galeri.',
    'pc': '<strong>Di Windows, Mac dan Chromebook:</strong> Tempel tautan di peramban web dan simpan video Full HD langsung ke komputer Anda.',
    'priv_h3': 'Perlindungan Privasi Tanpa Pencatatan Log',
    'priv_p': 'Anonimitas Anda terjamin penuh. Kami tidak memberi tahu pemilik video Snapchat bahwa kontennya telah diunduh, dan tidak menyimpan data unduhan Anda.'
}

SNAPCHAT_BN = {
    'qa_title': 'সহজ উত্তর: স্ন্যাপচ্যাট স্পটলাইট ভিডিও কীভাবে ডাউনলোড করবেন',
    'qa_text': 'যেকোনো স্ন্যাপচ্যাট স্পটলাইট বা পাবলিক স্টোরি সেভ করতে স্ন্যাপচ্যাটে <strong>Share > Copy link</strong> চাপুন, লিংকটি <strong>downsocial.net/snapchat-downloader/</strong> এ পেস্ট করুন, <strong>"Download Video"</strong> চাপুন এবং <strong>Video (HD MP4)</strong> বা <strong>Audio (HQ MP3)</strong> নির্বাচন করুন। এটি ১০০% ফ্রি, ক্রিয়েটর কোনো নোটিফিকেশন পাবে না এবং কোনো ওয়াটারমার্ক যুক্ত হয় না।',
    'h2': 'সেরা ফ্রি স্ন্যাপচ্যাট স্পটলাইট ও স্টোরি ডাউনলোডার',
    'intro': '<strong>Snapchat Spotlight</strong> এর মাধ্যমে ভাইরাল ভিডিও সেভ করার দ্রুততম ও নিরাপদ টুল হলো <strong>downsocial.net</strong>। সরাসরি কোনো বিজ্ঞাপন ছাড়াই ভিডিও সংরক্ষণ করুন।',
    't1_h3': 'সমর্থিত স্ন্যাপচ্যাট লিংক ফরম্যাট',
    't1_headers': ['কনটেন্টের ধরন', 'নমুনা লিংক', 'রেজোলিউশন', 'আউটপুট ফরম্যাট'],
    't1_rows': [
        ('স্ন্যাপচ্যাট স্পটলাইট ভিডিও', 'snapchat.com/spotlight/W...', '1080p Full HD (60fps)', 'MP4 ভিডিও'),
        ('পাবলিক ক্রিয়েটর স্টোরি', 'story.snapchat.com/s/...', 'আসল কোয়ালিটি', 'MP4 ভিডিও'),
        ('স্পটলাইট অডিও / সাউন্ড', 'snapchat.com/spotlight/...', '192kbps / 320kbps', 'MP3 অডিও'),
        ('শেয়ার করা শর্ট লিংক', 'snapchat.com/t/...', 'আসল কোয়ালিটি', 'MP4 / MP3')
    ],
    'comp_h3': 'অন্যান্য টুলের চেয়ে downsocial কেন সেরা',
    'comp_p': 'পুরানো টুলগুলোতে অতিরিক্ত বিজ্ঞাপন ও ব্যর্থ ডাউনলোডের সমস্যা থাকে। downsocial বিজ্ঞাপনমুক্ত সরাসরি ডাউনলোড ও তাৎক্ষণিক MP3 অডিও তৈরি করে।',
    'comp_headers': ['ফিচার তুলনা', 'downsocial.net', 'SnapVee', 'SnapAny', 'ScreenApp'],
    'comp_rows': [
        ('সর্বোচ্চ ভিডিও কোয়ালিটি', '1080p 60fps Full HD', '720p', '720p', '1080p'),
        ('স্পটলাইট অডিও (MP3)', '320kbps HQ MP3', 'সাধারণ', 'উপলব্ধ নয়', 'শুধু ভিডিও'),
        ('বিজ্ঞাপন ও পপ-আপ', 'শূন্য বিজ্ঞাপন / ১০০% ক্লিন', 'প্রচুর পপ-আপ', 'ঘন ঘন বিজ্ঞাপন', 'বিরক্তিকর ব্যানার'),
        ('ওয়াটারমার্ক', 'কোনো ওয়াটারমার্ক নেই', 'নেই', 'ফ্রি ভার্সনে ওয়াটারমার্ক', 'নেই'),
        ('লগইন বা অ্যাকাউন্ট', 'কোনো অ্যাকাউন্ট লাগবে না', 'না', 'অ্যাপ ইনস্টল চায়', 'না')
    ],
    'guide_h3': 'সকল ডিভাইসে ডাউনলোডের নিয়মাবলী',
    'ios': '<strong>iPhone ও iPad-এ:</strong> Safari খুলে <code>downsocial.net/snapchat-downloader/</code> এ লিংক পেস্ট করে ডাউনলোড চাপুন এবং সেভ ভিডিও দিন।',
    'android': '<strong>Android-এ:</strong> Chrome-এ পেস্ট করে ডাউনলোড চাপলে ফাইল সরাসরি Downloads ফোল্ডার ও গ্যালারিতে সেভ হবে।',
    'pc': '<strong>Windows ও Mac-এ:</strong> ব্রাউজারে লিংক পেস্ট করে সরাসরি Full HD ভিডিও সেভ করুন।',
    'priv_h3': 'সম্পূর্ণ অজ্ঞাতনামা ও সুরক্ষিত প্রাইভেসি',
    'priv_p': 'আপনার ডাউনলোড সম্পূর্ণ বেনামী থাকে এবং ক্রিয়েটর কোনো নোটিফিকেশন পায় না।'
}

# --- THREADS RU, ID, BN ---
THREADS_RU = {
    'qa_title': 'Быстрый ответ: как скачать видео из Threads',
    'qa_text': 'Чтобы скачать видео или фото из Meta Threads, откройте Threads, нажмите <strong>Поделиться > Скопировать ссылку</strong>, вставьте URL на <strong>downsocial.net/threads-downloader/</strong>, нажмите <strong>"Скачать видео"</strong> и выберите <strong>Video (HD MP4)</strong> или <strong>Audio (HQ MP3)</strong>. Сервис полностью бесплатен, не требует входа в Instagram и сохраняет файлы на iPhone, Android и ПК.',
    'h2': 'Самый быстрый и безопасный загрузчик видео из Meta Threads',
    'intro': '<strong>Meta Threads</strong> быстро стала популярной текстовой и медиа-платформой. <strong>downsocial.net</strong> предлагает современный веб-инструмент для сохранения видеороликов, аудиозаписей и каруселей из Threads в высоком качестве 1080p HD без рекламы.',
    't1_h3': 'Поддерживаемые форматы медиассылок Threads',
    't1_headers': ['Тип контента', 'Пример ссылки', 'Разрешение', 'Формат файла'],
    't1_rows': [
        ('Видеопост Threads', 'threads.net/@user/post/...', '1080p Full HD (60fps)', 'MP4 видео'),
        ('Аудиосообщение Threads', 'threads.net/@user/post/...', '192kbps / 320kbps', 'MP3 аудио'),
        ('Карусель из нескольких медиа', 'threads.net/@user/post/...', 'Исходное качество', 'Все медиафайлы'),
        ('Короткая ссылка Threads', 'threads.net/t/...', 'Оригинальное HD', 'MP4 / MP3')
    ],
    'comp_h3': 'Почему downsocial лучше Threadster и SaveThreads',
    'comp_p': 'Сайты вроде <em>Threadster</em> и <em>SaveThreads</em> страдают от навязчивой рекламы и частых сбоев при обработке каруселей. downsocial работает на выделенной облачной сети и гарантирует мгновенную загрузку.',
    'comp_headers': ['Сравнение возможностей', 'downsocial.net', 'Threadster', 'SaveThreads', 'SnapThreads'],
    'comp_rows': [
        ('Максимальное качество видео', '1080p 60fps Full HD', '720p', '1080p', '720p'),
        ('Карусели из нескольких фото/видео', 'Полная поддержка всех файлов', 'Только первое фото', 'Сбои при загрузке', 'Ограничено'),
        ('Аудиодорожка (MP3)', '320kbps HQ MP3', 'Недоступно', '128kbps', 'Только видео'),
        ('Всплывающая реклама', 'Ноль рекламы / 100% чисто', 'Много окон', 'Агрессивная реклама', 'Навязчивые баннеры'),
        ('Требование входа через Instagram', 'Не требуется (100% анонимно)', 'Нет', 'Нет', 'Нет')
    ],
    'guide_h3': 'Инструкция по загрузке для любых устройств',
    'ios': '<strong>На iPhone и iPad:</strong> откройте Safari, перейдите на <code>downsocial.net/threads-downloader/</code>, вставьте ссылку на публикацию Threads и нажмите "Скачать видео". В загрузках нажмите "Поделиться" и выберите <em>"Сохранить видео"</em> в Фото.',
    'android': '<strong>На Android:</strong> откройте Chrome, вставьте ссылку в downsocial и нажмите "Скачать видео". Файл MP4 сохранится в папку <code>Downloads</code> и отобразится в Галерее.',
    'pc': '<strong>На Windows, Mac и Chromebook:</strong> вставьте ссылку на пост Threads в браузере и сохраните видео прямо на компьютер.',
    'priv_h3': 'Конфиденциальность и безопасность данных',
    'priv_p': 'Полная конфиденциальность. Мы не собираем личные данные, не запрашиваем пароли от аккаунта и защищаем передачу по 256-битному протоколу SSL.'
}

THREADS_ID = {
    'qa_title': 'Jawaban Cepat: Cara Mengunduh Video Threads',
    'qa_text': 'Untuk mengunduh video atau media dari Meta Threads, buka aplikasi Threads, ketuk <strong>Bagikan > Salin Tautan</strong>, tempelkan URL di <strong>downsocial.net/threads-downloader/</strong>, klik <strong>"Download Video"</strong> dan pilih <strong>Video (HD MP4)</strong> atau <strong>Audio (HQ MP3)</strong>. Layanan ini 100% gratis, tanpa perlu masuk ke akun Instagram, bebas iklan, dan berfungsi di iPhone, Android, serta PC.',
    'h2': 'Pengunduh Video & Media Meta Threads Tercepat dan Paling Aman',
    'intro': '<strong>Meta Threads</strong> telah berkembang pesat sebagai platform berbagi teks dan media. <strong>downsocial.net</strong> menghadirkan utilitas modern untuk mengunduh video, rekaman suara, dan postingan carousel Threads berkualitas tinggi 1080p HD tanpa iklan.',
    't1_h3': 'Format Tautan Media Threads yang Didukung',
    't1_headers': ['Jenis Konten', 'Contoh Format Tautan', 'Resolusi', 'Format Output'],
    't1_rows': [
        ('Postingan Video Threads', 'threads.net/@user/post/...', '1080p Full HD (60fps)', 'Video MP4'),
        ('Pesan Suara / Audio Threads', 'threads.net/@user/post/...', '192kbps / 320kbps', 'Audio MP3'),
        ('Carousel Multi-Media', 'threads.net/@user/post/...', 'Kualitas Asli', 'Semua Media'),
        ('Tautan Pendek Threads', 'threads.net/t/...', 'HD Asli', 'MP4 / MP3')
    ],
    'comp_h3': 'Mengapa downsocial Lebih Baik dari Threadster dan SaveThreads',
    'comp_p': 'Situs seperti <em>Threadster</em> dan <em>SaveThreads</em> dipenuhi pop-up iklan dan sering gagal mengekstrak carousel. downsocial beroperasi dengan jaringan cloud berkecepatan tinggi tanpa iklan mengganggu.',
    'comp_headers': ['Perbandingan Fitur', 'downsocial.net', 'Threadster', 'SaveThreads', 'SnapThreads'],
    'comp_rows': [
        ('Kualitas Video Maksimal', '1080p 60fps Full HD', '720p', '1080p', '720p'),
        ('Pengunduh Carousel Lengkap', 'Dukungan Penuh Semua Slide', 'Hanya Slide Pertama', 'Sering Gagal', 'Terbatas'),
        ('Audio Suara (MP3)', '320kbps HQ MP3', 'Tidak Tersedia', '128kbps', 'Hanya Video'),
        ('Iklan Pop-up Mengganggu', 'Nol Iklan / 100% Bersih', 'Banyak Pop-up', 'Iklan Agresif', 'Banner Mengganggu'),
        ('Perlu Login Instagram', 'Tidak Perlu (100% Anonim)', 'Tidak', 'Tidak', 'Tidak')
    ],
    'guide_h3': 'Panduan Mengunduh Langkah demi Langkah di Semua Perangkat',
    'ios': '<strong>Di iPhone dan iPad:</strong> Buka Safari, akses <code>downsocial.net/threads-downloader/</code>, tempel tautan Threads dan ketuk "Download Video". Buka file di Safari, ketuk Bagikan dan pilih <em>"Simpan Video"</em> untuk menyimpannya di Foto.',
    'android': '<strong>Di Android:</strong> Buka Chrome, tempel tautan di downsocial dan klik "Download Video". File MP4 langsung tersimpan di folder <code>Downloads</code> dan muncul di Galeri ponsel Anda.',
    'pc': '<strong>Di Windows, Mac dan Chromebook:</strong> Tempel tautan Threads di peramban web dan simpan video ke komputer tanpa perangkat lunak pihak ketiga.',
    'priv_h3': 'Perlindungan Privasi Tanpa Pencatatan Log',
    'priv_p': 'downsocial tidak pernah meminta kredensial Instagram Anda dan tidak menyimpan riwayat unduhan media.'
}

THREADS_BN = {
    'qa_title': 'সহজ উত্তর: থ্রেডস ভিডিও কীভাবে ডাউনলোড করবেন',
    'qa_text': 'মেটা থ্রেডস থেকে ভিডিও ডাউনলোড করতে থ্রেডস অ্যাপে <strong>Share > Copy link</strong> চাপুন, লিংকটি <strong>downsocial.net/threads-downloader/</strong> এ পেস্ট করুন, <strong>"Download Video"</strong> চাপুন এবং <strong>Video (HD MP4)</strong> বা <strong>Audio (HQ MP3)</strong> নির্বাচন করুন। এটি সম্পূর্ণ বিনামূল্যে, ইনস্টাগ্রাম লগইন লাগবে না এবং বিজ্ঞাপনমুক্ত।',
    'h2': 'মেটা থ্রেডস ভিডিও ডাউনলোডার: দ্রুত ও নিরাপদ মিডিয়া সেভার',
    'intro': '<strong>Meta Threads</strong> এর ভিডিও, অডিও ও ক্যারোজেল পোস্ট সেভ করার জন্য <strong>downsocial.net</strong> হলো দ্রুততম ও বিজ্ঞাপনহীন নির্ভরযোগ্য টুল।',
    't1_h3': 'সমর্থিত থ্রেডস লিংক ফরম্যাট',
    't1_headers': ['কনটেন্টের ধরন', 'নমুনা লিংক', 'রেজোলিউশন', 'আউটপুট ফরম্যাট'],
    't1_rows': [
        ('থ্রেডস ভিডিও পোস্ট', 'threads.net/@user/post/...', '1080p Full HD (60fps)', 'MP4 ভিডিও'),
        ('থ্রেডস অডিও / ভয়েস নোট', 'threads.net/@user/post/...', '192kbps / 320kbps', 'MP3 অডিও'),
        ('ক্যারোজেল অ্যালবাম', 'threads.net/@user/post/...', 'আসল কোয়ালিটি', 'সব ফাইল'),
        ('থ্রেডস শর্ট লিংক', 'threads.net/t/...', 'আসল HD', 'MP4 / MP3')
    ],
    'comp_h3': 'Threadster ও SaveThreads এর চেয়ে downsocial কেন সেরা',
    'comp_p': 'অন্যান্য সাইটে পপ-আপ বিজ্ঞাপন ও সার্ভার এরর থাকে। downsocial বিজ্ঞাপনমুক্ত সরাসরি সার্ভার থেকে দ্রুত ডাউনলোড নিশ্চিত করে।',
    'comp_headers': ['ফিচার তুলনা', 'downsocial.net', 'Threadster', 'SaveThreads', 'SnapThreads'],
    'comp_rows': [
        ('সর্বোচ্চ ভিডিও কোয়ালিটি', '1080p 60fps Full HD', '720p', '1080p', '720p'),
        ('ক্যারোজেল আনপ্যাকার', 'সব স্লাইড ডাউনলোড সুবিধা', 'শুধু প্রথম স্লাইড', 'ত্রুটি হয়', 'সীমিত'),
        ('অডিও এক্সট্রাকশন (MP3)', '320kbps HQ MP3', 'উপলব্ধ নয়', '128kbps', 'শুধু ভিডিও'),
        ('বিজ্ঞাপন ও পপ-আপ', 'শূন্য বিজ্ঞাপন / ১০০% ক্লিন', 'প্রচুর পপ-আপ', 'আক্রমণাত্মক বিজ্ঞাপন', 'ব্যনার বিজ্ঞাপন'),
        ('ইনস্টাগ্রাম লগইন প্রয়োজন', 'কোনো লগইন লাগবে না', 'না', 'না', 'না')
    ],
    'guide_h3': 'সকল ডিভাইসে ডাউনলোডের নিয়মাবলী',
    'ios': '<strong>iPhone ও iPad-এ:</strong> Safari-তে <code>downsocial.net/threads-downloader/</code> খুলুন, লিংক পেস্ট করে ডাউনলোড চাপুন এবং সেভ ভিডিও দিন।',
    'android': '<strong>Android-এ:</strong> Chrome-এ পেস্ট করে ডাউনলোড চাপলে ফাইল সরাসরি Downloads ফোল্ডার ও গ্যালারিতে সেভ হবে।',
    'pc': '<strong>Windows ও Mac-এ:</strong> ব্রাউজারে লিংক পেস্ট করে এক ক্লিকে সেভ করুন।',
    'priv_h3': 'জিরো-লগ প্রাইভেসি প্রটেকশন',
    'priv_p': 'আমরা কোনো লগ বা ব্রাউজিং হিস্ট্রি সংরক্ষণ করি না।'
}

# --- UPDATE seo_data_index.py ---
def update_index():
    # Save back to file
    with open('scratch/seo_data_index.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace assignment
    old_assign = """# Clone for bn, ru, id with authentic localized terms
BN_DATA = dict(INDEX_DATA['hi']) # Fallback baseline with translated headers
RU_DATA = dict(INDEX_DATA['de'])
ID_DATA = dict(INDEX_DATA['pt'])
INDEX_DATA['bn'] = INDEX_DATA['hi']
INDEX_DATA['ru'] = INDEX_DATA['de']
INDEX_DATA['id'] = INDEX_DATA['pt']"""
    
    new_assign = f"""INDEX_DATA['ru'] = {repr(INDEX_RU)}
INDEX_DATA['id'] = {repr(INDEX_ID)}
INDEX_DATA['bn'] = {repr(INDEX_BN)}"""
    
    if old_assign in content:
        content = content.replace(old_assign, new_assign)
        with open('scratch/seo_data_index.py', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated seo_data_index.py with genuine RU, ID, BN!")
    else:
        print("Could not find old_assign in seo_data_index.py")

# --- UPDATE seo_data_tiktok.py ---
def update_tiktok():
    with open('scratch/seo_data_tiktok.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    old_assign = """TIKTOK_DATA['bn'] = TIKTOK_DATA['hi']
TIKTOK_DATA['ru'] = TIKTOK_DATA['de']
TIKTOK_DATA['id'] = TIKTOK_DATA['pt']"""
    
    new_assign = f"""TIKTOK_DATA['ru'] = {repr(TIKTOK_RU)}
TIKTOK_DATA['id'] = {repr(TIKTOK_ID)}
TIKTOK_DATA['bn'] = {repr(TIKTOK_BN)}"""
    
    if old_assign in content:
        content = content.replace(old_assign, new_assign)
        with open('scratch/seo_data_tiktok.py', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated seo_data_tiktok.py with genuine RU, ID, BN!")
    else:
        print("Could not find old_assign in seo_data_tiktok.py")

# --- UPDATE seo_data_snapchat.py ---
def update_snapchat():
    with open('scratch/seo_data_snapchat.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    old_assign = """SNAPCHAT_DATA['bn'] = SNAPCHAT_DATA['hi']
SNAPCHAT_DATA['ru'] = SNAPCHAT_DATA['de']
SNAPCHAT_DATA['id'] = SNAPCHAT_DATA['pt']"""
    
    new_assign = f"""SNAPCHAT_DATA['ru'] = {repr(SNAPCHAT_RU)}
SNAPCHAT_DATA['id'] = {repr(SNAPCHAT_ID)}
SNAPCHAT_DATA['bn'] = {repr(SNAPCHAT_BN)}"""
    
    if old_assign in content:
        content = content.replace(old_assign, new_assign)
        with open('scratch/seo_data_snapchat.py', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated seo_data_snapchat.py with genuine RU, ID, BN!")
    else:
        print("Could not find old_assign in seo_data_snapchat.py")

# --- UPDATE seo_data_threads.py ---
def update_threads():
    with open('scratch/seo_data_threads.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    old_assign = """THREADS_DATA['bn'] = THREADS_DATA['hi']
THREADS_DATA['ru'] = THREADS_DATA['de']
THREADS_DATA['id'] = THREADS_DATA['pt']"""
    
    new_assign = f"""THREADS_DATA['ru'] = {repr(THREADS_RU)}
THREADS_DATA['id'] = {repr(THREADS_ID)}
THREADS_DATA['bn'] = {repr(THREADS_BN)}"""
    
    if old_assign in content:
        content = content.replace(old_assign, new_assign)
        with open('scratch/seo_data_threads.py', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated seo_data_threads.py with genuine RU, ID, BN!")
    else:
        print("Could not find old_assign in seo_data_threads.py")

if __name__ == '__main__':
    update_index()
    update_tiktok()
    update_snapchat()
    update_threads()
