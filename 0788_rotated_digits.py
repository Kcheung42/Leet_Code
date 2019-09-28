from typing import *
# tags:

# Time = O()
# Space = O()
class Solution:
    def rotatedDigits(self, N):
        def isValidRotation(num):
            return (not any(s in {'3', '4', '7'} for s in num)) and any(s in {'2', '5', '6', '9'} for s in num)
        return sum([isValidRotation(str(i)) for i in range(1, N+1)])

import unittest
class TestSolution1(unittest.TestCase):
    def test_simple(self):
        n = 10
        s = Solution()
        self.assertEqual(s.rotatedDigits(n), 4)


unittest.main(verbosity=2)
