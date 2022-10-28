# Данный блок выводит на экран текущую базу данных.


from color_out_text import out_white as white
from color_out_text import out_yellow as yellow


def view_records(dict_list_: list):
    result = []
    for i in dict_list_:
        result.append(i)
        for key, value in i.items():
            print(f'{key} : {value}')
        print()
    yellow('Отображено текущее состояние базы.')
    white('')
    return result


def view_records_bot(dict_list):
    result = []
    strings = []
    for i in dict_list:
        strings.append('\n')
        for key, item in i.items():
            strings.append("{}: {}".format(key.capitalize(), item))
        result = "\n".join(strings)
    return result
