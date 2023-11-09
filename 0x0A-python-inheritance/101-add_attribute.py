#!/usr/bin/python3
"""A function for manipulating obj."""


def add_attribute(obj, name, value):
    """function that insert a new attribute to an obj
    TypeError, when  message can add new attribute
    """
    if ('__dict__' in dir(obj)) and (type(obj.__dict__) is dict):
        obj.__dict__[name] = value
    else:
        raise TypeError("can't add new attribute")
