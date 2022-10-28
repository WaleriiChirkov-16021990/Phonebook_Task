import telebot.types
from telebot import TeleBot
from phonebook_logger import logger_action as log_act
from export_data import export_data as ed
from import_data import import_data as idd
from search_data import search_person as sp
from view_current_data import view_records_bot as vrb


bot = TeleBot('5795145659:AAEfn_ciZ44yKZ5mW6TsCPZziIVuAfW4LAc')
dict_list = idd('records_db.txt')
search_canon = ''
search_value = ''


@bot.message_handler(content_types=['document']) # Вот на этом моменте проблема, бот отправляет данные с файла в виде
def imp_db(msg: telebot.types.Message):          # текста, в нужном формате, но если присвоить dict_list к данным, то
    global dict_list
    file = bot.get_file(msg.document.file_id)    # они будут в бинарном виде, и соответственно работать с импортируемыми
    downloaded_file = bot.download_file(file.file_path) # данными - невозможно
    with open(msg.document.file_name, 'wb') as f_out:
        f_out.write(downloaded_file)
        dict_list = idd(file.file_path)
    bot.send_message(msg.chat.id, downloaded_file)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, text='/start - Главное меню\n/export - Экспортировать файл БД\n'
                                           '/help - Доступные команды\n Напиши "запуск" для инициализации БД')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'{message.from_user.first_name}, добро пожаловать в телефонный справочник!\n'
                                      f'Напиши "запуск" для начала работы')

@bot.message_handler(commands=['export'])
def exp_user(msg: telebot.types.Message):
    ed(dict_list, 'exp_user.txt')
    bot.send_message(chat_id=msg.from_user.id,
                     text='Экспорт базы"\n')
    bot.send_document(chat_id=msg.from_user.id, document=open('exp_user.txt', 'rb'))

@bot.message_handler(content_types=['text'])
def main(msg: telebot.types.Message):
    global dict_list
    if msg.text.lower() == 'запуск':
        bot.send_message(msg.chat.id, f'Введите номер пункта для выбора:\n1. Показать все записи\n2. Добавить запись'
                                      f'\n3. Поиск записи\n4. Удаление записи \n5. Экспорт данных \n6. Импорт данных')
    elif msg.text == '1':
        bot.send_message(msg.chat.id, f'{vrb(dict_list)}')
        log_act("Пользователь просматривал все записи")
    elif msg.text == '2':
        log_act("Пользователь добавил контакт")
        bot.send_message(msg.chat.id, f' Введите данные нового контакта через пробел\n'
                                      f' Имя: \n Фамилия: \n Телефон: \n Описание \n')
        bot.register_next_step_handler(msg, create_new_contact_bot)
        bot.send_message(msg.chat.id, "После отправки введенных данных, просмотрите все записи для проверки внесения")
    elif msg.text == '3':
        log_act("Пользователь искал запись")
        bot.send_message(msg.chat.id, '1.Поиск по имени\n 2.Поиск по фамилии\n 3.Поиск по номеру')
        bot.register_next_step_handler(msg, find_contact_bot)
    elif msg.text == '4':
        log_act("Пользователь удалял запись")
        bot.send_message(msg.chat.id, '1.Поиск по имени\n 2.Поиск по фамилии\n 3.Поиск по номеру')
        bot.register_next_step_handler(msg, find_contact_bot_deletion)
    elif msg.text == '5':
        bot.send_message(msg.chat.id, 'Для экспорта - введите "/export" ')
    elif msg.text == '6':
        bot.send_message(msg.chat.id, 'Для импорта - загрузите файл .txt в нужном формате')
    else:
        bot.send_message(msg.chat.id, 'Неизвестная команда напиши "/help"')



def create_new_contact_bot(msg: telebot.types.Message):
    global dict_list
    new_contact = msg.text.split()
    dicts_contact = {'Имя': new_contact[0], 'Фамилия': new_contact[1],
                     'Телефон': new_contact[2], 'Описание': new_contact[3]}
    dict_list.append(dicts_contact)


