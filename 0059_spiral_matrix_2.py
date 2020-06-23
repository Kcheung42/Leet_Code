#------------------------------------------------------------------------------
# Question: 0059_spiral_matrix_2.py
#------------------------------------------------------------------------------
# tags: #medium #array
'''
Given a positive integer n, generate a square matrix filled with elements
from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
   s     e
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

   f            l
i  0    1   2   3

0[ 1,   2,  3 , 4],
1[ 12, 13, 14 , 5],
2[ 11, 16, 15 , 6],
3[ 10, 9, 8 ,   7],
'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *

class Solution:
    '''
    Time:
    Space:
    '''
    def generateMatrix(self, n: int) -> List[List[int]]:
        m = [[0] * n for i in range(n)]
        layers = n // 2
        start = 1
        for l in range(layers):
            first = l
            last = n - 1 - l
            diff = last-first
            for i in range(first, last):
                offset = i - first
                m[first][i] = start + offset
                m[i][last] = m[first][i] + (1 * diff)
                m[last][last-offset] = m[first][i] + (2 * diff)
                m[last-offset][first] = m[first][i] + (3 * diff)
            # two ways to updating start
            start = m[l+1][first] + 1
            # start += diff * 4

        if n % 2 == 1:
            m[n//2][n//2] = start
        return(m)


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple1(self):
        s = Solution()
        n = 3
        result = [[ 1, 2, 3 ], [ 8, 9, 4 ], [ 7, 6, 5 ]]
        self.assertEqual(s.generateMatrix(n), result)

    def test_simple2(self):
        s = Solution()
        n = 4
        result = [[ 1,   2,  3 , 4],
                  [ 12, 13, 14 , 5],
                  [ 11, 16, 15 , 6],
                  [ 10, 9, 8 , 7]]

        m = s.generateMatrix(n)

        self.assertEqual(s.generateMatrix(n), result)


unittest.main(verbosity=2)

