#------------------------------------------------------------------------------
# Question: 1055_shortest_way_to_form_string.py
#------------------------------------------------------------------------------
# tags: #medium #greedy
'''
From any string, we can form a subsequence of that string by deleting some
number of characters (possibly no deletions).

Given two strings
source and target, return the minimum number of subsequences of source such that
their concatenation equals target. If the task is impossible, return -1.

 

Example 1:

Input: source = "abc", target = "abcbc"
Output: 2
Explanation: The target "abcbc" can be formed by "abc" and "bc", which are
subsequences of source "abc".
Example 2:

Input: source = "abc", target = "acdbc"
Output: -1
Explanation: The target string cannot be constructed from the subsequences of
source string due to the character "d" in target string.
Example 3:

Input: source = "xyz", target = "xzyxz"
Output: 3
Explanation: The target string can be constructed as follows "xz" + "y" + "xz".
 

Constraints:

Both the source and target strings consist of only lowercase English letters from "a"-"z".
The lengths of source and target string are between 1 and 1000.

'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *

class Solution:
    '''
    Time: O(S*T)
    Space: O(1)
    '''
    def shortestWay(self, source: str, target: str) -> int:
        count = 0
        i = 0
        for c in target:
            i = source.find(c, i)
            if i == -1:
                # reset i to look from beggining of source
                i = source.find(c,0)
                if i == -1:
                    return -1
                count += 1
            i += 1
            return count + 1

import collections
class Solution2:
    '''
    Time: O()
    Space: O()

    source = abcabc
    target = ababab
    d[a] = [0,3]
    d[b] = [1,4]
    d[c] = [2,5]

j = 2
     i   i
    [0,1,2,3,4,5]
    '''
    def shortestWay(self, source: str, target: str) -> int:
        char_indices = collections.defaultdict(list)
        for i,v in enumerate(source):
            char_indices[v].append(i)
        print(char_indices)

#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        source = "abc"
        target = "abcbc"

        s = Solution()
        self.assertEqual(s.shortestWay(source, target), 2)

    def test_simple2(self):
        source = "abc"
        target = "abdc"

        s = Solution()
        self.assertEqual(s.shortestWay(source, target), -1)

    def test_simple3(self):
        source = "xyz"
        target = "xzyxz"

        s = Solution()
        self.assertEqual(s.shortestWay(source, target), 3)

        s = Solution2()
        self.assertEqual(s.shortestWay(source, target), 3)


unittest.main(verbosity=2)

