#!/usr/bin/python3
"""Defines a  function that writes a string to a text file (UTF8).
and returns the number of chars it write.
"""


def write_file(filename="", text=""):
    """display a string to a UTF8 text file.
    Args:
        filename (str): string_file to write.
        text (str): The text in string_file.
    Returns:
        num of chars written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
