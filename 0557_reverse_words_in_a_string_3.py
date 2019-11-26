#------------------------------------------------------------------------------
# Question:
#------------------------------------------------------------------------------
# tags:
'''

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
    def reverseWords(self, s:str) -> str:
        s = [c for c in s]
        n = len(s)
        i = 0
        while i < n:
            start = i
            while i < n and s[i] != ' ':
                i += 1
            temp = i
            i -= 1
            while start < i:
                s[start], s[i] = s[i], s[start]
                if start +1 == i:
                    break
                start += 1
                i -= 1
            i = temp + 1

        return "".join(s)

class SolutionRecur:
    def reverseWords(self, s:str) -> str:

        def reverse_str(string):
            if len(string) == 0:
                return ""
            first = string[0]
            remaining = string[1:]
            return reverse_str(remaining) + first

        def recur(s, start, cur):
            if cur == len(s):
                return []
            elif s[cur] == ' ':
                return (recur(s, cur+1, cur+1))
            elif cur+1 == len(s) or s[cur+1] == ' ':
                word = reverse_str(s[start:cur+1])
                return ([word] + recur(s, cur+1, cur+1))
            else:
                return(recur(s, start, cur+1))
        result = recur(s, 0,0)
        return " ".join(result)

#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        s = Solution()
        string = "Let's take LeetCode contest"
        self.assertEqual(s.reverseWords(string), "s'teL ekat edoCteeL tsetnoc")

        s = SolutionRecur()
        self.assertEqual(s.reverseWords(string), "s'teL ekat edoCteeL tsetnoc")


unittest.main(verbosity=2)

