#!/usr/bin/python3
"""
file: 10-class_to_json.py
functions:
-> class_to_json
"""


def class_to_json(obj):
    """ retuns the dictionary description with simple data structure """

    folder = {}
    if hasattr(obj, "__dict__"):
        folder = obj.__dict__.copy()
    return folder
