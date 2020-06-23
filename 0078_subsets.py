#------------------------------------------------------------------------------
# Question: 0078_subsets.py
#------------------------------------------------------------------------------
# tags: #medium
'''
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

[1]
[2]
[3]
[1,2]
[1,3]
[2,3]
[1,2,3]
'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *

class SolutionTuple:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first = 0, curr = ()):
        # if the combination of len k is done
            if len(curr) == k:
                output.append([c for c in curr])
            for i in range(first, n):
                backtrack(i + 1, curr + (nums[i],))
        output = []
        n = len(nums)
        for k in range(1, n + 1):
            backtrack()
        return output


class SolutionArray:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first = 0, curr = []):
            # if the combination is done
            if len(curr) == k:
                output.append(curr[:])
            for i in range(first, n):
                curr.append(nums[i])
                backtrack(i + 1, curr)
                curr.pop()
        output = []
        n = len(nums)
        for k in range(1, n + 1):
            # for subset of length k
            backtrack()
        return output


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        nums = [1,2,3]
        s = SolutionTuple()
        self.assertEqual(s.subsets(nums),
                         [[1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]])

        s = SolutionArray()
        self.assertEqual(s.subsets(nums),
                         [[1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]])


unittest.main(verbosity=2)

