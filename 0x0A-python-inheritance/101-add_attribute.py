#!/usr/bin/python3
"""Defining a func that adds attributes to objects."""


def add_attribute(objt, attr, val):
    """Adding a new attr to an object if possible.

    Args:
        objt (any): The object to be added an attribute to.
        attr (str): The name of the attribute to add to obj.
        val (any): The value of attr.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(objt, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(objt, attr, val)
