# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    075_Sort_Colors.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/01/31 17:25:52 by kcheung           #+#    #+#              #
#    Updated: 2018/01/31 18:16:43 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

'''

Given an array with n objects colored red, white or blue, sort them so that
objects of the same color are adjacent, with the colors in the order red, white
and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white,
and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.

click to show follow up.

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array
with total number of 0's, then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?

'''

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = 3
        output = [0 for i in range(n)]
        counts = [0 for i in range(k)]
        print(nums)
        for i,val in enumerate(nums):
            counts[val] += 1
        for i in range(1,3):
            counts[i] += counts[i - 1]
        print(counts)
        for i,v in enumerate(range(n)):
            index = counts[nums[i]] - 1
            output[index] = nums[i]
            counts[nums[i]] -= 1
        return output


import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        s = Solution()
        a = [2,1,0,2,0,0,0,1,1]
        self.assertEqual(s.sortColors(a), [0,0,0,0,1,1,1,2,2])


# Time Complexity: O(n+k) where n is the number of elements in input array and k is the range of input.
# Auxiliary Space: O(n+k)


unittest.main(verbosity=2)
