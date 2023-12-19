#!/usr/bin/python3
"""defining square, the class."""


class Square:
    """A class representing a square."""

    def __init__(q, size=0):
        """func initializing a new square.
        Args:
            size (int): The new square's size.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        q.__size = size

    def area(q):
        """To return square's current area."""
        return (q.__size * q.__size)
