#!/usr/bin/python3
""" the 5-text_indentation mddule supplies one function,text_indentation(text)"""

def text_indentation(text):
    """  prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text(string): text to be printed

    Raises:
        TypeError:if the input text is not a string

    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 0
    for a in text:
        if flag == 0:
            if a == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if a == '?' or a == '.' or a == ':':
                print(a)
                print()
                flag = 0
            else:
                print(a, end="")
