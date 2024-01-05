#!/usr/bin/python3
def magic_string():
    magic_string.q = getattr(magic_string, 'q', 0) + 1
    return ("BestSchool, " * (magic_string.q - 1) + "BestSchool")
