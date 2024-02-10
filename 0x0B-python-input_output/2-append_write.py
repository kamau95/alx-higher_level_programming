#!/usr/bin/python3
"""
contains a function to append str to a file
"""


def append_write(filename="", text=""):
    """"appends a str to a file"""
    with open(filename, "a", encoding = "utf-8") as f:
        return f.write(text)
