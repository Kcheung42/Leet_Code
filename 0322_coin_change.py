# ------------------------------------------------------------------------------
# Question:
# ------------------------------------------------------------------------------
# tags:
'''
You are given coins of different denominations and a total amount of money
amount. Write a function to compute the fewest number of coins that you need to
make up that amount. If that amount of money cannot be made up by any combination
of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.



'''

# ------------------------------------------------------------------------------
# Solutions
# ------------------------------------------------------------------------------
import unittest
from typing import *


class Solution:
    '''
    Time:
    Space:
    DFS
    '''
    def coinChange(self, coins, amount):
        def recur(target, count):
            if target == 0:
                return count
            if target < 0:
                return float("inf")

            # result = []
            # for c in coin:
            #     result.append(recur(coin, amount-c, count+1))
            # return min(result)

            return min([recur(target - c, count + 1) for c in coins])

        result = recur(amount, 0)
        return result if result != float("inf") else -1


class SolutionGreedy:
    '''
    Time: O(n+1)
    Space: O(n)

    Intuition: dp[i] stores minimum number of coins for target amount i
    '''
    def coinChange(self, coins, amount):
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(len(dp)):
            print(dp)
            if dp[i] != float("inf"):
                for c in coins:
                    if i + c <= amount:
                        dp[i + c] = min(dp[i + c], dp[i] + 1)
        return dp[-1] if dp[-1] != float("inf") else -1


class SolutionDP2:
    def coinChange(self, coins, amount):
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(1, len(dp)):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i - c] + 1)
        return dp[-1] if dp[-1] != float("inf") else -1

# ------------------------------------------------------------------------------
# Tests
# ------------------------------------------------------------------------------


class TestSolution(unittest.TestCase):
    def test_simple(self):
        coins = [1, 2, 5]
        amount = 11
        s = Solution()
        self.assertEqual(s.coinChange(coins, amount), 3)

        s = SolutionGreedy()
        self.assertEqual(s.coinChange(coins, amount), 3)

        s = SolutionDP2()
        self.assertEqual(s.coinChange(coins, amount), 3)


unittest.main(verbosity=2)
