# Config for part 1

OTHER_FOLDER = "other"
FOLDERS_DATA = {
        "archives": ('ZIP', 'GZ', 'TAR'),
        "video": ('AVI', 'MP4', 'MOV', 'MKV'),
        "audio": ('MP3', 'OGG', 'WAV', 'AMR'),
        "documents": ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX', 'CSV', 'XLS'),
        "images": ('JPEG', 'PNG', 'JPG', 'SVG'),
        OTHER_FOLDER: ()
    }
CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
TRANS = {}

for c, l in zip(list(CYRILLIC_SYMBOLS), TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()

# Helpers for part 1

def normalize(text):
    trans_str = ''

    for ch in text:
        tr_ch = '_'
        if ch.isalnum():
            tr_ch = ch.translate(TRANS)
        trans_str += tr_ch
    
    return trans_str