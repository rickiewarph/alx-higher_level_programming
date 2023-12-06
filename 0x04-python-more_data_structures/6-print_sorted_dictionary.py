#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    q = sorted(a_dictionary)
    for p in q:
        print("{}: {}".format(p, a_dictionary[p]))
