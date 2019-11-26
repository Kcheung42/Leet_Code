#------------------------------------------------------------------------------
# Question:
#------------------------------------------------------------------------------
# tags:
'''
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and
for the multiples of five output “Buzz”. For numbers which are multiples of
both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]

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
    def fizzBuzz(self, n: int) -> List[str]:
        def getfizzBuzz(x):
            result = ""
            if x % 3 == 0:
                result += "Fizz"
            if x % 5 == 0:
                result += "Buzz"
            return result

        return [
            getfizzBuzz(x) if x % 3 == 0 or x % 5 == 0 else str(x)
            for x in range(1, n + 1)
        ]


class Solution2:
    '''
    Time:
    Space:
    '''
    def fizzBuzz(self, n: int) -> List[str]:
        return [
            "Fizz" * (not i % 3) + "Buzz" * (not i % 5) or str(i)
            for i in range(1, n + 1)
        ]


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest


class TestSolution(unittest.TestCase):
    def test_simple(self):
        result = [
            "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz",
            "11", "Fizz", "13", "14", "FizzBuzz"
        ]
        n = 15

        s = Solution()
        self.assertEqual(s.fizzBuzz(n), result)

        s = Solution2()
        self.assertEqual(s.fizzBuzz(n), result)


unittest.main(verbosity=2)
