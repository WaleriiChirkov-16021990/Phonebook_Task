import csv

def export_csv(sorce_dict, path):
    with open('export.csv', 'w', encoding='utf8', newline='') as csvfile:
        fieldnames = ['Имя', 'Фамилия', 'Телефон', 'Описание']
        writer = csv.DictWriter(csvfile, delimiter=',', fieldnames=fieldnames,  dialect='excel')
        writer.writeheader()
        for i in sorce_dict:
            writer.writerow(i)
    print('Справочник успешно экспортирован!\n')

