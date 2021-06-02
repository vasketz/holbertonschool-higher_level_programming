#!/usr/bin/python3
"""
This is the module documentation
"""


def append_write(filename="", text=""):
    """ append a file and if it dont exist creat it """
    with open(filename, 'a', encoding='utf-8') as f:
        wr = f.write(text)
        return wr
