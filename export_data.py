# Данный блок экспортирует все данные получанные в виде списка(словарей)\
#      и записывает их в указанный пользователем файл в виде строк,\
#          вставляя между каждым контактом пустую строку.


def export_data(dates, path):
    with open(path, 'w', encoding='utf-8') as data:
        for i in dates:
            for keys, values in i.items():
                data.write(f'{keys}' f'\t{values}\n')
            data.write('\n')
    print('Справочник успешно экспортирован!\n')



