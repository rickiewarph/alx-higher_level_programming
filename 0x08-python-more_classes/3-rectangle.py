#!/usr/bin/python3
"""To define a Rectangle class."""


class Rectangle:
    """class to represent a rectangle."""

    def __init__(sel, width=0, height=0):
        """to initialize a new Rectangle.

        Args:
            width (int): The new rectangle's width.
            height (int): The new rectangle's height.
        """
        sel.width = width
        sel.height = height

    @property
    def width(sel):
        """To get or set the Rectangle's width."""
        return sel.__width

    @width.setter
    def width(sel, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        sel.__width = value

    @property
    def height(sel):
        """to get or set Rectangle's height."""
        return sel.__height

    @height.setter
    def height(sel, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        sel.__height = value

    def area(sel):
        """To return the Rectangle's area."""
        return (sel.__width * sel.__height)

    def perimeter(sel):
        """To return Rectangle's perimeter."""
        if sel.__width == 0 or sel.__height == 0:
            return (0)
        return ((sel.__width * 2) + (sel.__height * 2))

    def __str__(sel):
        """To return the printable representation of Rectangle.

        To represent rectangle using # character.
        """
        if sel.__width == 0 or sel.__height == 0:
            return ("")

        rect = []
        for m in range(sel.__height):
            [rect.append('#') for n in range(sel.__width)]
            if m != sel.__height - 1:
                rect.append("\n")
        return ("".join(rect))
