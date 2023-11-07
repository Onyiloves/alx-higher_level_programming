#!/usr/bin/python3
"""Sum Add all arguments lists and save to a file_add_item.json."""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        result = load_from_json_file("add_item.json")
    except FileNotFoundError:
        result = []
    result.extend(sys.argv[1:])
    save_to_json_file(result, "add_item.json")
