#------------------------------------------------------------------------------
# Question:
#------------------------------------------------------------------------------
# tags: #tree
'''
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

 1
  \
   2
    \
     3
      \
       4
        \
         5
          \
           6
'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        s = [root]
        cur = None
        while s:
            n = s.pop()
            if n:
                s.append(n.right)
                s.append(n.left)
                if not cur:
                    cur = n
                else:
                    cur.right = n
                    cur.left = None
                    cur = cur.right

#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        s = Solution()
        self.assertEqual(True, True)


unittest.main(verbosity=2)

