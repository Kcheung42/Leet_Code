#------------------------------------------------------------------------------
# Question: 0098_validate_binary_tree.py
#------------------------------------------------------------------------------
# tags:
''''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:
    2
   / \
  1   3
Binary tree [2,1,3], return true.
Example 2:
    1
   / \
  2   3
Binary tree [1,2,3], return false.

Definition for a binary tree node.
 class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


left < root.val < 4

            4
           / \
         2   5
        /
      4
     / \
   >2   6
   / \
  1   3




left < root.val < right
   2
/    \
1     2

    2
  /   \
-inf inf
at 1 , bounded by -inf < root.val < inf

    2
   / \
 >1   3
  /   \
-inf inf

at 1 , bounded by -inf < root.val < 2

    2
  /  \
 1    inf

Traps:
its not enough to know left_child < cur val < right_child.
          4
        /  \
       2    5
     /  \
    1    6
False because although 1 < 2 < 6,  6 also needs to be smaller than 4!
all roots need to compare 

'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *
from test_utils.BinaryTree import BinaryTree

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isValidBSTHelper(root, minValue, maxValue):
                if root is None:
                    return True

                if not(minValue < root.val < maxValue):
                    return False
                left = isValidBSTHelper(root.left, minValue, root.val)
                right = isValidBSTHelper(root.right, root.val, maxValue)
                return left and right

        return isValidBSTHelper(root, float("-inf"), float("inf"))



#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        root = [2,1,3]
        root = BinaryTree(root).root
        s = Solution()
        self.assertEqual(s.isValidBST(root), True)


unittest.main(verbosity=2)
