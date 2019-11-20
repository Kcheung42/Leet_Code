'''
Given a linked list and a value x, partition it such that all nodes less than
x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
'''

# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

	def __repr__(self):
		if self:
			return "{} -> {}".format(self.val, repr(self.next))

class Solution:
	def partition(self, head, x):
		"""
		:type head: ListNode
		:type x: int
		:rtype: ListNode
		"""
		if head is None:
			return
		leftHead = ListNode(-1)
		rightHead = ListNode(-1)
		left = leftHead
		right = rightHead
		while head:
			if head.val < x:
				left.next = head
				left = left.next
			else:
				right.next = head
				right = right.next
			head = head.next
		left.next = rightHead.next
		right.next = None
		return leftHead

if __name__ == "__main__":
	head = ListNode(1)
	head.next = ListNode(4)
	head.next.next = ListNode(3)
	head.next.next.next = ListNode(2)
	head.next.next.next.next = ListNode(5)
	head.next.next.next.next.next = ListNode(2)
	print(Solution().partition(head, 3))
