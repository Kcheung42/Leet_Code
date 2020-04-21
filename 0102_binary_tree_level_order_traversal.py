#------------------------------------------------------------------------------
# Question:
#------------------------------------------------------------------------------
# tags:
'''
Given a binary tree, return the level order traversal of its nodes' values.
(ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
Accepted

'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *

class Solution:
    '''
    Time:
    Space:
    1 loop, use Delimeter
    '''
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q = [root, None]
        temp = []
        result = []
        while len(q) > 0:
            node = q.pop(0)
            if node:
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            else:
                if len(q) > 0:
                    q.append(None)
                result.append(temp)
                temp = []
        return result


class Solution:
    '''
    2 Loops
    '''
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        q = [root]
        result = []
        while q:
            q_len = len(q)
            temp = []
            for _ in range(q_len):
                node = q.pop(0)
                if node:
                    temp.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if temp:
                result.append(temp)
        return result




#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        s = Solution()
        self.assertEqual(True, True)


unittest.main(verbosity=2)

