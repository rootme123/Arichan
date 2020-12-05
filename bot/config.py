class config:
    BOT_TOKEN = "1406139538:AAEP94o1m4ymJ-PHIyY7wXGGVXTpZJQnDAE"
    APP_ID = "2712048"
    API_HASH = "f7c49b6b1b6648252a5437bd86d6bf22"
    DATABASE_URL = "postgres://intifjlrzxdutl:906a12573f5bd9c58e11d2577c8cb6519c51b0cfcbae10ebd72a0097669cad96@ec2-52-22-238-188.compute-1.amazonaws.com:5432/d8ig9k62hhrj7b"
    SUDO_USERS = "811179153" # Sepearted by space.
    SUPPORT_CHAT_LINK = "https://t.me/joinchat/AAAAAE_9_4OkoTkfQBcQCw"
    DOWNLOAD_DIRECTORY = "./downloads/"


class BotCommands:
  Download = ['download', 'dl']
  Authorize = ['auth', 'authorize']
  SetFolder = ['setfolder', 'setfl']
  Revoke = ['revoke']
  Clone = ['copy', 'clone']
  Delete = ['delete', 'del']
  EmptyTrash = ['emptyTrash']
  Ytdl = ['ytdl']

class Messages:
    START_MSG = "**Hi Kakak {}.**\n__Aku Miku-chan.kakak dapat menggunakan aku untuk mengunggah file / video apa pun ke Google Drive dari tautan langsung atau File Telegram.__\n__You can know more from /help.__"

    HELP_MSG = [
        ".",
        "**Google Drive Uploader**\n__Aku dapat mengunggah file dari tautan langsung atau File Telegram ke Google Drive Kakak. Yang aku butuhkan hanyalah mengautentikasi aku ke Akun Google Drive kakak dan mengirim tautan unduhan langsung atau File Telegram.__\n\nAku punya bayak fitur lho kak hehehe... ! kakak pengen tahu ? Ikuti saja tutorial ini dan baca pesannya dengan cermat ya kak :) .",
        
        f"**Authenticating Google Drive**\n__Kirimkan aku /{BotCommands.Authorize[0]} perintah dan kakak akan menerima URL, kunjungi URL dan ikuti langkah-langkahnya dan kirim kode yang kakak terima di sini. Use /{BotCommands.Revoke[0]} untuk mencabut/membatalkan otentikasi Akun Google Drive kakak saat ini.__\n\n**Catatan: Aku tidak akan mendengarkan perintah atau pesan apa pun (except /{BotCommands.Authorize[0]} command) sampai kakak mengizinkan aku terhubung huhu.\nSo, Authorization itu wajib kakak huhuhu**",
        
        f"**Direct Links**\n__Kirimkan Aku tautan unduhan langsung untuk sebuah file dan Aku akan mengunduhnya di server punyaku dan Mengunggahnya langsung ke Akun Google Drive kakak :). Kakak dapat mengganti nama file kakak sebelum mengunggahnya ke Akun GDrive kakak. Kirimkan saja Aku URL dan nama file baru kakak yang dipisahkan oleh ' | '.__\n\n**__Examples:__**\n```https://contoh.com/AFileWithDirectDownloadLink.mkv | New FileName.mkv```\n\n**Telegram Files**\n__Untuk Mengunggah file telegram di Akun Google Drive Kakak, kirimkan saja file itu kepadaku dan aku akan mengunduh dan mengunggahnya langsung ke Akun Google Drive Kakak hehe. Catatan: Pengunduhan File Telegram mungkin akan lambat huhuhu. mungkin perlu waktu lebih lama untuk file besar.__\n\n**YouTube-DL Support**\n__Download files via youtube-dl.\nUse /{BotCommands.Ytdl[0]} (YouTube Link/YouTube-DL Supported site link)__",
        
        f"**Custom Folder for Upload**\n__Kakak ingin mengunggah file di folder khusus atau di__ **TeamDrive/SharedDrive** __ ?\nGunakan /{BotCommands.SetFolder[0]} (Folder URL) untuk mengatur folder unggahan khusus/kustom.\nSemua file diunggah di folder khusus/kustom yang kakak berikan.__",
        
        f"**Delete Google Drive Files**\n__Hapus file google drive. Gunakan /{BotCommands.Delete[0]} (File/Folder URL) untuk menghapus file kakak.\nKakak juga dapat mengosongkan file sampah. Gunakan /{BotCommands.EmptyTrash[0]}\nCatatan: File kakak akan dihapus secara permanen. Proses ini tidak dapat dibatalkan huhuhu :( .\n\n**Copy Google Drive Files**\n__Ya, Gandakan(klon) atau Salin File Google Drive.\n__Gunakan /{BotCommands.Clone[0]} (File id / Folder id or URL) untuk menyalin File Google Drive di Akun Google Drive Kakak.__",
        
        "**Rules & Precautions**\n__1. Jangan salin File / Folder Google Drive dengan ukuran BESAR. Aku mungkin hang dan file kakak mungkin rusak.\n2. Kirim Satu permintaan kakak saja dalam satu waktu kecuali kakak pengen aku ngambek.\n3. Jangan kirim tautan/link yang mungkin lambat, @transload dulu ya kak :) .\n4. Jangan menyalahgunakan atau membebani layanan gratis dari aku ini ya kak, kalo gak aku bakalan ngambek huft.__",
        
        # Dont remove this ↓ if you respect developer.
        "**Di Design ulang oleh @touchme_1911**"
        ]
     
    RATE_LIMIT_EXCEEDED_MESSAGE = "❗ **Batas Terlampaui.**\n__Coba lagi setelah setelah 24 jam ya kak, aku ngambek soalnya.__"
    
    FILE_NOT_FOUND_MESSAGE = "❗ **File/Folder tidak ketemu huft.**\n__File id - {} tidak ketemu huft. Tolong periksa lagi it\'u ada dan dapat diakses oleh akun yang sudah kakak Login-kan.__"
    
    INVALID_GDRIVE_URL = "❗ **Google Drive URL nya Invalid kakak :( .**\nPastikan Google Drive URL-nya dalam format yang valid ya kak :( ."
    
    COPIED_SUCCESSFULLY = "✅ **Menyalin file kakak sukses, PUJI AKU LAGI KAK.**\n[{}]({}) __({})__"
    
    NOT_AUTH = f"🔑 **Kakak belum mengautentikasi aku untuk mengunggah ke akun mana pun.**\n__Kirim /{BotCommands.Authorize[0]} untuk authenticate.__"
    
    DOWNLOADED_SUCCESSFULLY = "📤 **Mengunggah File kakak hihihi...**\n**Filename:** ```{}```\n**Size:** ```{}```"
    
    UPLOADED_SUCCESSFULLY = "✅ **Berhasil Mengunggah, HOORAYYY, TOLONG PUJI AKU KAK MUEHEHEH.**\n[{}]({}) __({})__"
    
    DOWNLOAD_ERROR = "❗**Downloader Gagal huft, menyebalkan**\n{}\n__Link - {}__"
    
    DOWNLOADING = "📥 **Mengunduh File kakak hihihi...\nLink:** ```{}```"
    
    ALREADY_AUTH = "🔒 **YEAY, Aku Sudah terhubung dengan Akun Google Drive Kakak.**\n__Gunakan /revoke untuk mencabut/membatalkan hubungan dengan akun kakak saat ini.__\n__Kirimi Aku tautan langsung atau File untuk Diunggah di Google Drive kakak__"
    
    FLOW_IS_NONE = f"❗ **Invalid Kodenya kakak**\n__Run {BotCommands.Authorize[0]} first.__"
    
    AUTH_SUCCESSFULLY = '🔐 **Akun Google Drive berhasil terhubung denganku, HOORAYYY.**'
    
    INVALID_AUTH_CODE = '❗ **Invalid Kodenya kakak**\n__Kode yang kakak kirimkan tidak valid atau sudah pernah digunakan sebelumnya (sayang sekali). Buat yang baru ya kak hehehe__'
    
    AUTH_TEXT = "⛓️ **Untuk Menhubungkan akun Google Drive Kakak, kunjungi ini [URL]({}) dan kirim kode yang dihasilkan ke sini.**\n__Kunjungi URLnya > Allow permissions > kakak dapat kodenya > salin kodenya > Tempel disini ya kak__"
    
    DOWNLOAD_TG_FILE = "📥 **Mendownload File kakak UwU...**\n**Filename:** ```{}```\n**Size:** ```{}```\n**MimeType:** ```{}```"
    
    PARENT_SET_SUCCESS = '🆔✅ **Tautan Folder Kustom berhasil disetel.**\n__ID folder kustom Kakak - {}\nGunakan__ ```/{} clear``` __to clear it.__'
    
    PARENT_CLEAR_SUCCESS = f'🆔🚮 **Folder Khusus Berhasil Dihapus.**\n__Gunakan__ ```/{BotCommands.SetFolder[0]} (Folder Link)``` __to set it back__.'
    
    CURRENT_PARENT = "🆔 **ID Folder Kustom Kakak Saat Ini - {}**\n__Gunakan__ ```/{} (Folder link)``` __to change it.__"
    
    REVOKED = f"🔓 **Berhasil memutus huhungan dengan akun yang kakak saat ini, hmm MENYEBALKAN.**\n__Gunakan /{BotCommands.Authorize[0]} untuk mengautentikasi dan menggunakan Aku lagi UwU.__"
    
    NOT_FOLDER_LINK = "❗ **Tautan foldernya tidak valid kakkkkkk.**\n__Tautan yang kakak kirim bukan milik foldernya.__"
    
    CLONING = "🗂️ **Kloning ke Google Drive Kakak...**\n__G-Drive Link - {}__"
    
    PROVIDE_GDRIVE_URL = "**❗ Kakak Tolong berikan URL Google Drive yang valid bersama dengan perintah.**\n__Usage - /{} (GDrive Link)__"
    
    INSUFFICIENT_PERMISSONS = "❗ **Anda tidak memiliki cukup izin untuk file ini, sayang sekali.**\n__File id - {}__"
    
    DELETED_SUCCESSFULLY = "🗑️✅ **File Kakak berhasil dihapus, HOORAYY, PUJI AKU KAK.**\n__File kakak sudah dihapus secara permanen !\nFile id - {}__"
    
    WENT_WRONG = "⁉️ **ERROR: SEPERTINYA ADA YANG SALAH, KAKAK NGAPAIN ?.**\n__Tolong coba lagi nanti ya kak, aku ngambek.__"
    
    EMPTY_TRASH = "🗑️🚮**Mengosongkan tempat sampah sukses, PUJI AKU KAK !**"
    
    PROVIDE_YTDL_LINK = "❗**Provide a valid YouTube-DL supported link.**"
