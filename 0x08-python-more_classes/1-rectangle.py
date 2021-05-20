#!/usr/bin/python3
"""0-rectangle.py"""


class Rectangle:
    """Creat a class rectangle"""
    def __init__(self, width=0, height=0):
        """initialize values"""
        if isinstance(width, int):
            self.__width = width
            if width < 0:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")
        if isinstance(height, int):
            self.__height = height
            if height < 0:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    @property
    def width(self):
        """Return getter of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter of width"""
        if isinstance(value, int):
            self.__width = value
            if value < 0:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """Return getter of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter of height"""
        if isinstance(value, int):
            self.__height = value
            if value < 0:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

