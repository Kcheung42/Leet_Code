#------------------------------------------------------------------------------
# Question: 0151_reverse_words_in_string.py
#------------------------------------------------------------------------------
# tags: #medium
'''
Given an input string, reverse the string word by word.

Example 1:

Input: "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single
space in the reversed string.


Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed
string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the
reversed string.

'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *


class SolutionIterative:
    '''
    Time:
    Space:
    '''
    def reverseWords(self, s: str) -> str:
        s = s.split()
        n = len(s)
        l = 0
        r = n - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        print(s)
        return(" ".join(s))


class SolutionRecur:
    '''
    Time:
    Space:
    '''
    def reverseWords(self, s: str) -> str:
        def str_reverse_words(s, start, cur):
            if cur == len(s):
                return []
            if s[cur] == " ":
                return str_reverse_words(s, cur+1, cur+1)
            elif cur+1 == len(s) or s[cur+1] == ' ':
                word =  s[start:cur+1]
                print(f'word:{word}')
                return str_reverse_words(s, cur+1, cur + 1) + [word]
            else:
                return str_reverse_words(s, start, cur+1)
        return(" ".join(str_reverse_words(s, 0, 0)))


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        str = "the sky is blue"
        s = SolutionRecur()
        self.assertEqual(s.reverseWords(str), "blue is sky the")

        s = SolutionIterative()
        self.assertEqual(s.reverseWords(str), "blue is sky the")


unittest.main(verbosity=2)

