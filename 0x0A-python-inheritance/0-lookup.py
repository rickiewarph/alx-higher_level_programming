#!/usr/bin/python3
"""To define an object attr lookup function."""


def lookup(obj):
    """To return a list of available attributes of an object."""
    return (dir(obj))
