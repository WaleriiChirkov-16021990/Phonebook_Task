# При вызове этого блока вызывается окно интерфейса, которое предлагает ввести\
#  все данные нового контакта. После отправки последнего параметра, новый\
# контакт отображается в командной строке и записывается в телефонную книгу.\
#  Далее программа возвращает пользователя в интерфейс главного меню,\
#  для выбора дальнейших операций.

from import_csv import check_char as check
from color_out_text import out_white as white
from color_out_text import out_red as red
from color_out_text import out_yellow as yellow
import re

path = 'records_db.txt'


def check_chars(x):
    reg = re.search(r'\D{2,20} \D{2,20} \d{3,11} \D{2,20}', x)
    return True if reg else False


def add_new_contact():
    count = 5
    data_inp = None
    while True:
        if count > 0:
            print('Имя: \nФамилия: \nТелефон: \nОписание: \n')
            data_inp = input(\
                'Введите данные нового контакта через пробел\
                    \n: ').strip()
            try:
                if check_chars(data_inp):
                    data_inp = data_inp.split()
                    break
                else:
                    raise ValueError
            except ValueError:
                yellow('\nВы ввели не корректные данные.\
                    \nВведите данные согласно порядку указанному выше через пробел '
                       '(4 параметра включая номер из 3+ цифр).  ')
                count -= 1
                print(f'Осталось попыток: {count} .\n')
                white('')
                continue
        else:
            red('\nИсчерпано количество попыток ввода!\n')
            white('')
            return False
    print('\nСоздан новый контакт.\n\n')

    dicts_contact = {'Имя': data_inp[0], 'Фамилия': data_inp[1], 'Телефон': data_inp[2], 'Описание': data_inp[3]}
    for keys, values in dicts_contact.items():
        print(f'{keys}: \t{values}')

def record_data(path, contact):
    with open(path, 'a', encoding='utf-8') as data:
        if check_file(path):
            data.write(f'\n{contact} \n')
        else:
            data.write(f'\n{contact}\n')


def check_file(path):
    with open(path, 'r', encoding='utf-8') as data:
        if data.readline():
            return data.readline()
        else:
            return False


def rec_new_contact(data: dict, path: str):
    if path:
        new_contact = '\n'.join('{} : {}'.format(key, value) \
                                for key, value in data.items())
        record_data(path, new_contact)
        return True
    else:
        return False


