#------------------------------------------------------------------------------
# Question:
#------------------------------------------------------------------------------
# tags:
'''
Given a non-empty string s, you may delete at most one character. Judge
whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of
the string is 50000.

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
    def validPalindrome(self, s: str) -> bool:

        def checkPalindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
                if i == j or i + 1 == j:
                    break
            return True

        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return checkPalindrome(i, j-1) or checkPalindrome(i+1, j)
            i += 1
            j -= 1
            if i == j or i + 1 == j:
                break
        return True

class Solution2:
    def validPalindrome(self, s: str) -> bool:
        n = len(s) // 2
        i = 0
        while i < n and s[i] == s[-(i+1)]:
            i += 1
        s = s[i:len(s)-i]

        return s[:-1] == s[:-1][::-1] \
            or s[1:] == s[1:][::-1]

#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        string = "aba"
        s = Solution()
        self.assertEqual(s.validPalindrome(string), True)

        s = Solution2()
        self.assertEqual(s.validPalindrome(string), True)

    def test_simple2(self):
        string = "aabaxa"
        s = Solution()
        self.assertEqual(s.validPalindrome(string), True)

        s = Solution2()
        self.assertEqual(s.validPalindrome(string), True)



unittest.main(verbosity=2)

