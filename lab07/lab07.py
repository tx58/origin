"""
A module with several recursive functions

Tianli Xia
Oct 17th
"""


# IMPLEMENT ALL OF THESE FUNCTIONS

def numberof(thelist, v):
    """
    Returns the number of times v occurs in thelist.

    Parameter thelist: The list to count from
    Precondition: thelist is a list of ints

    Parameter v: The value to count
    Precondition: v is an int
    """
    if (len(thelist)==0):
        return 0
    if (len(thelist)==1):
        if (thelist[0]==v):
            return 1
        else:
            return 0
    if (len(thelist)>1):
        return numberof(thelist[:len(thelist)//2], v)+ numberof(thelist[len(thelist)//2:], v)
    # HINT: Divide and conquer only applies to one of the arguments, not both


def replace(thelist,a,b):
    """
    Returns a COPY of thelist but with all occurrences of a replaced by b.

    Example: replace([1,2,3,1], 1, 4) = [4,2,3,4].

    Parameter thelist: The list to count from
    Precondition: thelist is a list of ints

    Parameter a: The value to replace
    Precondition: a is an int

    Parameter b: The value to replace with
    Precondition: b is an int
    """
    # HINT: Divide and conquer only applies to one of the arguments, not all three
    if (len(thelist)==0):
        return []
    if (len(thelist)==1):
        if (thelist[0]==a):
            return [b]
        else:
            return thelist
    if (len(thelist)>1):
        return replace(thelist[:len(thelist)//2], a,b)+ replace(thelist[len(thelist)//2:], a,b)


def remove_dups(thelist):
    """
    Returns a COPY of thelist with adjacent duplicates removed.

    Example: for thelist = [1,2,2,3,3,3,4,5,1,1,1]
    the answer is [1,2,3,4,5,1]

    Parameter thelist: The list to modify
    Precondition: thelist is a list of ints
    """
    # HINT: You can still do this with divide-and-conquer
    # The tricky part is combining the answers
    if len(thelist)>1:
        if thelist[0] != thelist[1]:
            return [thelist[0]] + remove_dups(thelist[1:])
        else:
            del(thelist[1])
            return remove_dups(thelist)
    else:
        return thelist
    # Stub return.  Replace this.


def oddsevens(thelist):
    """
    Returns a COPY of the list with odds at front, evens in the back.

    Odd numbers are in the same order as thelist. Evens are reversed.

    Example:
        oddsevens([3,4,5,6]) returns [3,5,6,4].
        oddsevens([2,3,4,5,6]) returns [3,5,6,4,2].
        oddsevens([1,2,3,4,5,6]) returns [1,3,5,6,4,2].

    Parameter thelist: The list to modify
    Precondition: thelist is a list of ints (may be empty)
    """
    # HINT: How you break up the list is important.  A bad division will
    # make it almost impossible to combine the answer together.
    # However, if you look at all three examples in the specification you
    # will see a pattern that should help you define the recursion.
    # Stub return.  Replace this.
    if len(thelist)>1:
        if (thelist[0] % 2==0) :
            return oddsevens(thelist[1:]) + [thelist[0]]
        else:
            return  [thelist[0]]+ oddsevens(thelist[1:])
    else:
        return thelist

# OPTIONAL EXERCISES

def number_not(thelist, v):
    """
    Returns the number of elements in seq that are NOT v.

    Parameter thelist: the list to search
    Precondition: thelist is a list of ints

    Parameter v: the value to search for
    Precondition: v is an int
    """
    return 0 # Stub return.  Replace this.


def remove_first(thelist, v):
    """
    Returns a COPY of thelist but with the FIRST occurrence of v removed (if present).

    Note: This can be done easily using index. Don't do that.
    Do it recursively.

    Parameter thelist: the list to search
    Precondition: thelist is a list of ints

    Parameter v: the value to search for
    Precondition: v is an int
    """
    return [] # Stub return.  Replace this.


def sum_list(thelist):
    """
    Returns the sum of the integers in list l.

        Example: sum_list([34]) is 34
        Example: sum_list([7,34,1,2,2]) is 46

    Parameter thelist: the list to sum
    Precondition: thelist is a list of ints
    """
    if (len(thelist)==0):
        return 0
    if (len(thelist)==1):
        return thelist[0]
    if (len(thelist)==2):
        return thelist[0]+thelist[1]
    if (len(thelist)>2):
        return sum_list(thelist[:len(thelist)//2])+ sum_list(thelist[len(thelist)//2:])


def flatten(thelist):
    """
    Returns a COPY of thelist flattened to remove all nested lists

    Flattening takes any nested list and recursively dumps its contents into the
    parent list.

    Examples:
        flatten([[1,2],[3,4]]) is [1,2,3,4]
        flatten([[1,[2,3]],[[4],[5,[6,7]]]]) is [1,2,3,4,5,6,7]
        flatten([1,2,3]) is [1,2,3]

    Parameter thelist: the list to flatten
    Precondition: thelist is a list of either ints or lists which satisfy the precondition
    """
    return [] # Stub return.  Replace this


### Numeric Examples ###

def sum_to(n):
    """
    Returns the sum of numbers 1 to n.

        Example: sum_to(3) = 1+2+3 = 6,
        Example: sum_to(5) = 1+2+3+4+5 = 15

    Parameter n: the number of ints to sum
    Precondition: n >= 1 is an int.
    """
    return 0 # Stub return.  Replace this.


def num_digits(n):
    """
    Returns the number of the digits in the decimal representation of n.

        Example: num_digits(0) = 1
        Example: num_digits(3) = 1
        Example: num_digits(34) = 2
        Example: num_digits(1356) = 4

    Parameter n: the number to analyze
    Precondition: n >= 0 is an int
    """
    return 0 # Stub return.  Replace this.


def sum_digits(n):
    """
    Returns the sum of the digits in the decimal representation of n.

        Example: sum_digits(0) = 0
        Example: sum_digits(3) = 3
        Example: sum_digits(34) = 7
        Example: sum_digits(345) = 12

    Parameter n: the number to analyze
    Precondition: n >= 0 is an int.
    """
    return 0 # Stub return.  Replace this.


def number2(n):
    """
    Returns the number of 2's in the decimal representation of n.

        Example: number2(0) = 0
        Example: number2(2) = 1
        Example: number2(234252) = 3

    Parameter n: the number to analyze
    Precondition: n >= 0 is an int.
    """
    return 0 # Stub return.  Replace this.


def into(n, c):
    """
    Returns the number of times that c divides n,

        Example: into(5,3) = 0 because 3 does not divide 5.
        Example: into(3*3*3*3*7,3) = 4.

    Parameter n: the number to analyze
    Precondition: n >= 1 is an int

    Parameter c: the number to divide by
    Precondition: c > 1 are ints.
    """
    if (n % c== 0):
        return 1+into(n/c, c) # Stub return.  Replace this.
    else:
        return 0
