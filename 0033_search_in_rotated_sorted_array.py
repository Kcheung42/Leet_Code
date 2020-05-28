#------------------------------------------------------------------------------
# Question: 0033_search_in_rotated_sorted_array.py

'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to
you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index,
otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
                       ^
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_rotate_index(left, right):
            '''
            Use Binary search to find rotation index as defined by
            nums[rotaiton_idx] > nums[rotation_idx+1]

            Returns: rotation idx
            NOTE: rotation index is the minimum element in the array
            '''

            # if the first number is less than the last number
            # then we don't have a rotation index.
            # what to return? 0?
            if nums[left] < nums[right]:
                return 0

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > nums[mid+1]:
                    return mid + 1
                if nums[mid] < nums[0]:
                    #search left
                    right = mid - 1
                else:
                    #search right
                    left = mid + 1

        def binary_search(start, end):
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return -1

        n = len(nums)
        if n == 0:
            return -1
        if n == 1:
            return 0 if nums[0] == target else -1

        idx = find_rotate_index(0, n-1)
        print(idx)
        if nums[idx] == target:
            return idx
        if idx == 0:
            return binary_search(0, n-1)
        if target < nums[0]:
            return binary_search(idx, n-1)
        return binary_search(0, idx)

#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        s = Solution()
        nums = [4,5,6,7,0,1,2]
        self.assertEqual(s.search(nums, 0), 4)

    def test_simple2(self):
        s = Solution()
        nums = [3,1]
        self.assertEqual(s.search(nums, 3), 0)

    def test_simple3(self):
        s = Solution()
        nums = [5, 1, 3]
        self.assertEqual(s.search(nums, 0), -1)

    def test_simple4(self):
        s = Solution()
        nums = [5, 1, 3]
        self.assertEqual(s.search(nums, 1), 1)

    def test_simple5(self):
        s = Solution()
        nums = [4,5,1,2,3]
        self.assertEqual(s.search(nums, 1), 2)



unittest.main(verbosity=2)

