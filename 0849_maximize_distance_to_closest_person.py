from typing import *
# tags: Easy
'''
In a row of seats, 1 represents a person sitting in that seat, and 0 represents
that the seat is empty.

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest
person to him is maximized.

Return that maximum distance to closest person.

Example 1:

Input: [1,0,0,0,1,0,1]
Output: 2
Explanation:
If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.
Example 2:

Input: [1,0,0,0]
Output: 3
Explanation:
If Alex sits in the last seat, the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.

'''
# Time = O()
# Space = O()
class Solution:
    def maxDistToClosest(self, seats):
        N = len(seats)
        left, right = [float("inf")] * N, [N] * N

        for i in range(N):
            if seats[i] == 1: left[i] = 0
            elif i > 0: left[i] = left[i-1] + 1

        for i in range(N-1, -1, -1):
            if seats[i] == 1: right[i] = 0
            elif i < N-1: right[i] = right[i+1] + 1

        return max(min(left[i], right[i])
                   for i, seat in enumerate(seats) if not seat)


import unittest
class TestSolution1(unittest.TestCase):
    def test_simple(self):
        seats = [1,0,0,0,1,0,1]
        s = Solution()
        self.assertEqual(s.maxDistToClosest(seats), 2)

    def test_simple2(self):
        seats = [1,0,0,0]
        s = Solution()
        self.assertEqual(s.maxDistToClosest(seats), 3)

    def test_simple3(self):
        seats = [0,0,0,1,1]
        s = Solution()
        self.assertEqual(s.maxDistToClosest(seats), 3)



unittest.main(verbosity=2)
