# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    106_construct_binary_tree_from_inorder_an          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/01/30 23:44:26 by kcheung           #+#    #+#              #
#    Updated: 2018/01/31 11:41:31 by kcheung          ###   ########.fr        #
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

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def buildTreeRecur(self, inorder, postorder,lookup, postorder_end, inorder_start, inorder_end):
		if inorder_start == inorder_end:
			return None
		node = TreeNode(postorder[postorder_end - 1])
		i = lookup[postorder[post_end - 1]]
		node.left = self.buildTreeRecur(inorder, postorder, lookup, postorder_end - 1 -  (inorder_end - i - 1), inorder_start, i)
		node.right = self.buildTreeRecur(inorder, postorder, lookup, postorder_end - 1, i + 1, inorder_end)
		return node


	def buildTree(self, inorder, postorder):
		"""
		:type inorder: List[int]
		:type postorder: List[int]
		:rtype: TreeNode
		"""
		lookup = {}
		for i,val in enumerate(inorder):
			lookup[val] = i
		return(self.buildTreeRecur(inorder, postorder, lookup, len(postorder), 0, len(inorder)))

s = Solution()
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
s.buildTree(inorder, postorder)

