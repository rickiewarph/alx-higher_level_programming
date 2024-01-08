#!/usr/bin/python3
"""Defining a base geometry class BaseGeometry."""


class BaseGeometry:
    """Reprsenting basegeometry."""

    def area(sel):
        """Not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(sel, name, value):
        """Validating a parameter as an int.

        Args:
            name (str): Parameter name.
            value (int): The parameter to be validated.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
