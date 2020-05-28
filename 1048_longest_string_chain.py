#------------------------------------------------------------------------------
# Question: 1048_longest_string_chain.py
#------------------------------------------------------------------------------
# tags:
'''
Given a list of words, each word consists of English lowercase letters.

Let's say word1 is a predecessor of word2 if and only if we can add exactly
one letter anywhere in word1 to make it equal to word2.  For example, "abc" is a
predecessor of "abac".

A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1,
where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.

Return the longest possible length of a word chain with words chosen from the
given list of words.

Example 1:

h[a] = 1
h[b] = 1
h[ba] = 2
h[bca] = 2 check:for x (_ca, b_a, ...), if in h, h[bca] = max([x1,x2,x3, ...])

Input: ["bdca", "a","b","ba","bca","bda","ca"]
Output: 4
Explanation: one of the longest word chain is "a","ba","bda","bdca".

init dp: -> serve as already visited node and store already calculated len
dp[bdca] = None
dp[a] = None
dp[b] = None
... etc

for word in words if dp[word] == None

start dfs: bdca
dp[bdca]: 4
    dp[dca]: return 0 NOT in DP
    dp[bca]: 3
        dp[ca]: 2
            dp[a]: 1
                dp[""]: return 0 NOT in DP
            dp[c]: return 0 NOT in DP
        dp[ba]: 2
            dp[b]: 1
                dp[""]: return 0 NOT in DP
            dp[a]: 1 -> already calcualted, don't dfs, just look up
    dp[bda]: 3
        dp[da]: return 0 Not in DP
        dp[ba]: 2 -> already calculated in dp, end dfs
        dp[bd]: return 0 Not in DP

current dp
bdca: 4
bca: 3
ca: 2
a: 1
b: 1
bda: 3

start dfs: a -> already calcualted in dp, skip
start dfs: b -> already calculated in dp, skip



'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *
from pprint import pprint

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        h = {}
        for w in sorted(words, key=len):
            h[w] = max(h.get(word[:i] + word[i+1:],0) + 1 for i in range(len(w)))
            return max(h.values())

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def dfs(word):
            if word not in dp:
                return 0
            if not dp[word]:
                dp[word] = max([dfs(word[:i]+word[i+1:]) + 1 for i in range(len(word))])
            return dp[word]

        #keep track of already visited and calculated lens (seen and memo)
        dp = {word: None for word in words}
        ans = [dfs(word) for word in dp if not dp[word]]
        print('\n')
        pprint(dp)
        return max(ans)

# class Solution:
#     def longestStrChain(self, words: List[str]) -> int:
#         h = set(words)
#         graph = {}
#         for w in words:
#             graph[w] = 1
#             for i in range(len(w)):
#                 x = w[:i] +w[i:1:]
#                 if x in h:
#                     graph[x] = graph.get(x,0) + graph[w]
#         return max(h.values())

#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        s = Solution()
        words = ["bdca", "a","b","ba","bca","bda","ca"]
        self.assertEqual(s.longestStrChain(words), 4)


unittest.main(verbosity=2)

