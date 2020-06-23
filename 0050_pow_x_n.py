#------------------------------------------------------------------------------
# Questions 0050_pow_x_n.py
#------------------------------------------------------------------------------
# tags: #medium
'''
Implement pow(x, n), which calculates x raised to the power n (x**n).

Example 1:
Input: 2.00000, 10
Output: 1024.00000

Example 2:
Input: 2.10000, 3
Output: 9.26100

Example 3:
Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

'''

def pow(x, n):
    ans = 1
    for i in range(n):
        ans = ans * x
    return ans

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *
from functools import reduce

class Solution:
    '''
    Brute Force
    Time: O(N)
    Space: O(1)
    '''
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        for i in range(n):
            ans = ans * x
        return ans


class SolutionRecurFast:
    '''
    Fast Pow: Recursion
    Time: O(log n)
    Space: O(1)

    Intuition: Given x^n to get x^2n we can (x^n)^2 instead of having to multiply
    x by n more times. Using this idea, go backwards from n to find the half.
    '''
    def myPow(self, x: float, n: int) -> float:
        def powHelper(x, n):
            if n == 0:
                return 1
            half = powHelper(x,n // 2)
            if n % 2 == 0:
                return half * half
            else:
                return half * half * x
        if n < 0:
            x = 1 // x
            n = -n
        return powHelper(x,n)


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        x = 2.0000
        n = 10
        s = Solution()
        self.assertEqual(s.myPow(x, n), 1024.0)

        s = SolutionRecurFast()
        self.assertEqual(s.myPow(x, n), 1024.0)


unittest.main(verbosity=2)

