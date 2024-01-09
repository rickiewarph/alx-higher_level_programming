#!/usr/bin/python3
"""To define JSON file-writing func."""
import json


def save_to_json_file(my_objt, filename):
    """Writing an ob to a txt file using JSON representation."""
    with open(filename, "w") as q:
        json.dump(my_objt, q)
