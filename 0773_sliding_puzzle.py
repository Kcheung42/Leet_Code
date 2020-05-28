#------------------------------------------------------------------------------
# Question: 0773_sliding_puzzle.py
#------------------------------------------------------------------------------
# tags: #Hard
'''
On a 2x3 board, there are 5 tiles represented by the integers 1 through 5,
and an empty square represented by 0.

A move consists of choosing 0 and a 4-directionally adjacent number and swapping
it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given a puzzle board, return the least number of moves required so that the
state of the board is solved. If it is impossible for the state of the board
to be solved, return -1.

Examples:

Input: board = [[1,2,3],[4,0,5]]
Output: 1
Explanation: Swap the 0 and the 5 in one move.
Input: board = [[1,2,3],[5,4,0]]
Output: -1
Explanation: No number of moves will make the board solved.

Input: board = [[4,1,2],[5,0,3]]
Output: 5
Explanation: 5 is the smallest number of moves that solves the board.
An example path:
After move 0: [[4,1,2],[5,0,3]]
After move 1: [[4,1,2],[0,5,3]]
After move 2: [[0,1,2],[4,5,3]]
After move 3: [[1,0,2],[4,5,3]]
After move 4: [[1,2,0],[4,5,3]]
After move 5: [[1,2,3],[4,5,0]]

Input: board = [[3,2,4],[1,5,0]]
Output: 14

'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *
from pprint import pprint
import collections
import heapq

class Solution:
    '''
    Create Graph where nodes is a state of the board and edges meaning a one move
    change from one state to the next


    Use hash table to represent graph where:
    key = node
    value = list of connected nodes

    init = [[4,1,2], [5,0,3]] => convert to tuple so we can store it in hash 

    412
    503

    graph[((4,1,2), (5,0,3))] = [3-neighbors...]
    graph[neig-1] = [((4,1,2), (5,0,3))]
    graph[neig-2] = [((4,1,2), (5,0,3))]
    graph[neig-3] = [((4,1,2), (5,0,3))]

    use BFS to build bi-directional graph

    '''
    def slidingPuzzle(self, board: List[List[int]]) -> int:

        def to_array(tup):
            return list(list(x) for x in tup)

        def to_tup(arr):
            return tuple(tuple(x) for x in arr)

        def neighbors(r,c):
            neighbors = ((-1, 0), (1,0), (0, -1), (0, 1))
            for nei in neighbors:
                new_r = r + nei[0]
                new_c = c + nei[1]
                if 0 <= new_r < R and 0 <= new_c < C:
                    yield new_r, new_c

        def get_zero_pos():
            for r in range(R):
                for c in range(C):
                    if board[r][c] == 0:
                        return r, c

        def dijkstra(s, e):
            q = [(0, s)]
            seen = set([])
            while q:
                cost, node = heapq.heappop(q)
                if node not in seen:
                    seen.add(node)
                    if node == e: return cost
                    for nei in graph[node]:
                        if nei not in seen:
                            heapq.heappush(q, (cost+1, nei))
            return -1


        #find r,c of 0
        R = len(board)
        C = len(board[0])
        r_start,c_start = get_zero_pos()
        print(f"r_start:{r_start}, c_start:{c_start}")
        graph = collections.defaultdict(list)
        seen = set([])
        first = tuple(tuple(x) for x in board)
        q = [(first, r_start, c_start)]

        #build graph
        while q:
            node, r, c = q.pop(0) #-> expecting array...
            if node not in seen:
                seen.add(node)
                for nr, nc in neighbors(r,c):
                    n_arr = to_array(node)
                    #swap 0 and neighbor
                    n_arr[r][c], n_arr[nr][nc] = n_arr[nr][nc], n_arr[r][c]
                    nei = tuple(tuple(x) for x in n_arr)
                    if nei not in graph[node]:
                        graph[node].append(nei)
                    graph[nei].append(node)
                    q.append((nei, nr, nc)) #> need to add tuple
            '''
        412
        053
            '''
        # pprint(graph)
        nums = [i for i in range(1, R*C)] + [0]
        end = tuple(tuple(nums[i:i+C]) for i in range(0,len(nums),C))
        # target = tuple(range(1, R*C) + (0))
        return dijkstra(first, end)


import itertools
class SolutionLeet(object):
    def slidingPuzzle(self, board):

        def neighbors(pos):
            for d in (-1, 1, -C, C):
                nei = pos + d
                if abs(nei//C -pos//C) + abs(nei%C -pos%C) == 1  and \
                   0 <= nei < R*C:
                    yield nei

        R, C = len(board), len(board[0])
        start = tuple(itertools.chain(*board))
        queue = collections.deque([(start, start.index(0), 0)])
        seen = {start}
        target = tuple(list(range(1, R*C)) + [0])
        while queue:
            board, posn, depth = queue.popleft()
            if board == target: return depth
            for nei in neighbors(posn):
                newboard = list(board)
                newboard[posn], newboard[nei] = newboard[nei], newboard[posn]
                newt = tuple(newboard)
                if newt not in seen:
                    seen.add(newt)
                    queue.append((newt, nei, depth+1))

        return -1


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple1(self):
        s = Solution()
        board = [[1,2,3],[4,0,5]]
        self.assertEqual(s.slidingPuzzle(board), 1)

    def test_simple2(self):
        s = Solution()
        board = [[4,1,2],[5,0,3]]
        self.assertEqual(s.slidingPuzzle(board), 5)

    def test_simple3(self):
        s = SolutionLeet()
        board = [[3,2,4],[1,5,0]]
        self.assertEqual(s.slidingPuzzle(board), 14)

unittest.main(verbosity=2)

