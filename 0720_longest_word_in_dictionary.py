import unittest

# import collections


class SolutionLeet(object):
    def longestWord(self, words):
        words_set = set['']
        longest_word = ''
        words.sort()
        for word in words:
            if word[:-1] in words_set:
                words_set.add(word)
                if len(word) > len(longest_word):
                    longest_word = word
        return longest_word


class TrieNode:
    def __init__(self, c):
        # self.children=collections.defaultdict(TrieNode)
        self.children = dict()
        self.isWord = False
        self.word = ''


class Trie:
    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, word):
        current = self.root
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode(c)
            current = current.children[c]
        current.isWord = True
        current.word = word

    def bfs(self):
        # q = collections.deque([self.root])
        q = [self.root]
        res = ''
        while q:
            cur = q.pop(0)
            for n in cur.children.values():
                if n.isWord:
                    q.append(n)
                    if len(n.word) > len(res) or n.word < res:
                        res = n.word
        return res


class Solution2(object):
    def longestWord(self, words):
        t = Trie()
        for w in words:
            t.insert(w)
        return t.bfs()


class TestSolution1(unittest.TestCase):

    def test_simple(self):
        words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
        self.assertEqual(Solution().longestWord(words), "apple", "solution 1")
        self.assertEqual(Solution2().longestWord(words), "apple", "solution 2")

if __name__ == "__main__":
    unittest.main()
