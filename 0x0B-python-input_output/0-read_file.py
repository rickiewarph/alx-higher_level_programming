#!/usr/bin/python3
"""To define a text file-reading func."""


def read_file(filename=""):
    """Printing contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as q:
        print(q.read(), end="")
