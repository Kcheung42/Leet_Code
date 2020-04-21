# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    535_Encode_and Decode_TinyURL.py                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/01/12 16:21:38 by kcheung           #+#    #+#              #
#    Updated: 2018/01/12 16:39:40 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

'''
Time: O(1)
Space: O(n)

TinyURL is a URL shortening service where you enter a URL such as
https://leetcode.com/problems/design-tinyurl and it returns a short URL
such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no
restriction on how your encode/decode algorithm should work. You just need to
ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded
to the original URL

'''
import random

class Codec:
    def __init__(self):
        self.tiny_urls = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        :type longUrl: str
        :rtype: str
        """
        num_form = random.randint(1, 1E10)
        while num_form in self.tiny_urls:
            num_form = random.randint(1,1E10)
        self.tiny_urls[num_form] = longUrl
        return ('http://tinyurl.com/' + str(num_form))


    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        :type shortUrl: str
        :rtype: str
        """
        num_form = int(shortUrl[19:])
        return self.tiny_urls[num_form]

# Your Codec object will be instantiated and called as such:

url = 'https://leetcode.com/problems/design-tinyurl'
codec = Codec()
print(codec.decode(codec.encode(url)))
