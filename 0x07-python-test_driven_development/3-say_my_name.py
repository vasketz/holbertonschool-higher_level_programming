#!/usr/bin/python3
"""
This is the documentation for the module of say_my_name
"""


def say_my_name(first_name, last_name=""):
    """
    This function prints the first name and the last name
    if the first name or the second name are differents than
    string show the TypeError first_name must be a string or
    last_name must be a string.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
