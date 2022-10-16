# Блок отображает все данные, полученные из хранилища


def show_data(data):
    if data:
        print(list(filter(None, data)))
        return True
    else:
        print('Нет данных !\n')
        return False
