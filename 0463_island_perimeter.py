#------------------------------------------------------------------------------
# Question: 0463_island_perimeter.py
#------------------------------------------------------------------------------
# tags: #easy
'''
You are given a map in form of a two-dimensional integer grid where 1 represents
land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid
is completely surrounded by water, and there is exactly one island
(i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the
water around the island). One cell is a square with side length 1. The grid is
rectangular, width and height don't exceed 100. Determine the perimeter of the
island.


Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

Explanation: The perimeter is the 16 yellow stripes in the image below:

'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *

class Solution:
    '''
    | |1| |
    |2|x|3|
    | |4| |
    '''
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        def neighbors(row, col):
            neighbors = ((-1, 0), (0, -1), (0, 1), (1, 0))
            for r, c in neighbors:
                n_r = row + r
                n_c = col + c
                yield n_r, n_c

        def dfs(r, c):
            if r < 0 or r >= R or c < 0 or c >= C or grid[r][c] == 0:
                return 1
            if grid[r][c] == -1:
                return 0
            grid[r][c] = -1
            perim = 0
            for n_r, n_c in neighbors(r, c):
                perim += dfs(n_r, n_c)
            return perim

        result = 0
        R = len(grid)
        C = len(grid[0])
        # for r in range(R):
        #     for c in range(C):
        #         if grid[r][c] == 1:
        #             result += dfs(r,c)
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 1:
                    result += dfs(r,c)
        return result


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        s = Solution()
        grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
        self.assertEqual(s.islandPerimeter(grid), 16)

    def test_simple2(self):
        s = Solution()
        grid = [[0,1]]
        self.assertEqual(s.islandPerimeter(grid), 4)


unittest.main(verbosity=2)

