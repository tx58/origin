"""
Unit test for module a1

When run as a script, this module invokes several procedures that
test the various functions in the module a1.

Author: YOUR NAME(S) AND NETID(S) HERE
Date:   THE DATE COMPLETED HERE
"""

import introcs
import a1

def testA():
    """
    Test procedure for urlread
    """
    print("Test the url is correct")
    a="USD"
    b="cny"
    c=1
    print(a1.passcurrency_response(a,b,c) )

def testB():
    """
    Test procedure for Part A
    """
    print("Test the function returns currency correctly.")
    a="USD"
    b="cny"
    c=1
    result=a1.exchange(a,b,c)
    introcs.assert_floats_equal(result, 6.8521)




testA()
testB()

print("Module a1 passed all tests")
