#!/usr/bin/python3
for q in range(0, 10):
    for p in range(q + 1, 10):
        if q == 8 and p == 9:
            print("{}{}".format(q, p))
        else:
            print("{}{}, ".format(q, p), end='')
