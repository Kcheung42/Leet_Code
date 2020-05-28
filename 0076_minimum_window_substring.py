#------------------------------------------------------------------------------
# Question: 0076_minimum_window_substring.py
#------------------------------------------------------------------------------
# tags:
'''
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *
import collections


class Solution:
    '''
    T = ABC
    TCount[A] = 1
    TCount[B] = 1
    Tcount[C] = 1

                 R
           L
    S = AxAxBxxxxCxxAxBxC
        01234567890123456
                  1111111
    ans = 5         |---|

    windowCount[A] = 0
    windowCount[B] = 1
    windowCount[C] = 1
    windowCount[x] = 5
    '''
    def minWindow(self, s: str, t: str) -> str:
        TCount = collections.Counter(t)
        windowCount = collections.defaultdict(int)
        l = r = 0
        ans = float("inf"), l, r
        required = len(TCount)
        x = 0 #when x == required, then I have a window with desired chars
        while r < len(s):
            char = s[r]
            windowCount[char] += 1
            if char in TCount and windowCount[char] == TCount[char]:
                x += 1
            while l < r and x == required:
                if l-r+1 < ans[0]:
                    ans = l+r+1, l, r
                char = s[l]
                windowCount[char] -= 1
                if char in TCount and windowCount[char] < TCount[char]:
                    x -= 1
                l += 1
            r += 1

        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]

class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        if not t or not s:
            return ""

        # Dictionary which keeps a count of all the unique characters in t.
        dict_t = Counter(t)

        # Number of unique characters in t, which need to be present in the desired window.
        required = len(dict_t)

        # formed is used to keep track of how many unique characters in t are present in the current window in its desired frequency.
        # e.g. if t is "AABC" then the window must have two A's, one B and one C. Thus formed would be = 3 when all these conditions are met.
        formed = 0  #formed must equal required for window to be desirable

        # left and right pointer
        l, r = 0, 0

        # Dictionary which keeps a count of all the unique characters in the current window.
        window_counts = {}

        # ans tuple of the form (window length, left, right)
        ans = float("inf"), None, None

        while r < len(s):

            # Add one character from the right to the window
            char = s[r]
            window_counts[char] = window_counts.get(char, 0) + 1

            # If the frequency of the current char added equals to the desired count in t then increment the formed count by 1.
            if char in dict_t and window_counts[char] == dict_t[char]:
                formed += 1

            # Try and contract the window till the point where it ceases to be 'desirable'.
            while l <= r and formed == required:
                # Save the smallest window until now.
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                char = s[l]

                # The char at the position pointed by the `left` pointer is no longer a part of the window.
                window_counts[char] -= 1
                if char in dict_t and window_counts[char] < dict_t[char]:
                    formed -= 1

                # Move the left pointer ahead, this would help to look for a new window.
                l += 1

            # Keep expanding the window once we are done contracting.
            r += 1
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest


class TestSolution(unittest.TestCase):
    def test_simple(self):
        s = Solution()
        S = "ADOBECODEBANC"
        T = "ABC"
        self.assertEqual(s.minWindow(S, T), "BANC")


unittest.main(verbosity=2)
