# Данный блок выводит на экран текущую базу данных.


from color_out_text import out_white as white
from color_out_text import out_yellow as yellow


def view_records(dict_list_: list):
    for i in dict_list_:
        for key, value in i.items():
            print(f'{key} : {value}')
        print()
    yellow('Отображено текущее состояние базы.')
    white('')