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
    '''


#     def canFinish(self, numCourses, prerequisites):

#         # @debug
#         def dfs(course):
#             visited[course] = True
#             for nei in graph[course]:
#                 if visited[nei] == False:
#                     dfs(nei)
#             stack.append(course)

#         visited = [False] * numCourses
#         graph = collections.defaultdict(set)
#         stack = []
#         for course, pre in prerequisites:
#             graph[course].add(pre)
#         print(graph)

#         # check for cycles

#         for i in range(numCourses):
#             if visited[i] == False:
#                 dfs(i)
#         print(stack)
#         return(len(stack) == numCourses)


class SolutionLeet:
    '''
    Time:
    Space:
    Intuition: Topological Sort
    '''
    def canFinish(self, numCourses, prerequisites):
        courses = collections.defaultdict(set)
        prereqs = collections.defaultdict(set)
        for course, pre in prerequisites:
            courses[course].add(pre)
            prereqs[pre].add(course)

        #get all nodes that don't have a prerequisite
        stack = [n for n in range(numCourses) if not courses[n]]
        '''
        0 > 1 > 2
            ^___|
        '''
        print(f'\n courses: {courses}')
        print(f'\n neighbors: {prereqs}')
        count = 0
        print(f'\n starting stack: {stack}')
        while stack:
            print(f'\n stack: {stack}')
            course = stack.pop()
            # print(f'\nnode: {course}')

            count += 1
            # print(f'\ncount: {count}')

            for p in prereqs[course]:
                courses[p].remove(course)
                # course does not have any pre-reqs to process
                if not courses[p]:
                    stack.append(p)
        # print(f'\ncount: {count}')

        return count == numCourses


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest


class TestSolution(unittest.TestCase):
    def test_simple_true(self):
        numsCourses = 2
        prereqs = [[0, 1]]
        s = SolutionLeet()
        self.assertEqual(s.canFinish(numsCourses, prereqs), True)

        prereqs = [[1, 0], [0, 1]]
        s = SolutionLeet()
        self.assertEqual(s.canFinish(numsCourses, prereqs), False)

    def test_simple_false2(self):
        '''
        1 > 0
        ^___|
        '''
        numsCourses = 2
        prereqs = [[0, 1], [1, 0]]
        s = SolutionLeet()
        self.assertEqual(s.canFinish(numsCourses, prereqs), False)

    def test_simple_false3(self):
        '''
        0 > 1 > 2
        ^_______|
        '''
        numsCourses = 3
        prereqs = [[2, 1], [1, 0], [0, 2]]
        s = SolutionLeet()
        self.assertEqual(s.canFinish(numsCourses, prereqs), False)


    def test_simple_false4(self):
        '''
        0 > 1 > 2
            ^___|
        '''
        numsCourses = 3
        prereqs = [[2, 1], [1, 0], [1, 2]]
        s = SolutionLeet()
        self.assertEqual(s.canFinish(numsCourses, prereqs), False)

    def test_two_classes_require_one(self):
        numsCourses = 3
        prereqs = [[0, 1], [0, 2], [1, 2]]
        s = SolutionLeet()
        self.assertEqual(s.canFinish(numsCourses, prereqs), True)

    def test_circular(self):
        '''
        graph:
        0 : []
        1 : [0,4]
        2 : [1]
        3 : [2]
        4 : [0]
        5 : []

        Cycle exists

                3
                ^
        0 > 1 > 2
        ^   |   |
        4<--*   |
        ^-------*
        '''

        numsCourses = 6
        prereqs = [[1, 0], [2, 1], [3, 2], [4, 1], [0, 4], [2, 4]]
        s = SolutionLeet()
        self.assertEqual(s.canFinish(numsCourses, prereqs), False)


unittest.main(verbosity=2)
