#!/usr/bin/python3
# 6-from_json_string.py
"""Defines a function From JSON string to Object."""
import json


def from_json_string(my_str):
    """Return the Python obj rep of a JSON_string."""
    return json.loads(my_str)
