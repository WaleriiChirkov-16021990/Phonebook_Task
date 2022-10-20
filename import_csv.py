import csv
import re
from color_out_text import out_blue as blue
from color_out_text import out_white as white

# Блок считывает файл csv, и создает список контактов \
# где каждый элемент списка это словарь каждого контакта.

# Метод проверяет что в строке есть номер телефона и возвращает тру или
def check_char(x):
    reg = re.search(r'\D\d{5,11}\D+$', x)
    return True if reg else False


def import_data(path):
    lines = None
    from_file = None
    read_lst_dct = []
    with open(path, 'r',encoding='utf-8', newline='') as csvfile:
        file_reader = list(csv.reader(csvfile, delimiter=','))
        from_file = [i for i in file_reader if check_char(''.join(i))]
        lines = [i for i in from_file if i]
        for list_ in lines:
            tmp_dct = {'Имя': "", 'Фамилия': "", 'Телефон': "", 'Описание': ""}
            tmp_dct['Имя'] = list_[0]
            tmp_dct['Фамилия'] = list_[1]
            tmp_dct['Телефон'] = list_[2]
            tmp_dct['Описание'] = list_[3]
            read_lst_dct.append(tmp_dct)
        blue(f'\nСправочник успешно импортирован из файла: {path}!\n')
        white('')
        return read_lst_dct
