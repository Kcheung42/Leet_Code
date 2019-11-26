#------------------------------------------------------------------------------
# Question:
#------------------------------------------------------------------------------
# tags:
'''
According to the Wikipedia's article: "The Game of Life, also known simply as
Life, is a cellular automaton devised by the British mathematician John Horton
Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead
(0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal)
using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

Write a function to compute the next state (after one update) of the board given its
current state. The next state is created by applying the above rules simultaneously
to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]

'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        '''
        Time:
        Space:
        Do not return anything, modify board in-place instead.
        '''
        def islive(x):
            return (x >> 1 & 1) == 1

        rows = len(board)
        cols = len(board[0])
        neighbors = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

        print()

        print(f'\nboard: {board}')
        for row in range(rows):
            for col in range(cols):
                board[row][col] = board[row][col] << 1

        print(f'\nboard: {board}')
        for row in range(rows):
            for col in range(cols):
                live = 0
                cur_cell = board[row][col]
                for nei in neighbors:
                    r = row + nei[0]
                    c = col + nei[1]
                    if r >= 0 and r < rows and c >=0 and c < cols and islive(board[r][c]):
                        live += 1
                print(f"cell[{row}[{col}] has {live} live neighbors]")
                if islive(cur_cell) and (live == 2 or live == 3):
                    print(f"cell[{row}[{col}] is live and lives on")
                    board[row][col] |= 1
                if not(islive(cur_cell)) and live == 3:
                    print(f"cell[{row}[{col}] is born")
                    board[row][col] |= 1

        print(f'\nboard: {board}')
        for row in range(rows):
            for col in range(cols):
                board[row][col] &= 1
        print(f'\nboard: {board}')

#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        board = [[0,1,0],
                 [0,0,1],
                 [1,1,1],
                 [0,0,0]]

        result = [[0,0,0],
                  [1,0,1],
                  [0,1,1],
                  [0,1,0]]

        s = Solution()
        s.gameOfLife(board)
        self.assertEqual(board, result)


unittest.main(verbosity=2)

