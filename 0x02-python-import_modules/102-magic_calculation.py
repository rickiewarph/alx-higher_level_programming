#!/usr/bin/python3


def magic_calculation(a, b):
    """Match bytecode offered with Holberton School."""
    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)
        for q in range(4, 6):
            c = add(c, q)
        return (c)

    else:
        return(sub(a, b))
