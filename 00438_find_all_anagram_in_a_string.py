# ------------------------------------------------------------------------------
# Question: 00438_find_all_anagram_in_a_string.py
# ------------------------------------------------------------------------------
# tags:
'''
Given a string s and a non-empty string p, find all the start indices of p's
anagrams in s.

Strings consists of lowercase English letters only and the length of both
strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

'''

# ------------------------------------------------------------------------------
# Solutions
# ------------------------------------------------------------------------------

import unittest
from typing import *


class SolutionBrute:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        '''
        s: "cbaebabacd" p: "abc"
                l
                  r

       ans= 0      6
       d[c] = 1
       d[b] = 0
       d[a] = 0
        '''
        def isAnagram(s, p):
            """
            Return True if substring is anagram of p
            """
            return sorted(s) == sorted(p)

        P = len(p) #=>2
        S = len(s) #=>4
        result = []
        if S < P:
            return result
        l = 0          #=>0/1
        r = l + P #=>2/3
        while l <= S-P:
            if isAnagram(str(s[l:r]), p): # string[1:3]=ba p=>ab
                result.append(l)
            l += 1
            r += 1
        return result


class SolutionBrute2:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        '''
        s: "cbaebabacd" p: "abc"
                l
                  r
        '''
        def isAnagram(s, p):
            """
            Return True if substring is anagram of p
            """
            counter = {}
            for c in s:
                counter[c] = counter.get(c, 0) + 1
            for c in p:
                if c not in counter:
                    return False
                counter[c] -= 1
                if counter[c] < 0:
                    return False
            return all(x == 0 for x in counter.values())

        P = len(p) #=>2
        S = len(s) #=>4
        result = []
        if S < P:
            return result
        l = 0          #=>0/1
        r = l + P #=>2/3
        while l <= S-P:
            if isAnagram(str(s[l:r]), p): # string[1:3]=ba p=>ab
                result.append(l)
            l += 1
            r += 1
        return result



import collections
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        '''
        Time: O(N_s + N_p), since its one pass along both strings

        Space: O(1), since pCount and sCount contain no more than 26
        elements

                  ?
        s: "cbaebabacd" p: "abc"
                 l  r

        use window
        p_count[a] = 1
        p_count[b] = 1
        p_count[c] = 1

        s_count[c] = 1/0/1
        s_count[b] = 1/2/1/2/1
        s_count[a] = 1/2/1/2/1
        s_count[e] = 1/0

        '''

        ns = len(s)
        np = len(p)

        if ns < np:
            return []

        # counter for chars in p
        p_count = collections.Counter(p)
        # counter for chars in working window
        s_count = collections.Counter()
        result = []
        '''
        window: [b a e]
        '''
        for i in range(ns):
            #left and right pointer of window
            r, l = i, (i-np)
            # add one more letter to right side of window
            s_count[s[r]] += 1
            # remove one letter from left side of window
            if r >= np:
                if s_count[s[l]] == 1:
                    del s_count[s[l]]
                else:
                    s_count[s[l]] -= 1
            #compare the counts of sliding window and pattern
            if p_count == s_count: #time complexity is O(1) since no more than 26
                result.append(l + 1)
        return result

# ------------------------------------------------------------------------------
# Tests
# ------------------------------------------------------------------------------

class TestSolution(unittest.TestCase):
    def test_simple(self):
        s = Solution()
        string = "cbaebabacd"
        pattern = "abc"
        self.assertEqual(s.findAnagrams(string, pattern), [0, 6])

    def test_simple2(self):
        s = Solution()
        string = "abab"
        pattern = "ab"
        self.assertEqual(s.findAnagrams(string, pattern), [0,1,2])

unittest.main(verbosity=2)

