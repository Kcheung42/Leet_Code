#------------------------------------------------------------------------------
# Question: 0215_kth_largest_element_in_an_array.py
#------------------------------------------------------------------------------
# tags:
'''
Find the kth largest element in an unsorted array. Note that it is the kth
largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.

'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *

class Solution:
    '''
    Time:
    Space:
    '''
    def findKthLargest(self, nums: List[int], k: int) -> int:

        '''
        Input: [3,5,1,5,2,4] and k = 2
                  p
                  i
        '''
        # def parition(start, end):
        #     # picking start as pivot
        #     pIndex = start+1
        #     pValue = nums[start]
        #     for i in range(start+1, end):
        #         if nums[i] <= pValue:
        #             nums[i], nums[pIndex] = nums[pIndex], nums[i]
        #             pIndex += 1
        #     nums[start], nums[pIndex-1] = nums[pIndex-1], nums[start]
            # return pIndex-1

        def parition(start, end):
            pIndex = start
            pValue = nums[end]
            for i in range(start, end):
                if nums[i] <= pValue:
                    nums[i], nums[pIndex] = nums[pIndex], nums[i]
                    pIndex += 1

            nums[end], nums[pIndex] = nums[pIndex], nums[end]
            return pIndex

        def find(start, end):
            if start <= end:
                pIndex = parition(start, end)
                if pIndex < k-1:
                    return find(pIndex + 1, end)
                elif pIndex > k-1:
                    return find(start, pIndex - 1)
                else:
                    return pIndex
        return(nums[find(0, len(nums)-1)])


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        s = Solution()
        nums = [3,5,1,6,2,4]
        k = 3
        self.assertEqual(s.findKthLargest(nums, k), 3)


unittest.main(verbosity=2)

