#!/usr/bin/python3
"""
module documentation of base geometry
"""


class BaseGeometry:
    """
    class BaseGeometric
    """
    def area(self):
        """Method area not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method to valide value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Class that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """instantiation of width and height"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
