# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    002_Add_Two_Numbers.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/12/20 14:55:08 by kcheung           #+#    #+#              #
#    Updated: 2018/01/17 09:16:41 by bambo            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

'''
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

class ListNode:
	def __init__(self, value):
		self.val = value
		self.next = None

class Solution:
	def addTwoNumbers(self, l1,l2):
		val1 = self.convert(l1)
		val2 = self.convert(l2)
		sum = val1 + val2
		if sum == 0:
			return ListNode(0)
		resultList = None
		while sum:
			if resultList is None:
				resultList = ListNode(sum % 10)
			else:
				self.addNode(resultList, sum % 10)
			sum //= 10
		return resultList

	def convert(self, list):
		if list is None:
			return 0
		cur = list
		val = 0
		digit_place = 1
		while(cur):
			val += cur.val * digit_place
			cur = cur.next
			digit_place *= 10
		return (int(val))

	def addNode(self, head, val):
		if head is None:
			head = ListNode(val)
		else:
			cur = head
			while cur.next:
				cur = cur.next
			cur.next = ListNode(val)


# test code
l1 = ListNode(2)
addNode(l1, 4)
addNode(l1, 3)

l2 = ListNode(5)
addNode(l2, 6)
addNode(l2, 4)

s = Solution()
result = s.addTwoNumbers(l1,l2)
while result:
	print(result.val, end=',')
	result = result.next
