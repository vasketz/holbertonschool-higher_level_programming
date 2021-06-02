#!/usr/bin/pyhton3
"""
This is the module documentation
"""


def write_file(filename="", text=""):
    """ write a file and if it dont exist creat it """
    with open(filename, 'w', encoding='utf-8') as f:
        wr = f.write(text)
        return wr
