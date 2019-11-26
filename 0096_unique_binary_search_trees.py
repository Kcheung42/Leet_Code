#------------------------------------------------------------------------------
# Question:
#------------------------------------------------------------------------------
# tags:
'''
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *
from test_utils.debug import debug

class SolutionDFS:
    '''
    Time:
    Space:
    '''
    # @debug
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return 1
        res = 0
        for i in range(1, n+1):
            left = self.numTrees(i-1)
            right = self.numTrees(n - i)
            res += left*right
        return res

class SolutionDP:
    '''
    Time:O(n^2)
    Space:O(n)
    '''
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return 1
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for n in range(2, n+1):
            for i in range(1, n+1):
                left = dp[i - 1]
                right = dp[n - i]
                dp[n] += left * right
        return dp[-1]

#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        s = SolutionDFS()
        self.assertEqual(s.numTrees(3), 5)

        s = SolutionDP()
        self.assertEqual(s.numTrees(3), 5)

    def test_one(self):
        s = SolutionDFS()
        self.assertEqual(s.numTrees(1), 1)

        s = SolutionDP()
        self.assertEqual(s.numTrees(1), 1)


unittest.main(verbosity=2)

