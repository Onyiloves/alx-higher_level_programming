#!/usr/bin/python3
"""define a module for working with rectangle shape.
"""


class Rectangle:
    """Represents a rectangle shape.
    """
    def __init__(self, width=0, height=0):
        """set-up a Rectangle with a defined width and height.
        Args:
            width (int): The width_rectangle.
            height (int): The height_rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """cal the width of the specified Rectangle.
        Returns:
            int: The width_Rectangle.
        """
        return self.__width

    @property
    def height(self):
        """cal the height of the defined Rectangle.
        Returns:
            int: The height_Rectangle.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """display the width_Rectangle.
        Args:
            value (int): The new_width of the Rectangle.
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """display the height_Rectangle.
        Args:
            value (int): The new_height of the Rectangle.
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """evaluate the area of the Rectangle.
        Returns:
            int: The area_Rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """evaluate the perimeter of the Rectangle.
        Returns:
            int: The perimeter_Rectangle.
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """Result a str representations of the Rectangle.
        Returns:
            str: A str representations of the Rectangle.
        """
        if self.width == 0 or self.height == 0:
            return ''
        else:
            res = list(map(
                lambda x: '#' * self.width + '\n' * (x != self.height - 1),
                range(self.height)))
            return ''.join(res)
