#------------------------------------------------------------------------------
# Questions: 0104_maximum_depth_of_binary_tree.py
#------------------------------------------------------------------------------
'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root
node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.

'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *
from test_utils.BinaryTree import BinaryTree, TreeNode
# tags:

class Solution:
    '''Recursion'''
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return 1 + max(left, right)
# Time = O(N) where N is the number of nodes
# Space:
# O(N): Worst case if tree is completely imbalanced and each node only has left child.
# Storage to keep the call stack will be O(N)
# O(log N): Best case if tree is balanced, since height of the tree would be Log N


class Solution2:
    '''Stack'''
    def maxDepth(self, root: TreeNode) -> int:
        stack = []
        stack.append((1, root))
        depth = 0
        while stack:
            current_depth, node = stack.pop()
            if node:
                depth = max(depth, current_depth)
                stack.append((current_depth+1, node.left))
                stack.append((current_depth+1, node.right))
        return depth
# Time = O(N)

#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution1(unittest.TestCase):
    def test_simple(self):
        root = [3,9,20,None,None,15,7]
        root = BinaryTree(root).root

        s = Solution()
        self.assertEqual(s.maxDepth(root), 3)

        s = Solution2()
        self.assertEqual(s.maxDepth(root), 3)


if __name__ == "__main__":
	unittest.main()
