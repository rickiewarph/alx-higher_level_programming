#!/usr/bin/python3
"""Defining JSON file-reading func."""
import json


def load_from_json_file(filename):
    """Creating a Python obj from a JSON file."""
    with open(filename) as q:
        return json.load(q)
