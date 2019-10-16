#------------------------------------------------------------------------------
# Question: 0788_rotated_digits.py
#------------------------------------------------------------------------------
# tags: Easy
'''
X is a good number if after rotating each digit individually by 180 degrees,
we get a valid number that is different from X.  Each digit must be rotated -
 we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. 0, 1, and 8
rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each other,
and the rest of the numbers do not rotate to any other number and become invalid.

Now given a positive number N, how many numbers X from 1 to N are good?

Example:
Input: 10
Output: 4

Explanation:
There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.

'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *

class Solution:
    '''
    Time:
    Space:
    '''
    def rotatedDigits(self, N):
        def isValidRotation(num):
            return (not any(s in {'3', '4', '7'} for s in num)) and any(s in {'2', '5', '6', '9'} for s in num)
        return sum([isValidRotation(str(i)) for i in range(1, N+1)])


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        n = 10
        s = Solution()
        self.assertEqual(s.rotatedDigits(n), 4)


unittest.main(verbosity=2)
