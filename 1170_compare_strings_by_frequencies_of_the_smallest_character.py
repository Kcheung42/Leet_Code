#------------------------------------------------------------------------------
# Question: 1170_compare_strings_by_frequencies_of_the_smallest_character.py
#------------------------------------------------------------------------------
# tags: Easy
'''
Let's define a function f(s) over a non-empty string s, which calculates the frequency
of the smallest character in s. For example, if s = "dcce" then f(s) = 2 because
the smallest character is "c" and its frequency is 2.

Now, given string arrays queries and words, return an integer array answer,
where each answer[i] is the number of words such that f(queries[i]) < f(W),
where W is a word in words.

Example 1:

Input: queries = ["cbd"], words = ["zaaaz"]
Output: [1]
Explanation:
On the first query we have f("cbd") = 1, f("zaaaz") = 3 so f("cbd") < f("zaaaz").
Example 2:

Input: queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]

f(1) = 1
f(2) = 1
f(3) = 1
f(4) = 1

Output: [1,2]
Explanation:
On the first query only f("bbb") < f("aaaa"). On the second query both f("aaa") and f("aaaa") are both > f("cc").

'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *
import collections

class Solution:
    '''
    Time:
    Space:
    '''
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s):
            smallest_count = 0
            smallest_char = s[0]
            for c in s:
                if c == smallest_char:
                    smallest_count += 1
                elif ord(c) < ord(smallest_char):
                    smallest_count = 0
                    smallest_char = c
            return smallest_count

        def comp(f_len, d):
            result = 0
            for k,v in list(d.items()):
                if k > f_len:
                    result += v
            return result

        result = []
        query_lens = (list (map(f, queries)))
        words_lens = (list (map(f, words)))
        d = collections.defaultdict(int)
        for w in words:
            n = f(w)
            d[n] += 1
        for q in query_lens:
            result.append(comp(q, d))

        return result


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        s = Solution()
        queries = ["bbbf","cc"]
        words = ["a","aa","aaa","aaaa"]
        self.assertEqual(s.numSmallerByFrequency(queries, words), [1,2])


unittest.main(verbosity=2)

