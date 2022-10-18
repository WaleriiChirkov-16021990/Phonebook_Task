import csv
import os
# Блок считывает файл csv, и создает список контактов \
# где каждый элемент списка это словарь каждого контакта.


#path = 'exp_contacts.csv'
#path1 = r"C:\Users\Sergio\Desktop\Поездка в Минск\exp_contacts1.csv"


def import_data(path):
    lines = []
    from_file = []
    read_lst_dct = []

    with open(path, 'r', newline='') as csvfile:
        file_reader = csv.reader(csvfile, delimiter=',')
        for row in file_reader:
            from_file.append(row)
        del from_file[0]
        for i in from_file:
            if i:
                lines.append(i)
        for list_ in lines:
            tmp_dct = {'Имя': "", 'Фамилия': "", 'Телефон': "", 'Описание': ""}
            tmp_dct['Имя'] = list_[0]
            tmp_dct['Фамилия'] = list_[1]
            tmp_dct['Телефон'] = list_[2]
            tmp_dct['Описание'] = list_[3]
            read_lst_dct.append(tmp_dct)
        print(read_lst_dct)
        return read_lst_dct


while True:
    read_path = input('Введите путь к файлу: ')
    if os.path.exists(read_path):
        if os.path.isfile(read_path):
            import_data(read_path)
            break
    else:
        print('Введите корректный путь к файлу')

