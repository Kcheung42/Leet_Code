#------------------------------------------------------------------------------
# Question: 0236_lowest_common_ancestor_of_binary_tree.py
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
            return root

        leftLCA = self.lowestCommonAncestor(root.left, p, q)
        rightLCA = self.lowestCommonAncestor(root.right, p, q)

        if leftLCA and rightLCA:
            return root

        return leftLCA if leftLCA is not None else rightLCA


class Solution2:
    '''
    Time: O(n)
    Space: O(1)
    Assumptions: p and/or q might not be present in the tree
    '''
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def lcaRecur(root, p, q, v):
            if root is None:
                return None

            if root.val == p:
                v[0] = True
                return root
            if root.val == q:
                v[1] = True
                return root

            lcaRight = lcaRecur(root.right, p, q, v)
            lcaLeft = lcaRecur(root.left, p, q, v)

            if lcaRight and lcaLeft:
                return root

            return lcaLeft if lcaLeft else lcaRight


        v = [False, False]
        lca = lcaRecur(root, p, q, v)
        # return lca only if both `p` and `v` are in the tree

        if v[0] and v[1]:
            return lca
        else:
            return None


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_lca_is_root(self):
        array = [3,5,1,6,2,0,8,None,None,7,4]
        p = 5
        q = 1
        root = BinaryTree(array).root
        s = Solution()
        self.assertEqual(s.lowestCommonAncestor(root, p, q).val, 3)

class TestSolution2(unittest.TestCase):
    def test_lca_is_root(self):
        array = [3,5,1,6,2,0,8,None,None,7,4]
        p = 5
        q = 1
        root = BinaryTree(array).root
        s = Solution2()
        self.assertEqual(s.lowestCommonAncestor(root, p, q).val, 3)

    def test_p_does_not_exist(self):
        array = [3,5,1,6,2,0,8,None,None,7,4]
        p = 100
        q = 4
        root = BinaryTree(array).root
        s = Solution2()
        self.assertEqual(s.lowestCommonAncestor(root, p, q), None)

    def test_p_and_q_does_not_exist(self):
        array = [3,5,1,6,2,0,8,None,None,7,4]
        p = 100
        q = 200
        root = BinaryTree(array).root
        s = Solution2()
        self.assertEqual(s.lowestCommonAncestor(root, p, q), None)



unittest.main(verbosity=2)

