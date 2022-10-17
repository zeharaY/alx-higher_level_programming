#!/usr/bin/python3
"""Class"""

class Rectangle:
    """Class Rectangle"""

    def __init__(self, width=0, height=0):
        """New Rectangle initialization

        Args:
            width (int): Width
            height (int): Height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("the value of width must be in an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("the value of height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
