#!/usr/bin/python3
""" 
This is the " 0-add_integer.py" module
The module supplies one function, add_integer(a, b).
"""


def add_integer(a, b=98):
    """ Returns the addition of two numbers a and b

    Check if a and b are integers or floats

    Raises:
     TypeError: if either of a or b is a non-integer and non-float.
     """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
