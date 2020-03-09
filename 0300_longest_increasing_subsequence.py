#------------------------------------------------------------------------------
# Question: 0300_longest_increasing_subsequence.py
#------------------------------------------------------------------------------
# tags:
'''
Given an unsorted array of integers, find the length of longest increasing
subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the
length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to
return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?


'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *
from test_utils.debug import debug

class Solution:
    '''
    Time: O(2^n)
    Space: O(n^2)
    '''
    def LIS(self, nums):

        # @debug
        def _lis(nums, prev, curpos):
            if curpos == len(nums):
                return 0
            taken = 0
            if nums[curpos] > prev:
                taken = 1 + _lis(nums, nums[curpos], curpos + 1)
            not_taken = _lis(nums, prev, curpos + 1)
            return  max(taken, not_taken)

        return (_lis(nums, float("-inf"), 0))

class SolutionDP:
    '''
    Time: O(n^2)
    Space: O(n)
    '''
    def LIS(self, nums):
        dp = [1] * len(nums)
        result = float("-inf")
        for i in range(len(nums)):
            maxVal = 0
            for j in range(i):
                print(dp)
                if nums[j] < nums[i]:
                    maxVal = max(maxVal, dp[j])
            dp[i] = max(dp[i], maxVal + 1)
            result = max(dp[i], result)
        return result


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        nums = [10,9,2,5,3,7,101,18]
        s = Solution()
        self.assertEqual(s.LIS(nums), 4)

        s = SolutionDP()
        self.assertEqual(s.LIS(nums), 4)


unittest.main(verbosity=2)

