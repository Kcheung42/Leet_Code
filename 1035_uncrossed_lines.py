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

class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        '''
        d[1] = 0
        d[4] = 5

        max
        1 4 2 9 8 7

        1 2 9 8 7 4
        '''
        def recur(A, B, d, cur_idx, total_conn):
            if cur_idx == len(A):
                return total_conn

            temp = []
            for i in range(cur_idx, len(A)):
                max_end = max(d.values()) if len(d) > 0 else 0
                end = B.index(A[i])
                ends = [idx for idx,v in enumerate(B) if v == A[i]]
                print(ends)
                for end in ends:
                    if end >= max_end:
                        print(f'connecting:num:{A[i]} start:{i} end:{end} total:{total_conn + 1}')
                        d[A[i]] = end
                        temp.append(recur(A,B,d, i+1, total_conn + 1))
                        print(d)
                        del d[A[i]]
            return max(temp) if len(temp) > 0 else 0

        result = recur(A, B, {}, 0,0)
        return (result)


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        A = [1,4,2]
        B =[1,2,4]
        [2,5,1,2,5]
        [10,5,2,1,5,2]
        s = Solution()
        self.assertEqual(s.maxUncrossedLines(A, B), 2)

    def test_simple(self):
        A = [2,5,1,2,5]
        B = [10,5,2,1,5,2]
        s = Solution()
        self.assertEqual(s.maxUncrossedLines(A, B), 2)



unittest.main(verbosity=2)

