#------------------------------------------------------------------------------
# Questions
#------------------------------------------------------------------------------
# tags:
'''
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same
element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.

Example 1:

Input:
matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]

Output: True
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
Example 2:

Input:
matrix = [
  [1,2],
  [2,2]
]
Output: False
Explanation:
The diagonal "[1, 2]" has different elements.

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
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        R = len(matrix)
        C = len(matrix[0])

        def checkDiagonals(r,c):
            '''returns true if diagnal is all the same number'''
            num = matrix[r][c]
            while r < R and c < C:
                print(f'({r},{c}):{matrix[r][c]}')
                if matrix[r][c] != num:
                    return False
                r += 1
                c += 1
            return True
        if all([checkDiagonals(0, c) for c in range(C)]) and \
           all([checkDiagonals(r, 0) for r in range(1, R)]):
            return True
        return False


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest


class TestSolution(unittest.TestCase):
    def test_simple(self):
        matrix = [
            [1,2,3,4],
            [5,1,2,3],
            [9,5,1,2]
            ]
        s = Solution()
        self.assertEqual(s.isToeplitzMatrix(matrix), True)

    def test_simple(self):
            matrix = [[1,2,3,4]]
            s = Solution()
            self.assertEqual(s.isToeplitzMatrix(matrix), True)


unittest.main(verbosity=2)


