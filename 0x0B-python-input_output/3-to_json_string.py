#!/usr/bin/python3
"""Defines a string function that reps JSON."""
import json


def to_json_string(my_obj):
    """Return the JSON reps string_object."""
    return json.dumps(my_obj)
