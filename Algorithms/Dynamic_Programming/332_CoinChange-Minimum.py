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
    '''

    C(11)

    C(10) | C(9) | C(6)

    C(9) C(8) C(7) | C(8) C(7) C(4) | C(5) C(4) C(1)

    t = amount
    DP = [inf, inf, inf, inf .. t+1]

    let DP[i] = min coins to make target i

    dp[0] = 0
    Iterate for each elem in DP
     Iterate for each coins:
        jump to index i + coinValue => DP[i + c]
        if

    '''
    def coinChange(self, coins, amount):
        def recur(coins, amount, memo):
            if amount == 0:
                return 0
            elif amount < 0:
                return float("inf")
            if amount in memo:
                return memo[amount]

            min_coins = float("inf")
            for c in coins:
                num_coins = 1 + recur(coins, amount-c, memo)
                min_coins = min(min_coins, num_coins)
                if num_coins != float("inf"):
                    memo[amount] = min_coins
            return min_coins

        memo = {}
        min_coins = recur(coins,amount, memo)
        return min_coins if min_coins != float("inf") else -1

class SolutionDP:
    def coinChange(self, coins, amount):
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(amount + 1):
            if dp[i] != float("inf"):
                for c in coins:
                    if i + c <= amount:
                        dp[i + c] = min(dp[i + c], dp[i] + 1)
        return dp[-1] if dp[-1] != float("inf") else -1

#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        coins = [1,2,5]
        target = 11

        s = Solution()
        self.assertEqual(s.coinChange(coins, target), 3)

        s = SolutionDP()
        self.assertEqual(s.coinChange(coins, target), 3)

    def test_simple2(self):
        coins = [1,2,5]
        target = 42

        s = Solution()
        self.assertEqual(s.coinChange(coins, target), 9)

        s = SolutionDP()
        self.assertEqual(s.coinChange(coins, target), 9)



unittest.main(verbosity=2)

