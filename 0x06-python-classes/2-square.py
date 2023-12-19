#!/usr/bin/python3
"""defining a class Square."""


class Square:
    """class to represent a square."""

    def __init__(q, size=0):
        """a func initializing new Square.
        Args:
            size (int): The new square's size.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        q.__size = size
