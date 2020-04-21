# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    054_Spiral_Matrix.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/02/10 15:05:22 by kcheung           #+#    #+#              #
#    Updated: 2018/02/11 14:57:56 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
import pprint

'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the
matrix in spiral order.

For example,
Given the following matrix:

[
[ 1, 2, 3 ],
[ 4, 5, 6 ],
[ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
'''

class Solution(object):
	def spiralOrder(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: List[int]
		"""
		n = len(matrix)
		layers = n // 2
		result = []
		for l in range(layers):
			first = l
			last = n - l - 1
			top = []
			right = []
			bottom = []
			left = []
			for i in range(first, last):
				offset = i - first
				top.append(matrix[first][i])
				right.append(matrix[i][last])
				bottom.append(matrix[last][last - offset])
				left.append(matrix[last - offset][first])
			comb = top + right + bottom + left
			result += comb
		if n % 2 != 0:
			x = (n // 2)
			result.append(matrix[x][x])
		return result

s = Solution()
pp = pprint.PrettyPrinter()
m = 3
n = 5
m = [[i+(j*n) for i in range(1,n+1)] for j in range(m)]
pp.pprint(m)
print(s.spiralOrder(m))
print("")

n = 6
m = [[i+(j*n) for i in range(1,n+1)] for j in range(n)]
pp.pprint(m)
print(s.spiralOrder(m))

