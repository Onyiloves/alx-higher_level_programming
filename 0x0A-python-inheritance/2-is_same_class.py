#!/usr/bin/python3
"""Defines a class validates function."""


def is_same_class(obj, a_class):
    """determines if an object is exactly an instances of a given class.

    Args:
        obj (any): The object to be determined.
        a_class (type): The class to validates objects.
    Returns:
        If obj is not exactly an instance of a_class - false.
        else - true.
    """
    if type(obj) == a_class:
        return True
    return False
