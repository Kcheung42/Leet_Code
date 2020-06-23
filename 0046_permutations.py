#------------------------------------------------------------------------------
# Question:0046_permutations.py
#------------------------------------------------------------------------------

# tags:
'''
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *


class Solution:
    '''
    Time:
    Space:

    Intuition: Back Tracking and Swapping
    '''
    def permute(self, nums: List[int]) -> List[List[int]]:
        def permuteRecur(l, r, result):
            if l == r:
                result.append(nums.copy())
            else:
                for i in range(l, r+1):
                    nums[l], nums[i] = nums[i], nums[l]
                    permuteRecur(l+1, r, result)
                    nums[l], nums[i] = nums[i], nums[l]

        result = []
        permuteRecur(0, len(nums)-1, result)
        return(result)

class Solution:
    '''
    Time:
    Space:

    '''
    def permute(self, nums: List[int]) -> List[List[int]]:
        def permuteRecur(nums,cur):
            if nums == []:
                result.append(cur)
                return
            for i,v in enumerate(nums):
                permuteRecur(nums[:i]+nums[i+1:], cur+str(v))
        result = []
        permuteRecur(nums, "")
        result = [[int(x) for x in r ] for r in result]
        return(result)


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        s = Solution()
        nums = [1,2,3]
        ans = [[3,2,1], [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2]]
        self.assertTrue(all([x in ans for x in s.permute(nums)]))

unittest.main(verbosity=2)

