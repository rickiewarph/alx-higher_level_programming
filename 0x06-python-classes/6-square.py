#!/usr/bin/python3
"""Defining a class Square."""


class Square:
    """a class representing a square."""

    def __init__(q, size=0, position=(0, 0)):
        """a func initializing a new square.
        Args:
            size (int): The new square's size.
            position (int, int): The new square's position.
        """
        q.size = size
        q.position = position

    @property
    def size(q):
        """a func to get or set the square's current size."""
        return (q.__size)

    @size.setter
    def size(q, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        q.__size = value

    @property
    def position(q):
        """a func to get or set square's current position."""
        return (q.__position)

    @position.setter
    def position(q, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(numb, int) for numb in value) or
                not all(numb >= 0 for numb in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        q.__position = value

    def area(q):
        """a func to return the square's current area."""
        return (q.__size * q.__size)

    def my_print(q):
        """a func printing square using # character."""
        if q.__size == 0:
            print("")
            return

        [print("") for m in range(0, q.__position[1])]
        for m in range(0, q.__size):
            [print(" ", end="") for n in range(0, q.__position[0])]
            [print("#", end="") for o in range(0, q.__size)]
            print("")
