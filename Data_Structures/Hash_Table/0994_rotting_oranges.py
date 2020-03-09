#------------------------------------------------------------------------------
# Question:
#------------------------------------------------------------------------------
# tags:
'''
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten
orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh
orange.  If this is impossible, return -1 instead.

Example 1:

Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

[[2,1,1],[1,1,0],[0,1,1]] t = 0
[[2,2,1],[2,1,0],[0,1,1]] t = 1
[[2,2,2],[2,2,0],[0,1,1]] t = 2
[[2,2,2],[2,2,0],[0,2,1]] t = 3
[[2,2,2],[2,2,0],[0,2,f]] t = 4

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never
rotten, because rotting only happens 4-directionally.
Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer
is just 0.


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
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def isFresh(x):
            return True if x == 1 else False

        def update_grid(row, col):
            neighbors = [(1, 0), (0, -1,), (1, 0), (0, 1)]
            for nei in neighbors:
                r = row + nei[0]
                c = col + nei[1]
                if r >=0 and r < rows and c >= 0 and c < cols and isFresh(grid[row], grid[col]):

        pass


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        s = Solution()
        grid = [[2,1,1],[1,1,0],[0,1,1]]
        self.assertEqual(s.orangesRotting(grid), 4)


unittest.main(verbosity=2)

