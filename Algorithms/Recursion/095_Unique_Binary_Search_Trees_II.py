# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    095_Unique_Binary_Search_Trees_II.py               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/01/30 18:50:40 by kcheung           #+#    #+#              #
#    Updated: 2018/01/30 21:13:18 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

'''
Given an integer n, generate all structurally unique BST's (binary search trees)
that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

1         3     3      2      1
\       /     /      / \      \
3     2     1      1   3      2
/     /       \                 \
2     1         2                 3

'''
# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):

	def generateHelper(self, low, high):
		result = []
		if low > high:
			result.append(None)
		for i in range(low, high + 1):
			left = self.generateHelper(low, i - 1)
			right = self.generateHelper(i + 1 ,high)
			for j in left:
				for k in right:
					cur = TreeNode(i)
					cur.left = j
					cur.right = k
					result.append(cur)
		return result


	def generateTrees(self, n):
		"""
		:type n: int
		:rtype: List[TreeNode]
		"""
		result = self.generateHelper(1,n)
		return result

s = Solution()
print(len(s.generateTrees(3)))
