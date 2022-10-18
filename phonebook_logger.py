# Данный блок регистрирует любое действия в текстовый файл.


import datetime


def logger_action(action: str):
    today = datetime.datetime.today()
    with open('log.txt', 'a', encoding='utf-8') as data:
        data.write(\
            f'{today.strftime("%Y-%m-%d-%H %H:%M")} Пользователь {action} \n')
