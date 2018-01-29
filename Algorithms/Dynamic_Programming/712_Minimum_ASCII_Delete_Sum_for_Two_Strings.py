# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    712_Minimum_ASCII_Delete_Sum_for_Two_Stri          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/01/10 12:05:59 by kcheung           #+#    #+#              #
#    Updated: 2018/01/12 16:07:55 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

'''
Given two strings s1, s2, find the lowest ASCII sum of deleted characters to make
two strings equal.

Example 1:
Input: s1 = "sea", s2 = "eat"
Output: 231

Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible
to achieve this.

Example 2:
Input: s1 = "delete", s2 = "leet"
Output: 403

Explanation: Deleting "dee" from "delete" to turn the string into "let",
adds 100[d]+101[e]+101[e] to the sum.  Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers
of 433 or 417, which are higher.
Note:

0 < s1.length, s2.length <= 1000.
All elements of each string will have an ASCII value in [97, 122].
'''
class Solution:
	def minimumDeleteSum(self, s1, s2):
		"""
		:type s1: str
		:type s2: str
		:rtype: int
		"""
		m = len(s1)
		n = len(s2)
		dp =[[0]*(m + 1) for i in range(n + 1)]

		for i in range(1, m + 1):
			dp[0][i] = dp[0][i-1] + ord(s1[i-1])
		for j in range(1, n + 1):
			dp[j][0] = dp[j-1][0] + ord(s2[j-1])

		for i in range(1, n + 1):
			for j in range(1, m + 1):
				a = ord(s1[j - 1])
				b = ord(s2[i - 1])
				dp[i][j] = min(
						dp[i-1][j-1] + (0 if (a==b) else (a+b)),
						dp[i][j-1] + a,
						dp[i-1][j] + b,
						)
		return dp[-1][-1]

s = Solution()
s1 = 'sea'
s2 = 'eat'
s1 = 'thought'
s2 = 'sloughs'
print(s.minimumDeleteSum(s1,s2))
