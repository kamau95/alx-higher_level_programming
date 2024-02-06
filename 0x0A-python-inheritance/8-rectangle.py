#!/bin/usr/python3
"""
class BaseGeometry (based on 5-base_geometry.py)
"""


class BaseGeometry:
    """ geometry class"""
    pass
    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates type and value of the value entered"""
        self.name = name
        self.value = value
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """ new child class rectangle"""
    pass
    def __init__(self, width, height):
        """initializes attributes of the child class"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
