# Данный блок экспортирует все данные получанные в виде списка(словарей)\
#      и записывает их в указанный пользователем файл в виде строк,\
#          вставляя между каждым контактом пустую строку.

from color_out_text import out_white as white
from color_out_text import out_blue as blue


def export_data(dates, path):
    with open(path, 'w', encoding='utf-8') as data:
        for i in dates:
            for keys, values in i.items():
                data.write(f'{keys}' f'\t{values}\n')
            data.write('\n')
    blue(f'\nСправочник успешно экспортирован в файл: {path}!\n')
    white('')
