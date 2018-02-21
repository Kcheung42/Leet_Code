# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    017_Letter_Combinations_of_Phone_Number.p          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/02/20 20:00:20 by kcheung           #+#    #+#              #
#    Updated: 2018/02/20 20:32:21 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
'''
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.


'''
class Solution:
	def letterCombinationsRecur(self, lookup,  digits, result, cur, n):
		if n == len(digits):
			result.append(cur)
		else:
			for c in lookup[int(digits[n])]:
				self.letterCombinationsRecur(lookup, digits, result, cur + c, n + 1)

	def letterCombinations(self, digits):
		"""
		:type digits: str
		:rtype: List[str]
		"""
		if digits == []:
			return []
		lookup = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
		result = []
		self.letterCombinationsRecur(lookup, digits, result, "", 0)
		return result

class SolutionCount:
	def letterCombinationsRecur(self, lookup, digits, n):
		if n == len(digits):
			return 1
		else:
			count = 0
			for c in lookup[int(digits[n])]:
				count += self.letterCombinationsRecur(lookup, digits, n + 1)
			return count
		pass

	def letterCombinations(self, digits):
		lookup = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
		return self.letterCombinationsRecur(lookup, digits, 0)
	

# s = Solution()
s = SolutionCount()
digits = "23"
print(s.letterCombinations(digits))

