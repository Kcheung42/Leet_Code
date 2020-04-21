#------------------------------------------------------------------------------
# Question:
#------------------------------------------------------------------------------
# tags: #linkedlist
'''

'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
LL:
    _______
   |       |
1  2   3 - 4 - N
|______|_______|
               o
           e


'''

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        head_e = head.next
        o = head
        e = o.next
        while o:
            if e:
                o.next = e.next
            prev = o
            o = o.next
            if o:
                e.next = o.next
            e = o.next
        prev.next = head_e
        return head

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return
        odd = head
        even = odd.next
        head_e = even
        while even or even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = head_e
        return head


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        s = Solution()
        self.assertEqual(True, True)


unittest.main(verbosity=2)

