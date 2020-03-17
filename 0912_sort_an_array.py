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

class BubbleSort:
    '''
    Quick Sort
    Time: O(n^2)
    Space: O(1)
    '''
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(n-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums

class QuickSort:
    '''
    Quick Sort
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


class CountSort:
    '''
    Count Sort
    Time: O(n+k) for elements in range 1 - k
    Space: O(1)
    '''
    def sortArray(self, nums: List[int]) -> List[int]:
        N = len(nums)
        output = [0 for i in range(N)]
        count = [0] * (max(nums) + 1)

        for n in nums:
            count[n] += 1

        for i in range(1, len(count)):
            count[i] += count[i-1]

        for n in nums:
            output[count[n] - 1] = n
            count[n] -= 1
        return output


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        nums = [9,8,7,6,5,4,3,2,1,0]
        # nums = [1,4,1,2,7,5,2]
        sorted_nums = sorted(nums)

        s = BubbleSort()
        self.assertEqual(s.sortArray(nums), sorted_nums)

        s = QuickSort()
        self.assertEqual(s.sortArray(nums), sorted_nums)

        s = CountSort()
        self.assertEqual(s.sortArray(nums), sorted_nums)

    def test_simple2(self):
        nums = [3, 30, 34, 5, 9]
        sorted_nums = sorted(nums)
        s = QuickSort()
        self.assertEqual(s.sortArray(nums), sorted_nums)


unittest.main(verbosity=2)

