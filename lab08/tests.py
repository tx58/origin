"""
A unit test for Lab 8

Author: Walker M. White (wmw2)
Date:   October 20, 2018
"""
import introcs
import funcs
import pair


def test_lesser_than():
    """
    Test procedure for function lesser_than
    """
    print('Testing function lesser_than')
    thelist = [5, 9, 5, 7, 3, 10, 4]
    introcs.assert_equals(2,funcs.lesser_than(thelist,5))
    introcs.assert_equals(1,funcs.lesser_than(thelist,4))
    introcs.assert_equals(0,funcs.lesser_than(thelist,3))
    introcs.assert_equals(4,funcs.lesser_than(thelist,6))
    introcs.assert_equals(6,funcs.lesser_than(thelist,10))
    introcs.assert_equals(7,funcs.lesser_than(thelist,20))


def test_clamp():
    """
    Test procedure for function clamp
    """
    print('Testing function clamp')

    thelist = [-1, 1, 3, 5]
    funcs.clamp(thelist,0,4)
    introcs.assert_equals([0,1,3,4],thelist)

    thelist = [1, 3]
    funcs.clamp(thelist,0,4)
    introcs.assert_equals([1,3],thelist)

    thelist = [-1, 1, 3, 5]
    funcs.clamp(thelist,1,1)
    introcs.assert_equals([1,1,1,1],thelist)

    thelist = []
    funcs.clamp(thelist,0,4)
    introcs.assert_equals([],thelist)


def test_row_sums():
    """
    Test procedure for function row_sums
    """
    print('Testing function row_sums')
    result = funcs.row_sums([[0.8, 0.2], [0.6, 0.9], [0.4, 0.3]])
    introcs.assert_float_lists_equal([1.0, 1.5, 0.7],result)
    result = funcs.row_sums([[0.2, -0.6, 0.1], [0.9, 0.8, -1.0]])
    introcs.assert_float_lists_equal([-0.3, 0.7],result)
    result = funcs.row_sums([[0.4, 0.8, 0.5, 0.4]])
    introcs.assert_float_lists_equal([2.1],result)
    result = funcs.row_sums([[0.3], [0.5], [0.8], [0.4]])
    introcs.assert_float_lists_equal([0.3, 0.5, 0.8, 0.4],result)


def test_letter_grades():
    """
    Test procedure for function letter_grades
    """
    print('Testing function letter_grades')
    netids = ['wmw2', 'abc123', 'jms45', 'qoz15', 'xyz2345', 'jms46', 'jms47']
    grades = [ 55,     90,       85,      72,      100,       63,      77    ]
    actual = ['F',    'A',      'B',     'C',     'A',       'D',     'C'    ]

    inputs = dict(zip(netids[:1],grades[:1]))
    result = funcs.letter_grades(inputs)
    introcs.assert_equals(dict(zip(netids[:1],actual[:1])), result)
    introcs.assert_equals(dict(zip(netids[:1],grades[:1])), inputs)  # Check unmodified

    inputs = dict(zip(netids[:3],grades[:3]))
    result = funcs.letter_grades(inputs)
    introcs.assert_equals(dict(zip(netids[:3],actual[:3])), result)
    introcs.assert_equals(dict(zip(netids[:3],grades[:3])), inputs)  # Check unmodified

    inputs = dict(zip(netids[:5],grades[:5]))
    result = funcs.letter_grades(inputs)
    introcs.assert_equals(dict(zip(netids[:5],actual[:5])), result)
    introcs.assert_equals(dict(zip(netids[:5],grades[:5])), inputs)  # Check unmodified

    inputs = dict(zip(netids,grades))
    result = funcs.letter_grades(inputs)
    introcs.assert_equals(dict(zip(netids,actual)), result)
    introcs.assert_equals(dict(zip(netids,grades)), inputs)  # Check unmodified


def test_pair_init():
    """
    Test procedure for the initializer in the Pair class
    """
    print('Testing class Pair (__init__)')
    try:
        result = pair.Pair(1,2)
    except:
        introcs.quit_with_error('The initializer for Pair has the wrong number of parameters')

    introcs.assert_equals(pair.Pair, type(result))
    introcs.assert_true(hasattr(result,'first'))
    introcs.assert_true(hasattr(result,'second'))
    introcs.assert_equals(1, result.first )
    introcs.assert_equals(2, result.second)

    result = pair.Pair(3,5)
    introcs.assert_equals(pair.Pair, type(result))
    introcs.assert_equals(3, result.first )
    introcs.assert_equals(5, result.second)


