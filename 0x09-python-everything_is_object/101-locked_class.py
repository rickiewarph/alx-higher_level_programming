#!/usr/bin/python3
"""To define a locked class."""


class LockedClass:
    """Prevents user from dynamically creating new instance attribute"""

    __slots__ = ["first_name"]
