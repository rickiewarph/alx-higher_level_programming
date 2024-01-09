#!/usr/bin/python3
# 6-from_json_string.py
"""Defining a JSON-to-object func."""
import json


def from_json_string(my_str):
    """Returning Python obj representative of a JSON string."""
    return json.loads(my_str)
