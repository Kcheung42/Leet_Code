# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    001_Two_Sum.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/12/20 14:05:46 by kcheung           #+#    #+#              #
#    Updated: 2018/01/12 11:37:19 by kcheung          ###   ########.fr        #
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

from typing import *
# tags:

# Time = O()
# Space = O()
class Solution:
    def twoSum(self, nums, target):
        d = {}
        for i, v in enumerate(nums):
            if v not in d:
                d[target-v] = i
            else:
                return  [d[v], i]
        return False

import unittest

class TestSolution1(unittest.TestCase):
    def test_simple(self):
        nums = [2,7,11,15]
        target = 9
        s = Solution()
        self.assertEqual(s.twoSum(nums, target), [0,1])

    def test_simple2(self):
        nums = [2,2]
        target = 4
        s = Solution()
        self.assertEqual(s.twoSum(nums, target), [0,1])

    def test_no_valid(self):
        nums = [2]
        target = 4
        s = Solution()
        self.assertEqual(s.twoSum(nums, target), False)

unittest.main(verbosity=2)
