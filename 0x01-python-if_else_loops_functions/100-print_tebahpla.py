#!/usr/bin/python3
for q in range(ord('z'), ord('a') - 1, -2):
    print("{}{}".format(chr(q), chr(q - 33)), end='')
