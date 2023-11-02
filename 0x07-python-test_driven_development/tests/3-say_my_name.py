#!/usr/bin/python3
# 3-say_my_name.py
"""Function that print my_name."""


def say_my_name(first_name, last_name=""):
    """Display a name.
    Args:
        first_name (str): The first name to print.
        last_name (str): The last name to print.
    Raises:
        Both first_name and last_name must be a string.
        or either first_name or last_name must be a string.
        else TypeError.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
