print("Добро пожаловать в интерактивное меню телефонного справочника!\n"
      "Пожалуйста, воспользуйтесь меню для дальнейшей работы.")


def check_user_click(user_click_input):
    while not user_click_input.isdigit():
        print("Вы ввели не число")
        user_click_input = int(input("Пожалуйста введите номер пункта меню: "))
        return user_click_input


def phonebook_interface():

        print('\nГлавное меню')
        print('1. Просмотр записей')
        print('2. Добавить запись')
        print('3. Экспорт данных')
        print('4. Импортировать данные')
        print('5. Поиск записи')
        print('6. Удаление записи')
        print('7. Завершение работы')
        user_click = check_user_click((input("\nВыберите пункт меню: ")))

phonebook_interface()