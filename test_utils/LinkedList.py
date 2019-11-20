import unittest

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, values=None):
        self.head = self.tail = None
        self.count = 0
        if values:
            self.add_multiple(values)

    def push_to_tail(self, data):
        node = Node(data)
        if self.tail is None:
            self.tail = self.head = node
        else:
            self.tail.next = node
            self.tail = node
        self.count += 1
        return self.tail


    def to_array(self):
        array = []
        cur = self.head
        while cur:
            array.append(cur.data)
            cur = cur.next
        return array


    def add_multiple(self, values):
        for v in values:
            self.push_to_tail(v)


    def remove_at_pos(self, pos):
        cur = self.head
        if not cur:
            return
        if pos == 0:
            self.head = cur.next
            return cur
        for i in range(pos-1):
            cur = cur.next
        if cur is None:
            return
        removed = cur.next
        next = cur.next.next
        cur.next = next
        return removed


    def remove_nth_from_end(self, n):
        if n > self.count:
            return self.head
        dummy = Node(0)
        dummy.next = self.head
        runner = current = dummy
        for i in range(n+1):
            runner = runner.next
        while runner:
            runner = runner.next
            current = current.next
        current.next = current.next.next
        if current == dummy:
            self.head = current.next
        return self.head


class TestSolution(unittest.TestCase):

    def test_add(self):
        ll = LinkedList()
        ll.push_to_tail(1)
        self.assertEqual(ll.count, 1)
        self.assertEqual(ll.head.data, 1)

    def test_to_array(self):
        '''testing to array'''
        ll = LinkedList()
        ll.push_to_tail(1)
        ll.push_to_tail(2)
        self.assertEqual(ll.to_array(), [1,2])

    def test_intialize_with_array(self):
        nums = [1,2,3,4,5,6]
        ll = LinkedList(nums)
        self.assertEqual(ll.to_array(),nums)

    def test_remove_node(self):
        nums = [1,2,3,4,5,6]
        ll = LinkedList(nums)
        removed = ll.remove_at_pos(3)
        self.assertEqual(removed.data, 4)
        self.assertEqual(ll.to_array(), [1,2,3,5,6])

    def test_remove_nth_node_from_end(self):
        nums = [1,2,3,4,5,6]
        ll = LinkedList(nums)
        removed = ll.remove_nth_from_end(2)
        self.assertEqual(ll.to_array(), [1,2,3,4,6])

    def test_remove_nth_node_from_end(self):
        nums = [1,2,3,4,5,6]
        ll = LinkedList(nums)
        removed = ll.remove_nth_from_end(6)
        self.assertEqual(ll.to_array(), [2,3,4,5,6])




if __name__ == "__main__":
	unittest.main()
