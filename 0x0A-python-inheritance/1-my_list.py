#!/usr/bin/python3
"""
module documentation of Mylist
"""


class MyList(list):
    """class MyList that inherits from list"""
    def print_sorted(self):
        """Function to print the list sorted"""
        print(sorted(self))
