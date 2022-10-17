def view_records():
    with open('record_data.txt', 'r', encoding='utf-8') as file:
        records = file.readlines()
    for i in records:
        print(i[:len(i)-1])



