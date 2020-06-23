# ------------------------------------------------------------------------------
# Question:0639_decode_ways_2.py
# ------------------------------------------------------------------------------
# tags:
'''
A message containing letters from A-Z is being encoded to numbers using the
following mapping way:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Beyond that, now the encoded string can also contain the character '*', which
can be treated as one of the numbers from 1 to 9.

Given the encoded message containing digits and the character '*', return the
total number of ways to decode it.

Also, since the answer may be very large, you should return the
output mod 109 + 7.

Example 1:
Input: "*"
Output: 9
Explanation: The encoded message can be decoded to the string:
 "A", "B", "C", "D", "E", "F", "G", "H", "I".

Example 2:
Input: "1*"
Output: 9 + 9 = 18
Note:
The length of the input string will fit in range [1, 105].
The input string will only contain the character '*' and digits '0' - '9'.

'''

# ------------------------------------------------------------------------------
# Solutions
# ------------------------------------------------------------------------------

import unittest
from typing import *

class Solution:
    '''
              3
             /
            *3
           /
         2*3
        /
    12*3
        \
           3 => 1
          /
         *3 =>
          \
           '' =>

    for len of 2 having *:
    *1...6 => *->[1,2] = 2 * 6
    *7...9 => *->[1] = 9


    ex: 1* , 9* , 11 , 19
    if index is a number:
    branch1 = recur and increment index by 1

    if first > 2 => don't branch
    branch2 = recur and increment index by 2
    if first = 1 and second = * => 9 * branch2
    if first = 2 and second = * => 6 * branch2
    if second 

    return branch1 + branch2


    if index is a *:
    branch1 = recur and increment index by 1
    branch2 = recur and increment index by 2
    return branch1 + branch2


    '''
    def numDecodings(self, s: str) -> int:


        pass

class Solution:
    '''
    Time:
    Space:

               3=>1
              /
            *3=>1 + 1 * 9
              \
           /   ''=>1
          2*3=>11
           \   *=>9
              /
             **=>11
              \
        /      ''=> 1
    12*3=>
        \   3=>1
           /
          *3=>
           \
            ''=>1

       *=> 9
      /
    1*=>18
      \
       ''=> 1

    * = 9
    1* = 18
    2* = 6

    *?
      ? 1->6 => 2
      ? 7->9 => 1

       1
    *1=>9 * 1 + 2
       1

        *1
    **1
        1
    '''
    def numDecodings(self, s: str) -> int:
        def dfs(cur):
            if not cur:
                return 1
            if cur[0] == '0':
                return 0

            if len(cur) == 1:
                if cur == '*':
                    return 9
                return 1

            if len(cur) == 2:
                if cur == '1*':
                    return 18
                elif cur == '2*':
                    return 6
                elif cur[0] == '*':
                    return 2 if int(cur[1]) <= 6 else 1

            multi = 1
            left = dfs(cur[1:])
            if cur[0] != '*':
                # 1*1, 1*9, 111, 999
                if cur[1] == '*' or int(cur[:2]) <= 26:
                    right = dfs(cur[2:])
            else:
                # *11, *99, **1
                if int(cur[1]) <= 6 or cur[:2] =='**':
                    right = dfs(cur[2:])

            if cur[0] == '*':
                multi = 9
            return (left + right) * multi
        d = {
            '*': 9,
            '1*': 18,
            '2*': 6,
        }
        return dfs(s)


# ------------------------------------------------------------------------------
# Tests
# ------------------------------------------------------------------------------

class TestSolution(unittest.TestCase):
    def test_simple(self):
        s = Solution()
        self.assertEqual(True, True)


unittest.main(verbosity=2)

