# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    016_3Sum_Closest.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/01/28 21:35:21 by kcheung           #+#    #+#              #
#    Updated: 2018/01/29 10:59:18 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

'''
Given an array S of n integers, find three integers in S such that the sum is
closest to a given number, target. Return the sum of the three integers. You
may assume that each input would have exactly one solution.

For example, given array S = {-1 2 1 -4}, and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

# -4, -1, 1, 2

class Solution(object):
	def threeSumClosest(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		i = 0
		result = float("inf")
		min_diff = float("inf")
		nums = sorted(nums)
		while(i < len(nums) - 2):
			if i == 0 or nums[i] != nums[i-1]: #ignore starting number if its the same as before
				j = i + 1
				k = len(nums) - 1
				while j < k:
					diff = nums[i] + nums[j] + nums[k] - target
					if abs(diff) < min_diff:
						min_diff = abs(diff)
						result = nums[i] + nums[j] + nums[k]
					if diff < 0:
						j += 1
					elif diff > 0:
						k -= 1
					else:
						return target
			i += 1
		return(result)

s = Solution()
a = [-5,-2,1,2,-1,-1]
print(s.threeSumClosest(a, -3))

