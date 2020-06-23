#------------------------------------------------------------------------------
# Question: 0006_zig_zag_conversion.py
#------------------------------------------------------------------------------
# tags:
'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
of rows like this: (you may want to display this pattern in a fixed font for
better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a
number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N = 0
A   L S  I G = 1
Y A   H R    = 2
P     I      = 3

[P I N]
[A L S I G]
[Y A H R]
[P I]


'''
#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *

class Solution:
    '''
    Time:
    Space:
    '''
    def convert(self, s: str, numRows: int) -> str:
        result = ["" for _ in range(numRows)]
        zig = True
        start = end = 0
        zag_len = max(numRows - 2, 0)
        while end < len(s):
            if zig:
                end = min(len(s), end+numRows)
                for j in range(start, end):
                    row = j % (numRows + zag_len)
                    result[row] += s[j]
                start = end
                zig = False
            else:
                end = min(len(s), end + zag_len)
                for i in range(zag_len):
                    if start+i < len(s):
                        row = numRows - 2 - i
                        result[row] += s[start + i]
                    else:
                        break
                zig = True
                start = end
        return "".join(result)

class Solution2:
    '''
    Time: O(n)
    Space: O(n)
    '''
    def convert(self, s: str, numRows: int) -> str:
        result = ["" for _ in range(min(numRows, len(s)))]
        going_down = False
        direction = -1
        cur_row = 0
        for c in s:
            result[cur_row] += c
            if cur_row == 0 or cur_row == numRows-1:
                direction *= -1
            cur_row += direction
        return "".join(result)

#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple1(self):
        s = Solution()
        s2 = Solution2()
        string = "PAYPALISHIRING"
        numRows = 4

        result = s.convert(string, numRows)
        self.assertEqual(result, "PINALSIGYAHRPI")

        result = s2.convert(string, numRows)
        self.assertEqual(result, "PINALSIGYAHRPI")

    def test_simple2(self):
        string = "A"
        numRows = 1

        s = Solution()
        result = s.convert(string, numRows)
        self.assertEqual(result, "A")

        s2 = Solution2()
        result = s2.convert(string, numRows)
        self.assertEqual(result, "A")

    def test_simple3(self):
        string = "ABCDE"
        numRows = 4

        s = Solution()
        result = s.convert(string, numRows)
        self.assertEqual(result, "ABCED")

        s2 = Solution2()
        result = s2.convert(string, numRows)
        self.assertEqual(result, "ABCED")




unittest.main(verbosity=2)

