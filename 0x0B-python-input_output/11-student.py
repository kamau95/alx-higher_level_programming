#!/usr/bin/python3
"""
here you find class Student
"""


class Student:
    """outlook of the class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dict representation of instance"""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """ method to replace all instances of class student"""
        for key in json:
            try:
                setattr(self, key, json[key])
            except FileNotFoundError:
                pass
