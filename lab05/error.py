"""
A module to show off what happens when an error occurs

Author: Walker M. White
Date:   September 6, 2017 (Python 3 Version)
"""


def function_1(x,y):
    """
    Have function_2 do all the work
    """
    return function_2(x,y)


def function_2(x,y):
    """
    Have function_3 do all the work
    """
    return function_3(x,y)


def function_3(x,y):
    """
    Returns: x divided by y
    """
    #assert y < 2, 'This is my error'
    return x/y


# Script Code
if __name__ == "__main__":
    #print(function_1(2,3))
    print(function_1(1,0))