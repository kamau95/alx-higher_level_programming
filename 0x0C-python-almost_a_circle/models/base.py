#!/usr/bin/python3
"""
will contain a class called base
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
