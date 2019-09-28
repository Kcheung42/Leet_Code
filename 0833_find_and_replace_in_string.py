from typing import *
# tags:

# Time = O()
# Space = O()
class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        S = list(S)
        for i, src, t in sorted(zip(indexes, sources, targets), reverse = True):
            if all(i+k < len(S) and S[i+k] == src[k] for k in range(len(src))):
                S[i:i+len(src)] = list(t)
            print(f'S:{S}')

        return "".join(S)

import unittest
class TestSolution1(unittest.TestCase):
    def test_simple(self):
        input = "abcd"
        indexes = [0, 2]
        sources = ["a", "cd"]
        targets = ["eee", "ffff"]
        s = Solution()
        self.assertEqual(s.findReplaceString(input, indexes, sources, targets), "eeebffff")


unittest.main(verbosity=2)
