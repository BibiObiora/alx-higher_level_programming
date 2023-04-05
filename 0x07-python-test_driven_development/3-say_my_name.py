#!/usr/bin/python3
"""
  The function takes two parameters, first_name and last_name
"""

def say_my_name(first_name, last_name=""):
    """ The function prints a name by first_name and last_name.

        Args:
           first_name(str): The first name
           last_name(str): The last name

        Raises:
           TypeError: If either first_name or last_name is not a string

    """

    if not isinstance(first_name, str) or not isinstance(last_name, str):
    raise TypeError("first_name must be a string or last_name must be a string")
    
     print(f"My name is {first_name} {last_name}")
