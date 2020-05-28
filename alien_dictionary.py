#------------------------------------------------------------------------------
# Question:
#------------------------------------------------------------------------------
# tags:
'''
There is a new alien language which uses the latin alphabet. However, the
order among letters are unknown to you. You receive a list of non-empty words
from the dictionary, where words are sorted lexicographically by the rules of
this new language. Derive the order of letters in this language.

Example 1:

Input:
[
   wer
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"
Example 2:

Input:
[
  "z",
  "x"
]

Output: "zx"
Example 3:

Input:
[
  "z",
  "x",
  "z"
] 

Output: "" 

Explanation: The order is invalid, so return "".

'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *
import collections

class Solution:
    '''
    Time:
    Space:

    m = average minimum length of words
    n = word in words
    '''
    def alienOrder(self, words: List[str]) -> str:

        # Extract dependencies from input and put into graph
        graph = collections.defaultdict(set)
        in_degree = collections.Counter({c: 0 for word in words for c in word})
        n = len(words)
        for w1, w2 in zip(words, words[1:]): #O(n*m)
            for c1, c2 in zip(w1, w2): #O
                if c1 != c2:
                    if c1 in graph[c2]: return ""
                    if c2 not in graph[c1]:
                        graph[c1].add(c2)
                        in_degree[c2] += 1
                    break
            else: # check if w2 is a perfix if w1
                if len(w2) < len(w1): return ""

        print(graph)
        print(in_degree)

        #check circular Reference
        # Don't have to check, instead check if the output len of char
        # is the same as the number of chars in the graph

        #traverse graph topological order
        result = []
        q = [c for c in in_degree if in_degree[c] == 0]
        print(q)
        while q:
            node = q.pop()
            result.append(node)
            #remove incomming edge from nodes that depend on node
            for nei in graph[node]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)
        if len(in_degree) != len(result): return ""
        return "".join(result)


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest


class TestSolution(unittest.TestCase):
    # def test_simple(self):
    #     s = Solution()
    #     input = ["wrt", "wrf", "er", "ett", "rftt"]
    #     self.assertEqual(s.alienOrder(input), "wertf")

    # def test_simple2(self):
    #     s = Solution()
    #     input = ["bsusz","rhn","gfbrwec","kuw","qvpxbexnhx","gnp","laxutz","qzxccww"]
    #     self.assertEqual(s.alienOrder(input), "")


    def test_simple3(self):
        s = Solution()
        input = ["wrt","wrf","er","ett","rftt","te"]
        self.assertEqual(s.alienOrder(input), "wertf")


unittest.main(verbosity=2)
