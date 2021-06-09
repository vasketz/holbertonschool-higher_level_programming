#!/usr/bin/python3
"""
class rectangle module the inherist from Base
file in the models folder
"""
from models.base import Base


class Rectangle(Base):
    """
    class rectangle that inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        class constructor to initialize
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter of width"""
        if isinstance(value, int):
            self.__width = value
        else:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        """Getter of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter of height"""
        if isinstance(value, int):
            self.__height = value
        else:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        """Getter of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter of x"""
        if isinstance(value, int):
            self.__x = value
        else:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        """Getter of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter of y"""
        if isinstance(value, int):
            self.__y = value
        else:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

    def area(self):
        """Calculate the area"""
        return self.__height * self.__width

    def display(self):
        """Prints to the stdout #"""
        for coly in range(self.__y):
            print("")
        for col in range(self.__height):
            for rowx in range(self.__x):
                print(" ", end="")
            for row in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """Return the value of attributes"""
        sid = str(self.id)
        sx = str(self.__x)
        sy = str(self.__y)
        shg = str(self.__height)
        swd = str(self.__width)
        strgn = "[Rectangle] ({}) {}/{} - {}/{}".format(sid, sx, sy, swd, shg)
        return strgn

    def update(self, *args, **kwargs):
        """print with args"""
        if args:
            if len(args) == 1:
                self.id = args[0]
            else:
                self.id
            if len(args) == 2:
                self.width = args[1]
            else:
                self.width
            if len(args) == 3:
                self.height = args[2]
            else:
                self.height
            if len(args) == 4:
                self.x = args[3]
            else:
                self.x
            if len(args) == 5:
                self.y = args[4]
            else:
                self.y
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
