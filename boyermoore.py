#------------------------------------------------------------------------------
# Question:
#------------------------------------------------------------------------------
# tags: #pattern_match
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
    def search(self, text, pat):
        P = len(pat)
        T = len(text)
        # l_occur = {v:i for i,v in enumerate(pat)}
        l_occur = collections.defaultdict(lambda: -1)
        result = []
        shift = 0
        while shift <= T - P:
            j = P-1
            while j > 0 and P[j] == T[shift+j]:
                j -= 1
            if j < 0: # found a match at shift
                result.append(shift)
                key = text[shift + P]
                x = l_occur.get(key, -1)
                shift += (P-x)
            else:
                key = text[shift + j]
                x = l_occur.get(key, -1)
                shift += max(1, (j-x))
        return result

class Solution:
    '''
    Bad Character Heuristic
    Time:
    Space:

    1. build last_occurance hashmap using pattern
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

        P = len(pat)
        T = len(txt)
        result = []
        l_occur = last_occurance(pat)
        print(l_occur)
        #s is the shift of pattern with respect to text
        s = 0
        while (s <= T-P):
            #start j at the end of the pattern
            j = P-1
            while j >= 0 and pat[j] == txt[s+j]:
                j -= 1
            # Every Char has matched
            if j < 0:
                print(f"pattern found at:{s}")
                result.append(s)
                # cond needed for when pattern is at end of T
                if s + P < T:
                    # shift pattern so next character in text
                    # aligns with last occurance in pattern
                    key = txt[s + P]
                    x = l_occur.get(key, -1)
                    s += (P-x)
                else:
                    s += 1
            else:
                cur_index = s+j
                key = txt[cur_index]
                # x = l_occur[key] if key in l_occur else -1
                x = l_occur.get(key, -1)

                #max is needed incase l_occur is at the right of j
                s += max(1, (j - x))
                # print(f"s:{s}")
        return result

        pass


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple1(self):
        s = Solution()
        txt = "THIS IS A TEST TEXT"
        pat = "TEST"
        result = s.boyer_moore(txt,pat)
        self.assertEqual(result, [10])

    def test_simple2(self):
        s = Solution()
        txt = "ATATAT"
        pat = "ATAT"
        result = s.boyer_moore(txt,pat)
        self.assertEqual(result, [0, 2])

    def test_simple3(self):
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

