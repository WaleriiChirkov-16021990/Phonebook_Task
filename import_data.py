# Блок считывает файл, и создает список контактов \
# где каждый элемент списка это словарь каждого контакта.


path = 'records_db.txt'


def import_data(path):
    lines = []
    date = []
    with open(path, 'r', encoding='utf-8') as data:
        while True:
            line = data.read().strip().split()
            if not line:
                break
            date.append(line)
    date_lo = []
    for i in range(len(date[0])):
        if date[0][i].find(':'):
            date_lo.append(date[0][i])
    for j in range(0, len(date_lo), 8):
        temp = date_lo[j:j+8:1]
        dict_ = {temp[i] : temp[i + 1] for i in range(0, len(temp) - 1, 2)}
        lines.append(dict_)
    return(lines)



