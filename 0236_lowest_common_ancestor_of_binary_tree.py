#------------------------------------------------------------------------------
# Question: 0236_lowest_common_ancestor_of_binary_tree.py
#------------------------------------------------------------------------------
# tags: Binary
'''
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two
given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor
is defined between two nodes p and q as the lowest node in T that has both
p and q as descendants (where we allow a node to be a descendant of itself).”

Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]
'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *
from test_utils.BinaryTree import BinaryTree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
        4
      /   \
     2     6
    / \   / \
   1   3 5   7

'''
class Solution:
    '''
    Time: O(n)
    Space: O(1)
    Assumptions: both p and q are present in the tree
    '''
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None

        if root.val == p or root.val == q:
            return root

        leftLCA = self.lowestCommonAncestor(root.left, p, q)
        rightLCA = self.lowestCommonAncestor(root.right, p, q)

        if leftLCA and rightLCA:
            return root

        return leftLCA if leftLCA is not None else rightLCA


class Solution2:
    '''
    Time: O(n)
    Space: O(1)
    Assumptions: p and/or q might not be present in the tree
    '''
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def LCA(root):
            if root is None:
                return None

            lcaR = LCA(root.right)
            lcaL = LCA(root.left)

            if root.val == p:
                v[0] = True
                return root

            if root.val == q:
                v[1] = True
                return root

            if lcaR and lcaL:
                return root

            return lcaR if lcaR else lcaL


        v = [False, False]
        lca = LCA(root)
        # return lca only if both `p` and `v` are in the tree
        return lca if v[0] and v[1] else None


class SolutionLeetIter:
    '''
    Time: O(n)
    Space: O(n)
    '''
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        '''
        h[3] = None
        h[5] = 3
        h[2] = 5
        h[7] = 2
        h[4] = 2
        h[6] = 5
        h[1] = 3
        h[0] = 1
        h[8] = 1

        create a set of ancestors for p or q.
        Doesn't matter who we choose since its guarenteed on will
        traverse the parent's tree while node, starting from p or q is not in ancestor set
        '''

        # Stack for tree traversal
        stack = [root]

        # Dictionary for parent pointers
        parent = {root: None}

        # Iterate until we find both the nodes p and q
        while p not in parent and q not in parent:

            node = stack.pop()

            # While traversing the tree, keep saving the parent pointers.
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        # Ancestors set() for node p.
        p_ancestors = set()

        # Process all ancestors for node p using parent pointers.
        while p:
            p_ancestors.add(p)
            p = parent[p]

        # The first ancestor of q which appears in
        # p's ancestor set() is their lowest common ancestor.
        while q not in p_ancestors:
            q = parent[q]
        return q

class SolutionLeetRecur:
    '''
    Time: O()
    Space: O()
    '''

    def __init__(self):
        # Variable to store LCA node.
        self.ans = None

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def recurse_tree(current_node):
            '''
                mid
              /    \
            left  right
            '''

            # If reached the end of a branch, return False.
            if not current_node:
                return False

            # Left Recursion
            left = recurse_tree(current_node.left)

            # Right Recursion
            right = recurse_tree(current_node.right)

            # If the current node is one of p or q
            mid = current_node == p or current_node == q

            # If any two of the three flags left, right or mid become True.
            if mid + left + right >= 2:
                self.ans = current_node
            # Return True if either of the three bool values is True.
            return mid or left or right

        # Traverse the tree
        recurse_tree(root)
        return self.ans



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_lca_is_root(self):
        array = [3,5,1,6,2,0,8,None,None,7,4]
        p = 5
        q = 1
        root = BinaryTree(array).root
        s = Solution()
        self.assertEqual(s.lowestCommonAncestor(root, p, q).val, 3)

class TestSolution2(unittest.TestCase):
    def test_lca_is_root(self):
        array = [3,5,1,6,2,0,8,None,None,7,4]
        p = 5
        q = 1
        root = BinaryTree(array).root
        s = Solution2()
        self.assertEqual(s.lowestCommonAncestor(root, p, q).val, 3)

    def test_p_does_not_exist(self):
        array = [3,5,1,6,2,0,8,None,None,7,4]
        p = 100
        q = 4
        root = BinaryTree(array).root
        s = Solution2()
        self.assertEqual(s.lowestCommonAncestor(root, p, q), None)

    def test_p_and_q_does_not_exist(self):
        array = [3,5,1,6,2,0,8,None,None,7,4]
        p = 100
        q = 200
        root = BinaryTree(array).root
        s = Solution2()
        self.assertEqual(s.lowestCommonAncestor(root, p, q), None)



unittest.main(verbosity=2)

