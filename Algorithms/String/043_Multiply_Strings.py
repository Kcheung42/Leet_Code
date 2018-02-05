# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    043_Multiply_Strings.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/01/31 16:15:17 by kcheung           #+#    #+#              #
#    Updated: 2018/01/31 16:22:10 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Given two non-negative integers num1 and num2 represented as strings, return
# the product of num1 and num2.
#
# Note:
#
# The length of both num1 and num2 is < 110.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer
# directly.

class Solution(object):
	def multiply(self, num1, num2):
		"""
		:type num1: str
		:type num2: str
		:rtype: str
		"""
