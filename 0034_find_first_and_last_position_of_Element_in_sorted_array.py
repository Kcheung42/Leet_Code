#------------------------------------------------------------------------------
# Questions: 0034_find_first_and_last_position_of_Element_in_sorted_array.py
#------------------------------------------------------------------------------
# tags: medium
'''
Given an array of integers nums sorted in ascending order, find the
starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *

# Time = O(log n)
# Space = O(1)
class Solution:
    def find(self, nums, target, left):
        lo = 0
        hi = len(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] > target or (left and nums[mid] == target):
                hi = mid
            else:
                lo = mid+1
        return lo

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_idx = self.find(nums, target, True)
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]
        right_idx = self.find(nums, target, False) - 1
        return [left_idx, right_idx]


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        nums = [5,7,7,8,8,10]
        target = 8
        s = Solution()
        self.assertEqual(s.searchRange(nums, target), [3,4])

    def test_no_range(self):
        nums = [5,7,7,8,8,10]
        target = 10
        s = Solution()
        self.assertEqual(s.searchRange(nums, target), [5,5])

    def test_no_input(self):
        nums = []
        target = 10
        s = Solution()
        self.assertEqual(s.searchRange(nums, target), [-1,-1])

unittest.main()
