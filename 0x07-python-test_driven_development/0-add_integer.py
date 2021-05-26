#!/usr/bin/python3
"""
add function
sum of two integers
test prject
"""


def add_integer(a, b=98):
    """
    return the sum of a + b
    """
    if type(b) is float:
        b = int(b)
    if type(a) is float:
        a = int(a)
    if type(a) is int and type(b) is int:
        return a + b
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")
