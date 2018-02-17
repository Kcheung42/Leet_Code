# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    031_Next_Permutation.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/02/09 13:22:07 by kcheung           #+#    #+#              #
#    Updated: 2018/02/09 14:23:32 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

'''
Implement next permutation, which rearranges numbers into the lexicographically
next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible
order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding
outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

'''
# 1 2 3 4 5
# 1 2 3 5 4
# 1 2 4 3 5
# 1 2 4 5 3
# 1 2 5 3 4
# 1 2 5 4 3
#
# 1 3 2 4 5
# 1 3 2 5 4
# 1 3 4 2 5
# 1 3 4 5 2
# 1 3 5 4 2
#
# 1 4 2 3 5
# 1 4 3 2 5
# 1 4 3 5 2
# 1 4 5 2 3
# 1 4 5 3 2

class Solution(object):
	def nextPermutation(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		n = len(nums)
		k = -1
		for i in range(n-2):
			if nums[i] < nums[i+1]:
				k = i
		if k == -1:
			return(nums[::-1])
		for i in range(k + 1, n):
			if nums[i] > nums[k]:
				l = i
		nums[l], nums[k] = nums[k], nums[l]
		nums[k+1:] = nums[:k:-1]

s = Solution()
nums = [1,3,5,4,2]
s.nextPermutation(nums)
print(nums)
