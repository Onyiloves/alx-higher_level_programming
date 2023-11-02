#!/usr/bin/python3
"""define a module for a rectangle.
"""


class Rectangle:
    """Represents a rectangle class.
    """
    def __init__(self, width=0, height=0):
        """set-up a Rectangle with a specified width and height.
        Args:
            width (int): The rectangle width.
            height (int): The rectangle height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """extract the width of a given Rectangle.
        Returns:
            int: The width of this Rectangle.
        """
        return self.__width

    @property
    def height(self):
        """evaluates the height of a given Rectangle.
        Returns:
            int: The height of this Rectangle.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """compute the width of a given Rectangles.
        Args:
            value (int): The new width of this Rectangles.
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """evaluate the height of a given Rectangle.
        Args:
            value (int): The new height of this Rectangle.
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value
