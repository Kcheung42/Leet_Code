#------------------------------------------------------------------------------
# Question:
#------------------------------------------------------------------------------
# tags:
'''
Given a string, find the length of the longest substring T that contains at
most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.

'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *


import collections
class Solution:
    '''
    eceba
       i

    max_len = 3
    h[e] = 2
    h[c] = 1 -> to delete, lookup del h[s[1]]
    h[b] = 3
    '''
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        if k == 0 or n == 0:
            return 0

        h = collections.defaultdict()
        max_len = 1
        start = 0
        for i, c in enumerate(s):
            h[c] = i
            if len(h) == k+1:
                min_index = min(h.values())
                del (h[s[min_index]])
                start = min_index + 1
            max_len = max(max_len, i - start + 1)
        return max_len


#leetcode sol
from collections import defaultdict
class SolutionLeet:
    def lengthOfLongestSubstringKDistinct(self, s: 'str', k: 'int') -> 'int':
        n = len(s)
        if k == 0 or n == 0:
            return 0

        # sliding window left and right pointers
        left, right = 0, 0
        # hashmap character -> its rightmost position
        # in the sliding window
        hashmap = defaultdict()

        max_len = 1
        while right < n:
            # add new character and move right pointer
            hashmap[s[right]] = right
            right += 1

            # slidewindow contains 3 characters
            if len(hashmap) == k + 1:
                # delete the leftmost character
                del_idx = min(hashmap.values())
                del hashmap[s[del_idx]]
                # move left pointer of the slidewindow
                left = del_idx + 1

            max_len = max(max_len, right - left)

        return max_len

#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest


class TestSolution(unittest.TestCase):
    def test_simple(self):
        s = Solution()
        string = "eceba"
        self.assertEqual(s.lengthOfLongestSubstringKDistinct(string, 2), 3)

    def test_simple2(self):
        s = Solution()
        string = "a"
        k = 0
        self.assertEqual(s.lengthOfLongestSubstringKDistinct(string, k), 0)

    def test_simple3(self):
        s = Solution()
        string = ""
        k = 1
        self.assertEqual(s.lengthOfLongestSubstringKDistinct(string, k), 0)

    def test_simple4(self):
        s = Solution()
        string = "abcd"
        k = 10
        self.assertEqual(s.lengthOfLongestSubstringKDistinct(string, k), 4)

unittest.main(verbosity=2)
