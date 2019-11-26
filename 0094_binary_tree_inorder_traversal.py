#------------------------------------------------------------------------------
# Question:
#------------------------------------------------------------------------------
# tags:
'''
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?
'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *
from test_utils.BinaryTree import TreeNode, BinaryTree

class Node():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class SolutionRecur:
    '''
    Time:
    Space:
    '''
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        def recurUtil(root, result):
            if root is None:
                return
            recurUtil(root.left, result)
            result.append(root.val)
            recurUtil(root.right, result)

        result = []
        recurUtil(root, result)
        return result

class SolutionIterative(object):
    def inorderTraversal(self, root):
        if root is None:
            return []
        stack = []
        result = []
        current = root
        while(current or len(stack) > 0):
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                result.append(current.val)
                current = current.right
        return result


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        root = [4,2,6,1,3,5,7]
        root = BinaryTree(root).root
        s = SolutionRecur()
        self.assertEqual(s.inorderTraversal(root), [1,2,3,4,5,6,7])

        s = SolutionIterative()
        self.assertEqual(s.inorderTraversal(root), [1,2,3,4,5,6,7])

    def test_no_root(self):
        root = None
        s = SolutionIterative()
        self.assertEqual(s.inorderTraversal(root), [])


unittest.main(verbosity=2)
