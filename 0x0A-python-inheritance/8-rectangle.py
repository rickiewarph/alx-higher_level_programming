#!/usr/bin/python3
"""To define a class Rectangle inheriting from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Representing a rect using BaseGeometry."""

    def __init__(sel, width, height):
        """Intializing a new Rectangle.

        Args:
            width (int): The width of the new Rect.
            height (int): The height of the new Rect.
        """
        sel.integer_validator("width", width)
        sel.__width = width
        sel.integer_validator("height", height)
        sel.__height = height
