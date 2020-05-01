#------------------------------------------------------------------------------
# Question:
#------------------------------------------------------------------------------
# tags:
'''
Given two lists of closed intervals, each list of intervals is pairwise
disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real
numbers x with a <= x <= b.  The intersection of two closed intervals is a
set of real numbers that is either empty, or can be represented as a closed
interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)




Example 1:


Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Reminder: The inputs and the desired output are lists of Interval
objects, and not arrays or lists.

Note:

0 <= A.length < 1000
0 <= B.length < 1000
0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9

'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------

'''
    Time:
    Space:

    example: A = [[0,2], [4,6], [8,10]]

    A   |--------|     |--------|     |--------|
    B      |--------|     |--------|     |--------|
    C         |--------|     |--------|     |--------|

        0  1  2  3  4  5  6  7  8  9  10 11 12

    Ans = [[2,3], [7,8], []]


    0 = start
    1 = 3nd

  Cases

  A   |---|
  B         |---|
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4
                        1 1 1 1 1

  A       |---|
  B         |---|
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4
                        1 1 1 1 1

  A         |---|
  B         |---|
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4
                        1 1 1 1 1

   check if B[start] < A[end], then interval = [B[start], A[end]]
   otherwise increment A


  A           |---|
  B         |---|
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4
                        1 1 1 1 1

  A               |---|
  B         |---|
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4
                        1 1 1 1 1

  A       |----------------|
  B         |---|   |---|
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4
                        1 1 1 1 1

       find overlapping interval
    else move i



    A [1,3] [6, 9] [15,20]
    B [2,4] [7,10] [13,15]

    => [2,3] [7,9] [15,15]


    O(log n)
    heap: [1,3] [2,4] [6,9] [7, 10] [13,15] [15,20]

    x = [1,3]
    y = [2,4]

    if y[start] <= x[end] then calculate interval.


'''

from typing import *
import heapq

class MinHeap():
    def __init__(self):
        self.heap = []
        self.size = 0

    def heapPop(self):

        def get_smaller_child(i):
            left = 2*i+1
            right = 2*i+2
            if right > self.size-1:
                return left
            return left if self.heap[left][0] < self.heap[right][0] else right

        def heapifyDown(i):
            while 2*i+1 <= self.size-1:
                smaller = get_smaller_child(i)
                if self.heap[smaller][0] < self.heap[i][0]:
                    self._swap(smaller, i)
                    i = smaller
                else:
                    break

        self._swap(0, self.size-1)
        self.size -= 1
        pop = self.heap.pop()
        heapifyDown(0)
        return pop

    def _swap(self, i,j):
        self.heap[i], self.heap[j] = self.heap[j] , self.heap[i]

    def heapPush(self, x):

        def heapifyUp(i):
            parent = (i - 1) // 2
            while parent >= 0:
                if self.heap[i][0] < self.heap[parent][0]:
                    self._swap(i, parent)
                    i = parent
                    parent = (parent-1) // 2
                else:
                    break
        self.heap.append(x)
        self.size += 1
        heapifyUp(self.size-1)
        pass

import heap
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        h = []
        for a in A:
            heapq.heappush(h, a)
        for b in B:
            heapq.heappush(h, b)
        # h = MinHeap()
        # for a in A:
        #     h.heapPush(a)
        # for b in B:
        #     h.heapPush(b)

        star, end = 0, 1
        x = h.heapPop()
        result = []
        while h.size > 0:
            y = h.heapPop
            lo = min(y[start], x[start])
            hi = max(y[end], x[end])
            if lo <= hi:
                result.append([lo, hi])
            if y[end] > x[end]:
                x = y

#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        s = Solution()
        A = [[1,3], [6,9], [15,20]]
        B = [[2,4], [7,10], [13,15]]
        self.assertEqual(s.intervalIntersection(A,B), [[2,3], [7,9], [15,15]])


unittest.main(verbosity=2)

