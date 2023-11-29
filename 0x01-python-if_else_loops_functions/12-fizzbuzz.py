#!/usr/bin/python3
def fizzbuzz():
    for q in range(1, 101):
        if q % 3 == 0 and q % 5 != 0:
            print("Fizz ", end='')
        elif q % 5 == 0 and q % 3 != 0:
            print("Buzz ", end='')
        elif q % 5 == 0 and q % 3 == 0:
            print("FizzBuzz ", end='')
        else:
            print("{} ".format(q), end='')
