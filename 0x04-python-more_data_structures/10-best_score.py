#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    MaxV = 0
    for qey, value in a_dictionary.items():
        if value > MaxV:
            MaxV = value
    for qey, value in a_dictionary.items():
        if value == MaxV:
            return qey
