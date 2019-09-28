#------------------------------------------------------------------------------
# Questions:0011_container_with_most_water.py
#------------------------------------------------------------------------------
# tags:
'''
Given n non-negative integers a1, a2, ..., an , where each represents a point
at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis
forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *

class Solution:
# Time: O(N)
# Space: O(1)
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        max_area = -1
        while end > start:
            cur_area = ((end - start) * min(height[start], height[end]))
            max_area = max(max_area, cur_area)
            if height[end] > height[start]:
                start += 1
            else:
                end -= 1
        return max_area


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        list = [1,8,6,2,5,4,8,3,7]
        s = Solution()
        self.assertEqual(s.maxArea(list), 49)

unittest.main()

