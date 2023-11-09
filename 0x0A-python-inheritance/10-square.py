#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """print a square."""

    def __init__(self, size):
        """set-up a new_square.

        Args:
            size (int): The size of the new_square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
