#!/usr/bin/python3
"""
module documentation of is_same_class
"""


def is_same_class(obj, a_class):
    """Funtion that return True if the object
    is an exactly instance of a class"""
    return type(obj) is a_class
