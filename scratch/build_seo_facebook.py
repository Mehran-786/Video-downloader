# scratch/build_seo_facebook.py
# Generates scratch/seo_data_facebook.py with complete translations for all 12 languages.

import json
import os

FACEBOOK_TRANSLATIONS = {
    'es': {
        'qa_title': 'Respuesta rápida: Cómo descargar videos de Facebook',
        'qa_text': 'Para descargar un video de Facebook, copia su enlace, pégalo en la casilla superior de esta página, presiona <em>Descargar video</em> y elige HD, Normal o MP3. Es gratis, no necesita inicio de sesión ni aplicación, y funciona en iPhone, Android, Windows y Mac. Solo se pueden descargar videos públicos.',
        'h2': 'Descargador de videos de Facebook: Guarda cualquier video público de Facebook en HD',
        'intro': 'Este <strong>descargador de videos de Facebook</strong> está diseñado para una sola tarea: convertir un enlace de video público, Reel o Watch de Facebook en un archivo descargable. Lee el video público, muestra los formatos disponibles y transmite tu elección a tu dispositivo como video MP4 o audio MP3. No se instala nada, no se almacena nada en nuestros servidores y tu cuenta de Facebook nunca se ve involucrada.',
        't1_h3': 'Descargador de videos de Facebook de un vistazo',
        't1_headers': ['Característica', 'Detalles'],
        't1_rows': [
            ('Contenido compatible', 'Videos públicos de Facebook, Reels, videos Watch y Stories públicas o transmisiones en vivo finalizadas mientras sigan disponibles'),
            ('Enlaces aceptados', 'facebook.com, m.facebook.com, facebook.com/share, fb.watch'),
            ('Formatos de salida', 'Video MP4 (HD y Normal), audio MP3 (192 kbps y 128 kbps)'),
            ('Calidad de video', 'La mejor versión que ofrece Facebook para ese video, comúnmente de 720p a 1080p. Sin escalado falso'),
            ('Precio', '<span class="badge-highlight">Gratis, sin límite de descargas</span>'),
            ('Cuenta o inicio de sesión', '<span class="badge-highlight">No requerido</span>'),
            ('Marca de agua', '<span class="badge-highlight">Ninguna añadida</span>'),
            ('Funciona en', 'iPhone, iPad, Android, Windows, macOS, Linux (cualquier navegador moderno)'),
            ('Archivos guardados por nosotros', 'Ninguno. Las transmisiones no se guardan'),
            ('Limitaciones', 'Solo videos públicos. No puede eludir grupos privados ni publicaciones solo para amigos. Calidad limitada por la subida original')
        ],
        't2_h3': '¿Qué enlaces de Facebook funcionan?',
        't2_intro': 'Facebook utiliza varios formatos de enlaces. Si el video detrás del enlace es público, todos estos son compatibles:',
        't2_headers': ['Tipo de enlace', 'Cómo se ve', 'Funciona cuando'],
        't2_rows': [
            ('Video Watch', 'facebook.com/watch/?v=...', 'El video es público'),
            ('Reel', 'facebook.com/reel/...', 'El Reel es público'),
            ('Enlace compartido', 'facebook.com/share/v/... o /share/r/...', 'El video compartido es público'),
            ('Enlace corto', 'fb.watch/...', 'El video es público'),
            ('Video de Página o perfil', 'facebook.com/NombrePagina/videos/...', 'El video es público'),
            ('Enlace móvil', 'm.facebook.com/...', 'El video es público'),
            ('Video de grupo', 'facebook.com/groups/.../posts/...', 'El grupo es público')
        ],
        'copy_h3': 'Cómo copiar el enlace de un video de Facebook',
        'copy_items': [
            '<strong>App de Facebook (iPhone o Android):</strong> toca <em>Compartir</em> debajo del video o Reel, luego <em>Copiar enlace</em>.',
            '<strong>Facebook en computadora:</strong> haz clic en el menú de tres puntos de la publicación y elige <em>Copiar enlace</em>, o haz clic derecho en la fecha de la publicación y copia la dirección del enlace.',
            '<strong>Messenger o WhatsApp:</strong> si alguien te envió un video de Facebook, copia el enlace directamente desde el mensaje.'
        ],
        'device_h3': 'Cómo descargar videos de Facebook en iPhone, Android y computadora',
        'ios': '<strong>En iPhone o iPad:</strong> abre esta página en Safari, pega el enlace y toca Descargar video. El archivo se guarda en Archivos y luego en Descargas. Ábrelo, toca Compartir y elige Guardar video para moverlo a Fotos.',
        'android': '<strong>En Android:</strong> abre esta página en Chrome, pega el enlace y toca Video (HD). El MP4 se guarda en tu carpeta Descargas y suele aparecer en tu Galería.',
        'pc': '<strong>En Windows o Mac:</strong> pega el enlace, haz clic en Descargar video y luego haz clic en el formato deseado. El archivo se guardará en la carpeta Descargas de tu navegador.',
        'priv_h3': '¿Se pueden descargar videos privados de Facebook?',
        'priv_p': 'No. Esta herramienta solo descarga videos que cualquiera puede abrir sin iniciar sesión. Las publicaciones solo para amigos, grupos privados y videos con audiencias restringidas no se pueden obtener, y nunca solicitamos tu contraseña de Facebook. El botón <em>Guardar video</em> de Facebook solo añade un marcador dentro de Facebook; no te entrega un archivo. Si necesitas un video privado, pídele a la persona que lo publicó que te envíe el archivo original.',
        'qual_h3': 'Calidad de video de Facebook: lo que realmente obtienes',
        'qual_p': 'Facebook almacena cada video en varias versiones. <strong>Video (HD)</strong> es la más alta disponible para ese clip y <strong>Video (Normal)</strong> es una versión más pequeña, útil con datos móviles lentos o almacenamiento limitado. La subida original marca el límite: un video subido a 480p no puede transformarse en 1080p, por lo que el descargador nunca realiza escalado artificial.',
        'mp3_h3': 'Convertir video de Facebook a MP3',
        'mp3_p': '¿Solo necesitas el sonido de una canción, entrevista, podcast o conferencia? Elige <strong>Audio (HQ MP3)</strong> para 192 kbps o <strong>Audio (Normal MP3)</strong> para 128 kbps. La conversión ocurre en el servidor mientras descargas, por lo que no necesitas instalar ninguna app adicional.',
        'trouble_h3': 'Por qué un video de Facebook podría no descargarse',
        'trouble_headers': ['Síntoma', 'Causa probable', 'Qué intentar'],
        'trouble_rows': [
            ('"No se pudo extraer el video"', 'El video es privado, solo para amigos o fue eliminado', 'Abre el enlace en una ventana privada. Si no se reproduce allí, no se puede descargar'),
            ('No pasa nada al pegar', 'El enlace apunta a un perfil, Página o publicación sin video', 'Abre el video en sí y copia su enlace desde Compartir'),
            ('El video en vivo falla', 'La transmisión aún está en curso', 'Espera a que finalice la transmisión y se guarde como video'),
            ('La historia falla', 'La historia expiró tras 24 horas o no es pública', 'Las historias desaparecen; intenta mientras siga disponible'),
            ('El enlace pide iniciar sesión', 'El contenido requiere una cuenta para verse', 'Solo se admiten videos totalmente públicos'),
            ('Muy lento o congelado', 'Archivo grande o conexión inestable', 'Prueba Video (Normal) o inténtalo en una red más rápida')
        ],
        'use_h3': 'Razones comunes para guardar videos de Facebook',
        'use_items': [
            'Guardar una copia de <strong>tus propios</strong> videos familiares, eventos y recuerdos antes de que se pierdan.',
            'Ver tutoriales, recetas y conferencias sin conexión durante viajes o con datos limitados.',
            'Guardar un clip que te permitieron compartir con amigos en WhatsApp.',
            'Extraer el audio de una charla o una canción para escucharla más tarde.'
        ],
        'safe_h3': '¿Es seguro y legal descargar videos de Facebook?',
        'safe_p': '<strong>Seguro:</strong> no ingresas contraseñas, no instalas software ni otorgas permisos. <strong>Legal:</strong> guardar un video público para visualización personal fuera de línea es un uso común, pero el video sigue perteneciendo a su creador. No resubas, vendas ni redistribuyas contenido sin los derechos correspondientes. downsocial es una herramienta independiente y no está afiliada ni respaldada por Meta Platforms, Inc.',
        'tips_h3': 'Consejos para obtener el mejor resultado',
        'tips_items': [
            'Copia el enlace desde el menú <em>Compartir</em> del propio video, no de la barra de direcciones de una página de perfil.',
            'Usa <strong>Video (HD)</strong> cuando planees verlo en un televisor o pantalla grande.',
            'Usa <strong>Video (Normal)</strong> o MP3 para ahorrar datos móviles.',
            'Si un enlace falla, pruébalo primero en una ventana privada del navegador.'
        ],
        'sister_h3': '¿Necesitas otra plataforma?',
        'sister_p': 'También ofrecemos herramientas dedicadas para <a href="../instagram-downloader/">Instagram</a>, <a href="../tiktok-downloader/">TikTok</a>, <a href="../youtube-downloader/">YouTube</a>, <a href="../snapchat-downloader/">Snapchat</a> y <a href="../threads-downloader/">Threads</a>, además del <a href="../index.html">descargador de videos todo en uno</a>.',
        'last_updated': 'Última actualización: 2 de octubre de 2026. ¿Preguntas o un enlace que falla? <a href="contact.html">Contactar a soporte</a>.'
    },

    'pt': {
        'qa_title': 'Resposta rápida: Como baixar vídeos do Facebook',
        'qa_text': 'Para baixar um vídeo do Facebook, copie o link, cole-o na caixa no topo desta página, toque em <em>Baixar vídeo</em> e escolha HD, Normal ou MP3. É gratuito, não precisa de login ou app e funciona no iPhone, Android, Windows e Mac. Apenas vídeos públicos podem ser baixados.',
        'h2': 'Baixador de vídeos do Facebook: Salve qualquer vídeo público do Facebook em HD',
        'intro': 'Este <strong>baixador de vídeos do Facebook</strong> foi criado para uma função essencial: transformar um link de vídeo público, Reel ou Watch do Facebook em um arquivo para você guardar. Ele lê o vídeo público, exibe os formatos disponíveis e transfere sua escolha diretamente para o seu dispositivo em MP4 ou áudio MP3. Nada é instalado, nada é mantido em nossos servidores e sua conta do Facebook nunca é solicitada.',
        't1_h3': 'Visão geral do baixador de vídeos do Facebook',
        't1_headers': ['Recurso', 'Detalhes'],
        't1_rows': [
            ('Conteúdo suportado', 'Vídeos públicos do Facebook, Reels, vídeos Watch e Stories públicas ou transmissões ao vivo encerradas enquanto ainda disponíveis'),
            ('Links aceitos', 'facebook.com, m.facebook.com, facebook.com/share, fb.watch'),
            ('Formatos de saída', 'Vídeo MP4 (HD e Normal), áudio MP3 (192 kbps e 128 kbps)'),
            ('Qualidade de vídeo', 'Melhor versão que o Facebook fornece para o vídeo, geralmente de 720p a 1080p. Sem upscaling artificial'),
            ('Preço', '<span class="badge-highlight">Grátis, sem limite de downloads</span>'),
            ('Conta ou login', '<span class="badge-highlight">Nenhum necessário</span>'),
            ('Marca d’água', '<span class="badge-highlight">Nenhuma adicionada</span>'),
            ('Compatibilidade', 'iPhone, iPad, Android, Windows, macOS, Linux (qualquer navegador moderno)'),
            ('Arquivos armazenados', 'Nenhum. Os fluxos não são salvos'),
            ('Limitações', 'Apenas vídeos públicos. Não ignora grupos privados ou postagens só para amigos. Qualidade limitada pelo upload original')
        ],
        't2_h3': 'Quais links do Facebook funcionam?',
        't2_intro': 'O Facebook utiliza vários formatos de link. Se o vídeo por trás do link for público, todos estes são aceitos:',
        't2_headers': ['Tipo de link', 'Aparência do link', 'Funciona quando'],
        't2_rows': [
            ('Vídeo Watch', 'facebook.com/watch/?v=...', 'O vídeo é público'),
            ('Reel', 'facebook.com/reel/...', 'O Reel é público'),
            ('Link de compartilhamento', 'facebook.com/share/v/... ou /share/r/...', 'O vídeo compartilhado é público'),
            ('Link curto', 'fb.watch/...', 'O vídeo é público'),
            ('Vídeo de Página ou perfil', 'facebook.com/NomeDaPagina/videos/...', 'O vídeo é público'),
            ('Link móvel', 'm.facebook.com/...', 'O vídeo é público'),
            ('Vídeo de grupo', 'facebook.com/groups/.../posts/...', 'O grupo é público')
        ],
        'copy_h3': 'Como copiar um link de vídeo do Facebook',
        'copy_items': [
            '<strong>App do Facebook (iPhone ou Android):</strong> toque em <em>Compartilhar</em> abaixo do vídeo ou Reel e depois em <em>Copiar link</em>.',
            '<strong>Facebook no computador:</strong> clique no menu de três pontos da publicação e escolha <em>Copiar link</em>, ou clique com o botão direito na data/hora do post e copie o endereço do link.',
            '<strong>Messenger ou WhatsApp:</strong> se alguém enviou um vídeo do Facebook, copie o link diretamente da mensagem.'
        ],
        'device_h3': 'Como baixar vídeos do Facebook no iPhone, Android e computador',
        'ios': '<strong>No iPhone ou iPad:</strong> abra esta página no Safari, cole o link e toque em Baixar vídeo. O arquivo é salvo no aplicativo Arquivos em Downloads. Abra-o, toque em Compartilhar e escolha Salvar vídeo para enviá-lo ao app Fotos.',
        'android': '<strong>No Android:</strong> abra esta página no Chrome, cole o link e toque em Vídeo (HD). O MP4 vai para sua pasta de Downloads e costuma aparecer na Galeria.',
        'pc': '<strong>No Windows ou Mac:</strong> cole o link, clique em Baixar vídeo e selecione o formato desejado. O arquivo será baixado para a pasta Downloads do seu navegador.',
        'priv_h3': 'É possível baixar vídeos privados do Facebook?',
        'priv_p': 'Não. Esta ferramenta só baixa vídeos acessíveis publicamente sem necessidade de login. Postagens exclusivas para amigos, grupos privados e vídeos com restrição de público não podem ser acessados, e nós nunca solicitamos sua senha do Facebook. O botão <em>Salvar vídeo</em> do próprio Facebook apenas guarda o link dentro da rede; não cria um arquivo no seu dispositivo. Se você precisa de um vídeo privado, peça o arquivo original a quem publicou.',
        'qual_h3': 'Qualidade do vídeo do Facebook: o que você realmente recebe',
        'qual_p': 'O Facebook disponibiliza cada vídeo em várias versões. <strong>Vídeo (HD)</strong> é a maior resolução disponível para o clipe e <strong>Vídeo (Normal)</strong> é uma versão mais compacta, ideal para conexões móveis lentas. O upload original determina o limite: um vídeo publicado em 480p não pode virar 1080p, portanto o baixador nunca promete upscaling falso.',
        'mp3_h3': 'Converter vídeo do Facebook para MP3',
        'mp3_p': 'Precisa apenas do áudio de uma música, entrevista, podcast ou palestra? Escolha <strong>Áudio (HQ MP3)</strong> para 192 kbps ou <strong>Áudio (Normal MP3)</strong> para 128 kbps. A conversão ocorre no servidor enquanto você baixa, sem instalar programas extras.',
        'trouble_h3': 'Por que um vídeo do Facebook pode não baixar',
        'trouble_headers': ['Sintoma', 'Causa provável', 'O que tentar'],
        'trouble_rows': [
            ('"Não foi possível extrair o vídeo"', 'O vídeo é privado, apenas para amigos ou foi excluído', 'Abra o link em uma janela anônima. Se não reproduzir lá, não pode ser baixado'),
            ('Nada acontece após colar', 'O link aponta para um perfil ou postagem sem vídeo', 'Abra o vídeo diretamente e copie o link em Compartilhar'),
            ('Transmissão ao vivo falha', 'A transmissão ainda está acontecendo', 'Aguarde o encerramento da live e sua conversão em vídeo'),
            ('Story falha', 'A Story expirou após 24 horas ou não é pública', 'Stories desaparecem; tente enquanto ainda estiver disponível'),
            ('O link pede login', 'O conteúdo exige login para visualização', 'Apenas vídeos totalmente públicos são suportados'),
            ('Muito lento ou travado', 'Arquivo grande ou sinal fraco', 'Tente Vídeo (Normal) ou teste em uma conexão mais rápida')
        ],
        'use_h3': 'Motivos comuns para salvar vídeos do Facebook',
        'use_items': [
            'Guardar uma cópia dos <strong>seus próprios</strong> vídeos familiares, eventos e memórias.',
            'Assistir tutoriais, receitas e aulas offline durante viagens.',
            'Salvar um clipe com permissão para compartilhar com amigos no WhatsApp.',
            'Extrair o áudio de uma palestra ou música para ouvir com frequência.'
        ],
        'safe_h3': 'Baixar vídeos do Facebook é seguro e legal?',
        'safe_p': '<strong>Seguro:</strong> você não informa senha, não instala programas nem concede permissões. <strong>Legal:</strong> salvar um vídeo público para uso pessoal e offline é comum, mas os direitos autorais pertencem ao criador. Não revenda ou redistribua conteúdo sem autorização. O downsocial é uma ferramenta independente e não possui vínculo com a Meta Platforms, Inc.',
        'tips_h3': 'Dicas para obter o melhor resultado',
        'tips_items': [
            'Copie o link no botão <em>Compartilhar</em> do próprio vídeo, não na barra de endereços de um perfil.',
            'Use <strong>Vídeo (HD)</strong> para assistir em telas maiores ou na TV.',
            'Use <strong>Vídeo (Normal)</strong> ou MP3 para economizar dados de internet móvel.',
            'Se um link falhar, teste-o antes em uma aba anônima do navegador.'
        ],
        'sister_h3': 'Precisa de outra rede social?',
        'sister_p': 'Também disponibilizamos ferramentas para <a href="../instagram-downloader/">Instagram</a>, <a href="../tiktok-downloader/">TikTok</a>, <a href="../youtube-downloader/">YouTube</a>, <a href="../snapchat-downloader/">Snapchat</a> e <a href="../threads-downloader/">Threads</a>, além do <a href="../index.html">baixador tudo-em-um</a>.',
        'last_updated': 'Última atualização: 2 de outubro de 2026. Dúvidas ou um link com falha? <a href="contact.html">Fale com o suporte</a>.'
    },

    'fr': {
        'qa_title': 'Réponse rapide : Comment télécharger des vidéos Facebook',
        'qa_text': 'Pour télécharger une vidéo Facebook, copiez son lien, collez-le dans le champ en haut de cette page, appuyez sur <em>Télécharger la vidéo</em> et choisissez HD, Normal ou MP3. C\'est gratuit, sans connexion ni application, et compatible iPhone, Android, Windows et Mac. Seules les vidéos publiques peuvent être téléchargées.',
        'h2': 'Téléchargeur de vidéos Facebook : Enregistrez toute vidéo publique en HD',
        'intro': 'Ce <strong>téléchargeur de vidéos Facebook</strong> est conçu dans un but précis : transformer un lien de vidéo publique, Reel ou Watch en un fichier hors ligne. Il extrait la vidéo, affiche les formats disponibles et diffuse directement votre choix sur votre appareil en vidéo MP4 ou audio MP3. Aucune installation requise, rien n\'est stocké sur nos serveurs et votre compte Facebook n\'est jamais requis.',
        't1_h3': 'Aperçu du téléchargeur de vidéos Facebook',
        't1_headers': ['Fonctionnalité', 'Détails'],
        't1_rows': [
            ('Contenu pris en charge', 'Vidéos publiques Facebook, Reels, vidéos Watch, Stories publiques et diffusions en direct terminées encore disponibles'),
            ('Liens acceptés', 'facebook.com, m.facebook.com, facebook.com/share, fb.watch'),
            ('Formats de sortie', 'Vidéo MP4 (HD et Normal), audio MP3 (192 kbps et 128 kbps)'),
            ('Qualité vidéo', 'Meilleure version servie par Facebook pour la vidéo, couramment de 720p à 1080p. Pas d\'upscaling artificiel'),
            ('Prix', '<span class="badge-highlight">Gratuit, téléchargements illimités</span>'),
            ('Compte ou connexion', '<span class="badge-highlight">Aucun requis</span>'),
            ('Filigrane', '<span class="badge-highlight">Aucun ajouté</span>'),
            ('Appareils compatibles', 'iPhone, iPad, Android, Windows, macOS, Linux (tout navigateur moderne)'),
            ('Fichiers conservés', 'Aucun. Les flux ne sont pas conservés'),
            ('Restrictions', 'Vidéos publiques uniquement. Ne peut pas contourner les groupes privés ou les publications réservées aux amis.')
        ],
        't2_h3': 'Quels liens Facebook sont compatibles ?',
        't2_intro': 'Facebook utilise plusieurs formats de liens. Si la vidéo est publique, tous les formats suivants sont acceptés :',
        't2_headers': ['Type de lien', 'Exemple d\'URL', 'Fonctionne quand'],
        't2_rows': [
            ('Vidéo Watch', 'facebook.com/watch/?v=...', 'La vidéo est publique'),
            ('Reel', 'facebook.com/reel/...', 'Le Reel est public'),
            ('Lien de partage', 'facebook.com/share/v/... ou /share/r/...', 'La vidéo partagée est publique'),
            ('Lien court', 'fb.watch/...', 'La vidéo est publique'),
            ('Vidéo de Page ou profil', 'facebook.com/NomPage/videos/...', 'La vidéo est publique'),
            ('Lien mobile', 'm.facebook.com/...', 'La vidéo est publique'),
            ('Vidéo de groupe', 'facebook.com/groups/.../posts/...', 'Le groupe est public')
        ],
        'copy_h3': 'Comment copier le lien d\'une vidéo Facebook',
        'copy_items': [
            '<strong>Application Facebook (iPhone ou Android) :</strong> appuyez sur <em>Partager</em> sous la vidéo ou le Reel, puis sur <em>Copier le lien</em>.',
            '<strong>Facebook sur ordinateur :</strong> cliquez sur les trois points de la publication et choisissez <em>Copier le lien</em>, ou faites un clic droit sur la date.',
            '<strong>Messenger ou WhatsApp :</strong> si l\'on vous a partagé une vidéo, copiez directement le lien depuis la conversation.'
        ],
        'device_h3': 'Comment télécharger des vidéos Facebook sur iPhone, Android et ordinateur',
        'ios': '<strong>Sur iPhone ou iPad :</strong> ouvrez cette page dans Safari, collez le lien et appuyez sur Télécharger la vidéo. Le fichier est stocké dans Fichiers > Téléchargements. Ouvrez-le, touchez Partager et sélectionnez Enregistrer la vidéo pour l\'ajouter à Photos.',
        'android': '<strong>Sur Android :</strong> ouvrez cette page dans Chrome, collez le lien et sélectionnez Vidéo (HD). Le fichier MP4 arrive dans Téléchargements et apparaît dans votre Galerie.',
        'pc': '<strong>Sur Windows ou Mac :</strong> collez le lien, cliquez sur Télécharger la vidéo et choisissez le format. Le fichier est enregistré dans votre dossier Téléchargements.',
        'priv_h3': 'Peut-on télécharger des vidéos Facebook privées ?',
        'priv_p': 'Non. Cet outil ne télécharge que les vidéos accessibles à tous sans connexion. Les publications réservées aux amis, groupes privés et contenus restreints ne peuvent pas être récupérés, et nous ne demandons jamais vos identifiants Facebook.',
        'qual_h3': 'Qualité vidéo Facebook : ce que vous obtenez réellement',
        'qual_p': 'Facebook encode chaque vidéo sous différents profils. <strong>Vidéo (HD)</strong> correspond à la meilleure définition disponible et <strong>Vidéo (Normal)</strong> est un fichier plus léger. La résolution d\'origine constitue le plafond : une vidéo en 480p ne peut pas être convertie magiquement en 1080p.',
        'mp3_h3': 'Convertir une vidéo Facebook en MP3',
        'mp3_p': 'Besoin uniquement du son d\'un podcast, d\'une interview ou d\'une chanson ? Choisissez <strong>Audio (HQ MP3)</strong> à 192 kbps ou <strong>Audio (Normal MP3)</strong> à 128 kbps. La conversion a lieu instantanément lors du téléchargement.',
        'trouble_h3': 'Pourquoi une vidéo Facebook ne se télécharge pas',
        'trouble_headers': ['Symptôme', 'Cause probable', 'Solution conseillée'],
        'trouble_rows': [
            ('"Impossible d\'extraire la vidéo"', 'La vidéo est privée, réservée aux amis ou supprimée', 'Ouvrez le lien dans un onglet privé. Si elle ne s\'affiche pas, elle ne peut être téléchargée'),
            ('Rien ne se passe', 'Le lien mène à une Page ou un profil sans vidéo directe', 'Ouvrez directement la vidéo et copiez le lien depuis Partager'),
            ('Direct en échec', 'La diffusion en direct est toujours en cours', 'Attendez la fin de la diffusion et son enregistrement'),
            ('Story en échec', 'La Story a expiré après 24 heures ou est privée', 'Réessayez pendant que la Story est encore active'),
            ('Page de connexion requise', 'Le contenu nécessite un compte utilisateur', 'Seules les vidéos entièrement publiques sont supportées'),
            ('Téléchargement très lent', 'Fichier volumineux ou réseau instable', 'Essayez Vidéo (Normal) ou connectez-vous au Wi-Fi')
        ],
        'use_h3': 'Pourquoi enregistrer des vidéos Facebook ?',
        'use_items': [
            'Sauvegarder une copie de <strong>vos propres</strong> vidéos de famille et souvenirs avant disparition.',
            'Consulter des tutoriels et recettes hors ligne en voyage.',
            'Partager une vidéo autorisée avec vos proches sur WhatsApp.',
            'Extraire la piste audio d\'une conférence ou d\'un morceau musical.'
        ],
        'safe_h3': 'Le téléchargement de vidéos Facebook est-il sûr et légal ?',
        'safe_p': '<strong>Sûr :</strong> aucun mot de passe requis, aucun logiciel à installer. <strong>Légal :</strong> enregistrer une vidéo publique pour un usage personnel hors ligne est courant, mais le droit d\'auteur appartient au créateur. downsocial est un service indépendant non affilié à Meta Platforms, Inc.',
        'tips_h3': 'Conseils pour une expérience optimale',
        'tips_items': [
            'Copiez le lien via l\'option <em>Partager</em> de la vidéo plutôt que depuis la barre d\'adresse.',
            'Privilégiez <strong>Vidéo (HD)</strong> pour un visionnage sur écran d\'ordinateur ou TV.',
            'Choisissez <strong>Vidéo (Normal)</strong> pour préserver votre forfait mobile.',
            'En cas de doute sur la visibilité, testez l\'URL dans un navigateur en navigation privée.'
        ],
        'sister_h3': 'Besoin d\'un outil pour un autre réseau ?',
        'sister_p': 'Découvrez également nos solutions pour <a href="../instagram-downloader/">Instagram</a>, <a href="../tiktok-downloader/">TikTok</a>, <a href="../youtube-downloader/">YouTube</a>, <a href="../snapchat-downloader/">Snapchat</a> et <a href="../threads-downloader/">Threads</a>, ainsi que notre <a href="../index.html">téléchargeur universel</a>.',
        'last_updated': 'Dernière mise à jour : 2 octobre 2026. Une question ou un lien défaillant ? <a href="contact.html">Contactez le support</a>.'
    },

    'de': {
        'qa_title': 'Schnellantwort: So laden Sie Facebook-Videos herunter',
        'qa_text': 'Um ein Facebook-Video herunterzuladen, kopieren Sie den Link, fügen ihn oben in das Feld ein, klicken auf <em>Video herunterladen</em> und wählen HD, Normal oder MP3. Es ist kostenlos, erfordert keine Anmeldung oder App und funktioniert auf iPhone, Android, Windows und Mac. Es können nur öffentliche Videos gespeichert werden.',
        'h2': 'Facebook Video Downloader: Jedes öffentliche Facebook-Video in HD speichern',
        'intro': 'Dieser <strong>Facebook Video Downloader</strong> wurde für eine Kernaufgabe entwickelt: öffentliche Facebook-Videos, Reels oder Watch-Links in dauerhafte Dateien umzuwandeln. Er liest das Video aus, zeigt verfügbare Qualitäten und lädt die Datei als MP4-Video oder MP3-Audio direkt auf Ihr Gerät. Keine Software-Installation, keine Speicherung auf unseren Servern und keine Facebook-Zugangsdaten erforderlich.',
        't1_h3': 'Facebook Video Downloader im Überblick',
        't1_headers': ['Funktion', 'Details'],
        't1_rows': [
            ('Unterstützte Inhalte', 'Öffentliche Facebook-Videos, Reels, Watch-Videos, öffentliche Storys und beendete Live-Übertragungen'),
            ('Akzeptierte Links', 'facebook.com, m.facebook.com, facebook.com/share, fb.watch'),
            ('Ausgabeformate', 'MP4-Video (HD und Normal), MP3-Audio (192 kbps und 128 kbps)'),
            ('Videoqualität', 'Beste von Facebook bereitgestellte Auflösung, meist 720p bis 1080p. Kein künstliches Upscaling'),
            ('Preis', '<span class="badge-highlight">Kostenlos, ohne Download-Limits</span>'),
            ('Konto oder Login', '<span class="badge-highlight">Nicht erforderlich</span>'),
            ('Wasserzeichen', '<span class="badge-highlight">Keine hinzugefügt</span>'),
            ('Kompatibilität', 'iPhone, iPad, Android, Windows, macOS, Linux (alle modernen Browser)'),
            ('Gespeicherte Daten', 'Keine. Streams werden nicht zwischengespeichert'),
            ('Einschränkungen', 'Nur öffentliche Videos. Keine privaten Gruppen oder Freunde-Inhalte. Qualität hängt vom Originalupload ab')
        ],
        't2_h3': 'Welche Facebook-Links werden unterstützt?',
        't2_intro': 'Facebook verwendet verschiedene URL-Formate. Sofern das Video öffentlich ist, funktionieren alle folgenden Links:',
        't2_headers': ['Link-Typ', 'Formatbeispiel', 'Funktioniert wenn'],
        't2_rows': [
            ('Watch-Video', 'facebook.com/watch/?v=...', 'Video öffentlich ist'),
            ('Reel', 'facebook.com/reel/...', 'Reel öffentlich ist'),
            ('Share-Link', 'facebook.com/share/v/... oder /share/r/...', 'Geteiltes Video öffentlich ist'),
            ('Kurzlink', 'fb.watch/...', 'Video öffentlich ist'),
            ('Seiten- oder Profilvideo', 'facebook.com/SeitenName/videos/...', 'Video öffentlich ist'),
            ('Mobiler Link', 'm.facebook.com/...', 'Video öffentlich ist'),
            ('Gruppenvideo', 'facebook.com/groups/.../posts/...', 'Gruppe öffentlich ist')
        ],
        'copy_h3': 'So kopieren Sie einen Facebook-Videolink',
        'copy_items': [
            '<strong>Facebook-App (iPhone oder Android):</strong> Tippen Sie unter dem Video auf <em>Teilen</em> und dann auf <em>Link kopieren</em>.',
            '<strong>Facebook am Computer:</strong> Klicken Sie auf das Drei-Punkte-Menü des Beitrags und wählen Sie <em>Link kopieren</em>.',
            '<strong>Messenger oder WhatsApp:</strong> Wenn Sie das Video per Nachricht erhalten haben, kopieren Sie den Link direkt aus dem Chat.'
        ],
        'device_h3': 'Facebook-Videos auf iPhone, Android und PC herunterladen',
        'ios': '<strong>Auf iPhone oder iPad:</strong> Öffnen Sie Safari, fügen Sie den Link ein und tippen Sie auf Video herunterladen. Die Datei landet in Dateien > Downloads. Öffnen Sie sie und wählen Sie Teilen > Video sichern, um sie in Fotos zu speichern.',
        'android': '<strong>Auf Android:</strong> Öffnen Sie Chrome, fügen Sie den Link ein und tippen Sie auf Video (HD). Die Datei wird im Ordner Downloads gespeichert und ist in der Galerie verfügbar.',
        'pc': '<strong>Auf Windows oder Mac:</strong> Fügen Sie den Link ein, klicken Sie auf Video herunterladen und wählen Sie das gewünschte Format.',
        'priv_h3': 'Können private Facebook-Videos heruntergeladen werden?',
        'priv_p': 'Nein. Dieses Tool lädt ausschließlich Inhalte herunter, die öffentlich ohne Login abrufbar sind. Inhalte aus privaten Gruppen oder Posts für Freunde können nicht geladen werden. Wir fragen niemals nach Ihren Zugangsdaten.',
        'qual_h3': 'Facebook-Videoqualität: Was Sie tatsächlich erhalten',
        'qual_p': 'Facebook speichert Videos in mehreren Bitraten. <strong>Video (HD)</strong> liefert die bestmögliche Qualität des Clips, während <strong>Video (Normal)</strong> eine datensparende Variante darstellt. Ein in 480p hochgeladenes Video kann nicht auf 1080p hochskaliert werden.',
        'mp3_h3': 'Facebook-Videos in MP3 umwandeln',
        'mp3_p': 'Möchten Sie nur den Ton einer Rede, Musik oder eines Podcasts sichern? Wählen Sie <strong>Audio (HQ MP3)</strong> mit 192 kbps oder <strong>Audio (Normal MP3)</strong> mit 128 kbps. Die Konvertierung erfolgt direkt beim Download.',
        'trouble_h3': 'Warum ein Download fehlschlagen könnte',
        'trouble_headers': ['Symptom', 'Wahrscheinliche Ursache', 'Lösungsvorschlag'],
        'trouble_rows': [
            ('"Video konnte nicht extrahiert werden"', 'Video ist privat, gelöscht oder nur für Freunde', 'Öffnen Sie den Link im privaten Modus. Läuft er dort nicht, ist kein Download möglich'),
            ('Keine Reaktion nach dem Einfügen', 'Link führt zu einem Profil ohne direktes Video', 'Öffnen Sie direkt das Video und kopieren Sie den Link über Teilen'),
            ('Live-Video schlägt fehl', 'Übertragung läuft noch live', 'Warten Sie, bis der Stream beendet und als Video archiviert ist'),
            ('Story schlägt fehl', 'Story ist älter als 24 Stunden oder privat', 'Stories sind flüchtig; versuchen Sie es rechtzeitig erneut'),
            ('Login-Aufforderung', 'Inhalt setzt ein Benutzerkonto voraus', 'Nur komplett frei zugängliche Videos sind kompatibel'),
            ('Sehr langsam', 'Große Datei oder schwaches Internet', 'Wählen Sie Video (Normal) oder ein stabileres WLAN')
        ],
        'use_h3': 'Typische Gründe für das Speichern von Facebook-Videos',
        'use_items': [
            'Sicherung <strong>eigener</strong> Familienvideos und Erinnerungen vor Datenverlust.',
            'Offline-Nutzung von Tutorials, Vorträgen und Rezepten auf Reisen.',
            'Teilen von erlaubten Clips mit Freunden via Messenger.',
            'Audiospur als MP3 für den Musikplayer unterwegs extrahieren.'
        ],
        'safe_h3': 'Ist der Download sicher und legal?',
        'safe_p': '<strong>Sicher:</strong> Keine Kennwörter, keine Werbesoftware, keine Plugins. <strong>Legal:</strong> Das Herunterladen für den rein privaten Gebrauch ist üblich, das Urheberrecht verbleibt beim Ersteller. downsocial ist ein unabhängiges Angebot ohne Verbindung zu Meta Platforms, Inc.',
        'tips_h3': 'Tipps für das beste Ergebnis',
        'tips_items': [
            'Kopieren Sie den Link immer über das Teilen-Menü des Videos selbst.',
            'Nutzen Sie <strong>Video (HD)</strong> für die Wiedergabe auf großen Bildschirmen.',
            'Wählen Sie <strong>Video (Normal)</strong>, um mobiles Datenvolumen zu schonen.',
            'Testen Sie problematische Links zuerst in einem Inkognito-Fenster.'
        ],
        'sister_h3': 'Benötigen Sie einen Downloader für eine andere Plattform?',
        'sister_p': 'Wir bieten zudem spezialisierte Tools für <a href="../instagram-downloader/">Instagram</a>, <a href="../tiktok-downloader/">TikTok</a>, <a href="../youtube-downloader/">YouTube</a>, <a href="../snapchat-downloader/">Snapchat</a> und <a href="../threads-downloader/">Threads</a> sowie den <a href="../index.html">Universal-Downloader</a>.',
        'last_updated': 'Zuletzt aktualisiert: 2. Oktober 2026. Fragen oder defekter Link? <a href="contact.html">Support kontaktieren</a>.'
    },

    'hi': {
        'qa_title': 'त्वरित उत्तर: फेसबुक वीडियो कैसे डाउनलोड करें',
        'qa_text': 'फेसबुक वीडियो डाउनलोड करने के लिए, उसका लिंक कॉपी करें, इस पेज के शीर्ष बॉक्स में पेस्ट करें, <em>Download Video</em> पर क्लिक करें और HD, Normal या MP3 चुनें। यह पूरी तरह मुफ्त है, किसी लॉगिन या ऐप की आवश्यकता नहीं है, और iPhone, Android, Windows व Mac पर काम करता है। केवल सार्वजनिक वीडियो ही डाउनलोड किए जा सकते हैं।',
        'h2': 'फेसबुक वीडियो डाउनलोडर: किसी भी पब्लिक फेसबुक वीडियो को HD में सेव करें',
        'intro': 'यह <strong>Facebook video downloader</strong> एक मुख्य काम के लिए बनाया गया है: पब्लिक फेसबुक वीडियो, रील्स या वॉच लिंक को आपके डिवाइस पर सेव करने योग्य फ़ाइल में बदलना। यह पब्लिक वीडियो को पढ़ता है, उपलब्ध फॉर्मेट दिखाता है और आपकी पसंद के अनुसार MP4 वीडियो या MP3 ऑडियो स्ट्रीम करता है। कोई सॉफ्टवेयर इंस्टॉल नहीं होता, हमारे पास कुछ सेव नहीं होता और आपका फेसबुक अकाउंट सुरक्षित रहता है।',
        't1_h3': 'फेसबुक वीडियो डाउनलोडर एक नज़र में',
        't1_headers': ['सुविधा', 'विवरण'],
        't1_rows': [
            ('समर्थित सामग्री', 'पब्लिक फेसबुक वीडियो, रील्स, वॉच वीडियो, और उपलब्ध पब्लिक स्टोरीज या समाप्त लाइव वीडियो'),
            ('स्वीकृत लिंक', 'facebook.com, m.facebook.com, facebook.com/share, fb.watch'),
            ('आउटपुट फॉर्मेट', 'MP4 वीडियो (HD और Normal), MP3 ऑडियो (192 kbps और 128 kbps)'),
            ('वीडियो क्वालिटी', 'फेसबुक पर उपलब्ध सर्वोत्तम क्वालिटी, आमतौर पर 720p से 1080p। कोई नकली अपस्केलिंग नहीं'),
            ('कीमत', '<span class="badge-highlight">बिल्कुल मुफ्त, असीमित डाउनलोड</span>'),
            ('अकाउंट या लॉगिन', '<span class="badge-highlight">कोई आवश्यकता नहीं</span>'),
            ('वॉटरमार्क', '<span class="badge-highlight">कोई वॉटरमार्क नहीं</span>'),
            ('डिवाइस सपोर्ट', 'iPhone, iPad, Android, Windows, macOS, Linux (सभी आधुनिक ब्राउज़र)'),
            ('स्टोरेज नीति', 'शून्य। कोई स्ट्रीम हमारे सर्वर पर सेव नहीं होती'),
            ('सीमाएं', 'केवल सार्वजनिक वीडियो। प्राइवेट ग्रुप या केवल दोस्तों वाले पोस्ट डाउनलोड नहीं हो सकते')
        ],
        't2_h3': 'कौन से फेसबुक लिंक काम करते हैं?',
        't2_intro': 'फेसबुक कई लिंक फॉर्मेट का उपयोग करता है। यदि वीडियो सार्वजनिक है, तो ये सभी लिंक काम करते हैं:',
        't2_headers': ['लिंक का प्रकार', 'लिंक का प्रारूप', 'कब काम करता है'],
        't2_rows': [
            ('वॉच वीडियो', 'facebook.com/watch/?v=...', 'वीडियो पब्लिक हो'),
            ('रील', 'facebook.com/reel/...', 'रील पब्लिक हो'),
            ('शेयर लिंक', 'facebook.com/share/v/... या /share/r/...', 'शेयर किया गया वीडियो पब्लिक हो'),
            ('शॉर्ट लिंक', 'fb.watch/...', 'वीडियो पब्लिक हो'),
            ('पेज या प्रोफाइल वीडियो', 'facebook.com/PageName/videos/...', 'वीडियो पब्लिक हो'),
            ('मोबाइल लिंक', 'm.facebook.com/...', 'वीडियो पब्लिक हो'),
            ('ग्रुप वीडियो', 'facebook.com/groups/.../posts/...', 'ग्रुप पब्लिक हो')
        ],
        'copy_h3': 'फेसबुक वीडियो लिंक कैसे कॉपी करें',
        'copy_items': [
            '<strong>फेसबुक ऐप (iPhone या Android):</strong> वीडियो या रील के नीचे <em>Share</em> पर टैप करें, फिर <em>Copy Link</em> चुनें।',
            '<strong>कंप्यूटर पर फेसबुक:</strong> पोस्ट के थ्री-डॉट मेनू पर क्लिक करें और <em>Copy link</em> चुनें, या पोस्ट के टाइमस्टैम्प पर राइट-क्लिक करके लिंक कॉपी करें।',
            '<strong>Messenger या WhatsApp:</strong> यदि किसी ने फेसबुक वीडियो का लिंक भेजा है, तो सीधे मैसेज से लिंक कॉपी करें।'
        ],
        'device_h3': 'iPhone, Android और कंप्यूटर पर फेसबुक वीडियो कैसे डाउनलोड करें',
        'ios': '<strong>iPhone या iPad पर:</strong> इस पेज को Safari में खोलें, लिंक पेस्ट करें और Download Video पर टैप करें। फाइल Files ऐप के Downloads फोल्डर में सेव होगी। इसे खोलकर Share दबाएं और Photos में सेव करने के लिए Save Video चुनें।',
        'android': '<strong>Android पर:</strong> Chrome में यह पेज खोलें, लिंक पेस्ट करें और Video (HD) पर टैप करें। MP4 फाइल आपके Downloads फोल्डर और गैलरी में सेव हो जाएगी।',
        'pc': '<strong>Windows या Mac पर:</strong> लिंक पेस्ट करें, Download Video पर क्लिक करें और मनचाहा फॉर्मेट चुनें। फाइल ब्राउज़र के Downloads फोल्डर में सेव होगी।',
        'priv_h3': 'क्या प्राइवेट फेसबुक वीडियो डाउनलोड किए जा सकते हैं?',
        'priv_p': 'नहीं। यह टूल केवल वही वीडियो डाउनलोड करता है जो बिना लॉगिन किए किसी के लिए भी उपलब्ध हैं। फ्रेंड्स-ओनली पोस्ट, प्राइवेट ग्रुप और प्रतिबंधित ऑडियंस वाले वीडियो नहीं निकाले जा सकते, और हम कभी आपका फेसबुक पासवर्ड नहीं मांगते।',
        'qual_h3': 'फेसबुक वीडियो क्वालिटी: आपको वास्तव में क्या मिलता है',
        'qual_p': 'फेसबुक हर वीडियो को कई रेजोल्यूशन में रखता है। <strong>Video (HD)</strong> उपलब्ध उच्चतम क्वालिटी है और <strong>Video (Normal)</strong> धीमे नेटवर्क या कम स्टोरेज के लिए उपयोगी छोटी फाइल है। मूल अपलोड ही अधिकतम सीमा तय करता है।',
        'mp3_h3': 'फेसबुक वीडियो को MP3 में बदलें',
        'mp3_p': 'किसी गाने, इंटरव्यू, भाषण या पॉडकास्ट की केवल ऑडियो चाहिए? 192 kbps के लिए <strong>Audio (HQ MP3)</strong> या 128 kbps के लिए <strong>Audio (Normal MP3)</strong> चुनें। डाउनलोड के दौरान ही यह कन्वर्ट हो जाता है।',
        'trouble_h3': 'फेसबुक वीडियो डाउनलोड न होने के सामान्य कारण',
        'trouble_headers': ['समस्या', 'संभावित कारण', 'समाधान'],
        'trouble_rows': [
            ('"Could not extract video"', 'वीडियो प्राइवेट, केवल दोस्तों के लिए या हटा दिया गया है', 'लिंक को इनकॉग्निटो विंडो में खोलें। अगर वहां नहीं चलता तो डाउनलोड नहीं हो सकता'),
            ('पेस्ट करने के बाद कुछ नहीं होता', 'लिंक वीडियो का नहीं बल्कि प्रोफाइल या पोस्ट का है', 'सीधे वीडियो को खोलें और Share से उसका लिंक कॉपी करें'),
            ('लाइव वीडियो फेल हो रहा है', 'लाइव प्रसारण अभी चल रहा है', 'लाइव स्ट्रीम समाप्त होने और वीडियो के रूप में प्रोसेस होने की प्रतीक्षा करें'),
            ('स्टोरी डाउनलोड नहीं हो रही', 'स्टोरी 24 घंटे बाद समाप्त हो चुकी है या प्राइवेट है', 'स्टोरी उपलब्ध रहने के दौरान ही पुनः प्रयास करें'),
            ('लॉगिन मांग रहा है', 'सामग्री देखने के लिए फेसबुक अकाउंट जरूरी है', 'केवल पूरी तरह सार्वजनिक वीडियो समर्थित हैं'),
            ('बहुत धीमा या रुका हुआ', 'बड़ी फाइल या कमजोर इंटरनेट', 'Video (Normal) आज़माएं या तेज़ वाई-फाई से जुड़ें')
        ],
        'use_h3': 'लोग फेसबुक वीडियो क्यों सेव करते हैं?',
        'use_items': [
            'अपने पारिवारिक वीडियो, कार्यक्रम और यादों की सुरक्षित बैकअप प्रति रखना।',
            'यात्रा के दौरान ट्यूटोरियल, रेसिपी और व्याख्यान ऑफलाइन देखना।',
            'अनुमति मिलने पर WhatsApp पर दोस्तों के साथ मजेदार क्लिप साझा करना।',
            'किसी भाषण या संगीत की ऑडियो फाइल निकालकर बाद में सुनना।'
        ],
        'safe_h3': 'क्या फेसबुक वीडियो डाउनलोड करना सुरक्षित और कानूनी है?',
        'safe_p': '<strong>सुरक्षित:</strong> कोई पासवर्ड दर्ज नहीं करना पड़ता, कोई सॉफ्टवेयर इंस्टॉल नहीं होता। <strong>कानूनी:</strong> व्यक्तिगत ऑफ़लाइन देखने के लिए पब्लिक वीडियो सेव करना सामान्य है, लेकिन कॉपीराइट निर्माता का ही रहता है। बिना अनुमति सामग्री का पुनर्वितरण न करें। downsocial मेटा प्लेटफॉर्म्स से संबद्ध नहीं है।',
        'tips_h3': 'बेहतरीन परिणाम के लिए उपयोगी सुझाव',
        'tips_items': [
            'लिंक हमेशा वीडियो के अपने <em>Share</em> मेनू से कॉपी करें, ब्राउज़र एड्रेस बार से नहीं।',
            'बड़ी स्क्रीन या टीवी पर देखने के लिए <strong>Video (HD)</strong> चुनें।',
            'मोबाइल डेटा बचाने के लिए <strong>Video (Normal)</strong> या MP3 चुनें।',
            'यदि लिंक काम न करे, तो पहले उसे प्राइवेट/इनकॉग्निटो विंडो में जांचें।'
        ],
        'sister_h3': 'अन्य प्लेटफॉर्म के लिए टूल चाहिए?',
        'sister_p': 'हम <a href="../instagram-downloader/">Instagram</a>, <a href="../tiktok-downloader/">TikTok</a>, <a href="../youtube-downloader/">YouTube</a>, <a href="../snapchat-downloader/">Snapchat</a> और <a href="../threads-downloader/">Threads</a> के लिए समर्पित टूल तथा <a href="../index.html">ऑल-इन-वन डाउनलोडर</a> भी प्रदान करते हैं।',
        'last_updated': 'अंतिम अपडेट: 2 अक्टूबर 2026. कोई प्रश्न या समस्या? <a href="contact.html">सपोर्ट से संपर्क करें</a>।'
    },

    'ar': {
        'qa_title': 'إجابة سريعة: كيفية تنزيل مقاطع فيديو فيسبوك',
        'qa_text': 'لتنزيل أي فيديو من فيسبوك، انسخ الرابط، والصقه في المربع أعلى هذه الصفحة، واضغط على <em>تنزيل الفيديو</em> واختر HD أو Normal أو MP3. الخدمة مجانية تماماً، ولا تتطلب تسجيل دخول أو تثبيت تطبيقات، وتعمل على iPhone و Android و Windows و Mac. يمكن تنزيل الفيديوهات العامة فقط.',
        'h2': 'برنامج تنزيل فيديو فيسبوك: حفظ أي فيديو عام بجودة عالية HD',
        'intro': 'تم تصميم <strong>برنامج تنزيل فيديو فيسبوك</strong> هذا لمهمة واحدة محددة: تحويل روابط الفيديوهات والريلز العامة إلى ملفات دائمة على جهازك. يقوم باستخراج الفيديو وعرض التنسيقات المتاحة وبث اختيارك مباشرة بصيغة MP4 أو MP3 دون الحاجة لأي تسجيل أو برامج.',
        't1_h3': 'نظرة سريعة على ميزات تنزيل فيديو فيسبوك',
        't1_headers': ['الميزة', 'التفاصيل'],
        't1_rows': [
            ('المحتوى المدعوم', 'فيديوهات فيسبوك العامة، الريلز، مقاطع Watch، والقصص العامة أو البث المباشر المنتهي'),
            ('الروابط المقبولة', 'facebook.com, m.facebook.com, facebook.com/share, fb.watch'),
            ('صيغ الإخراج', 'فيديو MP4 (HD و Normal)، صوت MP3 (192 kbps و 128 kbps)'),
            ('جودة الفيديو', 'أفضل دقة يقدمها فيسبوك للمقطع، عادة من 720p إلى 1080p دون ترقية وهمية'),
            ('السعر', '<span class="badge-highlight">مجاني 100% بدون حدود للتحميل</span>'),
            ('تسجيل الدخول', '<span class="badge-highlight">غير مطلوب مطلقاً</span>'),
            ('العلامة المائية', '<span class="badge-highlight">بدون أي علامة مائية</span>'),
            ('الأجهزة المدعومة', 'iPhone و iPad و Android و Windows و macOS و Linux'),
            ('تخزين الملفات', 'لا نقوم بحفظ أي ملفات على خوادمنا نهائياً'),
            ('القيود', 'الفيديوهات العامة فقط. لا يمكن تحميل منشورات المجموعات المغلقة أو الخاصة بالأصدقاء')
        ],
        't2_h3': 'ما هي روابط فيسبوك التي تعمل مع الأداة؟',
        't2_intro': 'يستخدم فيسبوك عدة صيغ للروابط. طالما أن الفيديو عام، فإن جميع الروابط التالية مدعومة:',
        't2_headers': ['نوع الرابط', 'شكل الرابط', 'يعمل عندما'],
        't2_rows': [
            ('فيديو Watch', 'facebook.com/watch/?v=...', 'الفيديو عام'),
            ('ريلز Reel', 'facebook.com/reel/...', 'المقطع عام'),
            ('رابط مشاركة', 'facebook.com/share/v/... أو /share/r/...', 'الفيديو المشترك عام'),
            ('رابط قصير', 'fb.watch/...', 'الفيديو عام'),
            ('فيديو صفحة أو بروفايل', 'facebook.com/PageName/videos/...', 'الفيديو عام'),
            ('رابط الهاتف', 'm.facebook.com/...', 'الفيديو عام'),
            ('فيديو مجموعة', 'facebook.com/groups/.../posts/...', 'المجموعة عامة')
        ],
        'copy_h3': 'كيفية نسخ رابط فيديو فيسبوك',
        'copy_items': [
            '<strong>تطبيق فيسبوك (iPhone أو Android):</strong> اضغط على <em>مشاركة (Share)</em> أسفل الفيديو ثم اختر <em>نسخ الرابط (Copy Link)</em>.',
            '<strong>فيسبوك على الكمبيوتر:</strong> انقر على القائمة الثلاثية للمنشور واختر <em>نسخ الرابط</em>، أو انقر بزر الفأرة الأيمن على وقت المنشور وانسخ العنوان.',
            '<strong>ماسنجر أو واتساب:</strong> إذا أرسل لك شخص رابط فيديو فيسبوك، انسخ الرابط مباشرة من الرسالة.'
        ],
        'device_h3': 'طريقة تنزيل مقاطع فيسبوك على iPhone و Android والكمبيوتر',
        'ios': '<strong>على iPhone أو iPad:</strong> افتح هذه الصفحة في Safari، والصق الرابط واضغط على تنزيل الفيديو. سيتم حفظ الملف في تطبيق "الملفات" في قسم التنزيلات. افتحه واضغط على مشاركة ثم "حفظ الفيديو" لنقله إلى تطبيق الصور.',
        'android': '<strong>على Android:</strong> افتح الصفحة في متصفح Chrome، والصق الرابط واختر Video (HD). سيتم حفظ ملف MP4 مباشرة في مجلد Downloads وسيظهر في معرض الصور.',
        'pc': '<strong>على Windows أو Mac:</strong> الصق الرابط واضغط تنزيل ثم اختر الجودة المطلوبة ليتم حفظ المقطع في مجلد التنزيلات بجهازك.',
        'priv_h3': 'هل يمكن تنزيل مقاطع فيسبوك الخاصة؟',
        'priv_p': 'لا. تعمل هذه الأداة فقط مع الفيديوهات العامة المتاحة للجميع دون تسجيل دخول. لا يمكن الوصول إلى المقاطع الخاصة بالأصدقاء أو المجموعات المغلقة، ونحن لا نطلب كلمة مرور حسابك أبداً.',
        'qual_h3': 'جودة فيديو فيسبوك: ما تحصل عليه فعلياً',
        'qual_p': 'يوفر فيسبوك كل مقطع بعدة جودات. <strong>Video (HD)</strong> هي أعلى جودة متوفرة للمقطع، بينما <strong>Video (Normal)</strong> نسخة أصغر حجماً لتوفير باقة الإنترنت. الجودة الأصلية المرفوعة هي الحد الأقصى دائماً.',
        'mp3_h3': 'تحويل فيديو فيسبوك إلى صوت MP3',
        'mp3_p': 'هل تحتاج فقط للصوت من خطبة أو مقابلة أو أغنية؟ اختر <strong>Audio (HQ MP3)</strong> بدقة 192 kbps أو <strong>Audio (Normal MP3)</strong> بدقة 128 kbps ليتم التحويل فوراً أثناء التنزيل.',
        'trouble_h3': 'أسباب شائعة لعدم تنزيل فيديو فيسبوك',
        'trouble_headers': ['المشكلة', 'السبب المحتمل', 'الحل المقترح'],
        'trouble_rows': [
            ('"تعذر استخراج الفيديو"', 'الفيديو خاص أو محذوف أو مقتصر على الأصدقاء', 'افتح الرابط في نافذة تصفح متخفية. إذا لم يفتح فلا يمكن تنزيله'),
            ('لا يحدث شيء بعد اللصق', 'الرابط لصفحة أو حساب وليس للفيديو مباشرة', 'افتح الفيديو نفسه وانسخ الرابط من خيار المشاركة'),
            ('فشل البث المباشر', 'البث المباشر ما زال جارياً ولم ينته بعد', 'انتظر حتى ينتهي البث ويتحول إلى فيديو مسجل'),
            ('فشل تنزيل القصة Story', 'انتهت مدة القصة (24 ساعة) أو أنها خاصة', 'أعد المحاولة قبل انتهاء صلاحية القصة'),
            ('الرابط يطلب تسجيل الدخول', 'المحتوى يتطلب حساباً لعرضه', 'الأداة تدعم المحتوى العام فقط'),
            ('تنزيل بطيء أو متوقف', 'ملف كبير أو اتصال ضعيف بالشبكة', 'اختر Video (Normal) أو اتصل بشبكة Wi-Fi أسرع')
        ],
        'use_h3': 'أسباب شائعة لحفظ مقاطع فيسبوك',
        'use_items': [
            'الاحتفاظ بنسخة احتياطية من فيديوهاتك العائلية وذكرياتك الشخصية.',
            'مشاهدة الشروحات والوصفات التعليمية دون الحاجة لإنترنت أثناء السفر.',
            'حفظ مقطع طريف لمشاركته مع العائلة عبر واتساب.',
            'استخراج الصوت من محاضرة أو نشيد للاستماع المتكرر لاحقاً.'
        ],
        'safe_h3': 'هل تنزيل مقاطع فيسبوك آمن وقانوني؟',
        'safe_p': '<strong>آمن:</strong> لا نطلب أي بيانات شخصية أو برامج إضافية. <strong>قانوني:</strong> حفظ الفيديوهات العامة للاستخدام الشخصي أمر معتاد، مع مراعاة حقوق الملكية الفكرية لصاحب المحتوى. downsocial أداة مستقلة تماماً وغير تابعة لشركة Meta Platforms, Inc.',
        'tips_h3': 'نصائح لتحقيق أفضل نتائج',
        'tips_items': [
            'انسخ الرابط دائماً من زر <em>مشاركة</em> الخاص بالفيديو نفسه.',
            'اختر <strong>Video (HD)</strong> للمشاهدة على الشاشات الكبيرة أو التلفاز.',
            'استخدم <strong>Video (Normal)</strong> لتوفير استهلاك بيانات الهاتف.',
            'إذا واجهت أي خطأ، جرب فتح الرابط أولاً في نافذة تصفح خاصة.'
        ],
        'sister_h3': 'هل تبحث عن منصات أخرى؟',
        'sister_p': 'نوفر أيضاً أدوات مخصصة لتنزيل الفيديو من <a href="../instagram-downloader/">Instagram</a> و <a href="../tiktok-downloader/">TikTok</a> و <a href="../youtube-downloader/">YouTube</a> و <a href="../snapchat-downloader/">Snapchat</a> و <a href="../threads-downloader/">Threads</a> بالإضافة إلى <a href="../index.html">البرنامج الشامل</a>.',
        'last_updated': 'آخر تحديث: 2 أكتوبر 2026. هل لديك استفسار؟ <a href="contact.html">تواصل مع الدعم الفني</a>.'
    },

    'bn': {
        'qa_title': 'দ্রুত উত্তর: কিভাবে ফেসবুক ভিডিও ডাউনলোড করবেন',
        'qa_text': 'যেকোনো ফেসবুক ভিডিও ডাউনলোড করতে, লিংকটি কপি করুন, এই পেজের উপরের বক্সে পেস্ট করুন, <em>Download Video</em> বাটনে ক্লিক করুন এবং HD, Normal বা MP3 নির্বাচন করুন। এটি সম্পূর্ণ ফ্রি, কোনো লগইন বা অ্যাপের প্রয়োজন নেই এবং iPhone, Android, Windows ও Mac-এ কাজ করে। কেবল পাবলিক ভিডিও ডাউনলোড করা যায়।',
        'h2': 'ফেসবুক ভিডিও ডাউনলোডার: যেকোনো পাবলিক ফেসবুক ভিডিও HD কোয়ালিটিতে সেভ করুন',
        'intro': 'এই <strong>Facebook video downloader</strong> তৈরি করা হয়েছে একটি নির্দিষ্ট উদ্দেশ্যে: যেকোনো পাবলিক ফেসবুক ভিডিও, রিল বা ওয়াচ লিংককে আপনার ডিভাইসে সংরক্ষণযোগ্য ফাইলে রূপান্তর করা। এটি সরাসরি ভিডিও বিশ্লেষণ করে এবং MP4 ভিডিও বা MP3 অডিও হিসেবে তাৎক্ষণিক ডাউনলোড প্রদান করে।',
        't1_h3': 'এক নজরে ফেসবুক ভিডিও ডাউনলোডার',
        't1_headers': ['ফিচার', 'বিবরণ'],
        't1_rows': [
            ('সমর্থিত কনটেন্ট', 'পাবলিক ফেসবুক ভিডিও, রিলস, ওয়াচ ভিডিও, পাবলিক স্টোরিজ বা সমাপ্ত লাইভ ভিডিও'),
            ('গ্রহণযোগ্য লিংক', 'facebook.com, m.facebook.com, facebook.com/share, fb.watch'),
            ('আউটপুট ফরম্যাট', 'MP4 ভিডিও (HD ও Normal), MP3 অডিও (192 kbps ও 128 kbps)'),
            ('ভিডিও কোয়ালিটি', 'ফেসবুকে উপলব্ধ সর্বোচ্চ কোয়ালিটি (সাধারণত 720p থেকে 1080p)। কোনো ভুয়া আপস্কেলিং নেই'),
            ('মূল্য', '<span class="badge-highlight">সম্পূর্ণ ফ্রি, কোনো ডাউনলোড লিমিট নেই</span>'),
            ('লগইন বা অ্যাকাউন্ট', '<span class="badge-highlight">কোনো লগইন লাগবে না</span>'),
            ('জলছাপ (Watermark)', '<span class="badge-highlight">কোনো ওয়াটারমার্ক যুক্ত হয় না</span>'),
            ('ডিভাইস সাপোর্ট', 'iPhone, iPad, Android, Windows, macOS, Linux (যেকোনো ব্রাউজার)'),
            ('সার্ভার স্টোরেজ', 'শূন্য। কোনো ফাইল সার্ভারে সংরক্ষণ করা হয় না'),
            ('সীমাবদ্ধতা', 'শুধুমাত্র পাবলিক ভিডিও। প্রাইভেট গ্রুপ বা ফ্রেন্ডস-অনলি পোস্ট ডাউনলোড করা যায় না')
        ],
        't2_h3': 'কোন কোন ফেসবুক লিংক কাজ করে?',
        't2_intro': 'ফেসবুকে বিভিন্ন ধরনের লিংক ব্যবহৃত হয়। ভিডিওটি পাবলিক হলে নিচের সব লিংক কাজ করে:',
        't2_headers': ['লিংকের ধরন', 'লিংকের নমুনা', 'কখন কাজ করে'],
        't2_rows': [
            ('ওয়াচ ভিডিও', 'facebook.com/watch/?v=...', 'ভিডিও পাবলিক হলে'),
            ('রিল', 'facebook.com/reel/...', 'রিল পাবলিক হলে'),
            ('শেয়ার লিংক', 'facebook.com/share/v/... বা /share/r/...', 'শেয়ার করা ভিডিও পাবলিক হলে'),
            ('শর্ট লিংক', 'fb.watch/...', 'ভিডিও পাবলিক হলে'),
            ('পেজ বা প্রোফাইল ভিডিও', 'facebook.com/PageName/videos/...', 'ভিডিও পাবলিক হলে'),
            ('মোবাইল লিংক', 'm.facebook.com/...', 'ভিডিও পাবলিক হলে'),
            ('গ্রুপ ভিডিও', 'facebook.com/groups/.../posts/...', 'গ্রুপটি পাবলিক হলে')
        ],
        'copy_h3': 'ফেসবুক ভিডিও লিংক কপি করার নিয়ম',
        'copy_items': [
            '<strong>ফেসবুক অ্যাপ (iPhone বা Android):</strong> ভিডিও বা রিলের নিচে <em>Share</em> বাটনে ট্যাপ করুন, তারপর <em>Copy Link</em> নির্বাচন করুন।',
            '<strong>কম্পিউটারে ফেসবুক:</strong> পোস্টের থ্রি-ডট মেনুতে ক্লিক করে <em>Copy link</em> নির্বাচন করুন অথবা পোস্টের সময়ের উপর রাইট-ক্লিক করে লিংক কপি করুন।',
            '<strong>মেসেঞ্জার বা হোয়াটসঅ্যাপ:</strong> কেউ ভিডিও পাঠালে সরাসরি মেসেজ থেকে লিংক কপি করুন।'
        ],
        'device_h3': 'iPhone, Android ও কম্পিউটারে ফেসবুক ভিডিও ডাউনলোড করবেন যেভাবে',
        'ios': '<strong>iPhone বা iPad-এ:</strong> Safari-তে এই পেজটি খুলুন, লিংক পেস্ট করে Download Video চাপুন। ফাইলটি Files অ্যাপের Downloads ফোল্ডারে সেভ হবে। সেখান থেকে Share চেপে Save Video দিলে Photos-এ চলে যাবে।',
        'android': '<strong>Android-এ:</strong> Chrome-এ পেজটি খুলে লিংক পেস্ট করুন এবং Video (HD) সিলেক্ট করুন। ফাইলটি সরাসরি আপনার ফোন গ্যালারিতে সেভ হবে।',
        'pc': '<strong>Windows বা Mac-এ:</strong> লিংক পেস্ট করে Download Video ক্লিক করুন এবং ফরম্যাট বেছে নিন। ফাইলটি সরাসরি ব্রাউজারের Downloads ফোল্ডারে সেভ হবে।',
        'priv_h3': 'প্রাইভেট ফেসবুক ভিডিও ডাউনলোড করা সম্ভব?',
        'priv_p': 'না। এই টুলটি কেবলমাত্র লগইন ছাড়া দেখা যায় এমন পাবলিক ভিডিও ডাউনলোড করতে পারে। ফ্রেন্ডস-অনলি পোস্ট বা প্রাইভেট গ্রুপের ভিডিও অ্যাক্সেস করা সম্ভব নয় এবং আমরা কখনোই আপনার পাসওয়ার্ড চাই না।',
        'qual_h3': 'ফেসবুক ভিডিও কোয়ালিটি: আপনি যা পাবেন',
        'qual_p': 'ফেসবুক প্রতিটি ভিডিও একাধিক রেজোলিউশনে রাখে। <strong>Video (HD)</strong> সর্বোচ্চ কোয়ালিটি প্রদান করে এবং <strong>Video (Normal)</strong> ধীরগতির ইন্টারনেটের জন্য উপযোগী ছোট আকারের ফাইল।',
        'mp3_h3': 'ফেসবুক ভিডিও থেকে MP3 অডিও তৈরি',
        'mp3_p': 'কোনো গান, ওয়াজ, সাক্ষাৎকার বা পডকাস্টের কেবল অডিও প্রয়োজন? 192 kbps-এর জন্য <strong>Audio (HQ MP3)</strong> অথবা 128 kbps-এর জন্য <strong>Audio (Normal MP3)</strong> নির্বাচন করুন। ডাউনলোডের সাথে সাথেই রূপান্তর সম্পন্ন হয়।',
        'trouble_h3': 'ভিডিও ডাউনলোড না হওয়ার সম্ভাব্য কারণ',
        'trouble_headers': ['লক্ষণ', 'সম্ভাব্য কারণ', 'করণীয়'],
        'trouble_rows': [
            ('"Could not extract video"', 'ভিডিওটি প্রাইভেট, শুধু বন্ধুদের জন্য বা মুছে ফেলা হয়েছে', 'ইনকগনিটো উইন্ডোতে লিংকটি খুলে দেখুন, সেখানে না চললে ডাউনলোড হবে না'),
            ('পেস্ট করার পর কিছু হয় না', 'লিংকটি ভিডিওর নয় বরং প্রোফাইল বা পোস্টের', 'মূল ভিডিওটি চালু করে Share অপশন থেকে লিংক কপি করুন'),
            ('লাইভ ভিডিও ব্যর্থ হয়', 'লাইভ সম্প্রচার এখনও চলমান আছে', 'লাইভ শেষ হওয়া পর্যন্ত অপেক্ষা করুন'),
            ('স্টোরি ডাউনলোড হয় না', 'স্টোরির ২৪ ঘণ্টা মেয়াদ শেষ বা প্রাইভেট', 'স্টোরি লাইভ থাকা অবস্থায় পুনরায় চেষ্টা করুন'),
            ('লগইন পেজ আসে', 'কনটেন্টটি দেখতে অ্যাকাউন্ট লগইন প্রয়োজন', 'কেবলমাত্র শতভাগ পাবলিক ভিডিও সমর্থিত'),
            ('ডাউনলোড খুব ধীরগতির', 'ফাইল সাইজ বড় বা দুর্বল ইন্টারনেট কানেকশন', 'Video (Normal) চেষ্টা করুন বা দ্রুতগতির ওয়াই-ফাই ব্যবহার করুন')
        ],
        'use_h3': 'মানুষ কেন ফেসবুক ভিডিও সেভ করে?',
        'use_items': [
            '<strong>নিজের</strong> পারিবারিক ভিডিও, স্মৃতি ও অনুষ্ঠান হারিয়ে যাওয়ার হাত থেকে নিরাপদে ব্যাকআপ রাখা।',
            'ভ্রমণের সময় বা ইন্টারনেট ছাড়া টিউটোরিয়াল, রান্না ও লেকচার দেখা।',
            'অনুমতি নিয়ে হোয়াটসঅ্যাপে বন্ধুদের সাথে ক্লিপ শেয়ার করা।',
            'যেকোনো বক্তব্য বা গানের অডিও ফাইল আলাদা করে পরবর্তীতে শোনার জন্য।'
        ],
        'safe_h3': 'ফেসবুক ভিডিও ডাউনলোড কি নিরাপদ ও বৈধ?',
        'safe_p': '<strong>নিরাপদ:</strong> কোনো পাসওয়ার্ড বা অ্যাপ ইনস্টল করার প্রয়োজন নেই। <strong>বৈধ:</strong> ব্যক্তিগত অফলাইন ব্যবহারের জন্য পাবলিক ভিডিও সংরক্ষণ করা স্বাভাবিক, তবে কপিরাইট সর্বদাই মূল নির্মাতার। downsocial কোনোভাবেই Meta Platforms, Inc.-এর সাথে সম্পর্কিত নয়।',
        'tips_h3': 'সেরা ফলাফলের জন্য কিছু টিপস',
        'tips_items': [
            'সর্বদা ভিডিওর নিজস্ব <em>Share</em> মেনু থেকে লিংক কপি করুন।',
            'বড় স্ক্রিন বা টিভিতে দেখার জন্য <strong>Video (HD)</strong> ব্যবহার করুন।',
            'মোবাইল ডেটা বাঁচাতে <strong>Video (Normal)</strong> বা MP3 নির্বাচন করুন।',
            'কোনো লিংকে সমস্যা হলে আগে ব্রাউজারের ইনকগনিটো মোডে পরীক্ষা করুন।'
        ],
        'sister_h3': 'অন্যান্য প্ল্যাটফর্মের জন্য ডাউনলোডার চাই?',
        'sister_p': 'আমরা <a href="../instagram-downloader/">Instagram</a>, <a href="../tiktok-downloader/">TikTok</a>, <a href="../youtube-downloader/">YouTube</a>, <a href="../snapchat-downloader/">Snapchat</a> এবং <a href="../threads-downloader/">Threads</a> এর জন্যও ডেডিকেটেড টুল এবং আমাদের <a href="../index.html">অল-ইন-ওয়ান ডাউনলোডার</a> অফার করি।',
        'last_updated': 'সর্বশেষ আপডেট: ২ অক্টোবর ২০২৬। কোনো প্রশ্ন আছে? <a href="contact.html">সাপোর্টে যোগাযোগ করুন</a>।'
    },

    'ru': {
        'qa_title': 'Быстрый ответ: как скачать видео с Facebook',
        'qa_text': 'Чтобы скачать видео с Facebook, скопируйте ссылку, вставьте ее в поле вверху этой страницы, нажмите <em>Скачать видео</em> и выберите HD, Normal или MP3. Это бесплатно, не требует входа или установки приложений и работает на iPhone, Android, Windows и Mac. Загружать можно только публичные видео.',
        'h2': 'Загрузчик видео с Facebook: сохраняйте любые публичные видео в HD',
        'intro': 'Этот <strong>загрузчик видео с Facebook</strong> создан для одной четкой задачи: превратить ссылку на публичное видео, Reel или Watch в файл на вашем устройстве. Он считывает видеопоток, отображает доступные разрешения и сохраняет файл в формате MP4 или MP3. Никаких программ, никакой регистрации и полная безопасность.',
        't1_h3': 'Краткий обзор загрузчика Facebook',
        't1_headers': ['Функция', 'Подробности'],
        't1_rows': [
            ('Поддерживаемый контент', 'Публичные видео Facebook, Reels, Watch, публичные Истории и завершенные прямые эфиры'),
            ('Поддерживаемые ссылки', 'facebook.com, m.facebook.com, facebook.com/share, fb.watch'),
            ('Форматы файлов', 'MP4 видео (HD и Normal), MP3 аудио (192 kbps и 128 kbps)'),
            ('Качество видео', 'Максимальное исходное качество Facebook, обычно от 720p до 1080p. Без искусственного апскейла'),
            ('Стоимость', '<span class="badge-highlight">Бесплатно, без ограничений по скачиванию</span>'),
            ('Аккаунт или вход', '<span class="badge-highlight">Не требуется</span>'),
            ('Водяные знаки', '<span class="badge-highlight">Не добавляются</span>'),
            ('Совместимость', 'iPhone, iPad, Android, Windows, macOS, Linux (все браузеры)'),
            ('Хранение файлов', 'Файлы не сохраняются на наших серверах'),
            ('Ограничения', 'Только публичные видео. Не скачивает из закрытых групп и постов "только для друзей"')
        ],
        't2_h3': 'Какие ссылки Facebook поддерживаются?',
        't2_intro': 'Facebook использует разные форматы ссылок. Если видео публичное, подходят следующие варианты:',
        't2_headers': ['Тип ссылки', 'Пример формата', 'Работает когда'],
        't2_rows': [
            ('Видео Watch', 'facebook.com/watch/?v=...', 'Видео является публичным'),
            ('Reel', 'facebook.com/reel/...', 'Reel является публичным'),
            ('Ссылка "Поделиться"', 'facebook.com/share/v/... или /share/r/...', 'Опубликованное видео публично'),
            ('Короткая ссылка', 'fb.watch/...', 'Видео является публичным'),
            ('Видео страницы или профиля', 'facebook.com/PageName/videos/...', 'Видео является публичным'),
            ('Мобильная ссылка', 'm.facebook.com/...', 'Видео является публичным'),
            ('Видео из группы', 'facebook.com/groups/.../posts/...', 'Группа является открытой')
        ],
        'copy_h3': 'Как скопировать ссылку на видео Facebook',
        'copy_items': [
            '<strong>В приложении Facebook (iPhone или Android):</strong> нажмите <em>Поделиться</em> под видео или Reel, затем выберите <em>Копировать ссылку</em>.',
            '<strong>На компьютере:</strong> нажмите меню из трех точек на посте и выберите <em>Копировать ссылку</em>, либо кликните правой кнопкой мыши по дате публикации.',
            '<strong>В Messenger или WhatsApp:</strong> если вам прислали видео, скопируйте URL прямо из текста сообщения.'
        ],
        'device_h3': 'Как скачать видео с Facebook на iPhone, Android и ПК',
        'ios': '<strong>На iPhone или iPad:</strong> откройте эту страницу в Safari, вставьте ссылку и нажмите Скачать видео. Файл загрузится в папку "Файлы" > "Загрузки". Откройте его, нажмите Поделиться и выберите "Сохранить видео" для переноса в Фото.',
        'android': '<strong>На Android:</strong> откройте страницу в Chrome, вставьте ссылку и выберите Video (HD). MP4 файл сохранится в папку "Загрузки" и появится в Галерее.',
        'pc': '<strong>На Windows или Mac:</strong> вставьте ссылку, нажмите Скачать видео и выберите нужный формат. Файл скачается в папку Загрузки вашего браузера.',
        'priv_h3': 'Можно ли скачать приватные видео Facebook?',
        'priv_p': 'Нет. Наш инструмент загружает только материалы, доступные каждому без авторизации. Посты для друзей и публикации из закрытых групп защищены настройками приватности, и мы никогда не запрашиваем ваш пароль.',
        'qual_h3': 'Качество видео Facebook: что вы получаете на самом деле',
        'qual_p': 'Facebook хранит видео в нескольких вариантах. <strong>Video (HD)</strong> — это максимальное доступное разрешение ролика, а <strong>Video (Normal)</strong> — облегченная версия для экономии трафика. Исходное разрешение задает предел: ролик в 480p невозможно превратить в 1080p.',
        'mp3_h3': 'Конвертация видео Facebook в MP3',
        'mp3_p': 'Нужна только аудиодорожка интервью, выступления или песни? Выберите <strong>Audio (HQ MP3)</strong> с битрейтом 192 kbps или <strong>Audio (Normal MP3)</strong> со 128 kbps. Конвертация происходит прямо во время загрузки.',
        'trouble_h3': 'Почему видео с Facebook может не скачиваться',
        'trouble_headers': ['Симптом', 'Возможная причина', 'Решение'],
        'trouble_rows': [
            ('"Не удалось извлечь видео"', 'Видео приватное, только для друзей или удалено', 'Откройте ссылку в режиме инкогнито. Если видео не запускается, его нельзя скачать'),
            ('Ничего не происходит после вставки', 'Ссылка ведет на профиль или страницу, а не на само видео', 'Откройте именно плеер с видео и скопируйте ссылку через "Поделиться"'),
            ('Прямой эфир не скачивается', 'Трансляция еще продолжается', 'Дождитесь завершения эфира и его публикации в виде видеозаписи'),
            ('История не скачивается', 'Срок действия Истории истек (24 часа) или она скрыта', 'Попробуйте снова, пока История еще активна'),
            ('Требуется авторизация', 'Контент закрыт настройками аккаунта', 'Поддерживаются исключительно полностью открытые видео'),
            ('Очень медленная загрузка', 'Большой файл или нестабильный интернет', 'Попробуйте Video (Normal) или переключитесь на быстрый Wi-Fi')
        ],
        'use_h3': 'Популярные причины сохранения видео с Facebook',
        'use_items': [
            'Резервное копирование <strong>своих</strong> семейных видео и памятных записей.',
            'Просмотр уроков, рецептов и лекций оффлайн во время поездок.',
            'Сохранение понравившегося ролика для отправки друзьям в WhatsApp.',
            'Извлечение аудиозаписи речи или трека для прослушивания в плеере.'
        ],
        'safe_h3': 'Безопасно и законно ли скачивать видео с Facebook?',
        'safe_p': '<strong>Безопасно:</strong> не требуется вводить пароли или устанавливать сомнительные расширения. <strong>Законно:</strong> скачивание публичных материалов для личного оффлайн-просмотра допустимо, однако авторские права сохраняются за владельцем. downsocial — независимый сервис, не связанный с Meta Platforms, Inc.',
        'tips_h3': 'Советы для наилучшего результата',
        'tips_items': [
            'Копируйте ссылку именно из кнопки <em>Поделиться</em> самого видеоролика.',
            'Выбирайте <strong>Video (HD)</strong> для просмотра на ТВ или мониторе.',
            'Используйте <strong>Video (Normal)</strong> для экономии мобильного интернета.',
            'При возникновении ошибок проверьте доступность ссылки в режиме инкогнито.'
        ],
        'sister_h3': 'Нужны загрузчики для других сетей?',
        'sister_p': 'Мы также предлагаем инструменты для <a href="../instagram-downloader/">Instagram</a>, <a href="../tiktok-downloader/">TikTok</a>, <a href="../youtube-downloader/">YouTube</a>, <a href="../snapchat-downloader/">Snapchat</a> и <a href="../threads-downloader/">Threads</a>, а также наш универсальный <a href="../index.html">All-in-One Downloader</a>.',
        'last_updated': 'Последнее обновление: 2 октября 2026 г. Возникли вопросы? <a href="contact.html">Служба поддержки</a>.'
    },

    'id': {
        'qa_title': 'Jawaban Cepat: Cara Mengunduh Video Facebook',
        'qa_text': 'Untuk mengunduh video Facebook, salin tautannya, tempelkan ke kolom di bagian atas halaman ini, klik <em>Download Video</em>, dan pilih HD, Normal, atau MP3. Layanan ini 100% gratis, tidak memerlukan login atau aplikasi tambahan, dan berfungsi di iPhone, Android, Windows, serta Mac. Hanya video publik yang dapat diunduh.',
        'h2': 'Facebook Video Downloader: Simpan Video Publik Facebook Berkualitas HD',
        'intro': '<strong>Facebook video downloader</strong> ini dirancang untuk satu tujuan utama: mengubah tautan video publik, Reel, atau Watch Facebook menjadi file permanen di perangkat Anda. Alat ini membaca video publik, menampilkan opsi resolusi yang tersedia, dan langsung mengunduh pilihan Anda sebagai video MP4 atau audio MP3 tanpa perlu memasang aplikasi pihak ketiga.',
        't1_h3': 'Sekilas Tentang Facebook Video Downloader',
        't1_headers': ['Fitur', 'Keterangan'],
        't1_rows': [
            ('Konten yang didukung', 'Video publik Facebook, Reels, video Watch, serta Stories publik atau siaran Live yang telah selesai'),
            ('Format tautan yang diterima', 'facebook.com, m.facebook.com, facebook.com/share, fb.watch'),
            ('Format output', 'Video MP4 (HD dan Normal), audio MP3 (192 kbps dan 128 kbps)'),
            ('Kualitas video', 'Kualitas tertinggi yang disediakan Facebook, umumnya 720p hingga 1080p tanpa upscaling palsu'),
            ('Harga', '<span class="badge-highlight">Gratis tanpa batas unduhan</span>'),
            ('Akun atau login', '<span class="badge-highlight">Tidak diperlukan</span>'),
            ('Watermark', '<span class="badge-highlight">Tanpa watermark tambahan</span>'),
            ('Dukungan perangkat', 'iPhone, iPad, Android, Windows, macOS, Linux (semua browser modern)'),
            ('Penyimpanan file', 'Nol. Tidak ada video yang disimpan di server kami'),
            ('Batasan', 'Hanya video publik. Tidak dapat mengunduh video dari grup privat atau kiriman khusus teman')
        ],
        't2_h3': 'Tautan Facebook Mana Saja yang Berfungsi?',
        't2_intro': 'Facebook memiliki beberapa format URL. Selama video berstatus publik, seluruh format berikut didukung:',
        't2_headers': ['Jenis Tautan', 'Contoh Tautan', 'Berfungsi Saat'],
        't2_rows': [
            ('Video Watch', 'facebook.com/watch/?v=...', 'Video berstatus publik'),
            ('Reel', 'facebook.com/reel/...', 'Reel berstatus publik'),
            ('Tautan Bagikan', 'facebook.com/share/v/... atau /share/r/...', 'Video yang dibagikan berstatus publik'),
            ('Tautan Pendek', 'fb.watch/...', 'Video berstatus publik'),
            ('Video Halaman / Profil', 'facebook.com/NamaHalaman/videos/...', 'Video berstatus publik'),
            ('Tautan Seluler', 'm.facebook.com/...', 'Video berstatus publik'),
            ('Video Grup', 'facebook.com/groups/.../posts/...', 'Grup bersifat publik')
        ],
        'copy_h3': 'Cara Menyalin Tautan Video Facebook',
        'copy_items': [
            '<strong>Aplikasi Facebook (iPhone atau Android):</strong> ketuk <em>Bagikan (Share)</em> di bawah video atau Reel, lalu pilih <em>Salin Tautan (Copy Link)</em>.',
            '<strong>Facebook di Komputer:</strong> klik menu tiga titik pada postingan dan pilih <em>Salin tautan</em>, atau klik kanan pada waktu postingan lalu salin alamat tautan.',
            '<strong>Messenger atau WhatsApp:</strong> jika ada yang mengirimkan video Facebook, salin tautan langsung dari ruang obrolan.'
        ],
        'device_h3': 'Cara Mengunduh Video Facebook di iPhone, Android, dan Komputer',
        'ios': '<strong>Di iPhone atau iPad:</strong> buka halaman ini di Safari, tempel tautan dan ketuk Download Video. File akan tersimpan di aplikasi File > Unduhan. Buka file tersebut, ketuk Bagikan, dan pilih "Simpan Video" untuk memindahkannya ke Foto.',
        'android': '<strong>Di Android:</strong> buka halaman ini di Chrome, tempel tautan dan pilih Video (HD). File MP4 akan terunduh ke folder Download dan muncul di Galeri ponsel Anda.',
        'pc': '<strong>Di Windows atau Mac:</strong> tempel tautan ke dalam kotak, klik Download Video, lalu pilih format yang diinginkan untuk disimpan ke folder Downloads.',
        'priv_h3': 'Bisakah Mengunduh Video Facebook Privat?',
        'priv_p': 'Tidak. Layanan ini hanya mengunduh video yang dapat dibuka oleh siapa saja tanpa perlu masuk ke akun. Kiriman khusus teman, grup privat, dan video dengan batas audiens tidak dapat diakses, dan kami tidak akan pernah meminta kata sandi Facebook Anda.',
        'qual_h3': 'Kualitas Video Facebook: Yang Sebenarnya Anda Dapatkan',
        'qual_p': 'Facebook mengunggah video dalam beberapa pilihan bitrate. <strong>Video (HD)</strong> memberikan resolusi terbaik yang tersedia, sedangkan <strong>Video (Normal)</strong> menyajikan ukuran file lebih kecil yang hemat kuota. Resolusi asli saat diunggah menjadi batas maksimal kualitas.',
        'mp3_h3': 'Mengubah Video Facebook Menjadi MP3',
        'mp3_p': 'Hanya membutuhkan suara dari lagu, wawancara, podcast, atau ceramah? Pilih <strong>Audio (HQ MP3)</strong> untuk 192 kbps atau <strong>Audio (Normal MP3)</strong> untuk 128 kbps. Konversi audio berlangsung cepat langsung saat proses pengunduhan.',
        'trouble_h3': 'Penyebab Video Facebook Gagal Diunduh',
        'trouble_headers': ['Masalah', 'Kemungkinan Penyebab', 'Solusi yang Dianjurkan'],
        'trouble_rows': [
            ('"Could not extract video"', 'Video berstatus privat, khusus teman, atau telah dihapus', 'Buka tautan di jendela penyamaran (incognito). Jika tidak bisa diputar, maka video tidak dapat diunduh'),
            ('Tidak ada respon setelah menempel', 'Tautan mengarah ke profil atau beranda, bukan video langsung', 'Buka video tersebut dan salin tautannya dari tombol Bagikan'),
            ('Video Live gagal', 'Siaran langsung masih berlangsung', 'Tunggu hingga siaran selesai dan tersimpan sebagai video rekaman'),
            ('Story gagal', 'Story telah kedaluwarsa (lebih dari 24 jam) atau bersifat privat', 'Coba kembali saat Story masih aktif dan dapat dilihat'),
            ('Tautan meminta login', 'Konten memerlukan akun Facebook untuk dilihat', 'Hanya video publik bebas yang dapat diproses'),
            ('Unduhan sangat lambat', 'Ukuran file besar atau koneksi internet tidak stabil', 'Gunakan opsi Video (Normal) atau beralih ke jaringan Wi-Fi')
        ],
        'use_h3': 'Alasan Populer Menyimpan Video Facebook',
        'use_items': [
            'Menyimpan salinan arsip video keluarga dan kenangan <strong>milik sendiri</strong>.',
            'Menonton video tutorial, resep masakan, dan edukasi secara offline saat bepergian.',
            'Menyimpan klip menarik untuk dibagikan kembali ke keluarga lewat WhatsApp.',
            'Mengekstrak trek audio ceramah atau musik untuk didengarkan berulang kali.'
        ],
        'safe_h3': 'Apakah Mengunduh Video Facebook Aman dan Legal?',
        'safe_p': '<strong>Aman:</strong> Anda tidak perlu memasukkan kata sandi atau memasang software apa pun. <strong>Legal:</strong> mengunduh video publik untuk konsumsi offline pribadi adalah hal yang lazim, namun hak cipta tetap milik pembuat aslinya. downsocial adalah layanan independen yang tidak berafiliasi dengan Meta Platforms, Inc.',
        'tips_h3': 'Tips Memperoleh Hasil Unduhan Terbaik',
        'tips_items': [
            'Salin tautan langsung dari tombol <em>Bagikan</em> pada video yang bersangkutan.',
            'Pilih opsi <strong>Video (HD)</strong> jika ingin menonton di layar TV atau monitor besar.',
            'Gunakan <strong>Video (Normal)</strong> atau MP3 guna menghemat kuota seluler.',
            'Jika tautan gagal diproses, pastikan video dapat diputar di mode penyamaran.'
        ],
        'sister_h3': 'Mencari Pengunduh untuk Media Sosial Lain?',
        'sister_p': 'Kami juga menyediakan pengunduh khusus untuk <a href="../instagram-downloader/">Instagram</a>, <a href="../tiktok-downloader/">TikTok</a>, <a href="../youtube-downloader/">YouTube</a>, <a href="../snapchat-downloader/">Snapchat</a>, dan <a href="../threads-downloader/">Threads</a>, serta alat serbaguna <a href="../index.html">All-in-One Video Downloader</a>.',
        'last_updated': 'Pembaruan terakhir: 2 Oktober 2026. Ada pertanyaan atau tautan bermasalah? <a href="contact.html">Hubungi tim bantuan</a>.'
    },

    'zh': {
        'qa_title': '快速解答：如何下载 Facebook 视频',
        'qa_text': '下载 Facebook 视频只需复制其链接，粘贴到本页面顶部的输入框中，点击<em>下载视频</em>，然后选择高清 (HD)、标清 (Normal) 或 MP3 音频。完全免费，无需登录或安装软件，兼容 iPhone、Android、Windows 和 Mac。仅支持下载公开视频。',
        'h2': 'Facebook 视频下载器：免费高清保存任何公开 Facebook 视频',
        'intro': '这款 <strong>Facebook 视频下载器</strong> 专为单一任务而生：将公开的 Facebook 视频、Reel 短视频或 Watch 链接转换为可在本地永久保存的文件。它会读取视频流，展示可用画质，并直接将文件以 MP4 视频或 MP3 音频形式保存到您的设备。无需安装任何扩展，不记录个人数据，也不会涉及您的 Facebook 账号。',
        't1_h3': 'Facebook 视频下载器一览',
        't1_headers': ['功能特点', '详细说明'],
        't1_rows': [
            ('支持的内容', '公开 Facebook 视频、Reels 短视频、Watch 视频、公开快拍 (Story) 以及已结束的公开直播'),
            ('支持的链接', 'facebook.com, m.facebook.com, facebook.com/share, fb.watch'),
            ('输出格式', 'MP4 视频（高清 HD 与标清 Normal）、MP3 音频（192 kbps 与 128 kbps）'),
            ('视频画质', '提供 Facebook 原视频具备的最高清晰度，通常在 720p 至 1080p 之间，绝不虚标分辨率'),
            ('服务费用', '<span class="badge-highlight">完全免费，无下载次数限制</span>'),
            ('账号要求', '<span class="badge-highlight">无需登录或注册</span>'),
            ('水印状态', '<span class="badge-highlight">不添加任何水印</span>'),
            ('适用设备', 'iPhone, iPad, Android, Windows, macOS, Linux（所有现代浏览器）'),
            ('文件留存', '不保存任何视频文件，仅作为实时提取通道'),
            ('限制条件', '仅支持公开内容，无法绕过私密群组或好友限定权限')
        ],
        't2_h3': '支持哪些 Facebook 链接格式？',
        't2_intro': 'Facebook 在网页和 App 中存在多种链接格式。只要视频本身是公开的，以下所有链接均可识别：',
        't2_headers': ['链接类型', '链接示例格式', '生效条件'],
        't2_rows': [
            ('Watch 视频', 'facebook.com/watch/?v=...', '视频必须为公开状态'),
            ('Reel 短视频', 'facebook.com/reel/...', 'Reel 必须为公开状态'),
            ('分享链接', 'facebook.com/share/v/... 或 /share/r/...', '被分享的视频为公开状态'),
            ('短网址', 'fb.watch/...', '视频必须为公开状态'),
            ('主页或个人主页视频', 'facebook.com/主页名/videos/...', '视频必须为公开状态'),
            ('移动版链接', 'm.facebook.com/...', '视频必须为公开状态'),
            ('群组视频', 'facebook.com/groups/.../posts/...', '群组必须为公开群组')
        ],
        'copy_h3': '如何复制 Facebook 视频链接',
        'copy_items': [
            '<strong>手机端 Facebook 应用程序（iPhone 或 Android）：</strong>点击视频或 Reel 下方的<em>分享</em>按钮，然后选择<em>复制链接</em>。',
            '<strong>电脑端网页：</strong>点击帖子右上角的三个小点选择<em>复制链接</em>，或者直接右键点击发布时间复制链接地址。',
            '<strong>Messenger 或微信/WhatsApp：</strong>如果别人在聊天中发送了视频，长按消息直接复制链接即可。'
        ],
        'device_h3': '在 iPhone、Android 和电脑上下载 Facebook 视频的步骤',
        'ios': '<strong>在 iPhone 或 iPad 上：</strong>使用 Safari 浏览器打开本页面，粘贴链接并点击“下载视频”。文件会保存到“文件”App的“下载”文件夹中。打开文件，点击分享按钮并选择“存储视频”，即可将其存入“照片”相册。',
        'android': '<strong>在 Android 设备上：</strong>在 Chrome 浏览器中打开本站，粘贴链接并点击“Video (HD)”。MP4 文件会直接保存到“下载”目录，并可在系统相册中查看。',
        'pc': '<strong>在 Windows 或 Mac 上：</strong>粘贴链接，点击“下载视频”，选择需要的格式，文件即可直接存入浏览器的下载目录中。',
        'priv_h3': '是否可以下载私密 Facebook 视频？',
        'priv_p': '不可以。本工具仅支持任何人无需登录即可浏览的公开视频。仅好友可见的动态、私密小组内的视频均无法提取，我们也绝不会索取您的密码来尝试登录。',
        'qual_h3': 'Facebook 视频画质说明：您能获得的实际效果',
        'qual_p': 'Facebook 会根据上传源文件生成不同档位的画质。<strong>Video (HD)</strong> 提供当前视频的最高源分辨率，而 <strong>Video (Normal)</strong> 则是文件较小的标清版本。如果原作者仅上传了 480p 视频，则无法强行提升为 1080p。',
        'mp3_h3': '将 Facebook 视频转换为 MP3 音频',
        'mp3_p': '如果您只需要访谈、演讲、音乐或搞笑片段的声音，请选择 <strong>Audio (HQ MP3)</strong>（192 kbps）或 <strong>Audio (Normal MP3)</strong>（128 kbps）。转换将在下载过程中实时完成。',
        'trouble_h3': 'Facebook 视频无法下载的常见排查原因',
        'trouble_headers': ['现象', '可能原因', '建议解决方法'],
        'trouble_rows': [
            ('“无法提取视频”提示', '视频为私密内容、仅限好友或已被作者删除', '在浏览器无痕隐身窗口中打开链接，若提示需登录则说明无法下载'),
            ('粘贴后没有反应', '所贴链接是个人主页或文字动态而非直接视频', '进入视频独立播放界面，重新通过“分享”按钮复制直接链接'),
            ('直播视频下载失败', '直播正在进行中尚未结束', '请等待直播彻底结束并自动转为录播视频后再试'),
            ('快拍 (Story) 提取失败', '快拍已满 24 小时过期或并非公开', '快拍时效性强，请在未失效前尽快下载'),
            ('提示需要登录', '该内容受目标用户权限保护', '本工具仅支持无需登录的完全公开内容'),
            ('下载速度极慢', '文件体积较大或当前网络波动', '尝试选择 Video (Normal) 或切换至 Wi-Fi 环境')
        ],
        'use_h3': '用户保存 Facebook 视频的常见用途',
        'use_items': [
            '备份<strong>自己</strong>的家庭聚会视频与珍贵回忆，避免因误删导致丢失。',
            '在出差、旅途或网络不便时，离线观看健身、烹饪和学术教程。',
            '将获得许可的有趣视频片段保存后通过聊天软件分享给家人。',
            '提取演讲或背景音乐音频以便在手机音乐播放器中随时收听。'
        ],
        'safe_h3': '下载 Facebook 视频是否安全合法？',
        'safe_p': '<strong>安全性：</strong>不需要输入任何密码，不需要安装任何第三方插件。<strong>合法性：</strong>下载公开视频供个人离线学习和观看是常规行为，但视频知识产权归原作者所有。downsocial 是独立的网络工具，与 Meta Platforms, Inc. 无任何隶属关系。',
        'tips_h3': '获得最佳下载体验的建议',
        'tips_items': [
            '务必从视频专属的<em>分享</em>菜单中复制直链，不要复制浏览器顶部的个人主页网址。',
            '在电视或电脑大屏幕上观看时，优先选择 <strong>Video (HD)</strong>。',
            '流量有限时，建议选择 <strong>Video (Normal)</strong> 或 MP3 音频。',
            '若遇到解析失败，建议先在隐身窗口中核实视频是否完全公开。'
        ],
        'sister_h3': '还需要下载其他平台的视频？',
        'sister_p': '我们还提供针对 <a href="../instagram-downloader/">Instagram</a>、<a href="../tiktok-downloader/">TikTok</a>、<a href="../youtube-downloader/">YouTube</a>、<a href="../snapchat-downloader/">Snapchat</a> 和 <a href="../threads-downloader/">Threads</a> 的专用工具，以及<a href="../index.html">全能社交媒体视频下载器</a>。',
        'last_updated': '最后更新：2026年10月2日。如有任何疑问或遇到异常链接，欢迎<a href="contact.html">联系客服支持</a>。'
    },

    'ur': {
        'qa_title': 'فوری جواب: فیس بک ویڈیو کیسے ڈاؤن لوڈ کریں',
        'qa_text': 'کسی بھی فیس بک ویڈیو کو ڈاؤن لوڈ کرنے کے لیے، اس کا لنک کاپی کریں، اس صفحے کے اوپری باکس میں پیسٹ کریں، <em>Download Video</em> پر کلک کریں اور HD، Normal یا MP3 منتخب کریں۔ یہ 100% مفت ہے، کسی لاگ ان یا ایپ کی ضرورت نہیں ہے، اور iPhone، Android، Windows اور Mac پر کام کرتا ہے۔ صرف پبلک ویڈیوز ہی ڈاؤن لوڈ کی جا سکتی ہیں۔',
        'h2': 'فیس بک ویڈیو ڈاؤنلوڈر: کسی بھی پبلک فیس بک ویڈیو کو HD میں محفوظ کریں',
        'intro': 'یہ <strong>Facebook video downloader</strong> ایک خاص مقصد کے لیے بنایا گیا ہے: کسی بھی پبلک فیس بک ویڈیو، ریل یا واچ لنک کو آپ کے موبائل یا کمپیوٹر پر محفوظ فائل میں تبدیل کرنا۔ یہ ویڈیو کو فوری طور پر حاصل کر کے MP4 ویڈیو یا MP3 آڈیو کے طور پر ڈاؤن لوڈ فراہم کرتا ہے۔ کوئی ایپ انسٹال نہیں کرنی پڑتی، کچھ بھی ہمارے سرور پر محفوظ نہیں ہوتا اور آپ کا فیس بک اکاؤنٹ مکمل محفوظ رہتا ہے۔',
        't1_h3': 'فیس بک ویڈیو ڈاؤنلوڈر کی نمایاں خصوصیات',
        't1_headers': ['خصوصیت', 'تفصیل'],
        't1_rows': [
            ('سپورٹ شدہ مواد', 'پبلک فیس بک ویڈیوز، ریلز، واچ ویڈیوز، پبلک اسٹوریز یا اختتام پذیر لائیو اسٹریمز'),
            ('قبول شدہ لنکس', 'facebook.com, m.facebook.com, facebook.com/share, fb.watch'),
            ('فائل فارمیٹس', 'MP4 ویڈیو (HD اور Normal)، MP3 آڈیو (192 kbps اور 128 kbps)'),
            ('ویڈیو کوالٹی', 'فیس بک پر موجود اصل بہترین ریزولوشن، عام طور پر 720p سے 1080p۔ کوئی نقلی اضافہ نہیں'),
            ('قیمت', '<span class="badge-highlight">بالکل مفت، لامحدود ڈاؤن لوڈز</span>'),
            ('اکاؤنٹ یا لاگ ان', '<span class="badge-highlight">کسی لاگ ان کی ضرورت نہیں</span>'),
            ('واٹر مارک', '<span class="badge-highlight">کوئی واٹر مارک نہیں لگایا جاتا</span>'),
            ('ڈیوائس سپورٹ', 'iPhone, iPad, Android, Windows, macOS, Linux (تمام جدید براؤزرز)'),
            ('ڈیٹا پرائیویسی', 'صفر۔ ہم کوئی بھی ویڈیو سرور پر محفوظ نہیں کرتے'),
            ('حدود', 'صرف پبلک ویڈیوز۔ پرائیویٹ گروپس یا فرینڈز اونلی پوسٹس ڈاؤن لوڈ نہیں ہو سکتیں')
        ],
        't2_h3': 'کون سے فیس بک لنکس کام کرتے ہیں؟',
        't2_intro': 'فیس بک پر مختلف انداز کے لنکس استعمال ہوتے ہیں۔ اگر ویڈیو پبلک ہے تو یہ تمام لنکس کام کرتے ہیں:',
        't2_headers': ['لنک کی قسم', 'لنک کی بناوٹ', 'کب کام کرتا ہے'],
        't2_rows': [
            ('واچ ویڈیو', 'facebook.com/watch/?v=...', 'ویڈیو پبلک ہو'),
            ('ریل', 'facebook.com/reel/...', 'ریل پبلک ہو'),
            ('شیئر لنک', 'facebook.com/share/v/... یا /share/r/...', 'شیئر کردہ ویڈیو پبلک ہو'),
            ('مختصر لنک', 'fb.watch/...', 'ویڈیو پبلک ہو'),
            ('پیج یا پروفائل ویڈیو', 'facebook.com/PageName/videos/...', 'ویڈیو پبلک ہو'),
            ('موبائل لنک', 'm.facebook.com/...', 'ویڈیو پبلک ہو'),
            ('گروپ ویڈیو', 'facebook.com/groups/.../posts/...', 'گروپ پبلک ہو')
        ],
        'copy_h3': 'فیس بک ویڈیو کا لنک کاپی کرنے کا طریقہ',
        'copy_items': [
            '<strong>فیس بک ایپ (iPhone یا Android):</strong> ویڈیو یا ریل کے نیچے <em>Share</em> پر ٹیپ کریں، پھر <em>Copy Link</em> منتخب کریں۔',
            '<strong>کمپیوٹر پر فیس بک:</strong> پوسٹ کے تھری ڈاٹ مینو پر کلک کر کے <em>Copy link</em> منتخب کریں یا ٹائم اسٹیمپ پر رائٹ کلک کر کے لنک کاپی کریں۔',
            '<strong>میسنجر یا واٹس ایپ:</strong> اگر کسی نے ویڈیو بھیجی ہے تو براہ راست میسج سے لنک کاپی کریں۔'
        ],
        'device_h3': 'iPhone، Android اور کمپیوٹر پر فیس بک ویڈیوز ڈاؤن لوڈ کرنے کا طریقہ',
        'ios': '<strong>iPhone یا iPad پر:</strong> Safari میں یہ صفحہ کھولیں، لنک پیسٹ کریں اور Download Video پر ٹیپ کریں۔ فائل Files ایپ میں Downloads کے اندر محفوظ ہوگی۔ وہاں سے Share دبا کر Save Video کریں تاکہ Photos ایپ میں چلی جائے۔',
        'android': '<strong>Android پر:</strong> Chrome میں یہ صفحہ کھولیں، لنک پیسٹ کریں اور Video (HD) پر کلک کریں۔ فائل فوراً آپ کی گیلری اور ڈاؤن لوڈز میں آ جائے گی۔',
        'pc': '<strong>Windows یا Mac پر:</strong> لنک پیسٹ کریں، Download Video پر کلک کریں اور مطلوبہ فارمیٹ منتخب کریں، فائل براؤزر کے ڈاؤن لوڈز میں محفوظ ہو جائے گی۔',
        'priv_h3': 'کیا پرائیویٹ فیس بک ویڈیوز ڈاؤن لوڈ کی جا سکتی ہیں؟',
        'priv_p': 'نہیں۔ یہ ٹول صرف وہی ویڈیوز ڈاؤن لوڈ کرتا ہے جو بغیر لاگ ان کے کوئی بھی دیکھ سکتا ہے۔ فرینڈز اونلی یا خفیہ گروپس کی ویڈیوز نہیں نکالی جا سکتیں، اور ہم کبھی آپ کا پاس ورڈ نہیں مانگتے۔',
        'qual_h3': 'فیس بک ویڈیو کوالٹی: آپ کو حقیقت میں کیا ملتا ہے',
        'qual_p': 'فیس بک ہر ویڈیو کو مختلف کوالٹیز میں رکھتا ہے۔ <strong>Video (HD)</strong> سب سے بہترین کوالٹی فراہم کرتا ہے جبکہ <strong>Video (Normal)</strong> کم انٹرنیٹ اسپیڈ کے لیے چھوٹی فائل ہوتی ہے۔ جو ویڈیو جس کوالٹی میں اپ لوڈ ہوئی ہو وہی اس کی آخری حد ہوتی ہے۔',
        'mp3_h3': 'فیس بک ویڈیو کو MP3 آڈیو میں تبدیل کریں',
        'mp3_p': 'اگر آپ کو کسی نعت، انٹرویو، تقریر یا گانے کی صرف آڈیو چاہیے تو 192 kbps کے لیے <strong>Audio (HQ MP3)</strong> یا 128 kbps کے لیے <strong>Audio (Normal MP3)</strong> منتخب کریں۔ ڈاؤن لوڈ کے ساتھ ہی آڈیو خود بخود تیار ہو جاتی ہے۔',
        'trouble_h3': 'فیس بک ویڈیو ڈاؤن لوڈ نہ ہونے کی ممکنہ وجوہات',
        'trouble_headers': ['علامت', 'ممکنہ وجہ', 'حل'],
        'trouble_rows': [
            ('"Could not extract video"', 'ویڈیو پرائیویٹ، فرینڈز اونلی ہے یا ڈیلیٹ ہو چکی ہے', 'لنک کو پرائیویٹ/انکوگنیٹو ونڈو میں کھول کر دیکھیں۔ اگر وہاں نہیں چلتی تو ڈاؤن لوڈ نہیں ہو سکتی'),
            ('پیسٹ کرنے کے بعد کچھ نہیں ہوتا', 'لنک ویڈیو کا نہیں بلکہ کسی پروفائل یا پوسٹ کا ہے', 'ویڈیو کو چلا کر اس کے Share بٹن سے لنک کاپی کریں'),
            ('لائیو ویڈیو ڈاؤن لوڈ نہیں ہو رہی', 'لائیو نشریات ابھی جاری ہے', 'لائیو مکمل ہونے اور باقاعدہ ویڈیو بننے کا انتظار کریں'),
            ('اسٹوری ڈاؤن لوڈ نہیں ہو رہی', 'اسٹوری کا 24 گھنٹے کا وقت ختم ہو چکا ہے یا پرائیویٹ ہے', 'اسٹوری کے لائیو رہنے کے دوران دوبارہ کوشش کریں'),
            ('لاگ ان کی ضرورت مانگ رہا ہے', 'مواد دیکھنے کے لیے اکاؤنٹ ضروری ہے', 'صرف مکمل پبلک ویڈیوز ہی ڈاؤن لوڈ ہو سکتی ہیں'),
            ('بہت سست یا رک گیا ہے', 'فائل بڑی ہے یا انٹرنیٹ کمزور ہے', 'Video (Normal) آزمائیں یا تیز وائی فائی سے منسلک ہوں')
        ],
        'use_h3': 'لوگ فیس بک ویڈیوز کیوں محفوظ کرتے ہیں؟',
        'use_items': [
            'اپنی <strong>ذاتی</strong> فیملی ویڈیوز، یادیں اور تقاریب ضائع ہونے سے بچانا۔',
            'سفر کے دوران بنا انٹرنیٹ تعلیمی اور کھانا پکانے کی ویڈیوز دیکھنا۔',
            'اجازت کے ساتھ واٹس ایپ پر دوستوں کے ساتھ ویڈیوز شیئر کرنا۔',
            'کسی اہم بیان یا گانے کی آڈیو نکال کر بعد میں سننا۔'
        ],
        'safe_h3': 'کیا فیس بک ویڈیوز ڈاؤن لوڈ کرنا محفوظ اور قانونی ہے؟',
        'safe_p': '<strong>محفوظ:</strong> کوئی پاس ورڈ یا سافٹ ویئر درکار نہیں ہے۔ <strong>قانونی:</strong> ذاتی استعمال کے لیے پبلک ویڈیو محفوظ کرنا عام بات ہے تاہم کاپی رائٹ حقوق تخلیق کار کے پاس رہتے ہیں۔ downsocial کا میٹا پلیٹ فارمز سے کوئی تعلق نہیں ہے۔',
        'tips_h3': 'بہترین نتائج کے لیے مفید تجاویز',
        'tips_items': [
            'لنک ہمیشہ ویڈیو کے اپنے <em>Share</em> مینو سے کاپی کریں۔',
            'بڑی اسکرین یا ٹی وی پر دیکھنے کے لیے <strong>Video (HD)</strong> استعمال کریں۔',
            'موبائل ڈیٹا بچانے کے لیے <strong>Video (Normal)</strong> یا MP3 منتخب کریں۔',
            'خرابی کی صورت میں پہلے لنک کو پرائیویٹ ونڈو میں چلا کر دیکھیں۔'
        ],
        'sister_h3': 'کیا آپ کو دیگر پلیٹ فارمز کے لیے ٹولز چاہئیں؟',
        'sister_p': 'ہم <a href="../instagram-downloader/">Instagram</a>, <a href="../tiktok-downloader/">TikTok</a>, <a href="../youtube-downloader/">YouTube</a>, <a href="../snapchat-downloader/">Snapchat</a> اور <a href="../threads-downloader/">Threads</a> کے لیے خصوصی ٹولز کے ساتھ <a href="../index.html">آل ان ون ڈاؤنلوڈر</a> بھی پیش کرتے ہیں۔',
        'last_updated': 'آخری اپ ڈیٹ: 2 اکتوبر 2026۔ کوئی سوال یا مسئلہ ہے؟ <a href="contact.html">سپورٹ سے رابطہ کریں</a>۔'
    }
}

