# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    105_construct_binary_tree_from_inorder_an          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/01/30 23:44:26 by kcheung           #+#    #+#              #
#    Updated: 2018/01/31 15:59:57 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

'''
Given inorder and preorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
preorder = [3,9,20,15,7]

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
	def buildTreeRecur(self, preorder, inorder, lookup,  inorder_start, inorder_end):
		if inorder_start > inorder_end:
			return None
		node = TreeNode(preorder[self.pIndex])
		inIndex = lookup[node.val] #find inorder index of chosen node
		self.pIndex += 1
		if inorder_start == inorder_end:
			return node
		node.left = self.buildTreeRecur(preorder, inorder,lookup, inorder_start, inIndex-1)
		node.right = self.buildTreeRecur(preorder, inorder,lookup, inIndex+1, inorder_end)
		return node

	def buildTree(self, preorder, inorder):
		"""
		:type inorder: List[int]
		:type preorder: List[int]
		:rtype: TreeNode
		"""
		n = len(inorder)
		self.pIndex = 0
		lookup = {}
		for i,val in enumerate(inorder):
			lookup[val] = i
		return(self.buildTreeRecur(preorder, inorder,lookup, 0, n-1))
	
def printInorder(root):
	if root is None:
		return
	printInorder(root.left)
	print(root.val, end=" ")
	printInorder(root.right)
	
def printPreorder(root):
	if root is None:
		return
	print(root.val, end=" ")
	printPreorder(root.left)
	printPreorder(root.right)

s = Solution()
preorder = [3,9,20,15,7] # use preorer as a list of root nodes to build
inorder = [9,3,15,20,7] # store in look up. 
tree = s.buildTree(inorder, preorder)
printInorder(tree)
print()
printPreorder(tree)

