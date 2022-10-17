def delete_person(dict_list: list, search_canon, search_value):
    result_lst = list(filter(lambda item: item[search_canon] == search_value, dict_list))
    return result_lst


def search_person(dict_list: list, search_canon, search_value):
    count = 0
    for j in dict_list:
        count += 1
        if j[search_canon] == search_value:
            print(count - 1, j)


