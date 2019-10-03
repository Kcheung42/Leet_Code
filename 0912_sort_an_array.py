#------------------------------------------------------------------------------
# Questions: 0912_sort_an_array.py
#------------------------------------------------------------------------------
# tags: Medium
'''
Given an array of integers nums, sort the array in ascending order.
'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *

class Solution:
    '''
    Time: O(nlogn)
    Space: O(1)
    '''
    def sortArray(self, nums: List[int]) -> List[int]:

        def partition(nums, start, end):
            '''return the partition index and swap (in place) all numbers less
            than the partition to the left and all greater to the right
            '''
            pivot = nums[end]
            pIndex = start
            for i in range(start, end):
                if nums[i] <= pivot:
                    nums[i], nums[pIndex] = nums[pIndex], nums[i]
                    pIndex += 1
            nums[pIndex] ,nums[end] = nums[end] ,nums[pIndex]
            return pIndex


        def qsort_helper(nums, start, end):
            if start < end:
                pivot = partition(nums, start, end)
                qsort_helper(nums, start, pivot - 1)
                qsort_helper(nums, pivot + 1, end)

        qsort_helper(nums, 0, len(nums) - 1)
        return nums


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        nums = [9,8,7,6,5,4,3,2,1,0]
        s = Solution()
        self.assertEqual(s.sortArray(nums), [0,1,2,3,4,5,6,7,8,9])


unittest.main(verbosity=2)

