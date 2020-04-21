#------------------------------------------------------------------------------
# Question: 0637_average_of_levels_in_binary_tree.py
#------------------------------------------------------------------------------
# tags:
'''
Given a non-empty binary tree, return the average value of the nodes on each
level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on
level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.

'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    '''
    Time:
    Space:
    BFS level order traversal using levels counter
    '''
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if root is None:
            return
        q = [(root, 0)]
        result = []
        sum = count = 0
        while len(q) > 0:
            node, level = q.pop(0)
            sum += node.val
            count += 1
            if node.left: q.append((node.left, level + 1))
            if node.right: q.append((node.right, level + 1))
            if len(q) > 0 and q[0][1] != level:
                result.append(sum / count)
                sum = count = 0
        result.append(sum / count)
        return result


class Solution:
    '''
    Time:
    Space:
    BFS level order traversal using levels counter
    '''
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if root is None:
            return
        q = [root]
        result = []
        while len(q) > 0:
            sum = 0
            count = len(q)
            for i in range(count):
                node = q.pop(0)
                sum += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            result.append(sum / count)
        return result

#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        s = Solution()
        self.assertEqual(True, True)


unittest.main(verbosity=2)

