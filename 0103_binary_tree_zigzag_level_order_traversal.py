#------------------------------------------------------------------------------
# Questions: 0103_binary_tree_zigzag_level_order_traversal.py
#------------------------------------------------------------------------------
# tags: Binary, Traversal
'''
Given a binary tree, return the zigzag level order traversal of its nodes' values.
(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
'''


#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------

# Time = O(N)
# Space = O(N)
class Solution(object):
    # Two Stacks
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        s_1 = [] #prints left to right
        s_2 = [] #prints right to left
        n = len(root)
        result = []
        cur = 0
        s_1.append((0, root[0]))
        while len(s_1) > 0 or len(s_2) > 0:
            temp = []
            while len(s_1) > 0:
                node = s_1.pop()
                temp.append(node[1])
                right_child = 2 * node[0] + 2
                left_child = 2 * node[0] + 1
                if left_child <= n-1 and root[left_child]:
                    s_2.append((left_child, root[left_child]))
                if right_child <= n-1 and root[right_child]:
                    s_2.append((right_child, root[right_child]))
            if len(temp) > 0:
                result.append(temp)
            temp = []
            while len(s_2) > 0:
                node = s_2.pop()
                temp.append(node[1])
                right_child = 2 * node[0] + 2
                left_child = 2 * node[0] + 1
                if right_child <= n-1 and root[right_child]:
                    s_1.append((right_child, root[right_child]))
                if left_child <= n-1 and root[left_child]:
                    s_1.append((left_child, root[left_child]))
            if len(temp) > 0:
            result.append(temp)
        return result


import queue
class Solution2(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        res = []
        temp = []
        n = len(root)
        q = queue.Queue()
        q.put((0, root[0]))
        flag = -1
        while not q.empty():
            for i in range(q.qsize()):
                node = q.get()
                temp+=[node[1]]
                right_child = 2 * node[0] + 2
                left_child = 2 * node[0] + 1
                if right_child <= n-1 and root[right_child]:
                    q.put((right_child, root[right_child]))
                if left_child <= n-1 and root[left_child]:
                    q.put((left_child, root[left_child]))
            res+=[temp[::flag]]
            temp=[]
            flag*=-1
        return res


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest
class TestSolution1(unittest.TestCase):
    def test_simple(self):
        root = [3,9,20,None,None,15,7]

        s = Solution()
        self.assertEqual(s.zigzagLevelOrder(root), [[3], [20,9], [15,7]])

        s2 = Solution2()
        self.assertEqual(s2.zigzagLevelOrder(root), [[3], [20,9], [15,7]])


    def test_none_root(self):
        root = None

        s = Solution()
        self.assertEqual(s.zigzagLevelOrder(None), [])

        s2 = Solution2()
        self.assertEqual(s2.zigzagLevelOrder(None), [])


if __name__ == "__main__":
	unittest.main()

