"""
Unit test script for Lab 7

Authors: Walker M. White (wmw2), Lillian Lee (ljl2)
Date:    October 10, 2018
"""
import introcs
import lab07


def test_sum_list():
    """
    Tests for function sum_list
    """
    introcs.assert_equals(0,  lab07.sum_list([]))
    introcs.assert_equals(34, lab07.sum_list([34]))
    introcs.assert_equals(46, lab07.sum_list([7,34,1,2,2]))


def test_numberof():
    """
    Tests for function numberof
    """
    mylist = [5, 3, 3455, 74, 74, 74, 3]
    introcs.assert_equals(0, lab07.numberof([],4))
    introcs.assert_equals(1, lab07.numberof([4],4))
    introcs.assert_equals(3, lab07.numberof(mylist,74))
    introcs.assert_equals(2, lab07.numberof(mylist,3))
    introcs.assert_equals(0, lab07.numberof(mylist,4))


def test_replace():
    """
    Tests for function replace
    """
    mylist = [5, 3, 3455, 74, 74, 74, 3]
    introcs.assert_equals([],  lab07.replace([], 1, 2))
    introcs.assert_equals([4], lab07.replace([5],5,4))
    introcs.assert_equals([5, 20, 3455, 74, 74, 74, 20], lab07.replace(mylist,3, 20))
    introcs.assert_equals([5, 3, 3455, 74, 74, 74, 3],   lab07.replace(mylist, 1, 3))

    # test for whether the code is really returning a copy of the original list
    introcs.assert_equals([5, 3, 3455, 74, 74, 74, 3], mylist)
    introcs.assert_equals(False, mylist is lab07.replace(mylist, 1, 3))


def test_remove_dups():
    """
    Tests for function remove_dups
    """
    mylist = [1,2,2,3,3,3,4,5,1,1,1]
    introcs.assert_equals([],  lab07.remove_dups([]))
    introcs.assert_equals([3], lab07.remove_dups([3,3]))
    introcs.assert_equals([4], lab07.remove_dups([4]))
    introcs.assert_equals([5], lab07.remove_dups([5, 5]))
    introcs.assert_equals([1,2,3,4,5,1], lab07.remove_dups(mylist))

    # test for whether the code is really returning a copy of the original list
    introcs.assert_equals([1,2,2,3,3,3,4,5,1,1,1], mylist)
    introcs.assert_equals(False, mylist is lab07.remove_dups(mylist))


### OPTIONAL EXERCISES ###

# Sequences Examples #

def test_number_not():
    """
    Tests for function number_not
    """
    mylist = [5, 3, 3455, 74, 74, 74, 3]
    introcs.assert_equals(0, lab07.number_not([],4))
    introcs.assert_equals(0, lab07.number_not([4],4))
    introcs.assert_equals(4, lab07.number_not(mylist,74))
    introcs.assert_equals(5, lab07.number_not(mylist,3))
    introcs.assert_equals(7, lab07.number_not(mylist,4))


def test_remove_first():
    """
    Tests for function remove_first
    """
    introcs.assert_equals([],  lab07.remove_first([],3))
    introcs.assert_equals([],  lab07.remove_first([3],3))
    introcs.assert_equals([3], lab07.remove_first([3],4))
    introcs.assert_equals([3, 4, 4, 5],    lab07.remove_first([3, 4, 4, 4, 5],4))
    introcs.assert_equals([3, 5, 4, 4, 4], lab07.remove_first([3, 4, 5, 4, 4, 4],4))

def test_oddsevens():
    """
    Tests for function oddsevens
    """
    mylist = [1,2,3,4,5,6]
    introcs.assert_equals([],     lab07.oddsevens([]))
    introcs.assert_equals([3],    lab07.oddsevens([3]))
    introcs.assert_equals([3,4],  lab07.oddsevens([4,3]))
    introcs.assert_equals([-1,1,2,0],    lab07.oddsevens([-1,0,1,2]))
    introcs.assert_equals([1,3,5,6,4,2], lab07.oddsevens(mylist))

    # test for whether the code is really returning a copy of the original list
    introcs.assert_equals([1,2,3,4,5,6], mylist)
    introcs.assert_equals(False, mylist is lab07.oddsevens(mylist))


def test_flatten():
    """
    Tests for function flatten
    """
    introcs.assert_equals([],  lab07.flatten([]))
    introcs.assert_equals([3], lab07.flatten([3]))
    introcs.assert_equals([3], lab07.flatten([[3]]))
    introcs.assert_equals([1,2,3,4], lab07.flatten([[1,2],[3,4]]))
    introcs.assert_equals([1,2,3,4,5,6,7], lab07.flatten([[1,[2,3]],[[4,[5,6]],7]]))
    introcs.assert_equals([1,2,3], lab07.flatten([1,2,3]))
    introcs.assert_equals([],  lab07.flatten([[[]],[]]))


def test_sum_to():
    """
    Tests for function sum_to
    """
    introcs.assert_equals(1,  lab07.sum_to(1))
    introcs.assert_equals(6,  lab07.sum_to(3))
    introcs.assert_equals(15, lab07.sum_to(5))


def test_num_digits():
    """
    Tests for function num_digits
    """
    introcs.assert_equals(1, lab07.num_digits(0))
    introcs.assert_equals(1, lab07.num_digits(3))
    introcs.assert_equals(2, lab07.num_digits(34))
    introcs.assert_equals(4, lab07.num_digits(1356))


def test_sum_digits():
    """
    Tests for function sum_digits
    """
    introcs.assert_equals(0,  lab07.sum_digits(0))
    introcs.assert_equals(3,  lab07.sum_digits(3))
    introcs.assert_equals(7,  lab07.sum_digits(34))
    introcs.assert_equals(12, lab07.sum_digits(345))


def test_number2():
    """
    Tests for function number2
    """
    introcs.assert_equals(0, lab07.number2(0))
    introcs.assert_equals(1, lab07.number2(2))
    introcs.assert_equals(2, lab07.number2(232))
    introcs.assert_equals(0, lab07.number2(333))
    introcs.assert_equals(3, lab07.number2(234252))


def test_into():
    """
    Tests for function into
    """
    introcs.assert_equals(0, lab07.into(5, 3))
    introcs.assert_equals(1, lab07.into(6, 3))
    introcs.assert_equals(2, lab07.into(9, 3))
    introcs.assert_equals(2, lab07.into(18, 3))
    introcs.assert_equals(4, lab07.into(3*3*3*3*7,3))


# Script Code
if __name__ == '__main__':
    test_sum_list()
    test_numberof()
    test_replace()
    test_remove_dups()

    # UNCOMMENT ANY OPTIONAL ONES YOU DO
    #test_number_not()
    #test_remove_first()
    #test_oddsevens()
    #test_flatten()
    #test_sum_to()
    #test_num_digits()
    #test_sum_digits()
    #test_number2()
    #test_into()
    print('Module lab07 is working correctly')
