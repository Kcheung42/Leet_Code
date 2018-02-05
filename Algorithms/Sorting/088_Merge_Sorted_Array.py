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

class Solution(object):
	def merge(self, nums1, m, nums2, n):
		arr = []
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

# Test Code
s = Solution()
a = [2,4,6,8]
num2 = [1,3,5,7,9]
num1= [0] * (len(a) + len(num2))
for i in range(len(a)):
	num1[i] = a[i]
print(num1)
print(num2)
s.merge(num1, 4 ,num2, 5)
print(num1)
