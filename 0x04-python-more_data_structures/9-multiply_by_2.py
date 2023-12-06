#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    me_dic = dict(a_dictionary)
    for q, v in me_dic.items():
        me_dic[q] = v * 2
    return me_dic
