# from heapq import *
from typing import List
import random


class Solution:

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        dist = lambda i: points[i][0]**2 + points[i][1]**2

        def sort(i, j, K):
            k = random.randint(i, j)
            points[j], points[k] = points[k], points[j]

            mid = partition(i, j)
            if K < mid - i - 1:
                sort(i, mid - 1, K)
            elif K > mid - i + 1:
                sort(mid + 1, j, K - (mid - i + 1))

        def partition(start, end):
            pIndex = start
            pivot = dist(end)
            i = start
            while i < end:
                if dist(i) <= pivot:
                    points[i], points[pIndex] = points[pIndex], points[i]
                    pIndex += 1
                i += 1
            points[pIndex], points[end] = points[end], points[pIndex]
            return pIndex

        sort(0, len(points) - 1, K)
        return points[:K]



s = Solution()
ans = s.kClosest([[3,3],[5,-1],[-2,4]], 2)
# ans = s.kClosest([[0,1],[1,0]], 2)
print(ans)
