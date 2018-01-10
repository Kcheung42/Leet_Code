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
arr = 'GEEKSFORGEEKS'
print "Length of lis is", s.lengthOfLongestSubstring(arr)
