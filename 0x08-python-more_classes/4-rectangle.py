#!/usr/bin/python3
"""0-rectangle.py"""


class Rectangle:
    """Creat a class rectangle"""
    def __init__(self, width=0, height=0):
        """initialize values"""
        if isinstance(height, int):
            self.__height = height
            if height < 0:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
        if isinstance(width, int):
            self.__width = width
            if width < 0:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    def area(self):
        """Area of rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Perimeter of rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """Function str"""
        strg = ""
        if self.__height == 0 or self.__width == 0:
            return strg
        for hg in range(self.__height):
            for wd in range(self.__width):
                strg = strg + '#'
            if hg < self.__height - 1:
                strg = strg + '\n'
        return strg

    def __repr__(self):
        """repr function"""
        strg = "Rectangle({}, {})".format(self.__width, self.__height)
        return strg

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
