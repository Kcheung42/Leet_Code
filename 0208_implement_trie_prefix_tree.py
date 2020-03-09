#------------------------------------------------------------------------------
# Question:
#------------------------------------------------------------------------------
# tags:
'''
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.


'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *


class TrieNode():
    def __init__(self, c):
        self.c = c
        self.children = dict()
        self.isword = False
        self.word = ''


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode(None)

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode(c)
            node = node.children[c]
        node.isword = True
        node.word = word

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return True

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest


class TestSolution(unittest.TestCase):
    def test_one_word(self):
        T = Trie()
        T.insert("hello")
        self.assertEqual(T.search("hello"), True)

    def test_one_char(self):
        T = Trie()
        T.insert("a")
        self.assertEqual(T.search("a"), True)

    def test_word_not_in_trie(self):
        T = Trie()
        self.assertEqual(T.search("hello"), False)


class TestStartsWith(unittest.TestCase):
    def test_exists(self):
        T = Trie()
        T.insert("abcdefg")
        prefix = "abc"
        self.assertEqual(T.startsWith("abc"), True)


unittest.main(verbosity=2)
