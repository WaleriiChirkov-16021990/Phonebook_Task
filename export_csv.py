# Блок импортирует базу в указанный файл csv.

import csv
from color_out_text import out_white as white
from color_out_text import out_blue as blue


def export_csv(sorce_dict, path):
    with open(path, 'a', encoding='utf8', newline='') as csvfile:
        fieldnames = ['Имя', 'Фамилия', 'Телефон', 'Описание']
        writer = csv.DictWriter(csvfile, delimiter=',', fieldnames=fieldnames,  dialect='excel')
        writer.writeheader()
        for i in sorce_dict:
            writer.writerow(i)
    blue(f'\nСправочник успешно экспортирован в файл: {path}!\n')

    white('')
