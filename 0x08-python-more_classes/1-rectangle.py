#!/usr/bin/python3
""" a class that defines a rectangle"""


class Rectangle:
    """class rectangle definition"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    @property
    def width(self):
        """getter mthd for the private instance atribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter mthd for the private instance attribute width"""
        if type(value) == int:
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """getter for the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the private instance attribute height"""
        if type(value) == int:
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
        else:
            raise TypeError("height must be an integer")
