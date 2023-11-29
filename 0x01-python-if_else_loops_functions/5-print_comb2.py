#!/usr/bin/python3
for q in range(0, 100):
    if q == 99:
        print("{}".format(q))
    else:
        print("{:02d}, ".format(q), end='')
