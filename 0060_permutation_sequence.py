#------------------------------------------------------------------------------
# Question:
#------------------------------------------------------------------------------
# tags:
'''
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the
following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def nextPermutation(numbers):
            n = len(numbers)
            k = -1
            for i in range(n-1):
                if numbers[i] < numbers[i+1]:
                    k = i
            if k == -1:
                return None
            l = k
            for i in range(k+1, n):
                if numbers[i] > numbers[k]:
                    l = i
            numbers[l], numbers[k] = numbers[k], numbers[l]
            numbers[k+1:] = numbers[k+1:][::-1]
            return numbers

        result = []
        numbers = [i for i in range(1, n+1)]
        for i in range(k-1):
            nextPermutation(numbers)
            print("".join(map(str,numbers)))
        return("".join(map(str,numbers)))




#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        s = Solution()
        n = 3
        k = 3
        self.assertEqual(s.getPermutation(n,k), "213")

    def test_simple(self):
        s = Solution()
        n = 9
        k = 219601
        self.assertEqual(s.getPermutation(n,k), "269011")


unittest.main(verbosity=2)

