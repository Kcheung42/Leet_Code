import unittest
from typing import *
from test_utils.BinaryTree import TreeNode, BinaryTree
# tags:

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Time = O()
# Space = O()
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def max_gain(root):
            nonlocal max_sum
            if root is None:
                return(0)

            # max sum on the left and right sub-trees of node
            left = max(max_gain(root.left), 0)
            right = max(max_gain(root.right), 0)

            # include both left and right sums
            sum = root.val + max_gain(root.left) + max_gain(root.right)

            # update max_sum if sum is higher
            max_sum = max(sum, max_sum)

            #for recursion:
            # return the max gain from one of the children
            return(root.val + max(left, right))

        max_sum = float('-inf')
        max_gain(root)
        return(max_sum)


class TestSolution1(unittest.TestCase):
    def test_simple(self):
        root = [1,2,3]
        root = BinaryTree(root).root
        s = Solution()
        self.assertEqual(s.maxPathSum(root), 6)

    def test_simple2(self):
        root = [-10,9,20,None,None,15,7]
        root = BinaryTree(root).root
        s = Solution()
        self.assertEqual(s.maxPathSum(root), 42)



if __name__ == "__main__":
	unittest.main()
