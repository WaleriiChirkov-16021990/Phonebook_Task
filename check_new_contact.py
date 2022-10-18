# Данный блок проверяет наличие данного контакта по телефону.
# # Если находит соответствие.Выводит на экран найденный контакт из словаря.


from search_data import search_person as sp


def out_red(text):
    print("\033[31m {}" .format(text))


def out_white(text):
    print("\033[37m {}" .format(text))


def check_new_contact(data, new_contact):
    search_value = new_contact['Телефон']
    search_canon = 'Телефон'
    result_search = sp(data, search_canon, search_value)
    if result_search:
        out_red('\nЭтот контакт уже присутствует в телефонной книге.')
        out_white('')
        return True
    else:
        return False
