#------------------------------------------------------------------------------
# Question:
#------------------------------------------------------------------------------
# tags:
'''
Given a binary tree rooted at root, the depth of each node is the shortest
distance to the root.

A node is deepest if it has the largest depth possible among any node in the
entire tree.

The subtree of a node is that node, plus the set of all descendants of that node.

Return the node with the largest depth such that it contains all the deepest
nodes in its subtree.


Example 1:

Input: [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation:



We return the node with value 2, colored in yellow in the diagram.
The nodes colored in blue are the deepest nodes of the tree.
The input "[3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]" is a serialization of the given tree.
The output "[2, 7, 4]" is a serialization of the subtree rooted at the node with value 2.
Both the input and output have TreeNode type.

'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *
from test_utils.BinaryTree import BinaryTree, TreeNode
from pprint import pprint

# class Solution(object):
#     '''
#     d[None] = -1
#     d[3] = 1
#     d[5] = 2
#     d[1] = 2
#     d[6] = 3
#     d[2] = 3
#     d[0] = 3
#     d[8] = 3
#     d[7] = 4
#     d[4] = 4

#     max = 4
#     '''
#     def subtreeWithAllDeepest(self, root):
#         # Store the depth of each node in a hash table
#         depth = {None: -1}
#         def dfs(node, parent=None):
#             if node:
#                 depth[node] = depth[parent] + 1
#                 dfs(node.left, node)
#                 dfs(node.right, node)
#         dfs(root)
#         max_depth = max(depth.values()) #4
#         pprint(depth)
#         def answer(node):
#             if node is None or depth[node] == max_depth:
#                 return node
#             # As the left and right child if they have nodes
#             # with the deepest depth
#             L = answer(node.left)
#             R = answer(node.right)
#             if L and R:
#                 return node
#             elif L: # only L
#                 return L
#             elif R: # only R
#                 return R
#             # or
#             # return node if L and R else L or R
#         return answer(root)



class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        '''
          1
         / \
        2!   3!
        ans = 1


          1
         / \
        2   3
       /
      4!
        ans = 4

          1
         / \
        2   3
       /     \
      4!       5!
        ans = 1

        '''
        # find all the deepest nodes and mark them

        def dfs(root, d):
            if root is None:
                return
            h[root] = d
            dfs(root.left, d+1)
            dfs(root.right, d+1)

        max_depth = float("-inf")
        h = {}
        dfs(root, 1)
        max_depth = max(h.values())
        max_nodes = set([n for n in h if h[n] == max_depth])

        def find(root):
            if root is None:
                return None

            if root in max_nodes:
                return root

            left = find(root.left)
            right = find(root.right)
            return root if left and right else left or right

        return find(root)

#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        s = Solution()
        root = [3,5,1,6,2,0,8,None,None,7,4]
        root = BinaryTree(root).root
        s.subtreeWithAllDeepest(root)
        self.assertEqual(True, True)


unittest.main(verbosity=2)

