#------------------------------------------------------------------------------
# Question:
#------------------------------------------------------------------------------
# tags: Binary
'''
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two
given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor
is defined between two nodes p and q as the lowest node in T that has both
p and q as descendants (where we allow a node to be a descendant of itself).”

Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]
'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *
from test_utils.BinaryTree import BinaryTree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    '''
    Time: O(n)
    Space: O(1)
    Assumptions: both p and q are present in the tree
    '''
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None

        if root.val == p or root.val == q:
            return root.val

        leftLCA = self.lowestCommonAncestor(root.left, p, q)
        rightLCA = self.lowestCommonAncestor(root.right, p, q)

        if leftLCA and rightLCA:
            return root.val

        return leftLCA.val if leftLCA is not None else rightLCA.val


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        array = [3,5,1,6,2,0,8,None,None,7,4]
        p = 5
        q = 1
        root = BinaryTree(array).root
        s = Solution()
        self.assertEqual(s.lowestCommonAncestor(root, p, q), 3)


unittest.main(verbosity=2)

