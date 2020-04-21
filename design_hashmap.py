#------------------------------------------------------------------------------
# Question:
#------------------------------------------------------------------------------
# tags:
'''

'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 100
        self.m = [None] * self.size

    def hash(self, string):
        h = 0
        for c in string:
            h += ord(c)

        return h % self.size

    def put(self, key: str, value: int) -> None:
        """
        value will always be non-negative.
        """
        k_hash = self.hash(key)
        k_value = [key, value]

        if self.m[k_hash]:
            for pair in self.m[k_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.m[k_hash].append(k_value)
        else:
            self.m[k_hash] = [k_value]


    def get(self, key: str) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        k_hash = self.hash(key)
        if self.m[k_hash] is None:
            return -1
        else:
            for k,v in self.m[k_hash]:
                if k == key:
                    return v
        return -1

    def remove(self, key: str) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        k_hash = self.hash(key)
        if self.m[k_hash]:
            self.m[k_hash] = list(filter(lambda x: x[0] != key, self.m[k_hash]))
            print(self.m[k_hash])
            if self.m[k_hash] == []:
                self.m[k_hash] = None


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_put_and_get(self):
        h = MyHashMap()
        h.put("hello", "world")
        self.assertEqual(h.get("hello"), "world")

    def test_override(self):
        h = MyHashMap()
        h.put("hello", "world")
        h.put("hello", "blah")
        self.assertEqual(h.get("hello"), "blah")

    def test_no_key(self):
        h = MyHashMap()
        h.put("bah", "world")
        self.assertEqual(h.get("hello"), -1)

    def test_no_key(self):
        h = MyHashMap()
        h.put("bah", "world")
        h.remove("bah")
        self.assertEqual(h.get('bah'), -1)


unittest.main(verbosity=2)



