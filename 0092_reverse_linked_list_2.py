#------------------------------------------------------------------------------
# Questions: 0092_reverse_linked_list_2.py
#------------------------------------------------------------------------------
# tags:
'''
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL

'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *
from test_utils.LinkedList import Node, LinkedList


class Solution(object):
    #Recursive Approach
    def reverse_range(self, head, m, n):
        if not head:
            return None

        left = head
        right = head
        stop = False
        def recur(right, m, n):
            nonlocal left, stop

            #base case
            if n == 1:
                return

            right = right.next
            if m > 1:
                left = left.next

            #Recurse with m and n reduced
            recur(right, m-1, n-1)

            #left and right are in the right place
            if left == right or right.next == left:
                stop = True

            if not stop:
                right.data, left.data = left.data, right.data
                left = left.next
        recur(right, m, n)
        return head


# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL
class Solution2(object):
    def reverse_range(self, head, m, n):
        if not head:
            return

        prev = None
        cur = head
        while m > 1:
            prev = cur
            cur = cur.next
            m -= 1
            n -= 1
        tail = cur
        con = prev

        while n:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            n -= 1

        if con:
            con.next = prev
        else:
            head = prev
        tail.next = cur

        return head


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution1(unittest.TestCase):
    def test_simple(self):
        '''Testing Recursive Solution'''
        # create linked list 0->1->2->3->4->5->6->7->8->9
        ll = LinkedList()
        for i in range(10):
            ll.push_to_tail(i)

        s = Solution()
        result = s.reverse_range(ll.head, 2, 4)
        self.assertEqual(ll.to_array(), [0, 3, 2, 1, 4, 5, 6, 7, 8, 9])

    def test_simple2(self):
        '''Testing Iteraive solution'''
        # create linked list 0->1->2->3->4->5->6->7->8->9
        ll = LinkedList()
        for i in range(10):
            ll.push_to_tail(i)

        s = Solution2()
        result = s.reverse_range(ll.head, 2, 4)
        self.assertEqual(ll.to_array(), [0, 3, 2, 1, 4, 5, 6, 7, 8, 9])


if __name__ == "__main__":
	unittest.main()
