#!/usr/bin/python3
"""Outline a class Rectangle that inherits from a non empty BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """display a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """set_up a new_Rectangle.
        Args:
            width (int): The new_Rectangle width.
            height (int): The new_Rectangle height.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
