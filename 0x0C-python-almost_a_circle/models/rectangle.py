#!/usr/bin/python3
"""
will contain parent class base
"""


class Base:
    """ my bas e class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Check if id is provided"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


class Rectangle(Base):
    """
    Rectangle class that inherits from
    the base class- inherits from the bae class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize the Rectangle class
        with width, height, and optional ID
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    """
    setter and getter methods
    for width, height, x, and y...
    """
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
