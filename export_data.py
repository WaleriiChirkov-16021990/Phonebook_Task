import csv
from import_data import import_data as read_file

path = 'records_db.txt'
data_list = read_file(path)

def export_data_txt(dat):
    file_name = 'exp_contacts.txt'
    with open(file_name, 'w', encoding='utf-8') as data:
        for i in dat:
            for key, value in i.items():
                data.write(f'{key} : {value}\n')
            data.write('\n')



def export_data_csv(dct):
    with open('exp_contacts.csv', 'w') as csvfile:
        fieldnames = ['Имя', 'Фамилия', 'Телефон', 'Описание']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(dct)





