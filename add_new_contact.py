# При вызове этого блока вызывается окно интерфейса, которое предлагает ввести\
#  все данные нового контакта. После отправки последнего параметра, новый\
# контакт отображается в командной строке и записывается в телефонную книгу.\
#  Далее программа возвращает пользователя в интерфейс главного меню,\
#  для выбора дальнейших операций.


path = 'records_db.txt'


def add_new_contact(a=None):
    print('Имя: \nФамилия: \nТелефон: \nОписание: \n')
    data_inp = input(
        'Введите данные нового контакта через пробел\n: ').split(' ')
    print('\nСоздан новый контакт.\n\n')
    if len(data_inp)== 3:
        data_inp.append('Пусто')
    dicts_contact = {'Имя': data_inp[0], 'Фамилия': data_inp[1], 'Телефон': data_inp[2], 'Описание': data_inp[3]}
    for keys, values in dicts_contact.items():
        print(f'{keys}: \t{values}')
    return dicts_contact


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


