# ------------------------------------------------------------------------------
# Question:
# ------------------------------------------------------------------------------
# tags:
'''

'''

# ------------------------------------------------------------------------------
# Solutions
# ------------------------------------------------------------------------------

import unittest
from typing import *


import heapq
import collections

class SolutionNotWorking:
    def shortestBridge(self, A: List[List[int]]) -> int:
        '''
        [
        [1,1,1,1,1],
        [1,0,0,0,1],
        [1,0,1,0,1],
        [1,0,0,0,1],
        [1,1,1,1,1]

        ]
        island1 = set([0,0], [0,1] ...)
        island2 = set([2,2], [2,3])
        '''

        def neighbors(r,c):
            nei = ((r-1,c),(r,c-1),(r+1,c),(r,c+1))
            for nr, nc in nei:
                if 0 <= nr < R and 0 <= nc < C and A[nr][nc] == 1:
                    yield nr, nc

        def dijkstras(s, e):
            h = [(s, 0)]
            visited = set([])
            while h:
                node, cost = heapq.heappop(h)

                if node == e: return cost

                if node not in visited:
                    visited.add(node)
                for r,c in neighbors(node[0],node[1]):
                    if (r,c) not in visited:
                        heapq.push(((r, c), cost + 1))
            return False

        def bfs(r, c, island_number):
            q = [(r,c)]
            visited = set([])
            while q:
                row, col = q.pop(0)
                A[row][col] = 0
                islands[island_number].append((row, col))
                visited.add((row, col))
                for nr, nc in neighbors(row, col):
                    if (nr,nc) not in visited:
                        q.append((nr, nc))

        def dfs(r,c,island_number):
            A[r][c] = 0
            islands[island_number].append((r, c))
            for nr, nc in neighbors(r, c):
                dfs(nr, nc, island_number)

        R = len(A)
        C = len(A[0])
        islands = collections.defaultdict(list)
        island_number = 0
        for r in range(R):
            for c in range(C):
                if A[r][c] == 1:
                    island_number += 1
                    bfs(r,c, island_number)
                    # dfs(r,c, island_number)
        return min([dijkstras(s,e) for s in islands[1] for e in islands[2]])
        print(islands)


class Solution(object):
    def shortestBridge(self, A):
        R, C = len(A), len(A[0])

        def neighbors(r, c):
            nei = ((r-1,c),(r,c-1),(r+1,c),(r,c+1))
            for nr, nc in nei:
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        def get_components():

            def dfs(r, c):
                for nei in neighbors(r, c):
                    if A[nei[0]][nei[1]] and nei not in seen:
                        seen.add(nei)
                        dfs(*nei)

            visited = set()
            components = []
            for r, row in enumerate(A):
                for c, val in enumerate(row):
                    if val and (r, c) not in visited:
                        # Start dfs
                        seen = {(r, c)}
                        dfs(r,c)
                        # stack = [(r,c)]
                        # while stack:
                        #     node = stack.pop()
                        #     for nei in neighbors(*node):
                        #         if A[nei[0]][nei[1]] and nei not in seen:
                        #             stack.append(nei)
                        #             seen.add(nei)
                        visited |= seen
                        components.append(seen)
            return components

        source, target = get_components()
        queue = collections.deque([(node, 0) for node in source])
        visited = set(source)
        while queue:
            node, d = queue.popleft()
            if node in target: return d-1
            for nei in neighbors(*node):
                if nei not in visited:
                    queue.append((nei, d+1))
                    visited.add(nei)
class Solution:
    def shortestBridge(self, A):
        def dfs(i, j):
            A[i][j] = -1
            bfs.append((i, j))
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < n and 0 <= y < n and A[x][y] == 1:
                    dfs(x, y)
        def first():
            for i in range(n):
                for j in range(n):
                    if A[i][j]:
                        return i, j
        n, step, bfs = len(A), 0, []
        dfs(*first())
        while bfs:
            new = []
            for i, j in bfs:
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < n and 0 <= y < n:
                        if A[x][y] == 1:
                            return step
                        elif not A[x][y]:
                            A[x][y] = -1
                            new.append((x, y))
            step += 1
            bfs = new

class Solution(object):
    def shortestBridge(self, A):
        '''
        [
        [x,x,x,1,1],
        [1,x,0,0,1],
        [1,0,1,0,1],
        [1,0,0,0,1],
        [1,1,1,1,1]
        ]
        grow island 1 by one pixel until reaching other island
        '''

        def neighbors(r, c):
            for nr, nc in ((r-1, c),(r+1, c),(r, c-1),(r, c+1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        def dfs(r, c):
            A[r][c] = -1
            bfs.append((r, c))
            for nr, nc in neighbors(r,c):
                if A[nr][nc] == 1:
                    dfs(nr, nc)

        def first():
            for r in range(R):
                for c in range(C):
                    if A[r][c] == 1:
                        return (r, c)
        R, C = len(A), len(A[0])
        bfs = []
        dfs(*first())
        step = 0
        while bfs:
            q_len = len(bfs)
            for _ in range(q_len):
                r, c = bfs.pop(0)
                for nr, nc in neighbors(r,c):
                    if A[nr][nc] == 1: # found second island
                        return step
                    elif A[nr][nc] == 0:
                        A[nr][nc] = -1
                        bfs.append((nr, nc))
            step += 1


# ------------------------------------------------------------------------------
# Tests
# ------------------------------------------------------------------------------

class TestSolution(unittest.TestCase):
    def test_simple(self):
        s = Solution()
        A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
        self.assertEqual(s.shortestBridge(A), 1)


unittest.main(verbosity=2)

# {1: [(0, 0), (1, 0), (0, 1), (2, 0), (0, 2), (3, 0), (0, 3), (4, 0), (0, 4), (4, 1), (1, 4), (4, 2), (2, 4), (4, 3), (3, 4), (4, 4), (4, 4)], 2: [(2, 2)]}

# {1: [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (3, 4), (2, 4), (1, 4), (0, 4), (0, 3), (0, 2), (0, 1)], 2: [(2, 2)]}
