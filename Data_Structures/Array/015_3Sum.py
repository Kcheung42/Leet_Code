# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    015_3Sum.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/01/21 15:52:48 by kcheung           #+#    #+#              #
#    Updated: 2018/01/29 20:01:56 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

'''
Given an array S of n integers, are there elements a, b, c in S such that
a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
	[-1, 0, 1],
	[-1, -1, 2]
]
'''

# T:O(n^2) S:O(1)
class Solution(object):
	def threeSum(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		nums = sorted(nums)
		result = []
		i = 0
		while i < len(nums) - 2: #i 0 -> 3 inclusive
			if i == 0 or nums[i] != nums[i-1]:
				j = i + 1
				k = len(nums) - 1
				while j < k:
					if nums[i] + nums[j] + nums[k] < 0:
						j += 1
					elif nums[i] + nums[j] + nums[k] > 0:
						k -= 1
					else:
						result.append([nums[i], nums[j], nums[k]])
						print(result[-1])
						j += 1
						k -= 1
						while j < k and nums[j] == nums[j - 1]: #skip if next j is same as previous j
							j += 1
						while j < k and nums[k] == nums[k + 1]:
							k -= 1
			i += 1
		return result

class Solution(object):
	def threeSum(self, nums):
		nums = sorted(nums)
		result = []
		i = 0
		while i < len(nums) - 2:
			j = i + 1
			k = j + 1

s = Solution()
a = [-1,0,1,2,-1,-4]
s.threeSum(a)

#hint: Order Does Not matter
