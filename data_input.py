records_data = []


def create_record(surname, name, phone_number, phone_info):
    global records_data
    new_record = [surname.title(), name.title(), phone_number, phone_info.title()]
    records_data.append(new_record)
    new_record = f'{surname.title()}, {name.title()}, {phone_number}, {phone_info.title()}'
    with open('records_db.txt', 'a', encoding='utf-8') as file:
        file.write(new_record + '\n')


def get_record(surname='', name='', phone_number='', phone_info=''):
    global records_data
    result = []
    for row in records_data:
        result.append(row)
    return result


def new_get_record():
    with open('records_db.txt', 'r', encoding='utf-8') as file:
        records_info = file.read()
    return records_info



