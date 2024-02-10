#!/usr/bin/python3
"""
creating a function to read a file and print it on the standard output
"""


def read_file(filename=""):
    """reads a file and prints to stdout"""
    with open(filename, "r", encoding = "utf-8") as f:
        """line to read data"""
        print(f.read(), end="")
