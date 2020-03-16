#------------------------------------------------------------------------------
# Question: 0067_add_binary.py
#------------------------------------------------------------------------------
# tags: #Easy #String
'''
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *

class Solution:

    def addBinary(self, a: str, b: str) -> str:
        '''
        longer =  11010
        shorter =  1011
                    i  |
        carry = 1
        i => 0 + carry
        ans = 10101
        '''

        n = max(len(a), len(b))
        a , b = a.zfill(n), b.zfill(n)
        carry = 0
        ans = ""
        for i in range(n-1, -1, -1):
            cur_sum = int(a[i]) + int(b[i]) + carry
            carry, rem = divmod(cur_sum,2)
            ans = str(rem) + ans
        if carry:
            ans = str(carry) + ans
        return "".join(ans)


class Solution2:
    def addBinary(self, a, b):
        res = ''
        carry = 0
        a_idx = len(a) - 1
        b_idx = len(b) - 1
        while a_idx >= 0 or b_idx >= 0 or carry:
            curval = (a_idx >= 0 and a[a_idx] == '1') + (b_idx >= 0 and b[b_idx] == '1')
            carry, rem = divmod(curval + carry, 2)
            res = str(rem) + res
            a_idx -= 1
            b_idx -= 1
        return res

#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple1(self):
        s = Solution()
        a = "1011"
        b = "1011"
        self.assertEqual(s.addBinary(a,b) , "10110")

    def test_simple2(self):
        s = Solution()
        a = "1011"
        b = "11111011"
        self.assertEqual(s.addBinary(a,b) , "100000110")

    def test_simple3(self):
        s = Solution()
        s2 = Solution2()
        a = "1010"
        b = "1011"
        self.assertEqual(s.addBinary(a,b) , "10101")
        self.assertEqual(s2.addBinary(a,b) , "10101")


unittest.main(verbosity=2)

