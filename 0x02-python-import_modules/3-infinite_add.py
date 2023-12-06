#!/usr/bin/python3

if __name__ == "__main__":
    """Print sum of all arguments."""
    import sys

    total = 0
    for q in range(len(sys.argv) - 1):
        total += int(sys.argv[q + 1])
    print("{}".format(total))
