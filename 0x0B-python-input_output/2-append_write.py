#!/usr/bin/python3
"""To define a file-appending func."""


def append_write(filename="", text=""):
    """Appending a string to end of a UTF8 txt file.

    Args:
        filename (str): The file name to append to.
        text (str): The string to be appended to the file.
    Returns:
        The no. of char appended.
    """
    with open(filename, "a", encoding="utf-8") as q:
        return q.write(text)
