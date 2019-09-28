import unittest
import collections

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        banset = set(banned)
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        count = collections.Counter(
        [word for word in paragraph.lower().split()])
        print(count)
        ans, best = '', 0
        for word in count:
            if count[word] > best and word not in banset:
                ans, best = word, count[word]

        return ans

class TestSolution1(unittest.TestCase):
    def test_simple(self):
        paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
        banned = ["hit"]
        s = Solution()
        self.assertEqual("ball", s.mostCommonWord(paragraph, banned))


if __name__ == "__main__":
	unittest.main()
