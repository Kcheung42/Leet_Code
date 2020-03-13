#------------------------------------------------------------------------------
# Question:
#------------------------------------------------------------------------------
# tags: Easy
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

[[2,1,1],
 [1,1,0],
 [0,1,1]] t = 0

[[2,2,1],
 [2,1,0],
 [0,1,1]] t = 1

[[2,2,2],
 [2,2,0],
 [0,1,1]] t = 2

[[2,2,2],
 [2,2,0],
 [0,2,1]] t = 3

[[2,2,2],
 [2,2,0],
[0,2,2]] t = 4

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

        def neighbors(row, col):
            neighbors = [(1, 0), (0, -1,), (-1, 0), (0, 1)]
            for nei in neighbors:
                r = row + nei[0]
                c = col + nei[1]
                if 0 <= r < R and 0 <= c < C:
                    yield r, c

        R = len(grid)
        C = len(grid[0])
        queue = []
        A = grid
        for r, row in enumerate(A):
            print(f"r:{r}, row:{row}")
            for c, val in enumerate(row):
                print(f"c:{c} val:{val}")
                if val == 2:
                    queue.append((r, c, 0))
        d = 0
        while queue:
            r, c, d = queue.pop(0)
            print(f"r:{r} c:{c} d:{d}")
            for nr, nc in neighbors(r, c):
                if isFresh(grid[nr][nc]):
                    grid[nr][nc] = 2
                    queue.append((nr, nc, d+1))
        if any(1 in row for row in grid):
            return -1
        return d


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

