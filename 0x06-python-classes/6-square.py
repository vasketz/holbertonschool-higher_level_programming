#!/usr/bin/python3
"""1-square.py"""


class Square():
    """define size on intance of class square"""
    def __init__(self, size=0, position=(0, 0)):
        """ inicialize the instance"""
        if isinstance(size, int):
            self.__size = size
            self.__position = position
            if size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Define an area of square"""
        return self.__size ** 2

    @property
    def size(self):
        """Getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter"""
        if isinstance(value, int):
            self.__size = value
            if value < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def my_print(self):
        """Print a square"""
        if self.__size == 0:
            print("")
        for k in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            for h in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print("")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, int):
            self.__position = value
            if value < 0:
                raise TypeError("position must be a tuple \
                of 2 positive integers")
