# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    094_Binary_Tree_Inorder_Traversal.py               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/01/29 16:30:23 by kcheung           #+#    #+#              #
#    Updated: 2018/01/30 21:45:04 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

'''
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?

'''
import unittest
from typing import *
# tags:


class Node():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Time = O()
# Space = O()
class Solution(object):
    def inorderTraversal(self, root):
        if root is None:
            return []
        stack = []
        result = []
        current = root
        while(True):
            if current:
                stack.append(current)
                current = current.left
            elif (len(stack) > 0):
                current = stack.pop()
                result.append(current.val)
                current = current.right
            else:
                break;
        return result

class TestSolution1(unittest.TestCase):
    def test_simple(self):
        root = Node(4)
        root.left = Node(2)
        root.right = Node(6)
        root.left.left = Node(1)
        root.left.right = Node(3)
        root.right.left = Node(5)
        root.right.right = Node(7)
        s = Solution()
        self.assertEqual(s.inorderTraversal(root), [1,2,3,4,5,6,7])

    def test_no_root(self):
        root = None
        s = Solution()
        self.assertEqual(s.inorderTraversal(root), [])


if __name__ == "__main__":
    unittest.main()
