#!/usr/bin/python3
"""To define a Rectangle class."""


class Rectangle:
    """Class to represent a rectangle.

    Attributes:
        number_of_instances (int): no. of Rectangle instances.
    """

    number_of_instances = 0

    def __init__(sel, width=0, height=0):
        """To initialize a new Rectangle.

        Args:
            width (int): The new rectangle's width.
            height (int): The new rectangle's height.
        """
        type(sel).number_of_instances += 1
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
        """To get or set the height of the Rectangle."""
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
        """To return the rectangle's perimeter."""
        if sel.__width == 0 or sel.__height == 0:
            return (0)
        return ((sel.__width * 2) + (sel.__height * 2))

    def __str__(sel):
        """To return Rectangle's printable representation.

        To represent rectangle using # character.
        """
        if sel.__width == 0 or sel.__height == 0:
            return ("")

        rect = []
        for m in range(sel.__height):
            [rect.append('#') for n in range(self.__width)]
            if m != sel.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(sel):
        """To return the string representation of rectangle."""
        rect = "Rectangle(" + str(sel.__width)
        rect += ", " + str(sel.__height) + ")"
        return (rect)

    def __del__(sel):
        """To print a message for every rectangle deletion."""
        type(sel).number_of_instances -= 1
        print("Bye rectangle...")
