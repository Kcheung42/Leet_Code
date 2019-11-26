#------------------------------------------------------------------------------
# Question: 0145_binary_tree_post_order_traversal.py
#------------------------------------------------------------------------------
# tags:
'''
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,null,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *
from test_utils.BinaryTree import TreeNode, BinaryTree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class SolutionRecur:
    '''
    Time: O(n)
    Space: O(1)
    '''
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        def recurUtil(root, result):
            if root is None:
                return
            result.append(root.val)
            recurUtil(root.left, result)
            recurUtil(root.right, result)

        result = []
        recurUtil(root, result)
        return result


class SolutionIter:
    '''
    Time: O(n)
    Space: O(n)
    '''
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [root]
        result = []
        while stack:
            root = stack.pop()
            result.append(root.val)
            if root.right is not None:
                stack.append(root.right)
            if root.left is not None:
                stack.append(root.left)
        return result



#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        root = [1,None,2,None,None,3]
        root = BinaryTree(root).root

        s = SolutionRecur()
        self.assertEqual(s.preorderTraversal(root), [1,2,3])

        s = SolutionIter()
        self.assertEqual(s.preorderTraversal(root), [1,2,3])


unittest.main(verbosity=2)

