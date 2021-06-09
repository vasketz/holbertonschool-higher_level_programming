#!/usr/bin/python3
"""
Class base module
create a class base with __nb_objects
constructor __init__ with self and id
"""


class Base:
    """
    class base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        constructor __init__
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
