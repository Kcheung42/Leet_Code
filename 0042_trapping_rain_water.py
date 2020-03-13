#------------------------------------------------------------------------------
# Question:
#------------------------------------------------------------------------------
# tags:
'''
Given n non-negative integers representing an elevation map where the width of
each bar is 1, compute how much water it is able to trap after raining.

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

                                |
      2x                        |
   x131xx1x                     |
 x1xx1xxxxxx                    |
------------
      r                         |
      l
------------
01234567890x

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
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        H = max(height)
        left_dp = right_dp =  [0] * H
        ans = 0
        n = len(height)
        l , r = 0, n-1
        while l < n and height[l] == 0:
            l += 1
        l_max = height[l]
        while r >= 0 and height[r] == 0:
            r -= 1
        r_max = height[r]
        while l < r:
            #process l
            if height[l] < l_max:
                #update dp
                diff = l_max - height[l] # 4
                start = height[l]        # 1
                end = l_max              # 5
                for i in range(start, end):
                    left_dp[i] += i - start + 1
                print(f"update dp: l:{l} left_dp:{left_dp}")
            elif height[l] >= l_max:
                #process dp, reset dp, update l_max
                ans += left_dp[min(l_max-1, height[l]-1)]
                print(f"proccess dp l:{l} ans:{ans}")
                left_dp = [0] * H
                l_max = height[l]

            #process r
            if height[r] < r_max:
                #update dp
                diff = r_max - height[r]
                start = height[r]
                end = r_max
                for i in range(start, end):
                    right_dp[i] += i - start + 1
                print(f"update dp: r:{r} right_dp:{right_dp}")
            elif height[r] >= r_max:
                #process dp, reset dp, update l_max
                ans += right_dp[min(r_max-1, height[r]-1)]
                print(f"proccess dp r:{r} ans:{ans}")
                right_dp = [0] * H
                r_max = height[r]
            l += 1
            r -= 1
        top_idx = min(l_max, r_max) - 1
        if l > r:
            left = left_dp[max(top_idx, height[r]-1)]
            right = right_dp[max(top_idx, height[l]-1)]
            print(f"l < r: ans:{ans} + left:{left} + right:{right}")
            ans += left + right
        elif l == r:
            left = left_dp[max(top_idx, height[l]-1)]
            right = right_dp[max(top_idx, height[r+1]-1)]
            print(f"l and r overlap: ans:{ans} + left:{left} + right:{right} {top_idx + 1 - height[l]}")
            ans += left + right + max(top_idx + 1 - height[l], 0)
        return ans


#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        s = Solution()
        height = [0,1,0,2,1,0,1,3,2,1,2,1]
        self.assertEqual(s.trap(height), 6)

    def test_simple2(self):
        s = Solution()
        height = [6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]
        self.assertEqual(s.trap(height), 83)

    def test_simple3(self):
        s = Solution()
        height = [1,7,5]
        self.assertEqual(s.trap(height), 0)

    def test_simple4(self):
        s = Solution()
        height = [2,0,2]
        self.assertEqual(s.trap(height), 2)

    def test_simple5(self):
        s = Solution()
        height = [9,6,8,8,5,6,3]
        '''
        x34                |
        x2xx               |
        x1xx               |
        xxxx1x             |
        xxxxxx             |
        xxxxxx             |
        xxxxxxx            |
        xxxxxxx            |
        xxxxxxx            |
        --------------------
           r               |
           l               |
        --------------------

        '''
        self.assertEqual(s.trap(height), 3)

    def test_simple6(self):
        s = Solution()
        height = [1,9,6,9,1,8,5]
        '''
         x x               |
         x x x             |
         x x x             |
         xxx x             |
         xxx xx            |
         xxx xx            |
         xxx xx            |
         xxx xx            |
        xxxxxxx            |
        --------------------
           r               |
           l               |
        --------------------
        '''
        self.assertEqual(s.trap(height), 10)



unittest.main(verbosity=2)

