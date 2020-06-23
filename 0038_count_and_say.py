#------------------------------------------------------------------------------
# Question: 0038_count_and_say.py
#------------------------------------------------------------------------------
# tags:
'''
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.
You can do so recursively, in other words from the previous member read off the digits,
counting the number of digits in groups of the same digit.

Note: Each term of the sequence of integers will be represented as a string.

 

Example 1:

Input: 1
Output: "1"
Explanation: This is the base case.
Example 2:

Input: 4
Output: "1211"
Explanation: For n = 3 the term was "21" in which we have two groups "2" and "1", "2" can be
read as "12" which means frequency = 1 and value = 2, the same way "1" is read as "11", so the
answer is the concatenation of "12" and "11" which is "1211".
'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *

# class Solution:
#     '''
#     Time:
#     Space:

#     '''
#     def countAndSay(self, n: int) -> str:
#         return nextSequence(n, ["1", "E"])
#         def nextSequence(n, prev):
#             if n == 1:
#                 return prev[::-1]
#             nextSeq = []
#             prevDigit = prev[1:]
#             pass

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        return ''.join(self.nextSequence(n, ['1', 'E']))

    def nextSequence(self, n, prevSeq):
        if n == 1:
            return prevSeq[:-1]

        nextSeq = []
        prevDigit = prevSeq[0]
        digitCnt = 1
        for digit in prevSeq[1:]:
            if digit == prevDigit:
                digitCnt += 1
            else:
                # the end of a sub-sequence
                nextSeq.extend([str(digitCnt), prevDigit])
                prevDigit = digit
                digitCnt = 1

        # add a Stopping point for the next sequence
        nextSeq.append('E')
        print(nextSeq)

        return self.nextSequence(n-1, nextSeq)

    def countAndSayIterative(self, n):
        stack = [(n, ['1', 'E'])]
        while len(stack) > 0:
            i, prevSeq = stack.pop()
            if i == 1:
                return prevSeq

            prevDigit = prevSeq[0]
            digitCount = 1
            nextSeq = []
            for d in prevSeq[1:]:
                if d == prevDigit:
                    digitCount += 1
                else:
                    nextSeq.extend([str(digitCount), prevDigit])
                    prevDigit = d
                    digitCount = 1
            nextSeq.append('E')
            stack.append((i-1, nextSeq))

#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        s = Solution()
        s.countAndSay(7)
        print(s.countAndSay(7))
        self.assertEqual(True, True)


unittest.main(verbosity=2)

