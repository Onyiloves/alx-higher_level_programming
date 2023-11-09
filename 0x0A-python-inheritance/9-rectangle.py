#!/usr/bin/python3
"""outline a class Rectangle that inherits from a non empty BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """display a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """set_up a new_Rectangle.
        Args:
            width (int): The new_Rectangle width.
            height (int): The the new_Rectangle height.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """print the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Result the print() and str() representation of a Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
