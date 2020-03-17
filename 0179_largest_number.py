#------------------------------------------------------------------------------
# Question:
#------------------------------------------------------------------------------
# tags:
'''
Given a list of non negative integers, arrange them such that they form the
largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of
an integer.

Regular Radix Sort
[9, 5 , 34, 3, 30]
output = [0,0,0,0,0]

first digit

index = a[i]/1
count[index%10] += 1

count = [1,0,0,1,1,1,0,0,0,1]
#convert count => count[i] += count[i-1]
count = [1,1,1,2,3,4,4,4,4,5]

Build Output Array backwards
output = [30,3,34,5,9]


second digit
prev_output = [30,3,34,5,9]
num = a[i]/10
index = num%10
count[index] += 1
count = [3,0,0,2,0,0,0,0,0,0]
#convert count => count[i] += count[i-1]
count = [3,3,3,5,5,5,5,5,5,5]


Build Output Array backwards
num = a[i]/10
index = num%10
modify count[index] -= 1 each time we update output
prev_output = [30,3,34,5,9]
count = [1,3,3,4,5,5,5,5,5,5]
output = [3,5,9,30,34]

[9, 5 , 3, 3, 30]

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
    def quick_sort(self, nums):

        def compare(x, y):
            return str(x) + str(y) > str(y) + str(x)

        def partition(start, end):
            pIndex = start
            pivot = nums[end]
            for i in range(start, end):
                if compare(nums[i], pivot):
                    nums[i], nums[pIndex] = nums[pIndex], nums[i]
                    pIndex += 1
            nums[end],nums[pIndex] = nums[pIndex], nums[end]
            return pIndex

        def qsort_helper(start, end):
            if start < end:
                pivot = partition(start, end)
                qsort_helper(start, pivot-1)
                qsort_helper(pivot+1, end)

        qsort_helper(0, len(nums)-1)
        return nums

    def largestNumber(self, nums: List[int]) -> str:
        self.quick_sort(nums)
        return "0" if nums[0] == 0 else "".join(map(str,nums))


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        s = Solution()
        nums = [3, 30, 34, 5, 9]
        result = s.largestNumber(nums)
        self.assertEqual(result, "9534330")


unittest.main(verbosity=2)

