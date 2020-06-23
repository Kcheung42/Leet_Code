# ------------------------------------------------------------------------------
# Question:
# ------------------------------------------------------------------------------
# tags:
'''
A message containing letters from A-Z is being encoded to numbers using the
following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of
ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

'''

# ------------------------------------------------------------------------------
# Solutions
# ------------------------------------------------------------------------------

import unittest
from typing import *
from test_utils.debug import debug


class Solution:
    '''
    Time:
    Space:
    '''
    '''
                2 => return 1
               /
             23
               \
                '' => return 1
            /
         223
            \
  L          3 => return 1
        /
  f(1223)
        \
  R      23 => return 1


    1223
        i

    edge case:


          01
         /
    f(101)
         \
          1

    '''
    def numDecodings(self, s: str) -> int:
        @debug
        def dfs(index):

            if index == len(s):
                return 1

            if s[index] == '0':
                return 0

            if index == len(s) - 1:
                return 1

            left = dfs(index + 1)

            right = dfs(index + 2) if int(s[index:index + 2]) <= 26 else 0

            return (left + right)
            pass

        return dfs(0)


# ------------------------------------------------------------------------------
# Tests
# ------------------------------------------------------------------------------


class TestSolution(unittest.TestCase):
    def test_simple(self):
        s = Solution()
        string = '226'
        result = s.numDecodings(string)
        self.assertEqual(result, 3)


unittest.main(verbosity=2)
