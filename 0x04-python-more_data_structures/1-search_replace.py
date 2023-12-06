#!/usr/bin/python3
def search_replace(my_list, search, replace):
    qew_list = list(my_list)
    for q in range(len(qew_list)):
        if qew_list[q] == search:
            qew_list[q] = replace
    return qew_list
