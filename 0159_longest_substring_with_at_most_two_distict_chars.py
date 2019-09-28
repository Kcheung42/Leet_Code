import unittest
from typing import *


# "Given a string s , find the length of the longest substring t
# that contains at most 2 distinct characters."

# class Solution: Fail some cases
#     def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
#         if not s:
#             return 0
#         distinct_chars = []
#         n = len(s)
#         cur_len = 1
#         max_len = 1
#         visited = [-1] * 256
#         distinct_chars.append(s[0])
#         visited[ord(s[0])] = 0
#         for i in range(1, n):
#             print(f'distince_chars:{distinct_chars}')
#             if len(distinct_chars) < 2:
#                 distinct_chars.append(s[i])
#                 visited[ord(s[i])] = i
#                 cur_len += 1
#                 print(f'2nd str:{s[i-cur_len:i]} i:{i} cur_len:{cur_len}, s[i]:{s[i]}')
#             elif s[i] in distinct_chars:
#                 if s[i] != s[i-1]:
#                     visited[ord(s[i])] = i
#                 cur_len += 1
#                 print(f'1st str:{s[i-cur_len:i]} i:{i} cur_len:{cur_len}, s[i]:{s[i]}')
#             else:
#                 print(f'3rd str:{s[i-cur_len:i]} i:{i} cur_len:{cur_len}, s[i]:{s[i]}')
#                 max_len = max(max_len, cur_len)
#                 if visited[ord(s[0])] > visited[ord(distinct_chars[1])]:
#                     prevIndex = visited[ord(distinct_chars[0])]
#                     distinct_chars.pop()
#                 else:
#                     prevIndex = visited[ord(distinct_chars[1])]
#                     distinct_chars.pop(0)
#                 cur_len = i - prevIndex + 1
#                 print(f'4th str:{s[i-cur_len:i]} i:{i} cur_len:{cur_len}, s[i]:{s[i]}')
#                 distinct_chars.append(s[i])
#                 visited[ord(s[i])] = i
#         max_len = max(max_len, cur_len)
#         return max_len


from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: 'str') -> 'int':
        n = len(s)
        if n < 3:
            return n

        # sliding window left and right pointers
        left = 0
        right = 0
        # hashmap character -> its rightmost position
        # in the sliding window
        hashmap = defaultdict()

        max_len = 2

        while right < n:
            # slidewindow contains less than 3 characters
            hashmap[s[right]] = right
            right += 1

            # slidewindow contains 3 characters
            if len(hashmap) == 3:
                # delete the leftmost character
                del_idx = min(hashmap.values())
                del hashmap[s[del_idx]]
                # move left pointer of the slidewindow
                left = del_idx + 1

            max_len = max(max_len, right - left)

        return max_len

class TestSolution1(unittest.TestCase):
    def test_simple(self):
        arr = "eceba"
        s = Solution()
        self.assertEqual(s.lengthOfLongestSubstringTwoDistinct(arr), 3)
        #substring 'ece'

    def test_simple1(self):
        arr = "ccaabbb"
        s = Solution()
        self.assertEqual(s.lengthOfLongestSubstringTwoDistinct(arr), 5)
        #substring 'aabbb'

    def test_simple2(self):
        arr = "ababcbcbaaabbdef"
        s = Solution()
        self.assertEqual(s.lengthOfLongestSubstringTwoDistinct(arr), 6)

    def test_simple3(self):
        arr = "abc"
        s = Solution()
        self.assertEqual(s.lengthOfLongestSubstringTwoDistinct(arr), 2)


unittest.main()
