# Question:
#------------------------------------------------------------------------------
# tags:
'''
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

 

Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)

'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *
import random

class Solution:

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        dist = lambda i: points[i][0]**2 + points[i][1]**2

        def sort(i, j, K):
            k = random.randint(i, j)
            points[j], points[k] = points[k], points[j]

            mid = partition(i, j)
            if K < mid - i - 1:
                sort(i, mid - 1, K)
            elif K > mid - i + 1:
                sort(mid + 1, j, K - (mid - i + 1))

        def partition(start, end):
            pIndex = start
            pivot = dist(end)
            i = start
            while i < end:
                if dist(i) <= pivot:
                    points[i], points[pIndex] = points[pIndex], points[i]
                    pIndex += 1
                i += 1
            points[pIndex], points[end] = points[end], points[pIndex]
            return pIndex

        sort(0, len(points) - 1, K)
        return points[:K]


#------------------------------------------------------------------------------
    '''
    Time:
    Space:
    '''
    def f():
        pass


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        s = Solution()
        points = [[3,3],[5,-1],[-2,4]]
        k = 2
        ans = s.kClosest(points, k)
        self.assertEqual(set(ans), set([[[3,3],[-2,4]]]) )


unittest.main(verbosity=2)

