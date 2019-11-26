#------------------------------------------------------------------------------
# Question: 0030_substring_with_concatenation_of_all_words.py
#------------------------------------------------------------------------------
# tags:
'''
You are given a string, s, and a list of words, words, that are all of the
same length. Find all starting indices of substring(s) in s that is a
concatenation of each word in words exactly once and without any intervening
characters.

Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input:
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
Output: []

'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *

class Solution:

    '''
    Time:
    Space:

    Counter dict:
    d[foo] = 1
    d[bar] = 1
    ...

    k = len(words[0]) = > 3
    n = len(s) => 17

    R -> range(n,k)
    s=[foobarthefoobarman]
    i=[L  R              ]

    word = s[R-k] => foo
    d[word] -= 1

    # R moves
    s=[foobarthefoobarman]
    i=[L     R           ]
    word = s[R-k:R] => bar
    d[word] -= 1

    Counter dict:
    d[foo] = 0
    d[bar] = 0
    ...
    all values in counter is exactly 0

    add L to result

    # R moves
    s=[foobarthefoobarman]
    i=[L        R        ]
    word = s[R-k:R] => the
    d[word] -= 1

    # fix dictionary
    while d[word] < 0:
        d[s[L:L+k]] += 1
        L += k
    Counter dict:
    d[foo] = 1
    d[bar] = 1
    d[the] = 0
    s=[foobarthefoobarman]
    i=[         R        ]
    i=[         L        ]


    # R moves
    s=[foobarthefoobarman]
    i=[         L  R     ]
    word = s[R-k:R] => foo
    d[word] -= 1

    '''
    from collections import Counter

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        k = len(words[0])
        d = Counter()
        result = []
        for w in words:
            d[w] = 1 if w not in d else d[w] + 1
        print(d)
        l = 0
        for L in range(n):
            for R in range(l+k,n+1,k):
                word = s[R-k:R]
                d[word] -= 1
                while d[word] == -1:
                    d[s[l:l+k]] += 1
                    l = l+k
                if all([x==0 for x in d.values()]):
                    result.append(l)
        return result

        pass


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        s = Solution()
        string = "barfoothefoobarman"
        words = ['foo', 'bar']
        result = s.findSubstring(string, words)
        self.assertEqual(set(result), set([0,9]))


unittest.main(verbosity=2)

