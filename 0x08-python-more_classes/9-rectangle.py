#!/usr/bin/python3
"""Defines a method for Rectangle shape class."""


class Rectangle:
    """Represent a rectangle shape.

    Attributes:
        num_of_instances (int): The num of Rectangle instances.
        print_symbol (any): The symbol used for string representation.
    """

    num_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """set-up a new Rectangle.

        Args:
            width (int): The width of the new_rectangle.
            height (int): The height of the new_rectangle.
        """
        type(self).num_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """cal the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """cal the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Result the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Result the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Result the Rectangle with the greater area.

        Args:
            rect_1 (Rectangle): The Rectangle1.
            rect_2 (Rectangle): The Rectangle2.
        Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """Result a new Rectangle with width and height equal to size.

        Args:
            size (int): The width and height of the new Rectangle.
        """
        return (cls(size, size))

    def __str__(self):
        """Result the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for j in range(self.__height):
            [rect.append(str(self.print_symbol)) for k in range(self.__width)]
            if j != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        type(self).num_of_instances -= 1
        print("Bye rectangle...")
