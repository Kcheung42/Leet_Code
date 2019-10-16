#------------------------------------------------------------------------------
# Questions
#------------------------------------------------------------------------------
# tags:
'''
In a N x N grid composed of 1 x 1 squares, each 1 x 1 square consists of a
/, \, or blank space.  These characters divide the square into contiguous regions.

(Note that backslash characters are escaped, so a \ is represented as "\\".)

Return the number of regions.
Input:
[
  " /",
  "/ "
]
Output: 2
Explanation: The 2x2 grid is as follows:


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
    def regionsBySlashes(self, grid: List[str]) -> int:
        pass


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        grid = [
            " /",
            "/ "
            ]
        s = Solution()
        self.assertEqual(regionsBySlashes(grid), 2)


unittest.main(verbosity=2)

