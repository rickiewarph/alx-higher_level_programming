#!/usr/bin/python3
"""To define class and inherited class that checks function."""


def is_kind_of_class(obj, q_class):
    """Will check if object is an instance or inherited instance of a class.

    Args:
        obj (any): The obj to check.
        a_class (type): The class to be matched the type of obj to.
    Returns:
        If obj is an instance or inherited instance of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, q_class):
        return True
    return False
