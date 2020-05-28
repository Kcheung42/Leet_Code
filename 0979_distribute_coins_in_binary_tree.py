# ------------------------------------------------------------------------------
# Question:
# ------------------------------------------------------------------------------
# tags: #binarytree
'''

'''

# ------------------------------------------------------------------------------
# Solutions
# ------------------------------------------------------------------------------

import unittest

from test_utils.BinaryTree import BinaryTree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    '''
    Time:
    Space:
    '''
    def distributeCoins(self, root: TreeNode) -> int:

        ans = 0

        def dfs(root):
            nonlocal ans

            if not root:
                return 0

            L = dfs(root.left)
            R = dfs(root.right)

            ans += (abs(L) + abs(R))

            excess = root.val + L + R - 1
            return excess

        dfs(root)
        return ans


# ------------------------------------------------------------------------------
# Tests
# ------------------------------------------------------------------------------


class TestSolution(unittest.TestCase):
    def test_simple(self):
        s = Solution()
        root = [3, 0, 0]
        root = BinaryTree(root).root
        ans = s.distributeCoins(root)
        self.assertEqual(ans, 2)


unittest.main(verbosity=2)
