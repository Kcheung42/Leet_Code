import unittest
from typing import *
import collections
# tags:

# Time = O()
# Space = O(N * L) where n is number of words and L is the length of word
class Solution:
    def wordSquares(self, words):
        n = len(words[0])
        lookup = collections.defaultdict(list)
        # create a lookup table for words that begin with a prefix
        for word in words:
            for i in range(n):
                lookup[word[:i]].append(word)

        def build(square):
            if len(square) == n:
                result.append(square)
                return
            for word in lookup[''.join(list(zip(*square))[len(square)])]:
                build(square + [word])
        result = []
        for word in words:
            build([word])
        return result

class TestSolution1(unittest.TestCase):
    def test_simple(self):
        words = ["ball","area","lead","wall","lady"]
        s = Solution()
        sol_set = set()
        # sol_set.add(["wall", "area", "lead", "lady"])
        # sol_set.add(["ball", "area", "lead", "lady"])
        self.assertEqual(s.wordSquares(words), sol_set)


if __name__ == "__main__":
	unittest.main()
