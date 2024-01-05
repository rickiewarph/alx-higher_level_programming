#!/usr/bin/python3
"""To define a name-printing function."""


def say_my_name(first_name, last_name=""):
    """func to print a name.

    Args:
        first_name (str): 1st name to print.
        last_name (str): 2nd name to print.
    Raises:
        TypeError: If first_name and last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
