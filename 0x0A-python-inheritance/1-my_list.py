#!/usr/bin/python3
"""To define an inherited list class MyList."""


class MyList(list):
    """To implement sorted printing of the built-in list class."""

    def print_sorted(self):
        """Printing list in sorted ascending order."""
        print(sorted(self))
