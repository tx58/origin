"""
A module to show off hwo to recover from an error

You will notice that the functions have been broken up so that
we assign the computation to a variable before returning it.
This is so we can add trace statements to better visualize
the error here.

Author: Walker M. White
Date:   September 6, 2017 (Python 3 Version)
"""

def function_1(x,y):
    """
    Have function_2 do all the work
    """
    print('Starting function_1')
    result = 0 # try-except is like if-else.  Initialize a var for right scope
    try:
        print('Starting try')
        result = function_2(x,y)
        print('Completing try')
    except:
        print('Starting except')
        result = float('inf')
        print('Completing except')
    print('Completing function_1')
    return result


def function_2(x,y):
    """
    Have function_3 do all the work
    """
    print('Starting function_2')
    try:
        result = function_3(x,y)
    except:
        result = float('inf')
    print('Completing function_2')
    return result


def function_3(x,y):
    """Returns: x divided by y"""
    print('Starting function_3')
    result = x/y
    print('Completing function_3')
    return result


# Application Code
if __name__ == "__main__":
    print(function_1(1,0))
    print() # blank line
    #print(function_1(2,2))
    print('Module ran successfully')
