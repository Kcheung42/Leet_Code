# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    106_construct_binary_tree_from_inorder_an          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/01/30 23:44:26 by kcheung           #+#    #+#              #
#    Updated: 2018/01/31 16:08:02 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

'''
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7

'''
import unittest
from typing import *
# tags:

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Time = O(N)
# Space = O()
class Solution(object):
    def buildTreeRecur2(self, inorder, postorder, lookup,  inorder_start, inorder_end):
        if inorder_start > inorder_end:
            return None

        val = postorder[self.pIndex]
        node = TreeNode(val)
        if inorder_start == inorder_end:
            return node

        inorderIndex = lookup[val] #find index of this val in Inorder lookup
        self.pIndex -= 1
        node.right = self.buildTreeRecur2(inorder, postorder, lookup, inorderIndex+1, inorder_end)
        node.left = self.buildTreeRecur2(inorder, postorder, lookup, inorder_start, inorderIndex-1)
        return node

    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        n = len(inorder)
        self.pIndex = n - 1
        lookup = {}
        for i,val in enumerate(inorder):
            lookup[val] = i
        return(self.buildTreeRecur2(inorder, postorder ,lookup, 0, n - 1))



class Solution2(object):
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(in_left, in_right):
            # if there is no elements to construct subtrees
            if in_left > in_right:
                return None

            # pick up the last element as a root
            # val = postorder.pop() #this modifies original post order
            val = postorder[self.pIndex]
            root = TreeNode(val)
            self.pIndex -= 1

            # root splits inorder list
            # into left and right subtrees
            index = idx_map[val]

            # build right subtree
            root.right = helper(index + 1, in_right)
            # build left subtree
            root.left = helper(in_left, index - 1)
            return root

        # build a hashmap value -> its index
        self.pIndex = len(postorder) - 1
        idx_map = {val:idx for idx, val in enumerate(inorder)}
        return helper(0, len(inorder) - 1)


class TestSolution1(unittest.TestCase):

    def test_simple(self):
        inorder = [9,3,15,20,7]
        postorder = [9,15,7,20,3]
        def get_inorder(root, res):
            if root is None:
                return
            get_inorder(root.left, res)
            res.append(root.val)
            get_inorder(root.right, res)

        def get_postorder(root, res):
            if root is None:
                return
            get_postorder(root.left, res)
            get_postorder(root.right, res)
            res.append(root.val)

        s = Solution2()
        myinorder = []
        mypostorder = []
        tree = s.buildTree(inorder, postorder)
        get_inorder(tree, myinorder)
        get_postorder(tree, mypostorder)
        self.assertEqual(myinorder, inorder)
        self.assertEqual(mypostorder, postorder)


if __name__ == "__main__":
    unittest.main()





