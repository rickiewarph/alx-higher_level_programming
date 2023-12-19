#!/usr/bin/python3
"""Defining a sqaure, the class."""


class Square:
    """A class to represent a square."""

    def __init__(q, size=0):
        """A func to initialize a new square.
        Args:
            size (int): The new square's size.
        """
        q.__size = size

    @property
    def size(q):
        """This func gets or sets current size of the square."""
        return (q.__size)

    @size.setter
    def size(q, val):
        if not isinstance(val, int):
            raise TypeError("size must be an integer")
        elif val < 0:
            raise ValueError("size must be >= 0")
        q.__size = val

    def area(q):
        """A func returning the square's current area."""
        return (q.__size * q.__size)
