# Данный блок проверяет наличие данного контакта по телефону.
# Если находит соответствие.Выводит на экран найденный контакт из словаря.
# Далее пользователю предлагается выбор, перезаписать имеющийся контакт или нет.
# В случае положительного ответа, на место контакта с номером идентичным
# номеру нового контакта, записываются все данные нового контатка.
# Старые данные контакта удаляются.


from search_data import search_person as sp


def out_red(text):
    print("\033[31m {}" .format(text))


def out_white(text):
    print("\033[37m {}" .format(text))


def check_new_contact(data, new_contact):
    sv = new_contact['Телефон']
    sc = 'Телефон'
    nc = new_contact
    result_search = sp(data, sc, sv)
    if result_search:
        out_red('\nЭтот контакт уже присутствует в телефонной книге.')
        out_white('')
        user_select = input('Перезаписать его? да/нет : ')
        if user_select.lower == 'да' or 'yes' or 'y':
            return [data[i] if data[i][sc] != sv else nc \
                    for i in range(len(data))]
    else:
        return False
