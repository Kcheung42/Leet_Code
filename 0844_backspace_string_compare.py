#------------------------------------------------------------------------------
# Question:
#------------------------------------------------------------------------------
# tags:
'''
Given two strings S and T, return if they are equal when both are typed into
empty text editors. # means a backspace character.

Explanation: Both S and T become "ac".


Example 1:
Input: S = "ab#c", T = "ad#c"
Output: true

Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".

'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *

class Solution:
    '''
    Time: O(n)
    Space: O(n)
    '''
    def backspaceCompare(self, S: str, T: str) -> bool:
        #loop through each S and T:
        # if char is  not #: push onto stack
        # if char is #: pop off stack
        # compare both stacks are equal
        stack = []
        stack2 = []
        for c in S:
            if c == '#':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(c)
        for c in T:
            if c == '#':
                if len(stack2) > 0:
                    stack2.pop()
            else:
                stack2.append(c)
        print(stack)
        print(stack2)
        return stack == stack2

class Solution2:
    '''
    Time: O(n)
    Space: O(1)
    '''
    def backspaceCompare(self, S: str, T: str) -> bool:
        #loop through each S and T:
        # if char is  not #: push onto stack
        # if char is #: pop off stack
        def build_string(string):
            result = ""
            i = len(string) - 1
            skip = 0
            while i >= 0:
                if string[i] == "#":
                    skip += 1
                elif skip > 0:
                    skip -= 1
                else:
                    result += string[i]
                i -= 1
            return result

        str1 = build_string(S)
        str2 = build_string(T)
        return(str1 == str2)


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        S = "ab#c"
        T = "ad#c"
        s = Solution2()
        self.assertEqual(s.backspaceCompare(S,T), True)

    def test_simple2(self):
        S = "bxj##tw"
        T = "bxj###tw"
        s = Solution2()
        self.assertEqual(s.backspaceCompare(S,T), False)


unittest.main(verbosity=2)

