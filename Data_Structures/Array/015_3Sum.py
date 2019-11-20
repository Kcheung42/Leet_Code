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

j must be less than k
Target = 0
[-4 -1 -1 0 1 2] => -3
 i   j        k

[-4 -1 -1 0 1 2] => -3
  i     j     k

[-4 -1 -1 0 1 2] => -2
  i       j   k

[-4 -1 -1 0 1 2] => -1
  i         j k

[-4 -1 -1 0 1 2] => 0 => append [-1,-1,2]
     i  j     k
when found move j and k inwards for more combinations


[-4 -1 -1 0 1 2] => 0 => append [-1,0,1]
[    i    j k  ]
when found move j and k inwards for more combinations

if j >= k move i inward, reset j, k
[-4 -1 -1 0 1 2] => 1
[       i j   k]

[-4 -1 -1 0 1 2] => 0 => append[-1, 0, 1]
[       i j k  ]


'''

from typing import List
import unittest
# T:O(n^2) S:O(1)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        result = []
        i = 0
        while i < n - 2:
            if i == 0 or nums[i] != nums[i-1]:
                j = i + 1
                k = n - 1
                while j < k:
                    if nums[i] + nums[j] + nums[k] < 0:
                        j += 1
                    elif nums[i] + nums[j] + nums[k] > 0:
                        k -= 1
                    else:
                        result.append([nums[i] for i in [i,j,k]])
                        j += 1
                        k -= 1
                        while j < k and nums[j] == nums[j-1]:
                            j += 1
                        while j < k and nums[k] == nums[k+1]:
                            k -= 1
            i += 1
        return result


class TestSolution1(unittest.TestCase):
    def test_simple(self):
        nums = [-1, 0, 1, 2, -1, -4]
        s = Solution()
        test_ans = [[-1, 0, 1], [-1, -1, 2]]
        test_set = set.union(*map(set, test_ans))
        ans = s.threeSum(nums)
        ans_set = set.union(*map(set, ans))
        self.assertEqual(ans_set, test_set)


if __name__ == "__main__":
    unittest.main()

