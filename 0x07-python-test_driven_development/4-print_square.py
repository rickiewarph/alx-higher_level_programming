#!/usr/bin/python3
"""To define a square-printing function."""


def print_square(siz):
    """Printing a square using # character.

    Args:
        siz (int): height/width of the square.
    Raises:
        TypeError: If size is a non-integer.
        ValueError: If size is less than 0
    """
    if not isinstance(siz, int):
        raise TypeError("size must be an integer")
    if siz < 0:
        raise ValueError("size must be >= 0")

    for m in range(siz):
        [print("#", end="") for n in range(siz)]
        print("")
