#!/usr/bin/python3
"""Defines a function print a square with char #."""


def print_square(size):
    """display a square with the # character.

    Args:
        size (int): The height/width of the square.
    Raises:
        size must be an integer, and size is a float and > 0.
        else TypeError
        or size must be >= 0, else ValueError.

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for j in range(size):
        [print("#", end="") for k in range(size)]
        print("")
