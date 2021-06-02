#!/usr/bin/python3
"""
This is the module documentation
"""


def read_file(filename=""):
    """open and read a .txt file format"""
    with open(filename, encoding='utf-8') as f:
        content = f.read()
        print(content, end="")
