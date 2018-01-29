# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    518_CoinChange_2-Combinations.py                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/01/11 12:15:39 by kcheung           #+#    #+#              #
#    Updated: 2018/01/15 21:44:57 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

'''
You are given coins of different denominations and a total amount of money.
Write a function to compute the number of combinations that make up that amount.
You may assume that you have infinite number of each kind of coin.

Note: You can assume that

0 <= amount <= 5000
1 <= coin <= 5000
the number of coins is less than 500
the answer is guaranteed to fit into signed 32-bit integer
'''

class Solution: #recursion + memoization
	def coinChangeHelper(self, target, coins, index, hashMap):
		if (target == 0):
			return (1)
		if(index >= len(coins)):
			return(0)
		key = str(target) + '-' + str(index)
		if key in hashMap:
			return hashMap[key]
		coinsValue = 0
		ways = 0
		while(coinsValue <= target):
			remaining = target - coinsValue
			ways += self.coinChangeHelper(remaining, coins, index+1, hashMap)
			coinsValue += coins[index]
		hashMap[key] = ways
		return ways

	def change(self, amount, coins):
		map = {}
		return(self.coinChangeHelper(amount, coins, 0, map))

class Solution2: #Tabulation
	def change(self, amount, coins):
		dp = [0] * (amount + 1)
		dp[0] = 1
		for i in range(len(coins)):
			for j in range(1,amount):
				if j >= coins[i]:
					dp[j] += dp[j - coins[i]]
		return dp[-1]


#Test Code
s = Solution2()
coins = [1,2,5]
target = 5
# coins = [1,2]
# target = 5000
print(s.change(target, coins))

# class Solution2:
# 	def change(self, amount, coins):
# 		combinations = [0] * amount
# 		combinations[0] = 1
# 		
# 		for i in range(len(coins)):
# 			for j in range(amount):
# 				if (j >= coins[i]):
# 					combinations[j] += combinations[j - coins[i]]
