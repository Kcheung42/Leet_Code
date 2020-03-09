#------------------------------------------------------------------------------
# Question: 0086_partition_list.py
#------------------------------------------------------------------------------
# tags: #linked_list
'''
Given a linked list and a value x, partition it such that all nodes less than
x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *
from test_utils.LinkedList import Node, LinkedList

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        Intuition: build two linked lists then merge at the end. (Stable)
        """
        if head is None:
            return
        leftHead = Node(-1)
        rightHead = Node(-1)
        left = leftHead
        right = rightHead
        while head:
            if head.data < x:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next
            head = head.next
        left.next = rightHead.next
        right.next = None
        return leftHead

class Solution2:
    def partition(self, head, x):
        """
        Time: O(n)
        Space: O(1)
        Not stable
        """
        node = head
        new_head = head
        new_tail = head
        while node:
            nextt = node.next
            if node.data < x:
                #add node to head
                node.next = new_head
                new_head = node
            else:
                #add node to end
                new_tail.next = node
                new_tail = node
            node = nextt
        new_tail.next = None
        return new_head


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

def isPartitioned(array, x):
    toggle = False
    n = len(array)
    if n == 0 or n == 1:
        return True
    for i in range(1,n-1):
        if array[i-1] < x and array[i] >= x:
            if toggle:
                return False
            else:
                toggle = True
    return True

class TestSolution(unittest.TestCase):

    def test_simple(self):
        s = Solution()

        ll = LinkedList([1,4,3,2,5,2])
        head = ll.head
        x = 3
        s.partition(head, x)
        self.assertTrue(isPartitioned(ll.to_array(), x))

    def test_simple2(self):
        s = Solution2()
        ll = LinkedList([1,4,3,2,5,2])
        head = ll.head
        x = 3
        s.partition(head, x)
        self.assertTrue(isPartitioned(ll.to_array(), x))


unittest.main(verbosity=2)
