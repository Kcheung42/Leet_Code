#------------------------------------------------------------------------------
# Question:
#------------------------------------------------------------------------------
# tags:
'''
Given a binary search tree and a node in it, find the in-order successor of that
node in the BST.

The successor of a node p is the node with the smallest key greater than p.val.


  2
 / \
1   3
Example 1:


Input: root = [2,1,3], p = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both p and the return
value is of TreeNode type.

Example 2:


Input: root = [5,3,6,2,4,null,null,1], p = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is null.


cases:

root is target, target's right exists, but doesn't have a left child
  2->t
 / \
1   3
ans = 3

  2->t
 / \
1   3
     \
      7
ans = 3

root is target, t's right exist, find lowest number in right subtree
2->t
 / \
1   5
   /
  4 -> lowest number of t's right
ans = 4


target is left
     2
    / \
t->1   5
  /
 0
ans = 2

target is left
     5->C
    / \
  >2   6
  / \
1   4
    /
   3
ans = 4

going left
candidats = [5, 4]

searching for t
going left, update candidate to cur
going right

if t is found:
cases:
t has right child, find lowest number in riht subtree
t has no children, pop off candidate stack
'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *


'''
h[2] = 5
h[4] = 2
h[3] = 4


target is left
     5->C
    / \
 1   4
    /
   3
ans = 4
'''
class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root: return None

        #search for p
        candidate = None
        cur = root
        while cur and cur != p:
            if cur.val > p.val: #going left
                candidate = cur
                cur = cur.left
            else:
                cur = cur.right
        if cur is None:
            return None
        if cur.right:
            candidate = cur.right
            while candidate and candidate.left:
                candidate = candidate.left
        return candidate

#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        s = Solution()
        self.assertEqual(True, True)


unittest.main(verbosity=2)

