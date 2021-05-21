#!/usr/bin/python3
"""0-rectangle.py"""


class Rectangle:
    """Creat a class rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """initialize values"""
        Rectangle.number_of_instances += 1
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
                strg = strg + str(self.print_symbol)
            if hg < self.__height - 1:
                strg = strg + '\n'
        return strg

    def __repr__(self):
        """repr function"""
        strg = "Rectangle({}, {})".format(self.__width, self.__height)
        return strg

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if isinstance(rect_1, Rectangle):
            re1 = Rectangle.area(rect_1)
        else:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle):
            re2 = Rectangle.area(rect_2)
        else:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if re1 > re2:
            return rect_1
        elif re2 > re1:
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        instance = cls()
        instance.width = size
        instance.height = size
        return instance

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
