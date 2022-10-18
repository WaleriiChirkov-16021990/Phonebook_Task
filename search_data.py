def delete_person(dict_list: list, search_canon, search_value):
    result_lst = list(filter(lambda item: item[search_canon] == search_value, dict_list))
    return result_lst


def search_person(dict_list: list, search_canon, search_value):
    count = 0
    result_search = None
    for j in dict_list:
        count += 1
        if j[search_canon] == search_value:
            print(count - 1, j)
            result_search = dict.fromkeys(f'{count-1}', f'{j}')
    if result_search:
        return result_search
    else:
        return False


