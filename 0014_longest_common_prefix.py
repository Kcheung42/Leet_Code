# ------------------------------------------------------------------------------
# Question: 0014_longest_common_prefix.py
# ------------------------------------------------------------------------------
# tags:
'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

'''

# ------------------------------------------------------------------------------
# Solutions
# ------------------------------------------------------------------------------

from typing import *


class TrieNode():
    def __init__(self, x):
        self.val = x
        self.children = {}
        self.count = 0
        self.isword = False


class Trie():
    '''
    Trie:

    r > f > l > o > w > e > r
              |   > s > s
              |   > b
              > i > c > k
              |
              > a > P
    '''
    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode(c)
            cur = cur.children[c]
            cur.count += 1
        cur.isword = True


class Solution:
    '''
    Time:
    Space:
    '''
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def dfs(root, result=""):
            # nonlocal result
            if len(root.children) > 1 or root.isword:
                return result
            for key, child in list(root.children.items()):
                # result += key
                return dfs(child, result + key)

        trie = Trie()
        for s in strs:
            trie.insert(s)
        result = ""
        return dfs(trie.root)
        # cur = trie.root
        # if len(cur.children) > 1:
        #     return ""
        # key = list(cur.children.keys())[0]
        # cur = cur.children[key]
        # while not cur.isword and len(cur.children) == 1:
        #     result += cur.val
        #     key = list(cur.children.keys())[0]
        #     cur = cur.children[key]
        return result


# ------------------------------------------------------------------------------
# Tests
# ------------------------------------------------------------------------------

import unittest


class TestSolution(unittest.TestCase):
    def test_simple(self):
        s = Solution()
        words = ["flower","flow","floght"]
        self.assertEqual(s.longestCommonPrefix(words), "flo")


unittest.main(verbosity=2)

