#------------------------------------------------------------------------------
# Question:
#------------------------------------------------------------------------------
# tags:

'''
125. Valid Palindrome
Given a string, determine if it is a palindrome, considering only alphanumeric
characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false

'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *

class Solution:
    '''
    Time: O(n)
    Space: O(n)
    Intuition: add the first half of chars to a stack then compare the rest
    with the top of the stack. For odd numbers the index needs to be increased.
    '''
    def isPalindrome(self, s: str) -> bool:
        new_s = ''.join(c.lower() for c in s if c.isalpha() or c.isdigit())
        n = len(new_s)
        mid = n // 2
        stack = []
        for i in range(mid):
            stack.append(new_s[i])

        #for odd strings
        mid = mid + 1 if n % 2 == 1 else mid

        for i in range(mid, n):
            top = stack.pop()
            if top != new_s[i]:
                return False
            i += 1
        return True


class Solution2:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''.join(c.lower() for c in s if c.isalpha() or c.isdigit())
        i = 0
        j = len(new_s)
        print(f'Testing:s[{i}:{j}]:{s[i:j]}')
        return all([s[k] == s[j-k+i] for k in range(i,j)])

#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        string = "A man, a plan, a canal: Panama"
        s = Solution()
        self.assertEqual(s.isPalindrome(string), True)

        s = Solution2()
        self.assertEqual(s.isPalindrome(string), False)

    def test_simple2(self):
        string = "0P"
        s = Solution()
        self.assertEqual(s.isPalindrome(string), False)

        s = Solution2()
        self.assertEqual(s.isPalindrome(string), False)

    def test_simple3(self):
        string = "aa"
        s = Solution()
        self.assertEqual(s.isPalindrome(string), True)

        s = Solution2()
        self.assertEqual(s.isPalindrome(string), True)



unittest.main(verbosity=2)

