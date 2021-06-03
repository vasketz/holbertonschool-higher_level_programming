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

    def to_json(self):
        """retrieves a dictionary"""
        return self.__dict__
