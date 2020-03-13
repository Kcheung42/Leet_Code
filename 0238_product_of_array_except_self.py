#------------------------------------------------------------------------------
# Question: 0238_product_of_array_except_self.py
#------------------------------------------------------------------------------
# tags:[medium, array]
'''
Given an array nums of n integers where n > 1,  return an array
output such that output[i] is equal to the product of all the elements of nums
except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or
suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not
count as extra space for the purpose of space complexity analysis.)

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

    Input:  [4,5,1,8,2]
    Output: [80, 64, 320, 40, 160]

    n = [4  5  1   8  2]
    L = [1  4  20 20 160]
    R = [80  16 16  2 1]
    Result[i] = L[i] * R[i]
    '''
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        L = [1] * n
        R = [1] * n
        for i in range(1, n):
            L[i] = nums[i-1] * L[i-1]
        for i in range(n - 2, -1, -1):
            R[i] = nums[i+1] * R[i+1]
        result = [L[i] * R[i] for i in range(n)]
        return (result)


class Solution2:
    '''
    Time: O(n)
    Space: O(1)
    '''
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1]
        for i in range(1, n):
            ans = ans + [nums[i - 1] * ans[-1]]
        R = 1
        for i in range(n - 2, -1, -1):
            R *= nums[i + 1]
            ans[i] *= R
        return (ans)


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest


class TestSolution(unittest.TestCase):
    def test_simple(self):
        s = Solution()
        nums = [4, 5, 1, 8, 2, 10, 6]
        result = s.productExceptSelf(nums)
        self.assertEqual(result, [4800, 3840, 19200, 2400, 9600, 1920, 3200])

    def test_simple2(self):
        s = Solution()
        nums = [4, 5, 1, 8, 2]
        result = s.productExceptSelf(nums)
        self.assertEqual(result, [80, 64, 320, 40, 160])


class TestSolution2(unittest.TestCase):
    def test_simple2(self):
        s = Solution2()
        nums = [4, 5, 1, 8, 2]
        result = s.productExceptSelf(nums)
        self.assertEqual(result, [80, 64, 320, 40, 160])


unittest.main(verbosity=2)
