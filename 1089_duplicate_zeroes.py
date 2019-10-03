#------------------------------------------------------------------------------
# Questions
#------------------------------------------------------------------------------
# tags: Easy
'''
Given a fixed length array arr of integers, duplicate each occurrence of zero,
shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything
from your function.

Example 1:

Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to:
[1,0,0,2,3,0,0,4]

Example 2:

Input: [1,2,3]
Output: null
Explanation: After calling your function, the input array is modified to:
[1,2,3]

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
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        dups = 0
        n = len(arr)
        last = n - 1
        for i in range(n):
            if i > n - dups - 1:
                break
            if arr[i] == 0:
                if i == last - dups:
                    arr[last] = 0
                    last -= 1
                    break
                dups += 1
        last = last - dups
        for i in range(last, -1 ,-1):
            if arr[i] != 0:
                arr[i+dups] = arr[i]
            else:
                arr[i+dups] = 0
                dups -= 1
                arr[i+dups] = 0


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        arr = [1,0,2,3,0,4,5,0]
        s = Solution()
        s.duplicateZeros(arr)
        self.assertEqual(arr, [1,0,0,2,3,0,0,4])

    def test_edge_case(self):
        arr = [1,2,3,0,0,0,0,7]
        s = Solution()
        s.duplicateZeros(arr)
        self.assertEqual(arr, [1,2,3,0,0,0,0,0])


unittest.main(verbosity=2)

