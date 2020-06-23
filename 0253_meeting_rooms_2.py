import unittest
from typing import *
import heapq
# tags:

'''
Given an array of meeting time intervals consisting of start and end times
[[s1,e1],[s2,e2],...] (si < ei),
find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1

[15, 20]

'''

# Time = O(nLogn)
# Space = O(n)
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        intervals = sorted(intervals, key=lambda x: x[0])

        h = []
        start = 0
        end = 1
        for i in intervals:
            if len(h) > 0 and h[0][0] <= i[start]:
                heapq.heappop(h)
            heapq.heappush(h, [i[end], i[start]])
        return len(h)


class Solution2:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        free_rooms = []
        intervals.sort(key= lambda x: x[0])
        heapq.heappush(free_rooms, intervals[0][1])
        for i in intervals[1:]:
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)
            heapq.heappush(free_rooms, i[1])
        return len(free_rooms)


class TestSolution1(unittest.TestCase):
    def test_smple(self):
        intervals = [[0, 30],[5, 10],[15, 20]]
        s = Solution()
        self.assertEqual(s.minMeetingRooms(intervals), 2)

        s = Solution2()
        self.assertEqual(s.minMeetingRooms(intervals), 2)

    def test_simple2(self):
        intervals = [[7,10],[2,4]]
        s = Solution()
        self.assertEqual(s.minMeetingRooms(intervals), 1)

        s = Solution2()
        self.assertEqual(s.minMeetingRooms(intervals), 1)


if __name__ == "__main__":
	unittest.main()
