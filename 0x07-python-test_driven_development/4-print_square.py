#!/usr/bin/python3
"""
This is a module of square documentation
"""


def print_square(size):
    """
    Function to print a square with the character '#'
    size is the lenght of the square
    size must be an integer othewise TypeError: size must be an integer
    if size is less than 0 ValueError: size must be >= 0
    if size is a float and is less than 0 TypeError: size must be an integer
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float < 0:
        raise TypeError("size must be an integer")
    for col in range(size):
        for row in range(size):
            print("#", end="")
        print("")
