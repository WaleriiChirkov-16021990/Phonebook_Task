# Данный блок выводит на экран телефонный справочник из переданного файла.

from color_out_text import out_white as white
from color_out_text import out_yellow as yellow


def view_records(path):
    with open(path, 'r', encoding='utf-8') as file:
        records = file.readlines()
    for i in records:
        print(i[:len(i)-1])
    yellow(f'\nСправочник прочитан в файле: {path}!\n Но не экспортирован!')
    white('')
