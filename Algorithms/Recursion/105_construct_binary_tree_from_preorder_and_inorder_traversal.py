#------------------------------------------------------------------------------
# Question: 105_construct_binary_tree_from_preorder_and_inorder_traversal.py
#------------------------------------------------------------------------------
# tags:
'''
Given inorder and preorder traversal of a tree, construct the binary tree.


Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
preorder = [3,9,20,15,7]

Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7


# Definition for a binary tree node.
'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *


class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(start, end):
            nonlocal cur_root
            if start >= end:
                return None

            r_value = preorder[cur_root]
            r = TreeNode(r_value)
            cur_root += 1
            pivot_idx = lookup[r_value]
            r.left = helper(start, pivot_idx)
            r.right = helper(pivot_idx+1, end)
            return r

        cur_root = 0
        lookup = {v:i for i,v in enumerate(inorder)}
        return (helper(0, len(inorder)))


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        def in_order(root, result):
            if root is None:
                return None
            in_order(root.left, result)
            result.append(root.val)
            in_order(root.right, result)

        preorder = [3,9,20,15,7] # use preorer as a list of root nodes to build
        inorder = [9,3,15,20,7] # store in look up.
        s = Solution()
        result = []
        tree = s.buildTree(preorder, inorder)
        in_order(tree, result)
        self.assertEqual(result, [9,3,15,20,7])

    def test_simple2(self):
        def in_order(root, result):
            if root is None:
                return None
            in_order(root.left, result)
            result.append(root.val)
            in_order(root.right, result)

        preorder = [1,2] # use preorer as a list of root nodes to build
        inorder = [1,2] # store in look up.
        s = Solution()
        result = []
        tree = s.buildTree(preorder, inorder)
        in_order(tree, result)
        self.assertEqual(result, [1, 2])


unittest.main(verbosity=2)
