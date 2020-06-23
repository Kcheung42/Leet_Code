import unittest
from typing import *
# tags:


class Solution1:
    def longestPalindrome(self, s: str) -> str:
        """
        Brute Force
        Time = O(N**3)
        Space = O(1)
        """

        def isPalindrome(i, j):
            return all([s[k] == s[j-k+i-1] for k in range(i,j)])

        n = len(s)
        max_len = 0
        start = -1
        for i in range(n):
            for j in range(i, n):
                if isPalindrome(i, j + 1):
                    # Calculate the starting point of LPS
                    if (j-i+1) > max_len:
                        start = i
                    max_len = max(j-i+1, max_len)
        return {'max_len': max_len, "start": start}


class Solution2:
    def longestPalindrome(self, s: str) -> str:
        """
        Dynamic Programming
        Time = O(N**2)
        Space = O(N**2)
        """
        n = len(s)
        max_len = 1
        start = 0

        table = [[False for i in range(n)] for j in range(n)]

        # for substring of len 1
        for i in range(n):
            table[i][i] = True

        # for substring of len 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                table[i][i + 1] = True
                start = i
                max_len = 2

        # for substring of len 3 up to substring of n
        # k is len of substring in question
        '''
          i   j
          b a b a d
        b 1 0 1
        a   1 0
        b     1 0
        a       1 0
        d         1

        T[i][j] = True if S[i:j] is palindrome
        '''
        for k in range(3, n + 1):
            for i in range(n + 1 - k):
                j = i + k - 1
                if table[i + 1][j - 1] and s[i] == s[j]:
                    table[i][j] = True
                    if k > max_len:
                        max_len = k
                        start = i #optional
        # return max_len
        return {'max_len': max_len, 'start': start}

class Solution3:
    """
    Manacher's Algorithm
    Time = O(N)
    Space = O(N)
    """
    def longestPalindrome(self, s: str) -> str:
        C = 0
        R = 0
        S = "$#" + "#".join(s) + "#$"
        n = len(S)
        P = [0 for i in range(n)]
        max_len = float("-inf")
        start = -1
        for i in range(1, n-1):
            mirror = 2 * C - i

            #if candidate for the new center within R boundary
            if i < R:
                P[i] = min(R-i, P[mirror])

            # expand palindrome past R boundary
            while (S[i - (P[i] + 1)] == S[i + (P[i] + 1)]):
                P[i] += 1
            max_len = max(P[i], max_len)

            # update new Center if the current candidate
            # has a palindromic len greater than the R boundary
            if i + P[i] > R:
                C = i
                R = C + P[i]
                start = R-i-1
        return {'max_len': max_len, 'start': start}


class TestSolution1(unittest.TestCase):
    def test_simple(self):
        input = "babad"
        s = Solution1()
        self.assertEqual(s.longestPalindrome(input)['max_len'], 3)
        self.assertEqual(s.longestPalindrome(input)['start'], 0)

        s = Solution2()
        self.assertEqual(s.longestPalindrome(input)['max_len'], 3)
        self.assertEqual(s.longestPalindrome(input)['start'], 0)

        s = Solution3()
        self.assertEqual(s.longestPalindrome(input)['max_len'], 3)
        self.assertEqual(s.longestPalindrome(input)['start'], 0)

    def test_simple2(self):
        input = "zabaxabxaba"

        s = Solution1()
        self.assertEqual(s.longestPalindrome(input)['max_len'], 5)
        self.assertEqual(s.longestPalindrome(input)['start'], 2)

        s = Solution2()
        self.assertEqual(s.longestPalindrome(input)['max_len'], 5)
        self.assertEqual(s.longestPalindrome(input)['start'], 2)


        s = Solution3()
        self.assertEqual(s.longestPalindrome(input)['max_len'], 5)
        self.assertEqual(s.longestPalindrome(input)['start'], 2)


if __name__ == "__main__":
	unittest.main()
