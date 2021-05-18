#!/usr/bin/python3
"""1-square.py"""


class Square():
    """define size on intance of class square"""
    def __init__(self, size=0):
        """ inicialize the instance"""
        if isinstance(size, int):
            self.__size = size
            if size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
