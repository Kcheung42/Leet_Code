import unittest
from typing import *
import collections
# tags:

# Algoirthm
# 1. Do the pre-processing on the given wordList and find all the possible
# generic/intermediate states. Save these intermediate states in a dictionary
# with key as the intermediate word and value as the list of words which have
# the same intermediate word.

# 2. Push a tuple containing the beginWord and 1 in a queue. The 1 represents the
# level number of a node. We have to return the level of the endNode as that
# would represent the shortest sequence/distance from the beginWord.

# 3. To prevent cycles, use a visited dictionary.

# 4. While the queue has elements, get the front element of the queue. Let's call
# this word as current_word.

# 5.Find all the generic transformations of the current_word and find out if any of
# these transformations is also a transformation of other words in the word list.
# This is achieved by checking the all_combo_dict.

# 6. The list of words we get from all_combo_dict are all the words which have a common
# intermediate state with the current_word. These new set of words will be the adjacent
# nodes/words to current_word and hence added to the queue.

# 7. Hence, for each word in this list of intermediate words, append (word, level + 1)
# into the queue where level is the level for the current_word.

# 8. Eventually if you reach the desired word, its level would represent the shortest
# transformation sequence length.

from collections import defaultdict
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        # Since all words are of same length.
        L = len(beginWord)

        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        all_combo_dict = defaultdict(list)

        for word in wordList:
            for i in range(L):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)

        # # Queue for BFS
        queue = collections.deque([(beginWord, 1)])

        # # Visited to make sure we don't repeat processing same word.
        visited = set([beginWord])

        while queue:
            current_word, level = queue.popleft()
            for i in range(L):
                # Intermediate words for current word
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]

                # Next states are all the words which share the same intermediate state.
                for word in all_combo_dict[intermediate_word]:
                    # If at any point if we find what we are looking for
                    # i.e. the end word - we can return with the answer.
                    if word == endWord:
                        return level + 1
                    # Otherwise, add it to the BFS Queue. Also mark it visited
                    if word not in visited:
                        visited.add(word)
                        queue.append((word, level + 1))
                all_combo_dict[intermediate_word] = []
        return 0

class TestSolution1(unittest.TestCase):
    def test_simple(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log","cog"]
        s = Solution()
        self.assertEqual(s.ladderLength(beginWord, endWord, wordList), 5)


if __name__ == "__main__":
	unittest.main()
