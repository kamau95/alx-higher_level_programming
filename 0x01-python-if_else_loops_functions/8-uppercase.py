#!/usr/bin/python3

def uppercase(input_str):
    output_str = ""

    for char in input_str:
        if 97 <= ord(char) <= 122:  # Check if character is lowercase
            output_str += chr(ord(char) - 32)
        else:
            output_str += char  # Keep non-alphabetic characters unchanged

    print(output_str)
