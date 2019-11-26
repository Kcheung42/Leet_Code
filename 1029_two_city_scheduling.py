#------------------------------------------------------------------------------
# Question: 1029_two_city_scheduling.py
#------------------------------------------------------------------------------
# tags: "Easy:Greedy"
'''
There are 2N people a company is planning to interview. The cost of flying the
i-th person to city A is costs[i][0], and the cost of flying the i-th person to
city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N
people arrive in each city.

Example 1:

Input: [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation:
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.

Note:

1 <= costs.length <= 100
It is guaranteed that costs.length is even.
1 <= costs[i][0], costs[i][1] <= 1000


'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *

class Solution:
    '''
    Time: O(nLogn)
    Space: O(1)
    Intuition: Company will always Pay price_A to send someone to A or priceB
    to send someone to B. By sending someone to A company would lose
    price_A - price_B (this could be negative or positive).

    1. Sort costs by (price_A - price_B)
    2. send first half to A and the others to B
    '''
    def twoCityScheduled(self, costs: List[List[int]]) -> int:
        half_n = len(costs) // 2
        costSorted = sorted(costs, key=lambda x: x[0]-x[1])
        result = 0
        for i in range(half_n):
            result += costs[i][0] + costs[i+ half_n][1]
        return result


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        costs = [[10,20],[30,200],[400,50],[30,20]]
        s = Solution()
        self.assertEqual(s.twoCityScheduled(costs), 110)

    def test_no_input(self):
        costs = []
        s = Solution()
        self.assertEqual(s.twoCityScheduled(costs), 0)


unittest.main(verbosity=2)

