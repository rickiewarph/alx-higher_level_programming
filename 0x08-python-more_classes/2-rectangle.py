#!/usr/bin/python3
"""To defines a rectangle class."""


class Rectangle:
    """class to represent a rectangle."""

    def __init__(self, width=0, height=0):
        """To initialize a new Rectangle.

        Args:
            width (int): The new rectangle's width.
            height (int): The new rectangle's height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """To get or set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """To get or set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """To return the Rectangle's area."""
        return (self.__width * self.__height)

    def perimeter(self):
        """To return the Rectangle's perimeter."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
