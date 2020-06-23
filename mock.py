# ------------------------------------------------------------------------------
# Question:
# ------------------------------------------------------------------------------
# tags:
'''
Implement a MyCalendarTwo class to store your events. A new event can be added
if adding the event will not cause a triple booking.

Your class will have one method, book(int start, int end). Formally, this
represents a booking on the half open interval [start, end), the range of real
numbers x such that start <= x < end.

A triple booking happens when three events have some non-empty intersection
(ie., there is some time that is common to all 3 events.)

For each call to the method MyCalendar.book, return true if the event can be
added to the calendar successfully without causing a triple booking. Otherwise,
return false and do not add the event to the calendar.

Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)
Example 1:

MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(50, 60); // returns true
MyCalendar.book(10, 40); // returns true
MyCalendar.book(5, 15); // returns false
MyCalendar.book(5, 10); // returns true
MyCalendar.book(25, 55); // returns true
Explanation: 
The first two events can be booked.  The third event can be double booked.
The fourth event (5, 15) can't be booked, because it would result in a triple booking.
The fifth event (5, 10) can be booked, as it does not use time 10 which is already double booked.
The sixth event (25, 55) can be booked, as the time in [25, 40) will be double booked with the third event;
the time [40, 50) will be single booked, and the time [50, 55) will be double booked with the second event.
 

Note:

The number of calls to MyCalendar.book per test case will be at most 1000.
In calls to MyCalendar.book(start, end), start and end are integers in the range [0, 10^9].

'''

# ------------------------------------------------------------------------------
# Solutions
# ------------------------------------------------------------------------------

import unittest
from typing import *


class MyCalendarTwo:

    def __init__(self):
        self.calendar = 0
        self.overlap = 0

        '''
        [4, 8]
        110000111
          1111
        '''
    def book(self, start: int, end: int) -> bool:
        def to_bit_string(start, end):
            result = 0
            n = end - start
            for _ in range(n):
                result <<= 1
                result |= 1
            return result
        b = to_bit_string(start,end) << start

        if ~self.calendar & b == b:
            self.calendar |= b
            return True
        elif self.calendar & b & self.overlap == 0:
            self.overlap |= (self.calendar & b)
            self.calendar |= b
            return True
        return False


class MyCalendarTwoLeet:
    '''
    Time: O(n^2), since we have to look at all previous events to determine elligability
    Space: O(N), where n is size of the calendar
    '''
    def __init__(self):
        self.calendar = []
        self.overlap = []

    def book(self, start: int, end: int) -> bool:

        #check for overlap exists
        for s, e in overlap:
            if start < e and end > s:
                return False
        for s,e in self.calendar:
            if start < e and end > s:
                self.overlap.append((max(start, s), max(end, e)))
            self.calendar.append((start, end))
        return True

class MyCalendarTwo:
    '''
    Time: O(N)
    Space: O(N)
    '''

    def __init__(self):
        self.root = None

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if not self.is_insertable(start, end, self.root):
            return False

        self.root = self.insert(start, end, self.root)
        return True



    def is_insertable(self, start, end, root):
        if not root:
            return True

        if start >= end:
            return True

        if end <= root.start:
            return self.is_insertable(start, end, root.left)

        elif start >= root.end:
            return self.is_insertable(start, end, root.right)

        else: #overlap
            if root.single_overlap:
                return False
            elif start >= root.start and end <= root.end:
                return True
            else:
                return self.is_insertable(start, root.start, root.left) and self.is_insertable(root.end, end, root.right)



    def insert(self, start, end, root):
        if not root:
            root = Node(start, end)
            return root

        if start >= end:
            return root

        if start >= root.end:
            root.right = self.insert(start, end, root.right)

        elif end <= root.start:
            root.left = self.insert(start, end, root.left)
        else:
            root.single_overlap = True
            a = min(root.start, start)
            b = max(root.start, start)
            c = min(root.end, end)
            d = max(root.end, end)
            root.start, root.end = b, c
            root.left, root.right = self.insert(a, b, root.left), self.insert(c, d, root.right)
        return root


class Node:
    """
    :type left: Node
    :type right: Node
    :type single_overlap: bool
    """
    def __init__(self, start, end):
        """
        :type start: int
        :type end: int
        """
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        self.single_overlap = False

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)

# ------------------------------------------------------------------------------
# Tests
# ------------------------------------------------------------------------------

class TestSolution(unittest.TestCase):
    def test_simple(self):
        s = Solution()
        self.assertEqual(True, True)


unittest.main(verbosity=2)

