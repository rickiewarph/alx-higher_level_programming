#!/usr/bin/python3
"""Defines a class, Square."""


class Square:
    """a class representing a square."""

    def __init__(q, size):
        """a func to initialize a new square.
        Args:
            size (int): The new square's size.
        """
        q.size = size

    @property
    def size(self):
        """a func to get or set the square's current size."""
        return (q.__size)

    @size.setter
    def size(q, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        q.__size = value

    def area(q):
        """a func to return the square's current area."""
        return (q.__size * q.__size)

    def my_print(q):
        """a func printing square using # character."""
        for m in range(0, q.__size):
            [print("#", end="") for n in range(q.__size)]
            print("")
        if q.__size == 0:
            print("")
