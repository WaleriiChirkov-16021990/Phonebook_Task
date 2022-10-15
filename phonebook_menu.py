from data_input import create_record as cr

print("Добро пожаловать в интерактивное меню телефонного справочника!\n"
      "Пожалуйста, воспользуйтесь меню для дальнейшей работы.")


def check_user_click(user_click_input):
    while not user_click_input.isdigit():
        print("Вы ввели не число")
        user_click_input = input("Пожалуйста введите номер пункта меню: ")
    return int(user_click_input)


def phonebook_interface():
    print('\nГлавное меню')
    print('1. Просмотр записей')
    print('2. Добавить запись')
    print('3. Экспорт данных')
    print('4. Импорт данных')
    print('5. Поиск записи')
    print('6. Удаление записи')
    print('7. Завершение работы')
    user_click = check_user_click((input("\nВыберите пункт меню: ")))
    if user_click == 1:
        return True

    elif user_click == 2:
        surname = input("Введите фамилию:")
        name = input("Введите имя: ")
        phone_number = input("Введите номер телефона: ")
        phone_info = input("Введите описание: ")
        cr(surname, name, phone_number, phone_info)

    elif user_click == 3:
        return True

    elif user_click == 4:
        return True

    elif user_click == 5:
        return True

    elif user_click == 6:
        return True

    elif user_click == 7:
        print("До свидания!")

    else:
        print("Такого пункта нет.\nВведите цифру из меню.")

phonebook_interface()
