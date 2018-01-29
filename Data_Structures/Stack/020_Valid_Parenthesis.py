# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    020_Valid_Parenthesis.py                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/01/10 11:12:58 by kcheung           #+#    #+#              #
#    Updated: 2018/01/10 12:57:30 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid
but "(]" and "([)]" are not.
'''

class Solution:
	def isValid(self, s):
		'''
		:type s: str
		:rtype: bool
		'''
		opening = set(['(', '{','['])
		closing = set([')','}',']'])
		stack = []
		for c in s:
			if c in opening:
				stack.append(c)
			elif c in closing:
				if len(stack) > 0:
					pop = stack.pop()
					if not self.isMatchingpair(pop, c):
						return False
				else:
					return False
		if len(stack) > 0:
			return False
		return True

	def isMatchingpair(self, a, b):
		if a =='(' and b == ')':
			return True
		if a =='{' and b == '}':
			return True
		if a =='[' and b == ']':
			return True
		return False

s = Solution()
print(s.isValid('{[(])}'))
