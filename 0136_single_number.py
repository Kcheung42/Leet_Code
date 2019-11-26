#------------------------------------------------------------------------------
# Question:
#------------------------------------------------------------------------------
# tags:
'''
Given a non-empty array of integers, every element appears twice except for
one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement
it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *
import functools

class Solution:
    '''
    Time: O(n)
    Space: O(n)
    '''
    def singleNumber(self, nums: List[int]) -> int:
        h = {}
        for n in nums:
            h[n] = False if n not in h else not(h[n])
        single = [n for n in h if h[n] is False]
        return(single[0])

class Solution2:
    '''
    Time: O(n)
    Space: O(n)
    '''
    def singleNumber(self, nums: List[int]) -> int:
        bit = 0
        for n in nums:
            bit ^= n
        return bit
        # return functools.reduce(lambda x,y: x^y, nums)

#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        nums = [2,2,1]
        s = Solution()
        self.assertEqual(s.singleNumber(nums), 1)

        s = Solution2()
        self.assertEqual(s.singleNumber(nums), 1)

    def test_simple2(self):
        nums = [4,1,2,1,2]
        s = Solution()
        self.assertEqual(s.singleNumber(nums), 4)

        s = Solution2()
        self.assertEqual(s.singleNumber(nums), 4)



unittest.main(verbosity=2)

