#!/usr/bin/python3
def remove_char_at(str, n):
    qew = ''
    q = 0
    for char in str:
        if q != n:
            qew += str[q]
        q += 1
    return (qew)
