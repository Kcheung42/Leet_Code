import unittest
from typing import *
# tags:

'''
# 55. Jump Game
Given an array of non-negative integers, you are initially positioned
at the first index of the array.

Each element in the array represents your maximum jump length at that
position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
'''

# Time = O(2**N)
# where n is the length of nums
# Space = O(n)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def backTrack(nums, pos):
            if pos == n - 1:
                return True
            furthest_jump = min(pos + nums[pos], n-1)
            for nextpos in range(pos+1, furthest_jump+1):
                if backTrack(nums, nextpos):
                    return True
            return False
        n = len(nums)
        return backTrack(nums,0)


class Solution2:
    """
    Dynamic Programming with memoization
    """
    def canJump(self, nums: List[int]) -> bool:
        def backTrack(nums, pos, cache):
            if pos == n - 1:
                return True
            if pos in cache:
                return cache[pos]
            furthest_jump = min(pos + nums[pos], n-1)
            for nextpos in range(pos+1, furthest_jump+1):
                if backTrack(nums, nextpos, cache):
                    cache[pos] = True
                    return True
            cache[pos] = False
            return False
        n = len(nums)
        return backTrack(nums,0,{})


class Solution3:
    """
    Greedy Algorithm
    """
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        last = n-1
        i = n-2
        for i in range(n-2, -1, -1):
            if i + nums[i] >= last:
                last = i
        return last == 0


class TestSolution(unittest.TestCase):
    def test_simple(self):
        nums = [2,3,1,1,4]

        s = Solution()
        self.assertEqual(s.canJump(nums), True)

        # s2 = Solution2()
        # self.assertEqual(s2.canJump(nums), True)

        s = Solution3()
        self.assertEqual(s.canJump(nums), True)

    def test_false(self):
        nums = [3,2,1,0,4]
        s = Solution3()
        self.assertEqual(s.canJump(nums), False)

    def test_simple2(self):
        nums = [2,0,0]
        s = Solution3()
        self.assertEqual(s.canJump(nums), True)

unittest.main()