def find_contact_bot(msg: telebot.types.Message):
    global search_canon
    if msg.text == '1':
        search_canon = 'Имя'
        bot.send_message(msg.chat.id, 'Введите имя: ')
        bot.register_next_step_handler(msg, find_person_name)
    elif msg.text == '2':
        search_canon = 'Фамилия'
        bot.send_message(msg.chat.id, 'Введите фамилию: ')
        bot.register_next_step_handler(msg, find_person_surname)
    elif msg.text == '3':
        search_canon = 'Телефон'
        bot.send_message(msg.chat.id, 'Введите номер телефона: ')
        bot.register_next_step_handler(msg, find_person_number)


def find_person_name(msg: telebot.types.Message):
    search_value = msg.text
    if type(sp(dict_list, search_canon, search_value)) != str:
        answer, count = sp(dict_list, search_canon, search_value)
        result = dict_to_str(answer)
        bot.send_message(msg.chat.id, f'{result}\n \nID по порядку {count}')
    else:
        bot.send_message(msg.chat.id, 'Совпадений не найдено')


def find_person_surname(msg: telebot.types.Message):
    search_value = msg.text
    answer, count = sp(dict_list, search_canon, search_value)
    result = dict_to_str(answer)
    bot.send_message(msg.chat.id, f'{result}\n \nID по порядку {count}')

def find_person_number(msg: telebot.types.Message):
    search_value = msg.text
    answer, count = sp(dict_list, search_canon, search_value)
    result = dict_to_str(answer)
    bot.send_message(msg.chat.id, f'{result}\n \nID по порядку {count}')


def find_contact_bot_deletion(msg: telebot.types.Message):
    global search_canon
    if msg.text == '1':
        search_canon = 'Имя'
        bot.send_message(msg.chat.id, 'Введите имя: ')
        bot.register_next_step_handler(msg, find_person_name_for_delete)
    elif msg.text == '2':
        search_canon = 'Фамилия'
        bot.send_message(msg.chat.id, 'Введите фамилию: ')
        bot.register_next_step_handler(msg, find_person_surname_for_delete)
    elif msg.text == '3':
        search_canon = 'Телефон'
        bot.send_message(msg.chat.id, 'Введите номер телефона: ')
        bot.register_next_step_handler(msg, find_person_number_for_delete)


def find_person_name_for_delete(msg: telebot.types.Message):
    search_value = msg.text
    answer, count = sp(dict_list, search_canon, search_value)
    result = dict_to_str(answer)
    bot.send_message(msg.chat.id, f'{result}\n \nID по порядку {count}\nВведите номер ID для удаления: ')
    bot.register_next_step_handler(msg, delete_person)


def find_person_surname_for_delete(msg: telebot.types.Message):
    search_value = msg.text
    answer, count = sp(dict_list, search_canon, search_value)
    result = dict_to_str(answer)
    bot.send_message(msg.chat.id, f'{result}\n \nID по порядку {count}\nВведите номер ID для удаления: ')
    bot.register_next_step_handler(msg, delete_person)

def find_person_number_for_delete(msg: telebot.types.Message):
    search_value = msg.text
    answer, count = sp(dict_list, search_canon, search_value)
    result = dict_to_str(answer)
    bot.send_message(msg.chat.id, f'{result}\n \nID по порядку {count}\nВведите номер ID для удаления: ')
    bot.register_next_step_handler(msg, delete_person)


def delete_person(msg: telebot.types.Message):
    delete_index = int(msg.text)
    dict_list.pop(delete_index)
    bot.send_message(msg.chat.id, f'Контакт с ID - {delete_index} успешно удален')


def dict_to_str(dict):
    result = []
    strings = []
    for i in dict:
        strings.append('\n')
        for key, item in i.items():
            strings.append("{}: {}".format(key.capitalize(), item))
        result = "\n".join(strings)
    return result


@bot.message_handler()
def echo(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=msg.text)


bot.polling()