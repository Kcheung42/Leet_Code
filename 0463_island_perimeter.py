#------------------------------------------------------------------------------
# Question:
#------------------------------------------------------------------------------
# tags:
'''

'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *

class Solution:
    '''
    |0|1|2|
    |3|x|4|
    |5|6|7|
    '''
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        def dfs(r, c, result):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 1
            if grid[r][c] == -1:
                return 0
            grid[r][c] = -1
            perim = 0
            for nei in neighbors:
                new_r = r + nei[0]
                new_c = c + nei[1]
                perim += dfs(new_r, new_c, result)
            return perim

        result = 0
        neighbors = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    result += dfs(r,c, result)
                break
        return result


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        s = Solution()
        self.assertEqual(True, True)


unittest.main(verbosity=2)

