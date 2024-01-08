#!/usr/bin/python3
"""To define an inherited class-checking function."""


def inherits_from(obj, q_class):
    """Will check if an object is an inherited instance of a class.

    Args:
        obj (any): The obj to check.
        a_class (type): The class to be match obj to.
    Returns:
        If obj is an inherited instance of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), q_class) and type(obj) != q_class:
        return True
    return False
