"""
A test script to test the module funcs.py

Name: Tianli Xia
Date: Sep 8th, 2018
"""

import introcs      # For assert_equals and assert_true
import funcs        # This is what we are testing

# TEST PROCEDURE
def test_asserts():
    """
    This is a simple test procedure to help you understand how assert works
    """
    print('Testing the introcs asserts')
    introcs.assert_equals('b c', 'ab cd'[1:4])
    #introcs.assert_equals('b c', 'ab cd'[1:3])     # UNCOMMENT ONLY WHEN DIRECTED

    introcs.assert_true(3 < 4)
    introcs.assert_equals(3, 1+2)

    introcs.assert_equals(3.0, 1.0+2.0)
    introcs.assert_floats_equal(6.3, 3.1+3.2)
    #introcs.assert_equals(6.3, 3.1+3.2)            # UNCOMMENT ONLY WHEN DIRECTED

def test_has_a_vowel():
    print('Testing function has_a_vowel()')
    s= 'aeiou'
    result= funcs.has_a_vowel(s)
    introcs.assert_equals(True, result)


# SCRIPT CODE (Call Test Procedures here)
test_asserts()
test_has_a_vowel()
print('Module funcs is working correctly')
