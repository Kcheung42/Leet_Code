#------------------------------------------------------------------------------
# Questions: 0053_maximum_subarray.py
#------------------------------------------------------------------------------
# tags:
'''
Given an integer array nums, find the contiguous subarray
(containing at least one number) which has the largest sum and
return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *

class Solution:
# Time = O(n)
# Space = O(n)
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        res = dp[0] = nums[0]
        for i in range(1, n-1):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
            res = max(dp[i], res)
        return res

    def maxSubArrayList(self, nums: List[int]) -> int:
            n = len(nums)
            dp = [0] * n
            max_sum = dp[0] = nums[0]
            start = end = 0
            for i in range(1, n-1):
                dp[i] = max(dp[i-1] + nums[i], nums[i])
                start = i if nums[i] > (dp[i-1] + nums[i]) and dp[i] > max_sum else start
                end = i if dp[i] > max_sum else end
                max_sum = max(dp[i], max_sum)
            return nums[start:end+1]


import unittest

#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
class TestSolution1(unittest.TestCase):
    def test_simple(self):
        nums = [-2,1,-3,4,-1,2,1,-5,4]
        s = Solution()
        self.assertEqual(s.maxSubArray(nums), 6)
        self.assertEqual(s.maxSubArrayList(nums), [4,-1,2,1])

    def test_simple2(self):
        nums = [-2,1,-3,-1]
        s = Solution()
        self.assertEqual(s.maxSubArray(nums), 1)


unittest.main()
