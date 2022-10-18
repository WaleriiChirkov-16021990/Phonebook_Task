# Данный блок проверяет наличие данного контакта по телефону.
# # Если находит соответствие.Выводит на экран найденный контакт из словаря и предлагает его перезаписать.


from search_data import search_person as sp

# data = [{'Имя': 'Виктор', 'Фамилия': 'Эррасти', 'Телефон': '89692112137', 'Описание': 'мобильный'},\
#      {'Имя': 'Анна', 'Фамилия': 'Симаненкова', 'Телефон': '89999999999', 'Описание': 'мобильный'},\
#          {'Имя': 'Вия', 'Фамилия': 'Эррасти', 'Телефон': '89692112137', 'Описание': 'мобильный'},\
#              {'Имя': 'Анна', 'Фамилия': 'Симаненкова', 'Телефон': '89999999999', 'Описание': 'мобильный'}, \
#                 {'Имя': 'Валерий', 'Фамилия': 'Чирков', 'Телефон': '89001001010', 'Описание': 'рабочий'}]

# con = {'Имя': 'Михаил', 'Фамилия': 'Гаврилов', 'Телефон': '89001001010', 'Описание': 'мобильный'}

def check_new_contact(data, new_contact):
    search_value = new_contact['Телефон']
    search_canon = 'Телефон'
    result_search = sp(data, search_canon, search_value)
    if result_search:
        print(result_search)
        print('Этот контакт уже присутствует в телефонной книге.')
        # user_select = input('Перезаписать его? да/нет : ')
        # if user_select.lower == 'да' or 'yes' or 'y':
        #     before_con = int(result_search.get(key[ default]))
        #     data.pop(before_con)
        #     # del data[result_search.keys()]
        #     data.append(new_contact)
        return True
    else:
        return False

# print(type(check_new_contact(data, con)))



