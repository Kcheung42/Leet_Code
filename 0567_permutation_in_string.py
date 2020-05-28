#------------------------------------------------------------------------------
# Question: 0567_permutation_in_string.py
#------------------------------------------------------------------------------
# tags:
'''
Given two strings s1 and s2, write a function to return true if s2 contains the
permutation of s1. In other words, one of the first string's permutations is the
substring of the second string.

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False
 

Note:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].

'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *

'''
brute force:
find all permutation of s1
check for substring
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
                abc
        s(a,a)  s(a,b)  s(a,c)
         /        |       \
        abc      bac      cba
        /  \
    s(b,b) s(b,c)
     /       |
   abc      acb

        '''
        def permute(w):
            def helper(first):
                if first == n:
                    result.append(w[:])
                    return

                for i in range(first, n):
                    w[first], w[i] = w[i], w[first]
                    helper(first+1)
                    w[first], w[i] = w[i], w[first]
            n = len(w)
            w = list(w)
            result = []
            helper(0)
            return result

        words = ["".join(x) for x in permute(s1)]
        for w in words:
            if s2.find(w) != -1:
                return True
        return False


class SolutionSort:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        s1 = "abcd"
        s2 = "eidbobacdoo"
        '''
        s1 = sorted(s1)
        n = len(s1)
        for i in range(len(s2)-n):
            if s1 == sorted(s2[i:i+n]):
                return True
        return False

import collections
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)

        s_h = collections.Counter(s1)
        n = len(s1)
        for i in range(len(s2)-n+1):
            h = collections.Counter(s2[i:i+n])
            print(h)
            print(s_h)
            if h == s_h:
                return True
        return False



#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        s1 = "ab"
        s2 = "eidboaoo"

        s = Solution()
        self.assertEqual(s.checkInclusion(s1,s2), False)

        s = SolutionSort()
        self.assertEqual(s.checkInclusion(s1,s2), False)

    def test_simple2(self):
        s = SolutionSort()
        s1 = "prosperity"
        s2 = "properties"
        self.assertEqual(s.checkInclusion(s1,s2), False)


unittest.main(verbosity=2)

