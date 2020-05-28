# ------------------------------------------------------------------------------
# Question:
# ------------------------------------------------------------------------------
# tags:
'''

'''

# ------------------------------------------------------------------------------
# Solutions
# ------------------------------------------------------------------------------

import unittest
from typing import *


class SolutionLeetBrute:
    '''
    Time: O(n^3)
    Time: O(1)

    1 2 3 4 5
    s
        e
      i
    s: 0 -> n-2
    e: s+2 -> n
    i: s+1 -> e
    A[i] - A[i-1] == diff, count += 1
    '''
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        result = 0
        n = len(A)
        for s in range(n - 2):
            diff = A[s + 1] - A[s]
            for e in range(s + 2, n):
                for i in range(s + 1, e):
                    if A[i] - A[i - 1] != diff:
                        break
                else:
                    result += 1
        return result


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        '''
        [1 2 3 4 5 6]
         l   r     x

        sum([i for i in range(x-r+1, 1)])

        slices = 4 + 3 + 2 + 1
        1 2 3
        2 3 4
        3 4 5
        4 5 6
        1 2 3 4
        2 3 4 5
        3 4 5 6
        1 2 3 4 5
        2 3 4 5 6
        1 2 3 4 5 6

        A[i:j]

        is arithmitic: if len(A[i:j]) >= 3, diff between consecutive alement is the same

         0 1 2 3 4  5  6
        [1 3 5 7 9 10 14]
                    i j
         l
             r

         diff = 1

         from l -> i how many slices with len 3,4 -> i-l

        Arithmitic Sequences:
        A[0:3] -> diff = 2
        A[3:6] -> diff = 3
        '''

        n = len(A)

        if n < 3: return 0

        result = 0  #count of arithmitic slices
        diff = A[1] - A[0]
        l = 0
        for j in range(1, n):
            i = j-1
            delta = A[j] - A[i]
            if delta != diff:
                r = l + 2
                if r <= i:
                    result += sum([x for x in range(i - r + 1, 0, -1)])
                l = i
                diff = delta

                '''
         0 1 2 3 4
        [1 3 5 7 9 ]
                 i j
             l
               r
        1 3 5
        3 5 1
        5 7 9
        1 3 5 7
        3 5 7 9
                '''
        if l != n - 2:
            r = l + 2
            if r <= n-1:
                result += sum([x for x in range((n-1) - r + 1, 0, -1)])
        return result


# ------------------------------------------------------------------------------
# Tests
# ------------------------------------------------------------------------------


class TestSolution(unittest.TestCase):
    def test_simple(self):
        s = Solution()
        A = [1, 2, 3, 4]
        self.assertEqual(s.numberOfArithmeticSlices(A), 3)


unittest.main(verbosity=2)
