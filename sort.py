# python sort.py D:/Dima/000/0
import os
import shutil
import re
import sys
from pathlib import Path


ext_images = ['JPEG', 'PNG', 'JPG', 'SVG']
ext_documents = ['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX']
ext_audio = ['MP3', 'OGG', 'WAV', 'AMR']
ext_video = ['AVI', 'MP4', 'MOV', 'MKV']
ext_archives = ['ZIP', 'GZ', 'TAR']

images = []
documents = []
audio = []
video = []
archives = []

extension_unknown = set()
extension_known = set()

folders_list = {'images': images, 'documents': documents,
                'audio': audio, 'video': video, 'archives': archives}
folders_ext = {'images': ext_images, 'documents': ext_documents,
               'audio': ext_audio, 'video': ext_video, 'archives': ext_archives}


CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
TRANS = {}

for arg in sys.argv:
    k = 9
    my_path0 = arg
my_path = arg
p0 = Path(my_path0)
if not p0.is_dir():
    print('Такой папки нет!\nЗапустите программу снова!\nНапример:\npython sort.py D:/Dima/000/0')
    exit()


for i in folders_list:
    p = Path(my_path0 + '/' + str(i))
    p.mkdir(mode=0o777, parents=False, exist_ok=True)


def normalize(tested_name):
    for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()
    tested_name = tested_name.translate(TRANS)
    norm_name = re.sub('[^\w]', '_', tested_name)
    return norm_name


def del_empty_dirs(my_path0):
    for d in os.listdir(my_path0):
        a = os.path.join(my_path0, d)
        if os.path.isdir(a):
            del_empty_dirs(a)
            if not os.listdir(a):
                os.rmdir(a)


def rename_folder(my_path0):
    p = Path(my_path0)
    for i in p.iterdir():
        name_string = str(i)
        if i.is_dir():
            if name_string in folders_list.keys():
                continue
            print(i, i.parent, i.name)
            norm = normalize(i.name)
            if i.name != norm:
                shutil.move(str(i), str(i.parent) + '/' + norm)
                rename_folder(str(i.parent) + '/' + norm)
            else:
                rename_folder(name_string)


def obxodFile(my_path, level=1):
    p = Path(my_path)
    for i in p.iterdir():
        k = 0
        name_string = str(i)
        if i.is_dir():
            if name_string in folders_list.keys():
                continue
            obxodFile(name_string)
        else:
            file_name = i.stem
            extension = i.name.split('.')[-1]
            flag_break = False
            for key, value in folders_ext.items():
                for ext in value:
                    if extension.upper() in value:
                        if key == 'images':
                            images.append(i.name)
                        elif key == 'documents':
                            documents.append(i.name)
                        elif key == 'audio':
                            audio.append(i.name)
                        elif key == 'video':
                            video.append(i.name)
                        elif key == 'archives':
                            archives.append(i.stem)
                        norm_name = normalize(file_name)
                        extension_known.add(extension.upper())
                        if key == 'archives':
                            arc_path = my_path0 + '/archives/' + norm_name
                            ppp = Path(arc_path)
                            ppp.mkdir(mode=0o777, parents=False, exist_ok=True)
                            shutil.unpack_archive(str(i), arc_path)
                            os.remove(str(i))

                        else:
                            shutil.move(str(i), my_path0 + '/' +
                                        key + '/' + norm_name + str(i.suffix))
                        flag_break = True
                        break
                if flag_break:
                    break
            else:
                extension_unknown.add(extension.upper())


obxodFile(my_path)
del_empty_dirs(my_path0)
rename_folder(my_path0)


print(
    f'Перечень всех известных скрипту расширений, которые встречаются в целевой папке:\n{extension_known}\n')
print(
    f'Перечень всех расширений, которые скрипту неизвестны:\n{extension_unknown}\n')
print(f'Список файлов папки images:\n{images}\n')
print(f'Список файлов папки documents:\n{documents}\n')
print(f'Список файлов папки audio:\n{audio}\n')
print(f'Список файлов папки video:\n{video}\n')
print(f'Список папок archives:\n{archives}\n')
