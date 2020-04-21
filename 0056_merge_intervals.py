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


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        '''

        SORT BY START
        [[1, 3], [2,6], [8, 10], [15, 18]]
                                  s    e

          [1,3] [2,6] - need merge
          [1,3] [3,6] - need merge
          [1,3] [4,6] - does not need to merge

        result [[1, 6], [8, 10], [15, 20]]

        2 var
        s -> start of interval ->init intervals[0][0]
        e -> end of interval ->.init intervals[0][1]

        loop through intervals:
           if i[start] <= e, then I need to merge
               merge: set e to interval[end]

           else add [s,e] to result and move s to next interval start and e to next interval end
        add [s, e] to result
        '''

        result = []
        n = len(intervals)
        if n == 0:
            return result
        intervals = sorted(intervals, key=lambda x: x[0])
        start = 0
        end = 1
        s = intervals[0][start]  # 1
        e = intervals[0][end]  # 3
        for i in range(1, n):  #[8, 10]
            if intervals[i][start] <= e:  #8 <= 6
                #merge
                e = max(e, intervals[i][end])  #
            else:
                result.append([s, e])
                s = intervals[i][start]
                e = intervals[i][end]
                '''
                result = [[1,6]]
                '''
        result.append([s, e])
        return result


class SolutionSort:
    '''
    Medium if sorting first
    [1, 4], [5, 10]
    result = [[1,4]]
    '''
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = []
        start = 0
        end = 1
        for interval in intervals:
            if not result or result[-1][end] < interval[start]:
                result.append(interval)
            else:
                #need to merge
                result[-1][end] = max(result[-1][end], interval[end])
        return result


import collections


class SolutionGraph:
    '''
    Complexity Analysis

    Time complexity : O(n^2)

    Building the graph costs O(V + E) = O(V) + O(E) = O(n) + O(n^2)
    time, as in the worst case all intervals are mutually overlapping. Traversing
    the graph has the same cost (although it might appear higher at first) because
    our visited set guarantees that each node will be visited exactly once.
    Finally, because each node is part of exactly one component, the merge step
    costs O(V)=O(n) time. This all adds up as follows:

    O(n^2) + O(n^2) + O(n) = O(n^2)

    Space complexity : O(n^2)

    As previously mentioned, in the worst case, all intervals are mutually
    overlapping, so there will be an edge for every pair of intervals.
    Therefore, the memory footprint is quadratic in the input size.
    '''

    '''
    Graph:
    {
    (1, 3): [[2, 6], [0, 4]],
    (2, 6): [[1, 3], [0, 4]],
    (0, 4): [[1, 3], [2, 6]],
    (8, 15): [[15, 18]],
    (15, 18): [[8, 15]]}
    '''
    def build_graph(self, intervals):
        '''
        generate graph where there is an undirected edge between intervals u
        and v iff u and v overlap.
        '''
        graph = collections.defaultdict(list)

        def overlap(a, b):
            # (1, 3) (2, 4)
            start = 0
            end = 1
            return a[start] <= b[end] and a[end] >= b[start]

        for i, interval_i in enumerate(intervals):
            # for j in range(i + 1, len(intervals)):
            for j, interval_j in enumerate(intervals[i+1:], i+1):
                if overlap(interval_i, intervals[j]):
                    graph[tuple(interval_i)].append(interval_j)
                    graph[tuple(interval_j)].append(interval_i)

        return graph

    # merges all of the nodes in this connected component into one interval.
    def merge_nodes(self, nodes):
        min_start = min(node[0] for node in nodes)
        max_end = max(node[1] for node in nodes)
        return [min_start, max_end]

    '''
    {
    comp-number : [(interval1), (interval2)]
    0: [(1, 3), (0, 4), (2, 6)],
    1: [(8, 15), (15, 18)],
    2: [(19, 20)]
    }
    '''
    def get_components(self, graph, intervals):
        '''
        gets the connected components of the interval overlap graph.
        '''
        visited = set()
        comp_number = 0
        nodes_in_comp = collections.defaultdict(list)

        #iterative
        def mark_component_dfs(start):
            stack = [start]
            while stack:
                node = tuple(stack.pop())
                if node not in visited:
                    visited.add(node)
                    nodes_in_comp[comp_number].append(node)
                    stack.extend(graph[node])

        # Recursive
        # def mark_component_dfs(start):
        #     node = tuple(start)
        #     visited.add(node)
        #     nodes_in_comp[comp_number].append(node)

        #     for children in graph[tuple(start)]:
        #         n = tuple(children)
        #         if n not in visited:
        #             visited.add(n)
        #             nodes_in_comp[comp_number].append(n)
        #             mark_component_dfs(n)

        # mark all nodes in the same connected component with the same integer.
        for interval in intervals:
            if tuple(interval) not in visited:
                mark_component_dfs(interval)
                comp_number += 1

        print(nodes_in_comp)
        return nodes_in_comp, comp_number

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        graph = self.build_graph(intervals)
        print(graph)
        nodes_in_comp, number_of_comps = self.get_components(graph, intervals)

        # all intervals in each connected component must be merged.
        result = [
            self.merge_nodes(nodes_in_comp[comp])
            for comp in range(number_of_comps)]

        return result


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest


class TestSolution(unittest.TestCase):
    def test_simple(self):
        s = SolutionGraph()
        intervals = [[1, 3], [2, 6], [8, 15], [15, 18], [0, 4], [19, 20]]
        self.assertEqual(s.merge(intervals), [[0, 6], [8, 18], [19, 20]])


unittest.main(verbosity=2)
