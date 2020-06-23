#------------------------------------------------------------------------------
# Question: 0282_expression_add_operators.py
#------------------------------------------------------------------------------
# tags: #pemdas
'''
Given a string that contains only digits 0-9 and a target value, return all
possibilities to add binary operators (not unary) +, -, or * between the
digits so they evaluate to the target value.

Example 1:

Input: num = "123", target = 6
Output: ["1+2+3", "1*2*3"]
Example 2:

Input: num = "232", target = 8
Output: ["2*3+2", "2+3*2"]
Example 3:

Input: num = "105", target = 5
Output: ["1*0+5","10-5"]
Example 4:

Input: num = "00", target = 0
Output: ["0+0", "0-0", "0*0"]
Example 5:

Input: num = "3456237490", target = 9191
Output: []

'''

#------------------------------------------------------------------------------
# Solutions
#------------------------------------------------------------------------------
from typing import *


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        '''
        operators = set([+,-,*])

        1,2,3,4,5
        1,2,3,45
        1,2,345
        1,2345

        12,3,4,5
        12,3,45
        12,345

        123,4,5
        123,45

        1234,5

        12345
        '''
        def default(x, y):
            return None

        def dispatch(opp, x, y):
            return {
                "+": lambda x, y: x + y,
                "-": lambda x, y: x - y,
                "*": lambda x, y: x * y,
            }.get(opp, default)(x, y)

        '''
        1+2*3+4*5+6
           V   V
        1+ 6 + 20 - 6
        '''
        def evaluate(exp):

            def isbad(e):
                '''
                105
                [1,+,05] -> 05 is bad path
                '''
                if len(e) > 1 and e[0] == '0':
                    return True
                return False

            if len(exp) == 0:
                return float("-inf")

            stack = []
            n1 = None
            for e in exp:
                if isbad(e):
                    return float('inf')
                if e == "*":
                    n1 = stack.pop()
                elif n1:
                    stack.append(str(int(n1) * int(e)))
                    n1 = None
                else:
                    stack.append(e)

            result = int(stack[0])
            for elem in stack[1:]:
                if elem in operations:
                    opp = elem
                else:
                    result = dispatch(opp, result, int(elem))

            return(result)


        def dfs(path=[], index=0):
            e = evaluate(path)
            if e == target:
                result.append(path)
                return
            for i in range(index, len(num)):
                x = num[index:i + 1]
                if len(path) == 0:
                    dfs(path+[x], i+1)
                else:
                    for opp in operations:
                        dfs(path + [opp] + [x], i + 1)

        operations = "+-*"
        result = []
        dfs()
        result = ["".join(x) for x in result]
        return (result)


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest


class TestSolution(unittest.TestCase):
    # def test_simple1(self):
    #     s = Solution()
    #     num = "123"
    #     target = 6
    #     self.assertEqual(s.addOperators(num, target), ["1+2+3", "1*2*3"])

    def test_simple2(self):
        s = Solution()
        num = "105"
        target = 5
        self.assertEqual(s.addOperators(num, target), ["1*0+5", "10-5"])


unittest.main(verbosity=2)
