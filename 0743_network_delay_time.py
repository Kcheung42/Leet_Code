import unittest
from typing import *
import collections
import heapq

# tags: Graph


# Time = O(ElogE) where E is the number of edges
# Space = O(E)
class Solution(object):
    def networkDelayTime(self, times, N, K):
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        pq = [(0, K)]
        seen = {}
        while pq:
            d, node = heapq.heappop(pq)
            if node in seen: continue
            seen[node] = d
            for nei, d2 in graph[node]:
                if nei not in seen:
                    heapq.heappush(pq, (d+d2, nei))

        print(seen)
        return max(seen.values()) if len(seen) == N else -1


# Time = O()
# Space = O()
class Solution2(object):
    def networkDelayTime(self, times, N, K):
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))

        dist = collections.defaultdict()
        def dfs(node, elapsed):
            print(dist)
            if node not in dist:
                dist[node] = float('inf')
            if elapsed >= dist[node]: return
            dist[node] = elapsed
            for time, nei in sorted(graph[node]):
                dfs(nei, elapsed + time)

        dfs(K, 0)
        ans = max(dist.values())
        return ans if ans < float('inf') else -1


class TestSolution1(unittest.TestCase):
    def test_simple(self):
        times = [['B','A',1],['B','C',1],['C','D',1]]
        N = 4
        K = 'B'
        s = Solution()
        s2 = Solution2()
        self.assertEqual(s.networkDelayTime(times, N, K), 2)
        self.assertEqual(s2.networkDelayTime(times, N, K), 2)


if __name__ == "__main__":
	unittest.main()
