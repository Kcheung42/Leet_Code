#------------------------------------------------------------------------------
# Question: 0953_verify_alien_dictionary.py
#------------------------------------------------------------------------------
# tags:
'''
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.


Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).

'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *

'''
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"

order -> hashtable to store the ranking of letters in alien dictionary
order[w] = 0
order[o] = 1
order[r] = 3
... etc

["word","world","row"]
         i       j

["word","rorld","row"]
           i       j
'''
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        def  in_order(w1, w2):
            w1_n = len(w1)
            w2_n = len(w2)
            n = min(w1_n, w2_n)
            for i in range(n):
                if w1[i] != w2[i]:
                    if order[w1[i]] > order[w2[i]]:
                        return False
                    else:
                        return True
            return True if w1_n < w2_n else False

        n = len(words) #3
        if n == 0 or n == 1:
            return True
        order = {v:i for i,v in enumerate(order)}
        i = 0
        for i in range(n-1):
            if not in_order(words[i], words[i+1]):
                return False
        return True


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        s = Solution()
        words = ["word","world","row"]
        order = "worldabcefghijkmnpqstuvxyz"
        self.assertEqual(s.isAlienSorted(words,order), False)


unittest.main(verbosity=2)

