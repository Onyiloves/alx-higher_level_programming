#!/usr/bin/python3
"""Defines a functn that appends a string at the end of a text file (UTF8)."""


def append_write(filename="", text=""):
    """Append a string to the end of a UTF8 text file.
        create file if it does not exit.
    Args:
        filename (str): file_name to append to.
        text (str): string_test to append to the file.
    Returns:
        The num of chars appends
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
