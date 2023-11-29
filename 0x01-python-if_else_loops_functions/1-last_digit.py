#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdig = abs(number) % 10
if number < 0:
    lastdig = -(lastdig)
string = "Last digit of {} is {}".format(number, lastdig)
if lastdig > 5:
    print(f"{string} and is 0")
elif lastdig == 0:
    print(f"{string} and is 0")
elif lastdig < 6:
    print(f"{string} and is less than 6 and not 0")
