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

'''
class Codec:
    [dog, cat, bird, worm]
    "%3%dog%3%cat bird worm"
    cat => %3%4,3,4%3%

    # def encode(self, strs):
    #     """Encodes a list of strings to a single string.

    #     :type strs: List[str]
    #     :rtype: str
    #     """
    #     result = []
    #     for s in strs:
    #         result.append("%")
    #         chars = [str(ord(c)) for c in s]
    #         result.append(','.join(chars))
    #     return "".join(result)

    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        print(chr(257).join(strs))

    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]

        %3%100,111,103%3%99,97,116%4%98,105,114,100
        %100,111,103%99,97,116%98,105,114,100
        """

        def get_word(s, i):
            if s[i] == '%':
                i += 1
                start = i
                while i < len(s) and s[i] != '%':
                    i += 1
                chars = s[start:i].split(',')
                word_array = [chr(int(c)) for c in chars if c != '']
                word = ''.join(word_array)
                return i, word

        result = []
        i = 0
        while i < len(s):
            i, word = get_word(s, i)
            result.append(word)
        return result

    '''

class Codec:
    def len_to_str(self, x):
        """
        Encodes length of string to bytes string
        """
        x = len(x)
        bytes = [chr(x >> (i * 8) & 0xff) for i in range(4)]
        bytes.reverse()
        bytes_str = ''.join(bytes)
        # print(bytes_str)
        return bytes_str
    
    def encode(self, strs):
        """Encodes a list of strings to a single string.
        :type strs: List[str]
        :rtype: str
        """
        # encode here is a workaround to fix BE CodecDriver error
        print(self.len_to_str(x) + x.encode('utf-8') for x in strs)
        return ''.join(self.len_to_str(x) + x.encode('utf-8') for x in strs)
        
    def str_to_int(self, bytes_str):
        """
        Decodes bytes string to integer.
        """
        result = 0
        for ch in bytes_str:
            result = result * 256 + ord(ch)
        return result
    
    def decode(self, s):
        """Decodes a single string to a list of strings.
        :type s: str
        :rtype: List[str]
        """
        i, n = 0, len(s)
        output = []
        while i < n:
            length = self.str_to_int(s[i: i + 4])
            i += 4
            output.append(s[i: i + length])
            i += length
        return output


#------------------------------------------------------------------------------
# Tests
#------------------------------------------------------------------------------
import unittest

class TestSolution(unittest.TestCase):
    def test_simple(self):
        strs = ['dog', 'cat', 'bird']
        codec = Codec()
        result = codec.decode(codec.encode(strs))
        self.assertEqual(result, strs)

    # def test_simple(self):
    #     strs = ['']
    #     codec = Codec()
    #     result = codec.decode(codec.encode(strs))
    #     self.assertEqual(result, strs)

unittest.main(verbosity=2)

