#!/usr/bin/python3
"""Module to find the maximum int in a list
"""


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        void, If the list is empty.
    """
    if len(list) == 0:
        return None
    result = list[0]
    j = 1
    while j < len(list):
        if list[j] > result:
            result = list[j]
        j += 1
    return result
