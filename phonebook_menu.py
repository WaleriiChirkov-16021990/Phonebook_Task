from re import U
from phonebook_view_records import view_records as vrf
from add_new_contact import add_new_contact as anc
from add_new_contact import rec_new_contact as rnc
from phonebook_logger import logger_action as log_act
from reserve_update import reserve_data as rd
from export_data import export_data as ed
from import_data import import_data as id
from search_data import search_person as sp
from search_data import delete_person as dp
from check_new_contact import check_new_contact as check
from search_data import search_interactive_menu as sim
from search_data import search_menu_click as smc
from export_csv import export_csv as ec
from import_csv import import_data as idc
from view_current_data import view_records as vr


path = 'records_db.txt'
reserve_copy_path = 'reserve_copy.txt'
export_path = 'export_data.txt'
import_path = 'export_data.txt'
import_path_csv = 'export.csv'


def check_user_click(user_click_input):
    while not user_click_input.isdigit():
        print("Вы ввели не число")
        user_click_input = input("Пожалуйста введите номер пункта меню: ")
    return int(user_click_input)


def phonebook_interface():
    global dict_list
    dict_list = id(path)
    print("Добро пожаловать в интерактивное меню телефонного справочника!")
    print('Пожалуйста, воспользуйтесь меню для дальнейшей работы.')
    while True:
        log_act(f'зашел в главное меню')
        print('\nГлавное меню')
        print('1. Просмотр записей')
        print('2. Добавить запись')
        print('3. Экспорт данных')
        print('4. Импорт данных')
        print('5. Поиск записи')
        print('6. Удаление записи')
        print('7. Предварительный просмотре базы из файла')
        print('8. Завершение работы')
        user_click = check_user_click((input("\nВыберите пункт меню: ")))
        if user_click == 1:
            log_act(f'просматривал записи')
            print("В базе есть следующие записи: \n")
            vr(dict_list)
        elif user_click == 2:
            dic_cont = anc()
            if not check(dict_list, dic_cont):
                rnc(dic_cont, path)
                log_act(f'добавил контакт:{dic_cont.get("Фамилия")}')
                dict_list.append(dic_cont)
            else:
                dict_list = check(dict_list, dic)
            print(dict_list)
        elif user_click == 3:
            print('1.Экспорт в .csv')
            print('2.Экспорт в .txt')
            user_click = check_user_click(input('Введите пункт меню: '))
            if user_click == 1:
                log_act(f'экспортировал данные')
                ec(dict_list)
            if user_click == 2:
                log_act(f'экспортировал данные')
                ed(dict_list, export_path)

        elif user_click == 4:
            print('1.Импорт в .csv')
            print('2.Импорт в .txt')
            user_click = check_user_click(input('Введите пункт меню: '))
            if user_click == 1:
                dict_list = idc(import_path_csv)
                log_act(f'импортировал данные')
            elif user_click == 2:
                dict_list = id(import_path)
                log_act(f'импортировал данные')
            print(dict_list)

        elif user_click == 5:
            user_click = check_user_click(sim())
            user_search_canon, user_search_value = smc(user_click)
            log_act(f'искал контакт с {user_search_canon}:{user_search_value}')
            sp(dict_list, user_search_canon, user_search_value)
        elif user_click == 6:
            user_click = check_user_click(sim())
            user_search_canon, user_search_value = smc(user_click)
            if sp(dict_list, user_search_canon, user_search_value):
                dp(dict_list, user_search_canon, user_search_value)
            else:
                log_act(f'хотел удалить контакт с критерием:{user_search_canon} '
                        f' и значением: {user_search_value}')
        elif user_click == 7:
            print(f'На данный момент в базу присутствуют следущие файлы \
                \n1.{path} \n2.{reserve_copy_path} \n3.{export_path}\
                 \n4.{import_path} \n5.{import_path_csv}')
            user_selec = input('Если хотите открыть файл из списка,\
                \nможно ввести соответствующий номер или введите \
                \nимя любого существующего файла \
                \nв формате "name.txt" или "name.csv": ').strip()
            path_view = None
            if user_selec.isdigit():
                if user_selec == '1':
                    path_view = path
                elif user_selec == '2':
                    path_view = reserve_copy_path
                elif user_selec == '3':
                    path_view = export_path
                elif user_selec == '4':
                    path_view = import_path
                elif user_selec == '5':
                    path_view = import_path_csv
            else:
                path_view = user_selec
            print(path_view)
            print("В базе есть следующие записи: \n")
            vrf(path_view)
            log_act(f'Предпросматривал записи в файле: {path_view}')
        elif user_click == 8:
            rd(dict_list, path)
            rd(dict_list, reserve_copy_path)
            log_act(f'вышел из программы')
            print("До свидания!")
            break
        else:
            print("Такого пункта нет.\nВведите цифру из меню.")


phonebook_interface()
