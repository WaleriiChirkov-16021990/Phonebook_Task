# Данный блок автоматически перезаписывает файл резервной копии базы данных,\
#  после выхода пользователя из программы.


def reserve_data(dat, path):
    with open(path, 'w', encoding='utf-8') as data:
        for i in dat:
            data.write(f'{i}\n')
