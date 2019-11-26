#------------------------------------------------------------------------------
# Question:
#------------------------------------------------------------------------------
# tags:
'''
Given an array of unique characters arr and a string str, Implement a function
getShortestUniqueSubstring that finds the smallest substring of str containing
all the characters in arr. Return "" (empty string) if such a substring doesn’t
exist. Come up with an asymptotically optimal solution and analyze the time and
space complexities.
Example:
input:  arr = ['x','y','z'], str = "axyyzyzyx"
output: "zyx"

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
    def smallestSubstring(self, arr, S):
        n = len(S)
        d = {}
        for a in arr:
            d[a] = 0

        patLen = len(arr)
        head = 0
        uniqueCount = 0
        result = ""
        for tail in range(n):
            c = S[tail]
            if c in d:
                if d[c] == 0:
                    uniqueCount += 1
                d[c] += 1

            # found substring with all chars
            while (uniqueCount == patLen):
                tempLen = head - tail + 1

                #check if cur len is smaller than result and update if necessary
                if tempLen < len(result) or result == "":
                    result = S[head:tail+1]

                # try to shorten the window
                headChar = S[head]

                if headChar in d:
                    d[headChar] -= 1
                if d[headChar] == 0:
                    uniqueCount -= 1
                head += 1
        return result


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        s = Solution()
        arr = ['x','y','z']
        string = "xyyzyzyx"
        self.assertEqual(s.smallestSubstring(arr, string), "zyx")


unittest.main(verbosity=2)

