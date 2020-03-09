'''
Write a function that compares two strings and returns whether or not they are anagrams of each other.
“adam”, “peter” => false
“sport”, “portsp” => true

d[s] = 1
d[p] = 0


def isAnagram(str1, str2):
    return(all([x[0]==x[1] for x in (zip(sorted(str1), sorted(str2)))]))


str1 = "foo"
str2 = "off"
print(isAnagram(str1,str2))

str1 = "sport"
str2 = "ports"
print(isAnagram(str1,str2))

'''


'''
Write a function that takes an array of strings and returns a string containing all of their vowels concatenated.
[“dog”, “cat”, "car"’] => “oaa”
["foo", "bar"] => "ooa"

filter(isVowel, "dogcatcar") 

def filter_vowels(arr):
    def isVowel(c):
        v = "aeiou"
        return True if c in v else False

    arr_str = "".join(arr)
    result = "".join(list(filter(isVowel, arr_str)))
    return result


print(filter_vowels(["dog", "cat", "car"]))
print(filter_vowels(["foo", "bar"]))
print(filter_vowels([]))
'''

'''
Write a function that makes this work:
add(1, 2) -> 3
add(1)(2) -> 3
add()()(1)()()(2) -> 3
'''

from functools import partial

def add(arg1=None, arg2=None):
    if arg2 is not None:
        return arg1 + arg2
    elif arg1 is None:
        return add
    else:
        return partial(add, arg1)

print(add(1,2))
print(add(1)(2))
print(add()()(1)()()(2))
