"""
The list functions for Lab 8

These functions all require for-loops.

Initial skeleton by W. White (wmw2)

Tianli Xia
Oct 21th, 2018
"""


# IMPLEMENT ALL OF THESE FUNCTIONS

def lesser_than(alist,value):
    """
    Returns the number of elements in alist strictly less than value

    Example: lesser_than([5, 9, 1, 7], 6) evaluates to 2

    Parameter alist: the list to check (WHICH SHOULD NOT BE MODIFIED)
    Precondition: alist is a list of ints

    Parameter value:  the value to compare to the list
    Precondition:  value is an int
    """
    return sum([x< value for x in alist])


def clamp(alist,a,b):
    """
    MODIFIES the list so that every element is between min and max.

    Any number in the list less than min is replaced with min.  Any number
    in the list greater than max is replaced with max. Any number between
    min and max is left unchanged.

    This is a PROCEDURE. It modifies alist, but does not return a new list.

    Example: if alist is [-1, 1, 3, 5], then clamp(thelist,0,4) changes
    alist to have [0,1,3,4] as its contents.

    Parameter alist: the list to modify
    Precondition: alist is a list of numbers (float or int)

    Parameter min: the minimum value for the list
    Precondition: min <= max is a number

    Parameter max: the maximum value for the list
    Precondition: max >= min is a number
    """
    return [max(min(x, b),a) for x in alist]

def row_sums(table):
    """
    Returns a list that is the sum of each row in a table.

    This function assumes that table has no header, so each row has only
    numbers in it.

    Example: row_sums([[0.1, 0.3, 0.5], [0.6, 0.2, 0.7], [0.5, 1.1, 0.1]])
    returns [0.8, 1.5, 1.7]

    Example: row_sums([[0.2, 0.1], [-0.2, 0.1], [0.2, -0.1], [-0.2, -0.1]])
    returns [0.3, -0.1, 0.1, -0.3]

    Parameter table: the nested list to process
    Precondition: table is a table of numbers with no header.  In other words,
    (1) table is a nested 2D list in row-major order, (2) each row contains
    only numbers, and (3) each row is the same length.
    """
    return [sum(x) for x in table]


def letter_grades(adict):
    """
    Returns a new dictionary with the letter grades for each student.

    The dictionary adict has netids for keys and numbers 0-100 for values.
    These represent the grades that the students got on the exam.  This function
    returns a new dictionary with netids for keys and letter grades (strings)
    for values.  Our cut-off is 90 for an A, 80 for a B, 70 for a C, 60 for a
    D.  Anything below 60 is an F.

    Example:  letter_grades({'wmw2' : 55, 'abc3' : 90, 'jms45': 86}) evaluates
    to {'wmw2' : 'F, 'abc3' : 'A', 'jms45': 'B'}.

    Parameter adict: the dictionary of grades
    Precondition: alist is a list of ints
    """
    # HINT: You will need a dictionary that acts as an accumulator
    # Start with result = {}.  Then add to this dictionary.
    return {a: grade_convert(b) for [a,b] in adict.items()}

def grade_convert(grade):
    '''
    Returns a new letter grade
    '''
    if grade>=90:
        return 'A'
    elif grade>=80:
        return 'B'
    elif grade>=70:
        return 'C'
    elif grade>=60:
        return 'D'
    else:
        return 'F'

### OPTIONAL EXERCISES ###

def uniques(alist):
    """
    Returns the number of unique elements in the list.

    Example: uniques([5, 9, 5, 7]) evaluates to 3
    Example: uniques([5, 5, 1, 'a', 5, 'a']) evaluates to 3

    Parameter alist: the list to check (WHICH SHOULD NOT BE MODIFIED)
    Precondition: alist is a list.
    """
    # Create a copy with no duplicates
    # return len([y for x,y in enumerate(alist) if alist.index(y)==x])
    return len([x for x,y in zip(alist, range(len(alist))) if alist.index(x)==y])


def place_sums(tables):
    """
    MODIFIES the table to add a column summing the previous elements in the row.

    This function assumes that table has no header, which means the first row
    only has strings in it.  The later rows are only numbers.  This function
    adds the string 'Sum' to the first row.  For each later row, it appends the
    sum of that row.

    This is a PROCEDURE. It modifies the table, but does not return a new table.

    Example: Suppose that a is

        [['First', 'Second', 'Third'], [0.1, 0.3, 0.5], [0.6, 0.2, 0.7], [0.5, 1.1, 0.1]]

    then place_sums(a) modifies the table a so that it is now

         [['First', 'Second', 'Third', 'Sum'],
         [0.1, 0.3, 0.5, 0.8], [0.6, 0.2, 0.7, 1.5], [0.5, 1.1, 0.1, 1.7]]

    Parameter table: the nested list to process
    Precondition: table is a table of numbers with a header.  In other words,
    (1) table is a nested 2D list in row-major order, (2) the first row only
    contains strings (the headers) (3) each row after the first contains only
    numbers, and (4) each row is the same length.
    """
    tables[0].append('Sum')
    for row in tables[1:]:
        row.append(sum(row))
    return tables


def average_grade(adict):
    """
    Returns the average grade among all students.

    The dictionary adict has netids for keys and numbers 0-100 for values.
    These represent the grades that the students got on the exam.  This function
    averages those grades and returns a value.

    Example:  letter_grades({'wmw2' : 55, 'abc3' : 90, 'jms45': 86}) evaluates
    to (55+90+86)/3 = 77.

    Parameter adict: the dictionary of grades
    Precondition: alist is a list of ints
    """
    # Hint: This needs two accumulators.
    # One for the sum, and one for the total to divide by.
    return sum(adict.values())/len(adict.values())
