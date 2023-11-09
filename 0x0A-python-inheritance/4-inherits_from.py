#!/usr/bin/python3
"""Defines an inheritance class function."""


def inherits_from(obj, a_class):
    """Determine if an object is an inherited instances of a specified class.
    Args:
        obj (any): The object to validates.
        a_class (type): The class to validates the type of object
    Returns:
        If object is not an inherited instance of a_class - False.
        Else - True.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
