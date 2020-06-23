#------------------------------------------------------------------------------
# Question:
#------------------------------------------------------------------------------
# tags: Easy
'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric
around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3

Note:
Bonus points if you could solve it both recursively and iteratively.

'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *
from test_utils.BinaryTree import BinaryTree, TreeNode


class SolutionRecur:
    '''
    Time: O(n) Traverse the entire Tree once
    Space: O(n) bound by height of the tree.
    In worse case root -> 1 -> 2 -> 3 ...etc

    Pass two pointers to each recursion
    '''
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(root1, root2):
            if root1 == None and root2 == None:
                return True
            if root1 is None or root2 is None:
                return False
            return (root1.val == root2.val
                    and isMirror(root1.left, root2.right)
                    and isMirror(root1.right, root2.left))

        return isMirror(root, root)


class SolutionIter:
    '''
    Time: O(n) Traverse the entire Tree once
    Space: O(n) bound by height of the tree.
    In worse case root -> 1 -> 2 -> 3 ...etc
    '''
    def isSymmetric(self, root: TreeNode) -> bool:
        stack = [(root, root)]
        while len(stack) > 0:
            root1, root2 = stack.pop()
            if root1 != None and root2 != None:
                if root1 == None or root2 == None:
                    return False
                if root1.val != root2.val:
                    return False
                stack.extend([(root1.left, root2.right),
                              (root1.right, root2.left)])
        return True


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest


class TestSolution(unittest.TestCase):
    def test_simple(self):
        root = [1, 2, 2, 3, 4, 4, 3]
        root = BinaryTree(root).root

        s = SolutionRecur()
        self.assertEqual(s.isSymmetric(root), True)

        s = SolutionIter()
        self.assertEqual(s.isSymmetric(root), True)

    def test_simple_false(self):
        root = [1, 2, 2, None, 3, None, 3]
        root = BinaryTree(root).root

        s = SolutionRecur()
        self.assertEqual(s.isSymmetric(root), False)

        s = SolutionIter()
        self.assertEqual(s.isSymmetric(root), False)


unittest.main(verbosity=2)
