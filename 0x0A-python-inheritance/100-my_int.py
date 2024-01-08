#!/usr/bin/python3
"""Defining a class MyInt inheriting from int."""


class MyInt(int):
    """Inverting int operators == and !=."""

    def __eq__(sel, value):
        """Override equals opeartor with != behavior."""
        return sel.real != value

    def __ne__(sel, value):
        """Override is not operator with == behavior."""
        return sel.real == value
