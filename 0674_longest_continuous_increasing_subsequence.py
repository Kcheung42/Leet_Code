# ------------------------------------------------------------------------------
# Question:
# ------------------------------------------------------------------------------
# tags:
'''
674. Longest Continuous Increasing Subsequence
Easy

715

116

Add to List

Share
Given an unsorted array of integers, find the length of longest continuous
increasing subsequence (subarray).

Example 1:
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3. 
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one
where 5 and 7 are separated by 4.
Example 2:
Input: [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2], its length is 1. 
Note: Length of the array will not exceed 10,000.

'''

# ------------------------------------------------------------------------------
# Solutions
# ------------------------------------------------------------------------------

import unittest
from typing import *


class SolutionTwoPointer:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        '''
        i:0 1 2 3 4
        n:1 3 5 4 7
            l
                r
        '''

        n = len(nums)
        if n == 0:
            return 0

        l = 0
        r = 1
        result = 1
        while r < n:
            while r < n and nums[r] > nums[r - 1]:
                r += 1
            if r >= n: break
            if nums[r] <= nums[r - 1]:
                result = max(result, r - l)
                l = r
                r += 1
        result = max(result, r - l)
        return result


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0

        result = 1
        count = 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                count += 1
                result = max(result, count)
            else:
                count = 1

        result = max(result, count)
        return result


# ------------------------------------------------------------------------------
# Tests
# ------------------------------------------------------------------------------


class TestSolution(unittest.TestCase):
    def test_simple(self):
        nums = [1, 3, 5, 4, 7]

        s = SolutionTwoPointer()
        self.assertEqual(s.findLengthOfLCIS(nums), 3)

        s = Solution()
        self.assertEqual(s.findLengthOfLCIS(nums), 3)

    def test_simple2(self):
        nums = []
        s = SolutionTwoPointer()
        self.assertEqual(s.findLengthOfLCIS(nums), 0)

        s = Solution()
        self.assertEqual(s.findLengthOfLCIS(nums), 0)

    def test_simple3(self):
        nums = [1, 3, 5, 4, 2, 3, 4, 5]

        s = SolutionTwoPointer()
        self.assertEqual(s.findLengthOfLCIS(nums), 4)

        s = Solution()
        self.assertEqual(s.findLengthOfLCIS(nums), 4)


unittest.main(verbosity=2)
