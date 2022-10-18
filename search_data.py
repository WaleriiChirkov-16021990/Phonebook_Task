from phonebook_logger import logger_action as log_act

log_path = 'log.txt'


def delete_person(dict_list: list, search_canon, search_value):
    user_click = int(input("Введите номер записи которую хотите удалить. Для выхода в главное меню "
                           "введите '0' "))
    if user_click == 0:
        return True
    try:
        dict_list.pop(user_click - 1)
        log_act(f'Пользователь удалил контакт с критерием:{search_canon} и значением {search_value}')
        print("Запись успешно удалена")
        return dict_list
    except IndexError:
        log_act(f'Пользователь пытался удалить контакт с критерием:{search_canon} и значением {search_value}')
        print("Такой записи не существует")


def search_person(dict_list: list, search_canon, search_value):
    if_correct = False
    count = 1  # в таблицах нумерация начинается с единицы обычно
    for j in dict_list:
        count += 1
        if j[search_canon] == search_value:
            print(count - 1, j)
            if_correct = True
    if not if_correct:
        print("Значение не найдено")
    return if_correct


def search_interactive_menu():
    print("Вы в меню поиска")
    print("1. Поиск по имени")
    print("2. Поиск по фамилии")
    print("3. Поиск по номеру телефона")
    print("4. Поиск по описанию\n")
    user_click = input("Выберите критерий поиска указав номер пункта: ")
    return user_click


def search_menu_click(user_click):
    if user_click == 1:
        search_canon = "Имя"
        search_value = input("Введите имя для поиска: ")
        return search_canon, search_value
    elif user_click == 2:
        search_canon = "Фамилия"
        search_value = input("Введите фамилию для поиска: ")
        return search_canon, search_value
    elif user_click == 3:
        search_canon = "Телефон"
        search_value = input("Введите номер телефона для поиска: ")
        return search_canon, search_value
    elif user_click == 4:
        search_canon = "Описание"
        search_value = input("Введите описание для поиска: ")
        return search_canon, search_value
