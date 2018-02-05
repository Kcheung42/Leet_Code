import heapq
class Solution(object):
	def nthSuperUglyNumber(self, n, primes):
		"""
		:type n: int
		:type primes: List[int]
		:rtype: int
		"""
		heap = []
		uglies = [0] * n
		idx = [0] * len(primes)
		ugly_by_last_prime = [0] * n
		uglies[0] = 1

		for k, p in enumerate(primes):
			heapq.heappush(heap, (p, k))

		for i in range(1, n):
			uglies[i], k = heapq.heappop(heap)
			ugly_by_last_prime[i] = k
			idx[k] += 1
			while ugly_by_last_prime[idx[k]] > k: #skip duplicate products
				idx[k] += 1
			heapq.heappush(heap, (primes[k] * uglies[idx[k]], k))
		return uglies[-1]

s = Solution()
primes = [2,7,13,19]
n = 12
print(s.nthSuperUglyNumber(n, primes))
