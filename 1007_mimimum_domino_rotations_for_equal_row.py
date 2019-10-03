#------------------------------------------------------------------------------
# Questions: 1007_mimimum_domino_rotations_for_equal_row.py
#------------------------------------------------------------------------------
# tags: Medium
'''
In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the
i-th domino.  (A domino is a tile with two numbers from 1 to 6 - one on
each half of the tile.)

We may rotate the i-th domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same,
or all the values in B are the same.

If it cannot be done, return -1.


Example 1:

Input: A = [2,1,2,4,2,2] ,
       B = [5,2,6,2,3,2]
Output: 2
Explanation: The first figure represents the dominoes as given by A and B:
before we do any rotations. If we rotate the second and fourth dominoes,
we can make every value in the top row equal to 2, as indicated by the second figure.

Example 2:

Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
Output: -1
Explanation: In this case, it is not possible to rotate the dominoes to make
one row of values equal.

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
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        def check(x):
            '''return the minimum rotation needed to turn either A
            or B row into x
            '''
            rotate_a = rotate_b = 0

            for i in range(n):
                if A[i] != x:
                    rotate_a += 1
                elif B[i] != x:
                    rotate_b += 1
                elif A[i] != x and B[i] != x:
                    return -1
            return(min(rotate_a, rotate_b))

        n = len(A)
        rotations = check(A[0])
        if rotations != -1:
            return rotations
        else:
            return check(B[0])


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        A = [2,1,2,4,2,2]
        B = [5,2,6,2,3,2]
        s = Solution()
        self.assertEqual(s.minDominoRotations(A,B), 2)


unittest.main(verbosity=2)

