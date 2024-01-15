#!/usr/bin/python3
"""Defining a rect class."""
from models.base import Base


class Rectangle(Base):
    """Representing a rect."""

    def __init__(sel, width, height, x=0, y=0, id=None):
        """Initializing a new Rect.

        Args:
            width (int): The new Rect's width.
            height (int): The new Rect's height.
            x (int): The new Rect's x coordinates.
            y (int): The new Rect's y coordinates.
            id (int): The new Rect's identity.
        Raises:
            TypeError: If either of width or height is'nt an integer.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an integer.
            ValueError: If either of x or y < 0.
        """
        sel.width = width
        sel.height = height
        sel.x = x
        sel.y = y
        super().__init__(id)

    @property
    def width(sel):
        """To set or get width of the Rect."""
        return sel.__width

    @width.setter
    def width(sel, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        sel.__width = value

    @property
    def height(sel):
        """To set or get the height of the Rect."""
        return sel.__height

    @height.setter
    def height(sel, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        sel.__height = value

    @property
    def x(sel):
        """To set or get the x coordinate of the Rect."""
        return sel.__x

    @x.setter
    def x(sel, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        sel.__x = value

    @property
    def y(sel):
        """To set or get the y coordinate of the Rect."""
        return sel.__y

    @y.setter
    def y(sel, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        sel.__y = value

    def area(sel):
        """Returning area of the Rect."""
        return sel.width * sel.height

    def display(sel):
        """Printing the Rect using the `#` char."""
        if sel.width == 0 or sel.height == 0:
            print("")
            return

        [print("") for y in range(sel.y)]
        for g in range(sel.height):
            [print(" ", end="") for x in range(sel.x)]
            [print("#", end="") for w in range(sel.width)]
            print("")

    def update(sel, *args, **kwargs):
        """Updating the Rect.

        Args:
            *args (ints): New attr values.
                - 1st arg representing id attribute
                - 2nd arg representing width attribute
                - 3rd arg representing height attribute
                - 4th arg representing x attribute
                - 5th arg representing y attribute
            **kwargs (dict): New key or value pairs of attributes.
        """
        if args and len(args) != 0:
            b = 0
            for arg in args:
                if b == 0:
                    if arg is None:
                        sel.__init__(sel.width, sel.height, sel.x, sel.y)
                    else:
                        sel.id = arg
                elif b == 1:
                    sel.width = arg
                elif b == 2:
                    sel.height = arg
                elif b == 3:
                    sel.x = arg
                elif b == 4:
                    sel.y = arg
                b += 1

        elif kwargs and len(kwargs) != 0:
            for i, v in kwargs.items():
                if i == "id":
                    if v is None:
                        sel.__init__(sel.width, sel.height, sel.x, sel.y)
                    else:
                        self.id = v
                elif i == "width":
                    sel.width = v
                elif i == "height":
                    sel.height = v
                elif i == "x":
                    sel.x = v
                elif i == "y":
                    sel.y = v

    def to_dictionary(sel):
        """Returning the dict representation of a Rect."""
        return {
            "id": sel.id,
            "width": sel.width,
            "height": sel.height,
            "x": sel.x,
            "y": sel.y
        }

    def __str__(sel):
        """Returning the print() and str() representation of the Rect."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(sel.id,
                                                       sel.x, sel.y,
                                                       sel.width, sel.height)
