#------------------------------------------------------------------------------
# Question:
#------------------------------------------------------------------------------
# tags:
'''
Given a string and an integer k, you need to reverse the first k
characters for every 2k characters counting from the start of the string.
If there are less than k characters left, reverse all of them. If there
are less than 2k but greater than or equal to k characters, then reverse
the first k characters and left the other as original.

Example
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *

# def reverseStr(self, s, k):
#   if not s: return s
#   i, j = 0, k-1
#   chars = [c for c in s]
#   while i < len(s):
#           x, y = i, min(j, len(s)-1)
#           while x < y:
#               chars[x], chars[y] = chars[y], chars[x]
#               x, y = x + 1, y - 1
#               i, j = i + 2*k, j + 2*k
#       return ''.join(chars)

# T:O(n) S:O(n)
class Solution:
    '''
    Time:
    Space:
    '''
    def reverseStr(self, s, k):
        r = [s[i:i+k] for i in range(0,len(s),k)]

        for i in range(0,len(r),2):
            if len(r[i]) <= k:
                r[i] = r[i][::-1]
        return ''.join(r)


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        string ="abcdefg"
        s = Solution()
        self.assertEqual(s.reverseStr(string, 2), "bacdfeg")


unittest.main(verbosity=2)




# s = Solution()
# print(s.reverseStr("abcdefghijkl", 5))

# class Solution2:
#   def reverseStr(self, s, k):
#       s = list(s)
#       for i in range(0, len(s), 2*k):
#           print(i)
#           s[i:i+k] = s[i:i+k][::-1]
#       return ("".join(s))

# s = Solution2()
# print(s.reverseStr("abcdefghijkl", 2))
