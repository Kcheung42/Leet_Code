# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    518_CoinChange_2-Combinations.py                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/01/11 12:15:39 by kcheung           #+#    #+#              #
#    Updated: 2018/02/16 15:15:24 by kcheung          ###   ########.fr        #
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

        #memo
        key = str(target) + '-' + str(index)
        if key in hashMap:
            return hashMap[key]
        #memo

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
        result = self.coinChangeHelper(amount, coins, 0, map)
        print(map)
        return(result)

class Solution2: #Tabulation
    def change(self, amount, coins):
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins)):
            for j in range(1,amount + 1):
                if j >= coins[i]:
                    dp[j] += dp[j - coins[i]]
        return dp[-1]


#Test Code
s = Solution2()
s = Solution()
coins = [1,2,5]
target = 5
print(s.change(target, coins))
