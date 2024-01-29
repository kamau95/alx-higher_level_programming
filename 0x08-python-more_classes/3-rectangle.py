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
        if value < 0:
            raise ValueError("width must be >= 0")
        if type(value) is not int:
            raise TypeError("width must be an integer")
        self.__width = value

    @property
    def height(self):
        """getter for the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the private instance attribute height"""
        if value < 0:
            raise ValueError("height must be >= 0")
        if type(value) is not int:
            raise TypeError("height must be an integer")
        self.__height = value

    def area(self):
        """calculates area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """calculates the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            perimeter = 0
        else:
            perimeter = 2 * (self.width + self.height)
        return perimeter

    def __str__(self):
        """returns printable string representation of the rectangle"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width
                                for j in range(self.__height))
        return string
