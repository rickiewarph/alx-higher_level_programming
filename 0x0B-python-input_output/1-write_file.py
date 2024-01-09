#!/usr/bin/python3
"""To define a file-writing func."""


def write_file(filename="", text=""):
    """To write a string to a UTF8 text file.

    Args:
        filename (str): Name of the file to write.
        text (str): Text to write to the file.
    Returns:
        The no. of char written.
    """
    with open(filename, "w", encoding="utf-8") as g:
        return g.write(text)
