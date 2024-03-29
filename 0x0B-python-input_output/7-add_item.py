#!/usr/bin/python3
"""Adding all args to a Python list & save them to a file."""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        tems = load_from_json_file("add_item.json")
    except FileNotFoundError:
        tems = []
    tems.extend(sys.argv[1:])
    save_to_json_file(tems, "add_item.json")
