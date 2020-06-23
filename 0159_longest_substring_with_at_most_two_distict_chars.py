#------------------------------------------------------------------------------
# Questions: 0159_longest_substring_with_at_most_two_distict_chars.py
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

        # hashmap character -> its rightmost position
        # [letter] = index of rightmost position
        hashmap = defaultdict()

        max_len = 2

        # sliding window left and right pointers
        left = 0
        for right in range(n):
            hashmap[s[right]] = right
            if len(hashmap) == 3:
                del_idx = min(hashmap.values())
                del hashmap[s[del_idx]]
                left = del_idx + 1
            cur_len = right - left + 1
            max_len = max(max_len, cur_len)

        # while right < n:
        #     # slidewindow contains less than 3 characters
        #     hashmap[s[right]] = right
        #     right += 1

        #     # slidewindow contains 3 characters
        #     if len(hashmap) == 3:
        #         # delete the leftmost character
        #         del_idx = min(hashmap.values())
        #         del hashmap[s[del_idx]]
        #         # move left pointer of the slidewindow
        #         left = del_idx + 1
        #     cur_len = right - left
        #     max_len = max(max_len, cur_len)

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
        '''
        d[letter] = index

        d[c] = 1 (del)

        d[a] = 3
        d[d] = 4

        0123456
        ccaabbb
          l
            r

        max = r-l
        max = 5
        '''
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
