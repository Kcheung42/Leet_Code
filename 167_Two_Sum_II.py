# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    167_Two_Sum_II.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/01/12 11:39:27 by kcheung           #+#    #+#              #
#    Updated: 2018/01/12 14:14:25 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


'''
Given an array of integers that is already sorted in ascending order, find two
numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add
up to the target, where index1 must be less than index2. Please note that your
returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may not
use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''

class Solution(object):
	def twoSum(self, numbers, target):
		"""
		:type numbers: List[int]
		:type target: int
		:rtype: List[int]
		"""
		dict = {};
		n = len(numbers)
		for i in range(n):
			if numbers[i] in dict:
				return ([dict[numbers[i]], i + 1])
			key = target - numbers[i]
			dict[key] = i + 1

s = Solution()
numbers = [2,7,11,15]
target = 9
numbers = [2,3,4]
target = 6
print(s.twoSum(numbers, target))

