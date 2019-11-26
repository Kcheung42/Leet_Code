#------------------------------------------------------------------------------
# Question: 0256_paint_house.py
#------------------------------------------------------------------------------
# tags:
'''
There are a row of n houses, each house can be painted with one of the three
colors: red, blue or green. The cost of painting each house with a certain
color is different. You have to paint all the houses such that no two
adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a
n x 3 cost matrix. For example, costs[0][0] is the cost of painting house
0 with color red; costs[1][2] is the cost of painting house 1 with color green,
and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Example:

Input: [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue. 
             Minimum cost: 2 + 5 + 3 = 10.

'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *
from test_utils.debug import debug

class SolutionBrute:
    '''
    Time: O()
    Space: O()
    '''
    def minCost(self, costs):
        @debug
        def recur(costs, cur_cost, i, last_color):
            if i > len(costs)-1:
                return cur_cost
            results = []
            house = costs[i]
            for color, cost in enumerate(house):
                if color == last_color:
                    continue
                results.append(recur(costs, cur_cost + house[color], i + 1, color))
            return min(results)
        return recur(costs, 0, 0, -1)


class SolutionDP:
    '''
    Time: O(n)
    Space: O(n)
    '''
    def minCost(self, costs):
        if not costs:
            return 0
        r, c = len(costs), len(costs[0])
        dp = [[0 for _ in range(c)] for _ in range(r)]
        dp[0] = costs[0]
        red, blue, green = 0, 1, 2
        for i in range(1, r):
            dp[i][red] = costs[i][red] + min(dp[i-1][blue:green+1])
            dp[i][blue] = costs[i][blue] + min(dp[i-1][red], dp[i-1][green])
            dp[i][green] = costs[i][green] + min(dp[i-1][:green])
        return min(dp[-1])


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        costs = [[17,2,17],[16,16,5],[14,3,19]]

        s = SolutionBrute()
        self.assertEqual(s.minCost(costs), 10)

        s = SolutionDP()
        self.assertEqual(s.minCost(costs), 10)



unittest.main(verbosity=2)

