#------------------------------------------------------------------------------
# Question: 0152_maximum_product_subarray.py
#------------------------------------------------------------------------------
# tags: Medium
'''
Given an integer array nums, find the contiguous subarray within an array
(containing at least one number) which has the largest product.

Example 1:

Input:
[2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *

class Solution:
    '''
    Time:
    Space:

    num:[2,3,-2,3,-4,5,-6]
    idx:[0 1  2 3        ]

    num:[-2,-3,-4,-5]
    '''
    def maxProduct(self, A):
        B = A[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i - 1] or 1
            B[i] *= B[i - 1] or 1
        print(A)
        print(B)
        print(A + B)
        return max(A + B)
    # def maxProduct(self, nums: List[int]) -> int:
    #     n  = len(nums)
    #     if n == 1:
    #         return nums[0]
    #     stack = []
    #     tally = 0
    #     cur = total = 1
    #     max_prod = float("-inf")
    #     for n in nums:
    #         total *= n
    #         if n > 0:
    #             cur *= n
    #             max_prod = (max(cur, max_prod))
    #             stack.append(n)
    #         else:
    #             tally += 1
    #             if tally % 2 == 0: #process stack
    #                 max_prod = (max(total, max_prod))
    #                 cur = max_prod
    #             else:
    #                 cur = 1
        # return max_prod


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        s = Solution()
        nums = [2,3,-2,3,-4,5,-6]
        self.assertEqual(s.maxProduct(nums), 720)

    def test_simple2(self):
        s = Solution()
        nums = [2,3,-2,4,5,6]
        self.assertEqual(s.maxProduct(nums), 6)

    def test_simple3(self):
        s = Solution()
        nums = [-2,0,-1]
        self.assertEqual(s.maxProduct(nums), 0)

    def test_simple4(self):
        s = Solution()
        nums = [-2]
        self.assertEqual(s.maxProduct(nums), -2)

    def test_simple5(self):
        s = Solution()
        nums = [-2,-3]
        self.assertEqual(s.maxProduct(nums), 6)

    def test_simple6(self):
        s = Solution()
        nums = [-2,-3,-4,-5]
        self.assertEqual(s.maxProduct(nums), 120)


unittest.main(verbosity=2)

