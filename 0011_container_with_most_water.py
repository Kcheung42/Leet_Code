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

# Psuedo
#loop while left <right
    #calc current area
    #update max
    #move pointer with smaller heiht towards the center


#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *

'''
Intuition: Using two pointers (left, right) to build a window we know that the
volume of water we can hold is the distance between them multiplied by the min
of the 2 values.

If left is larger, we don't need to check the window with right -= 1, because the
volume will always be smaller. We just need to move the left pointer += 1.

If right is larger, do the opposite.

As we move the pointer always calculate the volume and compare it to the max.
Update as needed
'''

class Solution:
# Time: O(N)
# Space: O(1)
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = -1
        while right > left:
            cur_area = ((right - left) * min(height[left], height[right]))
            max_area = max(max_area, cur_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
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

