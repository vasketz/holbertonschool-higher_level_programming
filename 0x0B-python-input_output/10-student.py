#!/usr/bin/python3
"""
This is the module documentation
"""


class Student:
    """define a class Student """
    def __init__(self, first_name, last_name, age):
        """instantiation of attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary"""
        diccio = {}
        if type(attrs) is not list:
            return self.__dict__
        else:
            for item in attrs:
                if type(item) is not str:
                    return self.__dict__
                else:
                    if item in self.__dict__:
                        diccio[item] = self.__dict__[item]
            return diccio
