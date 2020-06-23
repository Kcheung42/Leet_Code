#------------------------------------------------------------------------------
# Question: 043_Multiply_Strings.py
#------------------------------------------------------------------------------
# tags:
'''
Given two non-negative integers num1 and num2 represented as strings, return
the product of num1 and num2.

Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer
directly.

'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        '''
        [0,0,0,0,0,0]
        456
        123
        p

        6*123 + 5*123*10 + 4*123*100

        321
        654

        [0 0 0 0 0 12]
                    p
                    S
        '''
        result = [0] * (len(num1) * len(num2))
        start = len(result) - 1
        for n1 in num1[::-1]:
            for i, n2 in enumerate(num2[::-1]):
                pos = start - i
                prod = int(n1) * int(n2)
                result[pos] += prod
                result[pos - 1] += result[pos] // 10
                result[pos] %= 10
            start -= 1

        for i, v in enumerate(result):
            if v != 0:
                x = i
                break
        else:
            return "0"
        return "".join([str(x) for x in result[x:]])

#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        s = Solution()
        num1 = "123"
        num2 = "456"
        ans = s.multiply(num1, num2)
        self.assertEqual(ans, '56088')

    def test_simple2(self):
        s = Solution()
        num1 = "0"
        num2 = "0"
        ans = s.multiply(num1, num2)
        self.assertEqual(ans, '0')


unittest.main(verbosity=2)

