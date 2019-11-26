#------------------------------------------------------------------------------
# Question: 027_course_schedule.py
#------------------------------------------------------------------------------
# tags: medium
'''
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to
first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it
possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. To take course 1 you should
have finished course 0. So it is possible.

Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. To take course 1 you should
have finished course 0, and to take course 0 you should also have finished course
1. So it is impossible.

'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *
from test_utils.debug import debug
import collections

class Solution:
    '''
    Time:
    Space:
    Intuition: Topological Sort
    '''
    # def canFinish(self, numCourses, prerequisites):

    #     # @debug
    #     def TopologicalUtil(node, visited, stack, graph):
    #         visited[node] = True
    #         for nei in graph[node]:
    #             if visited[nei] == False:
    #                 TopologicalUtil(nei, visited, stack, graph)
    #         stack.append(node)

    #     visited = [False] * numCourses
    #     stack = []
    #     graph = collections.defaultdict(set)
    #     for course, pre in prerequisites:
    #         graph[course].add(pre)
    #     for i in range(numCourses):
    #         if visited[i] == False:
    #             TopologicalUtil(i, visited, stack, graph)
    #     print(f'\nstack: {stack}')
    #     return(len(stack) == numCourses)

    def canFinish(self, numCourses, prerequisites):
        graph = collections.defaultdict(set)
        neighbors = collections.defaultdict(set)
        for course, pre in prerequisites:
            graph[course].add(pre)
            neighbors[pre].add(course)
        stack = [n for n in range(numCourses) if not graph[n]]

        print(f'\ngraph: {graph}')
        print(f'\nneighbors: {neighbors}')
        count = 0
        while stack:
            # print(f'\nstack: {stack}')
            node = stack.pop()
            print(f'\nnode: {node}')

            count += 1
            # print(f'\ncount: {count}')

            for n in neighbors[node]:
                graph[n].remove(node)
                # print(f'\ngraph: {graph}')
                if not graph[n]:
                    stack.append(n)
        # print(f'\ncount: {count}')

        return count == numCourses


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    # def test_simple_true(self):
    #     numsCourses = 2
    #     prereqs = [[0,1]]
    #     s = Solution()
    #     self.assertEqual(s.canFinish(numsCourses, prereqs), True)

    #     prereqs = [[1,0],[0,1]]
    #     s = Solution()
    #     self.assertEqual(s.canFinish(numsCourses, prereqs), False)

    # def test_simple_false2(self):
    #     numsCourses = 2
    #     prereqs = [[0,1],[1,0]]
    #     s = Solution()
    #     self.assertEqual(s.canFinish(numsCourses, prereqs), False)

    # def test_two_classes_require_one(self):
    #     numsCourses = 3
    #     prereqs = [[0,1],[0,2],[1,2]]
    #     s = Solution()
    #     self.assertEqual(s.canFinish(numsCourses, prereqs), True)

    def test_circular(self):
        '''
        graph:
        0 : []
        1 : [0]
        2 : [1]
        3 : [2]
        4 : [0]
        5 : []
        '''
        numsCourses = 6
        prereqs = [[1,0],[2,1], [3,2], [4,0], [1,4]]
        s = Solution()
        self.assertEqual(s.canFinish(numsCourses, prereqs), False)

unittest.main(verbosity=2)

