# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    088_Merge_Sorted_Array.py                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/01/12 17:30:53 by kcheung           #+#    #+#              #
#    Updated: 2018/01/31 16:22:40 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one
sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n)
to hold additional elements from nums2. The number of elements initialized in
nums1 and nums2 are m and n respectively.
'''

import unittest
from typing import *
# tags:

# Time = O(N)
# Space = O(1)
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i, j, k = m-1, n-1, 0
        while(i >= 0 and j >= 0):
            if nums1[i] >= nums2[j]:
                nums1[-1 - k] = nums1[i]
                i -= 1
            else:
                nums1[-1 - k] = nums2[j]
                j -= 1
            k += 1
        while (i >= 0):
            nums1[-1 - k] = nums1[i]
            i -= 1
            k += 1
        while (j >= 0):
            nums1[-1 - k] = nums2[j]
            j -= 1
            k += 1

        return nums1

# Time = O(N)
# Space = O(N)
class Solution2():
    def merge(self, nums1, m, nums2, n):
        nums1_copy = nums1[:m]
        nums1[:] = []

        p1 = 0
        p2 = 0
        while p1 < m and p2 < n:
            if nums1_copy[p1] < nums2[p2]:
                nums1.append(nums1_copy[p1])
                p1 += 1
            else:
                nums1.append(nums2[p2])
                p2 += 1

        if p1 < m:
            nums1[p1+p2:] = nums1_copy[p1:]
        if p2 < n:
            nums1[p1+p2:] = nums2[p2:]

        return nums1


class TestSolution1(unittest.TestCase):
    def test_simple(self):
        nums1 = [1,2,3,0,0,0]
        m = 3
        nums2 = [2,5,6]
        n = 3
        s = Solution()
        self.assertEqual(s.merge(nums1, m, nums2, n), [1,2,2,3,5,6])


    def test_simple2(self):
        nums1 = [1,2,3,0,0,0]
        m = 3
        nums2 = [2,5,6]
        n = 3
        s = Solution2()
        self.assertEqual(s.merge(nums1, m, nums2, n), [1,2,2,3,5,6])

if __name__ == "__main__":
    unittest.main()
