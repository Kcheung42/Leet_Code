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
    '''
    abccabcbb
    l
      r
    d[c] = 0
    '''
    def lengthOfLongestSubstring(self, s:str) -> int:
        n = len(s)
        if n == 0:
            return 0

        # store the last seen index
        seen = {s[0]: 0}
        max_len = 1
        l = 0
        for r, c in enumerate(s[1:], start=1):
            cur_len = r - l
            prev_index = seen.get(c, -1)
            # calculate max len if repeat char found in window
            if prev_index >= l:
                l = prev_index + 1
            else:
                cur_len += 1
            seen[c] = r
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


    def test_simple4(self):
        str = "abcazgaa"
        s = Solution()
        self.assertEqual(s.lengthOfLongestSubstring(str), 5)

    def test_simple4(self):
        str = "au"
        s = Solution()
        self.assertEqual(s.lengthOfLongestSubstring(str), 2)



if __name__ == "__main__":
    unittest.main()
