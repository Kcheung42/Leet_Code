# ------------------------------------------------------------------------------
# Question:
# ------------------------------------------------------------------------------
# tags:
'''
Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words
have the same frequency, then the word with the lower alphabetical order comes
first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.
Follow up:
Try to solve it in O(n log k) time and O(n) extra space.

'''

# ------------------------------------------------------------------------------
# Solutions
# ------------------------------------------------------------------------------

import unittest
from typing import *


import collections
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        '''
        d[i] = 2
        d[love] = 2
        d[coding] = 1

        i, love, coding

        custom comp, first by count, then lexigraphically
        the day is sunny the the the sunny is is

        d[the] = 4
        d[day] = 1
        d[is] = 3
        d[sunny] = 2

        the day is sunny
        sort by -d[word] then by word
        '''
        def cmp(x): # x is tuple (word, freq)
            return (-counter[x], x)
        counter = collections.Counter(words)
        keys = list(counter.keys())
        keys.sort(key=cmp)
        return keys[:k]


import heapq
class Solution(object):
    def topKFrequent(self, words, k):
        count = collections.Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]


# ------------------------------------------------------------------------------
# Tests
# ------------------------------------------------------------------------------

class TestSolution(unittest.TestCase):
    def test_simple(self):
        s = Solution()
        words =  ["i", "love", "leetcode", "i", "love", "coding"]
        k = 2
        self.assertEqual(s.topKFrequent(words, k),
                         ['i', 'love'])

    def test_simple2(self):
        s = Solution()
        words =   ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
        k = 4
        self.assertEqual(s.topKFrequent(words, k),
                         ["the", "is", "sunny", "day"])


unittest.main(verbosity=2)

