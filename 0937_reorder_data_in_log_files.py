#------------------------------------------------------------------------------
# Question:
#------------------------------------------------------------------------------
# tags:
'''
You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.
Then, either:
Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.

We will call these two varieties of logs letter-logs and digit-logs.
It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.
The letter-logs are ordered lexicographically ignoring identifier, with the
identifier used in case of ties.  The digit-logs should be put in their original
order.

Return the final order of the logs.

Example 1:

Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

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
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def isDigit(log):
            return log.split()[1].isdigit()

        lets = list(filter(lambda x: not isDigit(x),logs))
        digits = list(filter(lambda x: isDigit(x),logs))
        lets.sort(key=lambda x: x.split()[0])
        lets.sort(key=lambda x: x.split()[1:])
        # lets.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        result = lets + digits

        return lets + digits


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):

    def test_simple(self):
        logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
        s = Solution()
        self.assertEqual(
            s.reorderLogFiles(logs),
            ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"])


    def test_simple2(self):
        logs = ["dig1 8 1 5 1","let3 art can","dig2 3 6","let2 art ab dig","let1 art art"]
        s = Solution()
        self.assertEqual(
            s.reorderLogFiles(logs),
            ["let1 art art","let3 art can","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"])


unittest.main(verbosity=2)

