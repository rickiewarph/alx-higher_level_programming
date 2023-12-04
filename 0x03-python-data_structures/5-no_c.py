#!/usr/bin/python3
def no_c(my_string):
    q_string = ""
    for elements in my_string:
        if elements != "c" and elements != "C":
            q_string += elements
    return q_string
