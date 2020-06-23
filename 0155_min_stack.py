#------------------------------------------------------------------------------
# Question:
#------------------------------------------------------------------------------
# tags:
'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.

'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------

class StackNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.minVal = val

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.head = None

    def push(self, x: int) -> None:
        if self.head is None:
            self.head = StackNode(x)
        else:
            node = StackNode(x)
            if node.val > self.head.minVal:
                node.minVal = self.head.minVal
            node.next = self.head
            self.head = node

    def pop(self) -> None:
        temp = self.head
        if self.head is not None:
            self.head = self.head.next
        return temp

    def top(self) -> int:
        return self.head.val


    def getMin(self) -> int:
        return self.head.minVal

#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        obj = MinStack()
        obj.push(-2)
        obj.push(0)
        obj.push(-3)
        self.assertEqual(obj.getMin(), -3)
        obj.pop()
        self.assertEqual(obj.top(), 0)
        self.assertEqual(obj.getMin(), -2)


unittest.main(verbosity=2)

