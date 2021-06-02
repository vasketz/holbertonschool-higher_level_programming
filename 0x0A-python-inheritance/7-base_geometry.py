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
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
