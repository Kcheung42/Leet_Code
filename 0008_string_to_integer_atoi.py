#------------------------------------------------------------------------------
# Question:
#------------------------------------------------------------------------------
# tags:
'''
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until
the first non-whitespace character is found. Then, starting from this character,
 takes an optional initial plus or minus sign followed by as many numerical
digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral
number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral
number, or if no such sequence exists because either str is empty or it contains
only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers
within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value
is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is
returned.
Example 1:

Input: "42"
Output: 42
Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.

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
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    def get_number(self, s, cur_idx, sign):
        i = cur_idx
        start = i
        while i < len(s) and s[i].isdigit():
            i += 1

        number = 0
        for c in s[start:i]:
            number *= 10
            number += int(c)

        if sign == '-':
            return number * -1 if number <= 2**31 else self.INT_MIN
        elif sign == '+' or sign is None:
            return number if number <= 2**31-1 else self.INT_MAX

    def myAtoi(self, s: str) -> int:
        wspc = set([' '])
        sign = set(['+', '-'])
        n = len(s)
        i = 0
        number = 0

        while i < n and s[i] in wspc:
            i += 1

        if i < n and (s[i] in sign or s[i].isdigit()):
            if s[i] in sign:
                sign = s[i]
                number = self.get_number(s, i+1, sign)
            else:
                number = self.get_number(s, i, None)
        return number


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    maxInt = 2**31 -1
    minInt = -2**31
    def test_simple1(self):
        s = Solution()
        string = "42"
        self.assertEqual(s.myAtoi(string), 42)

    def test_simple2(self):
        s = Solution()
        string = "4193 with words"
        self.assertEqual(s.myAtoi(string), 4193)

    def test_simple3(self):
        s = Solution()
        string = "words and 987"
        self.assertEqual(s.myAtoi(string), 0)

    def test_simple4(self):
        s = Solution()
        string = "-91283472332"
        self.assertEqual(s.myAtoi(string), self.minInt)

    def test_simple1(self):
        s = Solution()
        string = "+91283472332"
        self.assertEqual(s.myAtoi(string), self.maxInt)

    def test_simple5(self):
        s = Solution()
        string = "91283472332"
        self.assertEqual(s.myAtoi(string), self.maxInt)

    def test_simple6(self):
        s = Solution()
        string = "        -42"
        self.assertEqual(s.myAtoi(string), -42)

    def test_simple7(self):
        s = Solution()
        string = ""
        self.assertEqual(s.myAtoi(string), 0)



unittest.main(verbosity=2)

