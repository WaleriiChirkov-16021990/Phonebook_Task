def delete_person(dict_list: list, search_canon, search_value):
    result_lst = list(filter(lambda item: item[search_canon] == search_value, dict_list))
    return result_lst


def search_person(dict_list: list, search_canon, search_value):
    result_lst = list(filter(lambda item: item[search_canon] == search_value, dict_list))
    return result_lst

