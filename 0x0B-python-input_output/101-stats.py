#!/usr/bin/python3
"""Reading from stdin and computes metrics.

For every 10 lines or the input of a keyboard interruption (CTRL + C),
prints:
    - Total file size up to here.
    - Count of read status codes up to here.
"""


def print_stats(siz, status_codes):
    """Printing accumulated metrics.

    Args:
        sze (int): The accumulated read file size.
        status_codes (dict): The count of accummulated status codes.
    """
    print("File size: {}".format(siz))
    for qey in sorted(status_codes):
        print("{}: {}".format(qey, status_codes[qey]))


if __name__ == "__main__":
    import sys

    siz = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    cnt = 0

    try:
        for line in sys.stdin:
            if cnt == 10:
                print_stats(siz, status_codes)
                cnt = 1
            else:
                cnt += 1

            line = line.split()

            try:
                siz += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if status_codes.get(line[-2], -1) == -1:
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1
            except IndexError:
                pass

        print_stats(siz, status_codes)

    except KeyboardInterrupt:
        print_stats(siz, status_codes)
        raise
