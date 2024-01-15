#!/usr/bin/python3
"""Defining a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Representing a sq."""

    def __init__(sel, size, x=0, y=0, id=None):
        """Initializing a new Square.

        Args:
            size (int): The new Square's size.
            x (int): The new Square's x coordinates.
            y (int): The new Square's y coordinates.
            id (int): The new Square's identity.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(sel):
        """Geting or setting the size of the Square."""
        return sel.width

    @size.setter
    def size(sel, value):
        sel.width = value
        sel.height = value

    def update(sel, *args, **kwargs):
        """Updates the Sqr.

        Args:
            *args (ints): New attr values.
                - 1st arg representing id attribute
                - 2nd arg representing size attribute
                - 3rd arg representing x attribute
                - 4th arg representing y attribute
            **kwargs (dict): New key or value pairs of attributes.
        """
        if args and len(args) != 0:
            b = 0
            for arg in args:
                if b == 0:
                    if arg is None:
                        sel.__init__(sel.size, sel.x, sel.y)
                    else:
                        sel.id = arg
                elif b == 1:
                    sel.size = arg
                elif b == 2:
                    sel.x = arg
                elif b == 3:
                    sel.y = arg
                b += 1

        elif kwargs and len(kwargs) != 0:
            for i, v in kwargs.items():
                if i == "id":
                    if v is None:
                        sel.__init__(sel.size, sel.x, sel.y)
                    else:
                        sel.id = v
                elif i == "size":
                    sel.size = v
                elif i == "x":
                    sel.x = v
                elif i == "y":
                    sel.y = v

    def to_dictionary(sel):
        """Returning the dict representation of the Square."""
        return {
            "id": sel.id,
            "size": sel.width,
            "x": sel.x,
            "y": sel.y
        }

    def __str__(sel):
        """Returning the print() and str() rep of a Square."""
        return "[Square] ({}) {}/{} - {}".format(sel.id, sel.x, sel.y,
                                                 sel.width)
