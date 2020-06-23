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
            # if sum is negative, exclude that path of sums
            left = max(max_gain(root.left), 0)
            right = max(max_gain(root.right), 0)

            # include both left and right sums
            sum = root.val + left + right

            # update max_sum if sum is higher
            max_sum = max(sum, max_sum)

            #for recursion:
            # return the max gain from one of the children
            return(root.val + max(left, right))

        max_sum = float('-inf')
        max_gain(root)
        return(max_sum)


# class Solution:
#     '''

#     cases: path is through root
#       1
#      / \
#     2   3
#     ans = [1, 2 3]


#     cases: path is not through root
#        -1
#        /
#       1
#      / \
#     2   3
#     ans = [1, 2 3]


#     cases:
#         1
#        /
#       2
#      / \
#    -1   3
#     ans = [1, 2 3]


#     cases:
#        -1
#        /
#       2
#      / \
#     3   1
#     ans = [1, 2 3]

#     '''
#     def maxPathSum(self, root: TreeNode) -> int:
#         def helper(root):
#             nonlocal max_path
#             if root is None:
#                 return 0

#             #better way to write this
#             left = helper(root.left)
#             right = helper(root.right)
#             paths = [left + root.val, right+root.val, left+right+root.val, root.val]
#             max_path = max(*paths, max_path)

#             # return max(left+root.val, right+root.val)
#             return root.val + max(left, right) #better

#         max_path = float("-inf")
#         helper(root)
#         return max_path

class SolutionIter:
    def maxPathSum(self, root: TreeNode) -> int:
        stack = [root]
        r = {None: 0} # store the return value of recursion
        max_path = float("-inf")
        while stack:
            root = stack.pop()
            if root in h:
                left = max(r[root.left],0)
                right = max(r[root.right],0)
                max_path = max(max_path, root.val + right + left)
                h[root] = root.val + max(left, right)
            elif root:
                h[root] = None
                stack.append(root)
                stack.append(root.left)
                stack.append(root.right)
        return max_path

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

        s = SolutionIter()
        self.assertEqual(s.maxPathSum(root), 42)

    def test_simple3(self):
        root = [1,2,3,5,10]
        root = BinaryTree(root).root
        s = Solution()
        self.assertEqual(s.maxPathSum(root), 17)

    def test_simple4(self):
        root = [9,6,-3,None,None,-6,2,None,None,2,None,-6,-6,-6]
        tree = BinaryTree(root)
        print(tree)
        root = tree.root
        s = Solution()
        self.assertEqual(s.maxPathSum(root), 16)

        s = SolutionIter()
        self.assertEqual(s.maxPathSum(root), 16)


if __name__ == "__main__":
	unittest.main()
