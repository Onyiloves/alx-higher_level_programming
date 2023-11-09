#!/usr/bin/python3
"""Defines a class and inheritance function."""


def is_kind_of_class(obj, a_class):
    """Determines if an object is an instance.
    inherited instance of a specified class.

    Args:
        obj (any): The object to validates.
        a_class (type): The class to validates the type of object.
    Returns:
        If object is not an instance or inherited instance of a_class - false.
        else - true.
    """
    if isinstance(obj, a_class):
        return True
    return False
