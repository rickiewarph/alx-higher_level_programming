#!/usr/bin/python3
"""To define a function that sums integers."""


def add_integer(a, b=98):
    """Func to return sum of a and b.

    Typecast float args to ints before addition is performed.

    Raises:
        TypeError: If either of a or b is not an integer or non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
