# ------------------------------------------------------------------------------
# Question:
# ------------------------------------------------------------------------------
# tags:
'''
Given a string S, return the "reversed" string where all characters that are not a
letter stay in the same place, and all letters reverse their positions.

 

Example 1:

Input: "ab-cd"
Output: "dc-ba"
Example 2:

Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"

'''

# ------------------------------------------------------------------------------
# Solutions
# ------------------------------------------------------------------------------

import unittest
from typing import *


class Solution:

    '''
    Input: "a-bC-dEf-ghIj"
    Output: "j-Ih-gfE-dCba"

    a           j
    j-Ih-gfE-dCba
      s
               e

    --j-----c---
            s
            e
    '''
    def reverseOnlyLetters(self, S: str) -> str:
        n = len(S)
        s = 0
        e = n-1
        arr = list(S)
        while s < n and not(S[s].isalpha()):
            s += 1
        while e > 0 and not(S[e].isalpha()):
            e -= 1

        while s < e:
            l,r = arr[s].isalpha(), arr[e].isalpha()
            if l == r:
                if l:
                    arr[s], arr[e] = arr[e], arr[s]
                s += 1
                e -= 1
            elif not(l):
                s += 1
            elif not(r):
                e -= 1
        return "".join(arr)

# ------------------------------------------------------------------------------
# Tests
# ------------------------------------------------------------------------------

class TestSolution(unittest.TestCase):
    def test_simple(self):
        s = Solution()
        S = "a-bC-dEf-ghIj"
        self.assertEqual(s.reverseOnlyLetters(S), "j-Ih-gfE-dCba")


unittest.main(verbosity=2)

