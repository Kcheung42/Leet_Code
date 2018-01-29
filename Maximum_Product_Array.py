# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Maximum_Product_Array.py                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/01/17 00:10:17 by kcheung           #+#    #+#              #
#    Updated: 2018/01/29 11:15:33 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Solution:
	def maxProd(self, arr):
		n = len(arr)
		max_here = 1
		min_here = 1
		result = 1

		for i in range(n):
			if arr[i] > 0:
				max_here = max_here * arr[i]
				min_here = arr[i] * min_here
			elif arr[i] < 0:
				temp = max_here
				max_here = max(max_here, arr[i] * min_here)
				min_here = temp * arr[i]
			if result < max_here:
				result = max_here
		return result

s = Solution()
# arr = [-2,-3, 0, 4,-5]
arr = [-2,-3, 0, 4,-5]
print(s.maxProd(arr))

'''
| Vars     | init | -2 | -3 | 0  | 4   | -5  |
|----------+------+----+----+----+-----+-----|
| max_here | 1    | 1  | 6  | 6  | 24  | 60  |
| min_here | 1    | -2 | -3 | -3 | -12 | 120 |
| result   | 1    | 1  | 6  | 6  | 24  | 60  |
'''

| Vars | init | 02 |
|------+------+----|