def test_pair_sum():
    """
    Test procedure for the sum method in the Pair class
    """
    print('Testing class Pair (sum)')
    try:
        obj = pair.Pair(1,2)
    except:
        introcs.quit_with_error('The initializer for Pair has the wrong number of parameters')

    introcs.assert_true(hasattr(obj,'sum'))
    result = 0
    try:
        result = obj.sum()
    except:
        introcs.quit_with_error('The sum method has the wrong number of parameters')
    introcs.assert_equals(3,result)
    introcs.assert_equals(7,pair.Pair(3,4).sum())


### OPTIONAL EXERCISES ###

def test_uniques():
    """
    Test procedure for function uniques
    """
    print('Testing function uniques')
    thelist = [5, 9, 5, 7]
    introcs.assert_equals(3,funcs.uniques(thelist))

    thelist = [5, 5, 1, 'a', 5, 'a']
    introcs.assert_equals(3,funcs.uniques(thelist))

    thelist = [1, 2, 3, 4, 5]
    introcs.assert_equals(5,funcs.uniques(thelist))

    thelist = []
    introcs.assert_equals(0,funcs.uniques(thelist))

    # Make sure the function does not modify the original
    thelist = [5, 9, 5, 7]
    result  = funcs.uniques(thelist)
    introcs.assert_equals([5, 9, 5, 7],thelist)


def test_place_sums():
    """
    Test procedure for function place_sums
    """
    print('Testing function place_sums')

    table = [['I1','I2','I3'], [0.8, 0.2], [0.6, 0.9], [0.4, 0.3]]
    goal  = [['I1','I2','I3','Sum'], [0.8, 0.2, 1.0], [0.6, 0.9, 1.5], [0.4, 0.3, 0.7]]
    funcs.place_sums(table)
    introcs.assert_equals(goal[0],table[0])
    for pos in range(1,len(table)):
        introcs.assert_float_lists_equal(goal[pos],table[pos])

    table = [['I1','I2'], [0.2, -0.6, 0.1], [0.9, 0.8, -1.0]]
    goal  = [['I1','I2','Sum'], [0.2, -0.6, 0.1, -0.3], [0.9, 0.8, -1.0, 0.7]]
    funcs.place_sums(table)
    introcs.assert_equals(goal[0],table[0])
    for pos in range(1,len(table)):
        introcs.assert_float_lists_equal(goal[pos],table[pos])

    table = [['I1'], [0.4, 0.8, 0.5, 0.4]]
    goal  = [['I1','Sum'], [0.4, 0.8, 0.5, 0.4, 2.1]]
    funcs.place_sums(table)
    introcs.assert_equals(goal[0],table[0])
    for pos in range(1,len(table)):
        introcs.assert_float_lists_equal(goal[pos],table[pos])

    table = [['I1','I2','I3','I4'], [0.3], [0.5], [0.8], [0.4]]
    goal  = [['I1','I2','I3','I4','Sum'], [0.3, 0.3], [0.5, 0.5], [0.8, 0.8], [0.4, 0.4]]
    funcs.place_sums(table)
    introcs.assert_equals(goal[0],table[0])
    for pos in range(1,len(table)):
        introcs.assert_float_lists_equal(goal[pos],table[pos])


def test_average_grade():
    """
    Test procedure for function average_grade
    """
    print('Testing function average_grade')
    netids = ['wmw2', 'abc123', 'jms45', 'qoz15', 'xyz2345', 'jms46', 'jms47']
    grades = [ 55,     90,       85,      72,      100,       63,      77    ]

    inputs = dict(zip(netids[:1],grades[:1]))
    result = funcs.average_grade(inputs)
    introcs.assert_floats_equal(55.0,result)
    introcs.assert_equals(dict(zip(netids[:1],grades[:1])), inputs)  # Check unmodified

    inputs = dict(zip(netids[:3],grades[:3]))
    result = funcs.average_grade(inputs)
    introcs.assert_floats_equal(76.666666667,result)
    introcs.assert_equals(dict(zip(netids[:3],grades[:3])), inputs)  # Check unmodified

    inputs = dict(zip(netids[:5],grades[:5]))
    result = funcs.average_grade(inputs)
    introcs.assert_floats_equal(80.4,result)
    introcs.assert_equals(dict(zip(netids[:5],grades[:5])), inputs)  # Check unmodified

    inputs = dict(zip(netids,grades))
    result = funcs.average_grade(inputs)
    introcs.assert_floats_equal(77.428571428,result)
    introcs.assert_equals(dict(zip(netids,grades)), inputs)  # Check unmodified


# Script code
if __name__ == '__main__':
    test_lesser_than()
    test_clamp()
    test_row_sums()
    test_letter_grades()
    test_pair_init()
    test_pair_sum()

    # UNCOMMENT ANY OPTIONAL ONES YOU DO
    #test_uniques()
    #test_place_sums()
    #test_average_grade()
    print('Lab 8 is working correctly')
