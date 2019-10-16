#------------------------------------------------------------------------------
# Questions
#------------------------------------------------------------------------------
# tags:
'''
Equations are given in the format A / B = k, where A and B are variables represented
as strings, and k is a real number (floating point number). Given some queries,
return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values,
vector<pair<string, string>> queries , where equations.size() == values.size(),
and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].

'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *
import collections

class Solution(object):
    '''
    Time:
    Space:
    '''
    def calcEquation(self, equations, values, queries):

        def dfs(start, end, cost, paths):
            if start == end and start in G:
                paths[0] = cost
                return
            if start in vis:
                return
            if start not in G or end not in G:
                return
            vis.add(start)
            for v, node in G[start]:
                dfs(node, end, cost * v, paths)

        G = collections.defaultdict(set)
        for (A, B), V in zip(equations, values):
            G[A].add((V,B))
            G[B].add((1.0/V,A))
        res = []
        for X, Y in queries:
            paths = [-1.0]
            vis = set()
            dfs(X, Y, 1.0, paths)
            res += paths[0],
        return res


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        equations = [["a", "b"], ["b", "c"]]
        values = [2.0, 3.0]
        queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]
        s = Solution()
        self.assertEqual(s.calcEquation(equations, values, queries), [6.0, 0.5, -1.0, 1.0, -1.0 ])


    def test_simple2(self):
        equations = [["a", "b"], ["b", "c"]]
        values = [2.0, 3.0]
        queries = [["a", "e"]]
        s = Solution()
        self.assertEqual(s.calcEquation(equations, values, queries), [-1.0])


unittest.main(verbosity=2)

