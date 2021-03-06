# ------------------------------------------------------------------------------
# Question:
# ------------------------------------------------------------------------------
# tags:
'''
Given a set of candidate numbers (candidates) (without duplicates) and a
target number (target), find all unique combinations in candidates where the
candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]

paths:
2,2,2,2 N
2,2,3 Y
2,2,6 N
2,3,6 N

3,

Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]


'''

# ------------------------------------------------------------------------------
# Solutions
# ------------------------------------------------------------------------------
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int],
                       target: int) -> List[List[int]]:
        def dfs(t, path=[], index=0):
            if t == 0:
                result.append(path.copy())
            if t < 0:
                return
            for i, c in enumerate(candidates[index:], start=index):
                dfs(t - c, path + [c], i)

        result = []
        dfs(target)
        return result


# ------------------------------------------------------------------------------
# Tests
# ------------------------------------------------------------------------------

import unittest


class TestSolution(unittest.TestCase):
    def test_simple(self):
        s = Solution()
        candidates = [2, 3, 6, 7]
        target = 7
        self.assertEqual(s.combinationSum(candidates, target),
                         [[7], [2, 2, 3]])

    def test_simple2(self):
        s = Solution()
        candidates = [2, 3, 5]
        target = 8
        self.assertEqual(s.combinationSum(candidates, target),
                         [[2, 2, 2, 2], [2, 3, 3], [3, 5]])


unittest.main(verbosity=2)
