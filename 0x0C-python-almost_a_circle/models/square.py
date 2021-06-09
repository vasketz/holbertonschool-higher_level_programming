#!/usr/bin/python3
"""
class square module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        constructor to initialize attributes
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Return the value of attributes"""
        sid = str(self.id)
        sx = str(self.x)
        sy = str(self.y)
        swd = str(self.width)
        strgn = "[Square] ({}) {}/{} - {}".format(sid, sx, sy, swd)
        return strgn

    @property
    def size(self):
        """Getter of size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter of size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """print with args"""
        if args:
            if len(args) == 1:
                self.id = args[0]
            else:
                self.id
            if len(args) == 2:
                self.id = args[0]
                self.size = args[1]
            else:
                self.size
            if len(args) == 3:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
            else:
                self.x
            if len(args) == 4:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            else:
                self.y
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
