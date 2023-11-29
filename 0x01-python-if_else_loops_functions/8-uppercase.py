#!/usr/bin/python3
def uppercase(str):
    for iterat in str:
        tmp = interat
        if ord(tmp) >= 97 and ord(tmp) <= 122:
            tmp = chr(ord(iterat) - 32)
        print("{}".format(tmp), end='')
    print()
