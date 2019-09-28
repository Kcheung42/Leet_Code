import unittest
from typing import *
# tags:

# Time = O(N**2)
# Space = O(N**2)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_len = 1
        start = 0

        table = [[False for i in range(n)] for j in range(n)]

        for i in range(n):
            table[i][i] = True

        for i in range(n-1):
            if s[i] == s[i+1]:
                table[i][i+1] = True
                start = i
                max_len = 2

        for k in range(3, n+1):
            for i in range(n-k+1):
                j = i + k - 1
                if table[i+1][j-1] == True and s[i] == s[j]:
                    table[i][j] = True
                    if k > max_len:
                        max_len = k
                        start = i
        return {'max_len': max_len, 'start': start}

class TestSolution1(unittest.TestCase):
    def test_simple(self):
        input = "babad"
        s = Solution()
        self.assertEqual(s.longestPalindrome(input)['max_len'], 3)
        self.assertEqual(s.longestPalindrome(input)['start'], 0)


if __name__ == "__main__":
	unittest.main()
