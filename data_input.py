records_data = []


def create_record(surname, name, phone_number, phone_info):
    new_record = f'{surname.title()}, {name.title()}, {phone_number}, {phone_info.title()}'
    records_data.append(new_record)

    with open('records_db.txt', 'a', encoding='utf-8') as file:
        file.write(new_record + '\n')
