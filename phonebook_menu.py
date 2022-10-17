from phonebook_view_records import view_records as vr
from add_new_contact import add_new_contact as anc
from add_new_contact import rec_new_contact as rnc
from phonebook_logger import logger_action as log_act
from reserve_update import reserve_data as rd
from export_data import export_data as ed
from import_data import import_data as id
from search_data import search_person as sp
from search_data import delete_person as dp



dict_list = []
path = 'records_db.txt'
log_path = 'log.txt'
reserve_copy_path = 'reserve_copy.txt'
export_path = 'export_data.txt'
import_path = 'records_db.txt'


print("Добро пожаловать в интерактивное меню телефонного справочника!\n"
      "Пожалуйста, воспользуйтесь меню для дальнейшей работы.")


def check_user_click(user_click_input):
    while not user_click_input.isdigit():
        print("Вы ввели не число")
        user_click_input = input("Пожалуйста введите номер пункта меню: ")
    return int(user_click_input)


def phonebook_interface():
    global dict_list
    while True:
        print('\nГлавное меню')
        print('1. Просмотр записей')
        print('2. Добавить запись')
        print('3. Экспорт данных')
        print('4. Импорт данных')
        print('5. Поиск записи')
        print('6. Удаление записи')
        print('7. Завершение работы')
        print('8. Показать словарь') # для тестирования
        user_click = check_user_click((input("\nВыберите пункт меню: ")))
        if user_click == 1:
            print("В базе есть следующие записи: \n")
            vr()
        elif user_click == 2:
            dic_cont = anc()
            rnc(dic_cont, path)
            log_act(f'добавил контакт:{dic_cont.get("Фамилия")}', log_path)
            dict_list.append(dic_cont)
            print(dict_list)

        elif user_click == 3:
            ed(dict_list, export_path)

        elif user_click == 4:
            dict_list = id(import_path)
            print(dict_list)

        elif user_click == 5:
            print("Вы в меню поиска")
            print("1. Поиск по имени")
            print("2. Поиск по фамилии")
            print("3. Поиск по номеру телефона")
            print("4. Поиск по описанию\n")
            user_click = check_user_click(input("Выберите критерий поиска указав номер пункта: "))
            if user_click == 1:
                search_canon = "Имя"
                search_value = input("Введите имя для поиска: ")
                print(sp(dict_list, search_canon, search_value))
            elif user_click == 2:
                search_canon = "Фамилия"
                search_value = input("Введите фамилию для поиска: ")
                print(sp(dict_list, search_canon, search_value))
            elif user_click == 3:
                search_canon = "Телефон"
                search_value = input("Введите номер телефона для поиска: ")
                print(sp(dict_list, search_canon, search_value))
            elif user_click == 4:
                search_canon = "Описание"
                search_value = input("Введите описание для поиска: ")
                print(sp(dict_list, search_canon, search_value))
            else:
                print("Некорректный ввод. Возврат к главному меню.")
        elif user_click == 6:
            print("Вы в меню поиска")
            print("1. Поиск по имени")
            print("2. Поиск по фамилии")
            print("3. Поиск по номеру телефона")
            print("4. Поиск по описанию\n")
            user_click = check_user_click(input("Выберите критерий поиска указав номер пункта: "))
            if user_click == 1:
                search_canon = "Имя"
                search_value = input("Введите имя для поиска: ")
                sp(dict_list, search_canon, search_value)
                user_click = check_user_click(input("Введите номер записи которую хотите удалить. Для выхода в главное меню "
                                       "введите '-1' "))
                if user_click == -1:
                    continue
                else:
                    try:
                        dict_list.pop(user_click)
                        print("Запись успешно удалена")
                    except IndexError:
                        print("Такой записи не существует")
            elif user_click == 2:
                search_canon = "Фамилия"
                search_value = input("Введите фамилию для поиска: ")
                sp(dict_list, search_canon, search_value)
                user_click = check_user_click(input("Введите номер записи которую хотите удалить. Для выхода в главное меню "
                                       "введите '-1' "))
                if user_click == -1:
                    continue
                else:
                    try:
                        dict_list.pop(user_click)
                        print("Запись успешно удалена")
                    except IndexError:
                        print("Такой записи не существует")
            elif user_click == 3:
                search_canon = "Телефон"
                search_value = input("Введите номер телефона для поиска: ")
                sp(dict_list, search_canon, search_value)
                user_click = check_user_click(input("Введите номер записи которую хотите удалить. Для выхода в главное меню "
                                       "введите '-1' "))
                if user_click == -1:
                    continue
                else:
                    try:
                        dict_list.pop(user_click)
                        print("Запись успешно удалена")
                    except IndexError:
                        print("Такой записи не существует")
            elif user_click == 4:
                search_canon = "Описание"
                search_value = input("Введите описание для поиска: ")
                sp(dict_list, search_canon, search_value)
                user_click = int(input("Введите номер записи которую хотите удалить. Для выхода в главное меню "
                                       "введите '-1' "))
                if user_click == -1:
                    continue
                else:
                    try:
                        dict_list.pop(user_click)
                        print("Запись успешно удалена")
                    except IndexError:
                        print("Такой записи не существует")
            else:
                print("Некорректный ввод. Возврат к главному меню.")

        elif user_click == 7:
            rd(dic_cont, reserve_copy_path)
            print("До свидания!")

        elif user_click == 8:
            try:
                print(dict_list)
            except UnboundLocalError:
                print("Словарь пуст")
        else:
            print("Такого пункта нет.\nВведите цифру из меню.")


phonebook_interface()

