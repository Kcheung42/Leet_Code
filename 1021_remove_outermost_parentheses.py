#------------------------------------------------------------------------------
# Question:
#------------------------------------------------------------------------------
# tags:
'''
A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where
A and B are valid parentheses strings, and + represents string concatenation.
For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

A valid parentheses string S is primitive if it is nonempty, and there does not
exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string S, consider its primitive decomposition:
S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

Return S after removing the outermost parentheses of every primitive string
in the primitive decomposition of S.

 

Example 1:

Input: "(()())(())"
Output: "()()()"
Explanation: 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
Example 2:

Input: "(()())(())(()(()))"
Output: "()()()()(())"
Explanation: 
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
Example 3:

Input: "()()"
Output: ""
Explanation: 
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".

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
    def removeOuterParentheses(self, S: str) -> str:
        print('here')
        def find_end(i):
            open_count = 1
            i += 1
            while open_count > 0:
                if S[i] == '(':
                    open_count += 1
                else:
                    open_count -= 1
                i += 1
            return i

        n = len(S)
        if n == 0:
            return ""
        partitions = []
        start = 0
        i = start
        while i < n:
            end = find_end(i)
            partitions.append([start, end])
            start = i = end
        partitions = [[x+1,y-1] for x,y in partitions]
        return "".join([S[x:y] for x,y in partitions])


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        string = "((1)(2))((3))"
        s = Solution()
        self.assertEqual(s.removeOuterParentheses(string), "(1)(2)(3)")

    def test_simple(self):
        string = "(()())(())(()(()))"
        s = Solution()
        self.assertEqual(s.removeOuterParentheses(string), "()()()()(())")


unittest.main(verbosity=2)

