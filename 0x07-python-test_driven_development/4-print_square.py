#!/usr/bin/python3
""" a function that prints a square with the character #."""



def print_square(size):
    """ Prints a squre with # character"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        print(("#" * size + "\n") * size, end="")
