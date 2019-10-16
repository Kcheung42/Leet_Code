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

	def buildTreeRecur(self, preorder, inorder, lookup,  inorder_start, inorder_end, pIndex):
		if inorder_start > inorder_end:
			return None
		node = TreeNode(preorder[pIndex])
		inIndex = lookup[node.val] #find inorder index of chosen node
		if inorder_start == inorder_end:
			return node
		node.left = self.buildTreeRecur(preorder, inorder,lookup, inorder_start, inIndex-1, pIndex+1)
		node.right = self.buildTreeRecur(preorder, inorder,lookup, inIndex+1, inorder_end, pIndex+2)
		return node

	def buildTree(self, preorder, inorder):
		"""
		:type inorder: List[int]
		:type preorder: List[int]
		:rtype: TreeNode
		"""
		n = len(inorder)
		lookup = {}
		for i,val in enumerate(inorder):
			lookup[val] = i
		return(self.buildTreeRecur(preorder, inorder,lookup, 0, n-1, 0))


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


unittest.main(verbosity=2)
