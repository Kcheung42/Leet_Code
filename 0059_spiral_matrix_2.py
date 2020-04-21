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

[
   f            l
i  0    1   2   3

0[ 1,   2,  3 , 4],
1[ 12, 13, 14 , 5],
2[ 11, 16, 15 , 6]
,
3[ 10, 9, 8 , 7],
]

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
            last = n - l - 1
            diff = last-first
            print(f"first:{first} -> last:{last}")
            print(f"starting number:{start}")
            for i in range(first, last):
                offset = i - first
                print(f"{first}, {i}")
                print(f"{i}, {last}")
                print(f"{last}, {last-offset}")
                print(f"{last-offset}, {first}")
                m[first][i] = start + offset
                m[i][last] = start + (1 * diff) + offset
                m[last][last-offset] = start + (2 * diff) + offset
                m[last-offset][first] = start + (3 * diff) + offset
            start = start + diff * 4
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
        self.assertEqual(s.generateMatrix(n), result)


unittest.main(verbosity=2)

