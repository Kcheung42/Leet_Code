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

        # for substring of len 1
        for i in range(n):
            table[i][i] = True

        # for substring of len 2
        for i in range(n-1):
            if s[i] == s[i+1]:
                table[i][i+1] = True
                start = i
                max_len = 2

        # for substring of len 3 up to substring of n
        # k is len of substring in question
        for k in range(3, n+1):
            for i in range(n+1-k):
                j = i - 1 + k
                if table[i+1][j-1] == True and s[i] == s[j]:
                    table[i][j] = True
                    if k > max_len:
                        max_len = k
                        start = i
        # return max_len
        return {'max_len': max_len, 'start': start}

class Solution2:
    def longestPalindrome(self, s: str) -> str:
        C = 0
        R = 0
        T = "$#" + "#".join(s) + "#$"
        n = len(T)
        P = [0 for i in range(n)]
        max_len = float("-inf")
        start = -1
        for i in range(1, n-1):
            mirror = 2 * C - i

            #if candidate for the new center within R boundary
            if i < R:
                P[i] = min(R-i, P[mirror])

            # expand palindrome past R boundary
            while (T[i - (P[i] + 1)] == T[i + (P[i] + 1)]):
                P[i] += 1
            max_len = max(P[i], max_len)

            # update new Center if the current candidate
            # has a palindromic len greater than the R boundary
            if i + P[i] > R:
                C = i
                R = C + P[i]
                start = R-i-1
        return {'max_len': max_len, 'start': start}


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(i, j):
            return all([s[k] == s[j-k+i] for k in range(i,j)])

        n = len(s)
        max_len = 0
        start = -1
        for i in range(n):
            for j in range(i, n):
                if isPalindrome(i,j):
                    if (j-i+1) > max_len:
                        start = i
                    max_len = max((j-i+1), max_len)
        return {'max_len': max_len, "start": start}

class TestSolution1(unittest.TestCase):
    def test_simple(self):
        input = "babad"
        s = Solution()
        self.assertEqual(s.longestPalindrome(input)['max_len'], 3)
        self.assertEqual(s.longestPalindrome(input)['start'], 0)

        s = Solution2()
        self.assertEqual(s.longestPalindrome(input)['max_len'], 3)
        self.assertEqual(s.longestPalindrome(input)['start'], 0)

    def test_simple2(self):
        input = "zabaxabxaba"

        s = Solution()
        self.assertEqual(s.longestPalindrome(input)['max_len'], 5)
        self.assertEqual(s.longestPalindrome(input)['start'], 2)

        s = Solution2()
        self.assertEqual(s.longestPalindrome(input)['max_len'], 5)
        self.assertEqual(s.longestPalindrome(input)['start'], 2)


if __name__ == "__main__":
	unittest.main()
