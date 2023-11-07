#!/usr/bin/python3
"""Defines a function that drived an Obj from a JSON_file"""
import json


def load_from_json_file(filename):
    """drive an obj from a JSON file."""
    with open(filename) as f:
        return json.load(f)
