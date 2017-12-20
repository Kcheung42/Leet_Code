# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    001.Two_Sum.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/12/20 14:05:46 by kcheung           #+#    #+#              #
#    Updated: 2017/12/20 14:08:20 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
