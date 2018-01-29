# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    198_House_Robber.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/01/15 21:51:27 by kcheung           #+#    #+#              #
#    Updated: 2018/01/16 11:35:44 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

'''
You are a professional robber planning to rob houses along a street. Each house
has a certain amount of money stashed, the only constraint stopping you from
robbing each of them is that adjacent houses have security system connected and
it will automatically contact the police if two adjacent houses were broken into
on the same night.

Given a list of non-negative integers representing the amount of money of each
house, determine the maximum amount of money you can rob tonight without
alerting the police.
'''

class Solution(object):
	def rob(self, num):
		last, now = 0, 0
		for i in num:
			print('val:{} last:{} now:{}'.format(i,last,now))
			last, now = now, max(last + i, now)
		return now

s = Solution()
print(s.rob([8,100,8,100,500,6,5,4,4,10]))
