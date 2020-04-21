#------------------------------------------------------------------------------
# Question:
#------------------------------------------------------------------------------
# tags:
'''
Input:  txt[] = "THIS IS A TEST TEXT"
        pat[] = "TEST"
Output: Pattern found at index 10

Input:  txt[] =  "AABAACAADAABAABA"
        pat[] =  "AABA"
Output: Pattern found at index 0
        Pattern found at index 9
        Pattern found at index 12

badChar = [-1,-1,-1 ...]
badChar = [3,2,-1 ...]
'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *

class Solution:
    '''
    Bad Character Heuristic
    Time:
    Space:
    '''
    def boyer_moore(self, txt, pat):
        def last_occurance(pat):
            # 3 ways to do this

            # n = len(pat)
            # d = {}
            # for i in range(n):
            #     d[pat[i]] = i

            # 2nd way
            # for i,v in enumerate(pat):
            #     d[v] = i

            # 3rd way Most Ellegant
            d = {v: i for i,v in enumerate(pat)}
            return d

        m = len(pat)
        n = len(txt)
        result = []
        l_occur = last_occurance(pat)
        print(l_occur)

        #s is the shift of the pattern with respect to text
        s = 0
        while (s <= n-m):
            #start j at the end of the pattern
            j = m-1
            while j >= 0 and pat[j] == txt[s+j]:
                j -= 1

            # Every Char has matched
            if j < 0:
                print(f"pattern found at:{s}")
                result.append(s)
                cur_index = s+m
                s += 1
                # s += (m - l_occur[txt[cur_index]])
            else:
                cur_index = s+j
                key = txt[cur_index]
                if key not in l_occur:
                    x = -1
                else:
                    x = l_occur[key]
                    # print(f"j:{j} cur_index:{cur_index}, last_ocur:{x} key:{key} pat:{pat[j]}")
                s += (j - x)
                # print(f"shift:{s}")
        return result

        pass


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    # def test_simple(self):
    #     s = Solution()
    #     txt = "THIS IS A TEST TEXT"
    #     pat = "TEST"
    #     result = s.boyer_moore(txt,pat)
    #     self.assertEqual(result, [10])

    # def test_simple2(self):
    #     s = Solution()
    #     txt = "ATATAT"
    #     pat = "ATAT"
    #     result = s.boyer_moore(txt,pat)
    #     self.assertEqual(result, [0, 2])

    def test_simple2(self):
        s = Solution()
        txt = "WYXZTEATATT"
        pat = "ATATT"
        result = s.boyer_moore(txt,pat)
        self.assertEqual(result, [6])

    def test_not_found(self):
        s = Solution()
        txt = "WYXZTETATT"
        pat = "ATATT"
        result = s.boyer_moore(txt,pat)
        self.assertEqual(result, [])


unittest.main(verbosity=2)

