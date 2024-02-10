#!/usr/bin/python3
"""
contains a function(save_to_json_file) that writes an Object to a text file,in JSON representation
Args:
    - obj: The Python object to be saved.
    - filename: The name of the file where the object will be saved.
"""


import json


def save_to_json_file(my_obj, filename):
    """Object to a text file, using a JSON representation"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
