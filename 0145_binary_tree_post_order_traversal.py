#------------------------------------------------------------------------------
# Question: 0145_binary_tree_post_order_traversal.py
#------------------------------------------------------------------------------
# tags:
'''
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?

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
    Time:
    Space:
    '''
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        def recurUtil(root, result):
            if root is None:
                return
            recurUtil(root.left, result)
            recurUtil(root.right, result)
            result.append(root.val)

        result = []
        recurUtil(root, result)
        return result


class SolutionIter:
    '''
    Time:
    Space:
    '''
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [root]
        result = []
        while stack:
            root = stack.pop()
            result.append(root.val)
            if root.left is not None:
                stack.append(root.left)
            if root.right is not None:
                stack.append(root.right)
        return result[::-1]



#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        root = [1,None,2,None,None,3]
        root = BinaryTree(root).root

        s = SolutionRecur()
        self.assertEqual(s.postorderTraversal(root), [3,2,1])

        s = SolutionIter()
        self.assertEqual(s.postorderTraversal(root), [3,2,1])


unittest.main(verbosity=2)

