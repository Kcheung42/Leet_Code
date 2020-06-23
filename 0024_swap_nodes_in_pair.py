# ------------------------------------------------------------------------------
# Question:
# ------------------------------------------------------------------------------
# tags:
'''
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be
changed.


Example:

Given 1->2->3->4->5, you should return the list as 2->1->4->3.

'''

# ------------------------------------------------------------------------------
# Solutions
# ------------------------------------------------------------------------------

import unittest
from typing import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        '''
        Time:
        Space:
        '''
        '''

        ------
        |     |
        h  1<-2  3->N
           |     |
            -----

        h->1->2->3

        prev = 3
        cur = 4


        while cur:
        '''
        if not head:
            return
        if head.next:  # there are atleast 2 node
            prev = head
            cur = head.next
        else:  # only one node
            return head
        head = cur

        # swap logic
        while cur:
            prev.next = cur.next
            cur.next = prev
            cur = prev.next
            if cur:
                if cur.next:
                    prev.next = cur.next
                    prev = cur
                    cur = cur.next
                else:
                    break
        return head


# ------------------------------------------------------------------------------
# Tests
# ------------------------------------------------------------------------------

class TestSolution(unittest.TestCase):
    def test_simple(self):
        s = Solution()
        self.assertEqual(True, True)


unittest.main(verbosity=2)

