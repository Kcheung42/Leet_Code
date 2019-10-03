#------------------------------------------------------------------------------
# Questions:0011_container_with_most_water.py
#------------------------------------------------------------------------------
'''
"Given a string s , find the length of the longest substring t
that contains at most 2 distinct characters."
'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *

from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: 'str') -> 'int':
        n = len(s)
        if n < 3:
            return n

        # sliding window left and right pointers
        left = 0
        right = 0
        # hashmap character -> its rightmost position
        # in the sliding window
        hashmap = defaultdict()

        max_len = 2

        while right < n:
            # slidewindow contains less than 3 characters
            hashmap[s[right]] = right
            right += 1

            # slidewindow contains 3 characters
            if len(hashmap) == 3:
                # delete the leftmost character
                del_idx = min(hashmap.values())
                del hashmap[s[del_idx]]
                # move left pointer of the slidewindow
                left = del_idx + 1
            cur_len = right - left
            max_len = max(max_len, cur_len)

        return max_len


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution1(unittest.TestCase):
    def test_simple(self):
        arr = "eceba"
        s = Solution()
        self.assertEqual(s.lengthOfLongestSubstringTwoDistinct(arr), 3)
        #substring 'ece'

    def test_simple1(self):
        arr = "ccaabbb"
        s = Solution()
        self.assertEqual(s.lengthOfLongestSubstringTwoDistinct(arr), 5)
        #substring 'aabbb'

    def test_simple2(self):
        arr = "ababcbcbaaabbdef"
        s = Solution()
        self.assertEqual(s.lengthOfLongestSubstringTwoDistinct(arr), 6)

    def test_simple3(self):
        arr = "abc"
        s = Solution()
        self.assertEqual(s.lengthOfLongestSubstringTwoDistinct(arr), 2)

    def test_empty_string(self):
        arr = ''
        s = Solution()
        self.assertEqual(s.lengthOfLongestSubstringTwoDistinct(arr), 0)

unittest.main()
