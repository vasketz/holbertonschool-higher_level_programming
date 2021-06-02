#!/usr/bin/python3
"""
module documentation of inherits from
"""


def inherits_from(obj, a_class):
    """Return True if the object is an instance of a classs"""
    return type(obj) is not a_class
