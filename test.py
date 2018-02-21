class Solution(object):
	def countAndSayHelper(self,n):
		if n == 1:
			return "1"
		cur = ""
		prev = self.countAndSayHelper(n-1)
		count = 0
		digit = prev[0]
		for p in prev:
			if p == digit:
				count += 1
			else:
				cur += chr(count)
				cur += chr(digit)
				digit = p
				count = 0
		return cur

	def countAndSay(self, n):
		"""
		:type n: int
		:rtype: str
		"""
		return(self.countAndSayHelper(n))

s = Solution()
print(s.countAndSay(4))
