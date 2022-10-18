# Данный блок проверяет наличие данного контакта по телефону.
# # Если находит соответствие.Выводит на экран найденный контакт из словаря и предлагает его перезаписать.


from search_data import search_person as sp

def check_new_contact(data, new_contact):
    search_value = new_contact['Телефон']
    search_canon = 'Телефон'
    result_search = sp(data, search_canon, search_value)
    if result_search:
        print('Этот контакт уже присутствует в телефонной книге.')
        print(sp(data, search_canon, search_value))
        user_select = input('Перезаписать его? да/нет : ')
        if user_select.lower == 'да' or 'yes' or 'y':
            data[sp(data, search_canon, search_value)] = new_contact
        return data
    else:
        return False



