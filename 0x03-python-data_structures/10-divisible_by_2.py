#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    q_list = []
    if my_list:
        for number in my_list:
            q_list.append(False if number % 2 else True)
        return q_list
