# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    003_Longest_Substring_Without_Repeating_C          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/01/10 11:13:03 by kcheung           #+#    #+#              #
#    Updated: 2018/01/28 19:00:57 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

'''
Given a string, find the length of the longest substring without repeating characters.
Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must
be a substring, "pwke" is a subsequence and not a substring.
'''

import unittest

# Pseudo Code
# use a visited array to store the index of the last seen char
# use a working window to keep track of
# Loop through entire string
    # if not seen char or the last seen index is not within my working window
        # then increase working window
    # else update max length seen and reset window to minimum
    # Always update visited array
# update and return max length

class Solution:
    def lengthOfLongestSubstring(self, s:str) -> int:
        n = len(s)
        # store the last seen index
        visited = [-1] * 256
        visited[ord(s[0])] = 0
        cur_len = 1
        max_len = 1
        prev_index = 0
        for i in range(1, n):
            prev_index = visited[ord(s[i])]
            if prev_index == -1 or (i - cur_len) > prev_index:
                cur_len += 1
            else:
                max_len = max(cur_len, max_len)
                cur_len = 1
            visited[ord(s[i])] = i
            max_len = max(cur_len, max_len)
        return(max_len)

class TestSolution1(unittest.TestCase):
    def test_simple1(self):
        str = "abcabcbb"
        s = Solution()
        self.assertEqual(s.lengthOfLongestSubstring(str), 3)

    def test_simple2(self):
        str = "bbbbbb"
        s = Solution()
        self.assertEqual(s.lengthOfLongestSubstring(str), 1)

    def test_simple3(self):
        str = "pwwkew"
        s = Solution()
        self.assertEqual(s.lengthOfLongestSubstring(str), 3)



if __name__ == "__main__":
    unittest.main()

