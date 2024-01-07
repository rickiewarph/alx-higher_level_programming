#!/usr/bin/python3
"""This module locates maximum integer in a list
"""


def max_integer(list=[]):
    """Func ffinding and returning max integer in a list of integers
        Func returns None if the list is empty
    """
    if len(list) == 0:
        return None
    outcome = list[0]
    m = 1
    while m < len(list):
        if list[m] > outcome:
            outcome = list[m]
        m += 1
    return outcome
