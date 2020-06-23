#------------------------------------------------------------------------------
# Question:0450_delete_node_in_a_bst.py
#------------------------------------------------------------------------------
# tags:
'''
Given a root node reference of a BST and a key, delete the node with the given
key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Note: Time complexity should be O(height of tree).

Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7

         x
       /   \
      x     x
     / \   / \
    x   x x   x

'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *
from test_utils.BinaryTree import BinaryTree, TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    '''
    Time:
    Space:
    '''
    def findMin(self, root):
        if root.left is None:
            return root.val
        return self.findMin(root.left)

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        elif key < root.val: root.left = self.deleteNode(root.left, key)
        elif key > root.val: root.right = self.deleteNode(root.right, key)
        else:
            # case 1 no child
            if not(root.right and root.left):
                root = None
            # case 2: One child
            elif root.left and root.right is None:
                temp = root
                root = root.left
                del(temp)
            elif root.right and root.left is None:
                temp = root
                root = root.right
                del(temp)
            # case 3: Two children
            else:
                min_val = self.findMin(root.right)
                root.val = min_val
                root.right = self.deleteNode(root.right, min_val)

        return root


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def inorder(self, root):
        def recur(root, result):
            if root is None:
                return
            recur(root.left, result)
            result.append(root.val)
            recur(root.right, result)

        result = []
        recur(root, result)
        return result

    def test_simple(self):
        tree = [5,3,6,2,4,None,7]
        root = BinaryTree(tree).root
        s = Solution()
        self.assertEqual(self.inorder(s.deleteNode(root, 3)), [2,4,5,6,7])

    def test_simple2(self):
        tree = [1,None,3]
        root = BinaryTree(tree).root
        key = 3
        s = Solution()
        self.assertEqual(self.inorder(s.deleteNode(root, key)), [1])


unittest.main(verbosity=2)

