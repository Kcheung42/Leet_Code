# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    003_Longest_Substring_Without_Repeating_C          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/01/10 11:13:03 by kcheung           #+#    #+#              #
#    Updated: 2018/01/11 10:57:37 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

'''
Given a string, find the length of the longest substring without repeating characters.
Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must
be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution:
	def lengthOfLongestSubstring(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		if s == "" :
			return 0
		n = len(s)
		cur_len = 1
		max_len = 1
		prev_index = 0
		i = 0
		visited = [-1] * 256

		visited[ord(s[0])] = 0
		for i in range(1,n):
			prev_index = visited[ord(s[i])]
			if prev_index == -1:
				cur_len += 1
			elif (i - cur_len > prev_index):
				cur_len += 1
			else:
				if cur_len > max_len:
					max_len = cur_len
				cur_len = i - prev_index 
			visited[ord(s[i])] = i
		if cur_len > max_len:
			max_len = cur_len
		return (max_len)

s = Solution()
# arr = 'GEEKSFORGEEKS'
arr = ''
print "Length of lis is", s.lengthOfLongestSubstring(arr)
