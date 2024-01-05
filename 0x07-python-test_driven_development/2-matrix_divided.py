#!/usr/bin/python3
"""To define a matrix division function."""


def matrix_divided(matrix, div):
    """Division of all elements of a matrix.

    Args:
        matrix (list): lists of ints or floats.
        div (int/float): divisor.
    Raises:
        TypeError: Matrix has non-numbers.
        TypeError: Matrix has rows of different sizes.
        TypeError: If div is not a float or an int.
        ZeroDivisionError: If div equals 0.
    Returns:
        A new matrix represeentative of the division outcome.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(ro, list) for ro in matrix) or
            not all((isinstance(elen, int) or isinstance(elen, float))
                    for elen in [numb for ro in matrix for numb in ro])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(ro) == len(matrix[0]) for ro in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), ro)) for ro in matrix])