code = '''# scratch/seo_data_facebook.py
# Complete 12-language Facebook SEO Article data
import os

FACEBOOK_DATA = ''' + repr(FACEBOOK_TRANSLATIONS) + '''

def get_facebook_seo(lang):
    if lang == 'en':
        path = os.path.join(os.path.dirname(__file__), 'orig_seo_facebook.html')
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    
    d = FACEBOOK_DATA.get(lang, FACEBOOK_DATA['es'])
    
    t1_th = "".join(f"<th>{h}</th>" for h in d['t1_headers'])
    t1_tr = "".join(f"<tr><td>{r[0]}</td><td>{r[1]}</td></tr>" for r in d['t1_rows'])
    
    t2_th = "".join(f"<th>{h}</th>" for h in d['t2_headers'])
    t2_tr = "".join(f"<tr><td>{r[0]}</td><td>{r[1]}</td><td>{r[2]}</td></tr>" for r in d['t2_rows'])
    
    copy_li = "".join(f"<li>{item}</li>" for item in d['copy_items'])
    
    trb_th = "".join(f"<th>{h}</th>" for h in d['trouble_headers'])
    trb_tr = "".join(f"<tr><td>{r[0]}</td><td>{r[1]}</td><td>{r[2]}</td></tr>" for r in d['trouble_rows'])
    
    use_li = "".join(f"<li>{item}</li>" for item in d['use_items'])
    tips_li = "".join(f"<li>{item}</li>" for item in d['tips_items'])
    
    html = f"""<article class="seo-article" id="guide">
    <h2 id="overview">{d['h2']}</h2>
    <p class="pro-tip quick-answer"><strong>{d['qa_title']}:</strong> {d['qa_text']}</p>
    <p>{d['intro']}</p>
    
    <h3 id="at-a-glance">{d['t1_h3']}</h3>
    <div class="seo-table-container">
        <table class="seo-table">
            <thead>
                <tr>{t1_th}</tr>
            </thead>
            <tbody>
                {t1_tr}
            </tbody>
        </table>
    </div>

    <h3 id="supported-links">{d['t2_h3']}</h3>
    <p>{d['t2_intro']}</p>
    <div class="seo-table-container">
        <table class="seo-table">
            <thead>
                <tr>{t2_th}</tr>
            </thead>
            <tbody>
                {t2_tr}
            </tbody>
        </table>
    </div>

    <h3 id="how-to-copy">{d['copy_h3']}</h3>
    <ul>
        {copy_li}
    </ul>

    <h3 id="device-instructions">{d['device_h3']}</h3>
    <p>{d['ios']}</p>
    <p>{d['android']}</p>
    <p>{d['pc']}</p>

    <h3 id="private-videos">{d['priv_h3']}</h3>
    <p>{d['priv_p']}</p>

    <h3 id="video-quality">{d['qual_h3']}</h3>
    <p>{d['qual_p']}</p>

    <h3 id="mp3-audio">{d['mp3_h3']}</h3>
    <p>{d['mp3_p']}</p>

    <h3 id="troubleshooting">{d['trouble_h3']}</h3>
    <div class="seo-table-container">
        <table class="seo-table">
            <thead>
                <tr>{trb_th}</tr>
            </thead>
            <tbody>
                {trb_tr}
            </tbody>
        </table>
    </div>

    <h3 id="use-cases">{d['use_h3']}</h3>
    <ul>
        {use_li}
    </ul>

    <h3 id="safety-legal">{d['safe_h3']}</h3>
    <p>{d['safe_p']}</p>

    <h3 id="tips">{d['tips_h3']}</h3>
    <ul>
        {tips_li}
    </ul>

    <h3 id="sister-tools">{d['sister_h3']}</h3>
    <p>{d['sister_p']}</p>

    <p><small>{d['last_updated']}</small></p>
</article>"""
    return html
'''

target_path = os.path.join(os.path.dirname(__file__), 'seo_data_facebook.py')
with open(target_path, 'w', encoding='utf-8') as f:
    f.write(code)
print("Wrote seo_data_facebook.py successfully!")
