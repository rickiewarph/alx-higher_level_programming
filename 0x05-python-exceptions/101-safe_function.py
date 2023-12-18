#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        number = fct(*args)
        return number
    except Exception as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return None
