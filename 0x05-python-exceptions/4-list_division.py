#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    q_list = []
    for q in range(list_length):
        try:
            divide = my_list_1[q] / my_list_2[q]
        except TypeError:
            print("wrong type")
            divide = 0
        except ZeroDivisionError:
            print("division by 0")
            divide = 0
        except IndexError:
            print("out of range")
            divide = 0
        finally:
            q_list.append(divide)
    return q_list
