#------------------------------------------------------------------------------
# Question: 0199_binary_tree_right_side_view.py
#------------------------------------------------------------------------------
# tags:
'''
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *

class Solution:
    '''
     1
    / \
   2   3
   \
    4
   / \
  6   5

    ans = 1 3 4 5
          r  d
    node = (2,1)
    cur_d = 2
    result = [1, 3, 4]

    proccess q:
    get from q (node, depth)
    if the depth of node is equal to current depth in question, append node to result
       , then update current depth += 1
    add right child
    add left child

    '''
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        q = [(root, 0)]
        cur_d = 0
        result = []
        while q:
            q_size = len(q)
            for _ in range(q_size):
                node, depth = q.pop(0)
                if node:
                    if depth == cur_d:
                        result.append(node.val)
                        cur_d += 1
                    q.append((node.left, depth + 1))
                    q.append((node.right, depth + 1))
        return result

def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        q = [(root, 0)]
        result = []
        while q:
            q_size = len(q)
            for i in range(q_size):
                node, depth = q.pop(0)
                if i == 0:
                    result.append(node.val)
                if node.left:
                    q.append((node.left, depth + 1))
                if node.right:
                    q.append((node.right, depth + 1))
        return result

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        q = [(root, 0)]
        result = []
        while q:
            q_size = len(q)
            for i in range(q_size):
                node, level = q.pop(0)
                if i == q_size-1:
                    result.append(node.val)
                if node.left:
                    q.append((node.left, level+1))
                if node.right:
                    q.append((node.right, level+1))
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

