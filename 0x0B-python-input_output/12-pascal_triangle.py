#!/usr/bin/python3
"""Defining a Pascal's Triangle func."""


def pascal_triangle(q):
    """Representing Pascal's Triangle of size q.

    Returning a list of lists of ints representing the triangle.
    """
    if q <= 0:
        return []

    triangls = [[1]]
    while len(triangls) != q:
        tri = triangls[-1]
        temp = [1]
        for m in range(len(tri) - 1):
            temp.append(tri[m] + tri[m + 1])
        temp.append(1)
        triangls.append(temp)
    return triangls
