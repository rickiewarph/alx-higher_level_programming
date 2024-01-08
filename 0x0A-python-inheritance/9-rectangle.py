#!/usr/bin/python3
"""Defining a class Rectangle inheriting from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Representative of a rectangle using BaseGeometry."""

    def __init__(sel, width, height):
        """Intializing new Rectangle.

        Args:
            width (int): The new Rectangle's width.
            height (int): The new Rectangle's height.
        """
        super().integer_validator("width", width)
        sel.__width = width
        super().integer_validator("height", height)
        sel.__height = height

    def area(sel):
        """Returning the rectangle's area."""
        return sel.__width * sel.__height

    def __str__(sel):
        """Returning the print() and str() representative of a Rectangle."""
        string = "[" + str(sel.__class__.__name__) + "] "
        string += str(sel.__width) + "/" + str(sel.__height)
        return string
