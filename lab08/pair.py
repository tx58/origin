"""
The class definition for Lab 8

The class Pair should have exactly two methods in it: __init__ and sum.  The __init__
method should initialize the first and second attributes.  The sum method returns the
sum of these two attributes.

Initial skeleton by W. White (wmw2)

Tianli Xia
Oct 21th, 2018
"""


class Pair(object):
    """
    A class representing a pair of values.

    INSTANCE ATTRIBUTES:
        first:  The first value [an int]
        second: The second value [an int]

    This class has a single method: sum() which returns the sum of first and second.
    """
    def __init__(self,a,b):
        self.first= a
        self.second= b

    def sum(self):
        return self.first + self.second
