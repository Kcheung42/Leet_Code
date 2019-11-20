import unittest

# import collections

class Solution(object):
	def longestWord(self, words):
		words.sort()
		words_set, longest_word = set(['']), ''
		for word in words:
			if word[:-1] in words_set:
				words_set.add(word)
				if len(word) > len(longest_word):
					longest_word = word
		return longest_word


class TrieNode(object):
	def __init__(self, c):
		# self.children=collections.defaultdict(TrieNode)
		self.children = dict()
		self.isWord = False
		self.word = ''


class Trie(object):
	def __init__(self):
		self.root = TrieNode(None)

	def insert(self, word):
		node = self.root
		for c in word:
			if c not in node.children:
				node.children[c] = TrieNode(c)
			node = node.children[c]
		node.isWord = True
		node.word = word


	def bfs(self):
		# q = collections.deque([self.root])
		q = [self.root]
		res = ''
		while q:
			cur = q.pop()
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
