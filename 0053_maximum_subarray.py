#------------------------------------------------------------------------------
# Questions: 0053_maximum_subarray.py
#------------------------------------------------------------------------------
# tags: Easy
'''
Given an integer array nums, find the contiguous subarray
(containing at least one number) which has the largest sum and
return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Followup:
How to Return the indexes of the max sum Array
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
        max_sum = dp[0] = nums[0]
        for i in range(1, n-1):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
            max_sum = max(dp[i], max_sum)
        return max_sum


    def maxSubArrayList(self, nums: List[int]) -> int:
        """Returns List"""
        n = len(nums)
        dp = [0] * n
        max_sum = dp[0] = nums[0]
        start = end = 0
        for i in range(1, n-1):
            include_prev = dp[i-1] + nums[i]
            cur = nums[i]
            if include_prev > cur:
                dp[i] = include_prev
                if dp[i] > max_sum:
                    max_sum = dp[i]
                    end = i
            else:
                start = i
                dp[i] = cur

            #Same as above
            # dp[i] = max(dp[i-1] + nums[i], nums[i])
            # start = i if nums[i] > (dp[i-1] + nums[i]) and dp[i] > max_sum else start
            # end = i if dp[i] > max_sum else end
            # max_sum = max(dp[i], max_sum)
        return nums[start:end+1]

    #followup
    # If you have figured out the O(n) solution,
    # try coding another solution using the divide
    # and conquer approach, which is more subtle.



#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

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
