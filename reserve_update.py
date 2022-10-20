# Данный блок автоматически перезаписывает файл резервной копии базы данных,\
#  после выхода пользователя из программы.


def reserve_data(dat, path):
    with open(path, 'w', encoding='utf-8') as data:
        for j in dat:
            for keys, values in j.items():
                data.write(f'{keys} :\t{values}\n')
            data.write('\n')
