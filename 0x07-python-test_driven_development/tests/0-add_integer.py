#!/usr/bin/python3
# 0-add_integer.py
"""function that add two integer a and b"""


def add_integer(a, b=98):
    """
    a and b must be either integers or floats.
     if a and b is float, integer must be first cast
     else TypeError, when either a or b is not integer or floats.
     return addition of a and b integer
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
