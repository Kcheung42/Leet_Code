# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    332_CoinChange-Minimum.py                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/01/11 11:36:46 by kcheung           #+#    #+#              #
#    Updated: 2018/02/16 16:04:27 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

'''
You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up
that amount. If that amount of money cannot be made up by any combination of the
coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

Note:
You may assume that you have an infinite number of each kind of coin.
'''


class Solution:
	def coinChange(self, coins, amount):
		dp = [float("inf")] * (amount + 1)
		dp[0] = 0
		for i in range(amount + 1):
			if dp[i] != float("inf"):
				for c in coins:
					if dp[i + c] <= amount:
						dp[i + c] = min(dp[i + c], dp[i] + 1)
		return dp[-1] if dp[-1] != float("inf") else -1
