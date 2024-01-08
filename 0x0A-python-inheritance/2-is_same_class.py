#!/usr/bin/python3
"""To define a class that checks function."""


def is_same_class(obj, a_class):
    """will check whether an object is exactly an instance of a given class.

    Args:
        obj (any): The object to be checked.
        a_class (type): The class to be matched the type of obj to.
    Returns:
        If obj is an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
