#!/usr/bin/python3
"""To define a text-indentation function."""


def text_indentation(text):
    """Func printing text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to be printed.
    Raises:
        TypeError: If text is a non-string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    q = 0
    while q < len(text) and text[q] == ' ':
        q += 1

    while q < len(text):
        print(text[q], end="")
        if text[q] == "\n" or text[q] in ".?:":
            if text[q] in ".?:":
                print("\n")
            q += 1
            while q < len(text) and text[q] == ' ':
                q += 1
            continue
        q += 1
