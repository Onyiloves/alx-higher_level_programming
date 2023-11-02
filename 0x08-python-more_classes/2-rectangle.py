#!/usr/bin/python3
"""define a method for working with rectangle.
"""


class Rectangle:
    """Represent a rectangle
    """
    def __init__(self, width=0, height=0):
        """set-up a Rectangle with a define width and height.
        Args:
            width (int): The width_rectangle.
            height (int): The height_rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of this Rectangle.
        Returns:
            int: The width of this Rectangle.
        """
        return self.__width

    @property
    def height(self):
        """cal the height of the defined Rectangle.
        Returns:
            int: The height of the define Rectangle.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """state the width of this Rectangle.
        Args:
            value (int): The new_width of the defined Rectangle.
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """cal the height of the define Rectangle.
        Args:
            value (int): The new_height of the define Rectangle.
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        '''evaluate the area of the define Rectangle.
        Returns:
            int: The area_Rectangle.
        '''
        return self.width * self.height

    def perimeter(self):
        '''evaluate the perimeter of the define Rectangle.
        Returns:
            int: The perimeter_Rectangle.
        '''
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)
