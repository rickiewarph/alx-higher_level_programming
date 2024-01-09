#!/usr/bin/python3
"""Defining a txt file insertion func."""


def append_after(filename="", search_string="", new_string=""):
    """Inserting a txt after each line that has a given string in a file.

    Args:
        filename (str): The file name.
        search_string (str): The str to search for within the file.
        new_string (str): The str to insert.
    """
    text = ""
    with open(filename) as q:
        for line in q:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
