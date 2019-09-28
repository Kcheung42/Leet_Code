# def split(s):
# 	l = len(s)
# 	spaces = [' ']
# 	words = []
# 	i = 0
# 	while i < l:
# 		if s[i] not in spaces:
# 			word_start = i
# 			while i < l and s[i] not in spaces:
# 				i += 1
# 			words.append(s[word_start:i])
# 		i += 1

# 	return words


# def my_reversed(words):
# 	for i in range(len(words) // 2):
# 		tmp = words[i]
# 		words[i] = words[len(words) - i - 1]
# 		words[len(words) - i - 1] = tmp
# 	return words

# def reverse2(s):
# 	return " ".join(my_reversed(split(s)))

# def reverse1 (s):
# 	return " ".join(reversed(s.split()))

# def reverse3(s):
# 	return s.split()[::-1]

# for start in range(0, 10, 2):
# 	print start

# # print(reverse1("This is the best"))
# # print(reverse2("This is the best"))
# print(reverse3("This is the best"))

# def max_height(arr, idx):
#     if idx > len(arr)-1 or arr[idx] == -1:
#         return 0
#     else:
#         leftchild = 2 * idx + 1
#         rightchild = 2 * idx + 2
#         return arr[idx] + max([max_height(arr, leftchild) , max_height(arr, rightchild)])

# def solution(arr):
#     # Type your solution here
#     if len(arr) < 0:
#         return 0
#     else:
#         idx = 0
#         left = max_height(arr, 2 * idx + 1)
#         right = max_height(arr, 2 * idx + 2)
#         if left > right:
#             return "Left"
#         elif right > left:
#             return "Right"
#         else:
#             return ""
#     pass

# print(solution([3, 6, 2, 9, -1, 10]))

# class TrieNode():
#     def __init__(self, c):
#         self.count = 0
#         self.char = ""
#         self.word = ""
#         self.isEnd = False
#         self.children = dict()

# class Trie(object):
#     def __init__(self):
#         self.root = TrieNode(None)

#     def insert(self, word):
#         node = self.root
#         for c in word:
#             if c not in node.children:
#                 node.children[c] = TrieNode(c)
#             node = node.children[c]
#             node.count += 1
#         node.word = word
#         node.isEnd = True

#     def pfx(self, word, n):
#         node = self.root
#         s = ""
#         for c in word:
#             if node.children[c].count == n:
#                 s += c
#             node = node.children[c]
#         return s

# def solution(strings):
#     # Type your solution here =
#     if len(strings) == 0:
#         return ""
#     t = Trie()
#     for s in strings:
#         t.insert(s)
#     print(len(strings))
#     return t.pfx(strings[0], len(strings))
#     pass

# print(solution(["abcdef","adegh","a"]))

# def solution(s, t):
#     # Type your solution here
#     if len(s) != len(t):
#         return false
#     n = len(s)
#     d = dict()
#     d2 = dict()
#     for i in range(n-1):
#         if s[i] not in d and s[i] not in d2:
#             d[s[i]] = t[i]
#             d2[t[i]] = s[i]
#         elif d[s[i]] != t[i]:
#             return False
#     print(d)
#     return True

# print(solution("zqgiuydhxvmiywfadkvjldrebyhxewdksmiw", "dkmbzfqtyjabflrhqwjhnqcugftyulqwpabl"))




# def solution(angles):
#     stack = []
#     openCount = 0
#     closeCount = 0
#     for a in angles:
#         if a == '<':
#             stack.append(a)
#         elif a == '>':
#             if len(stack) > 0:
#                 stack.pop()
#             else:
#                 openCount += 1
#     return '<' * openCount + angles + '>' * len(stack)

###################################################
# Partition
###################################################

# def partition(arr, start, end):
#     pIndex = start
#     pivot = arr[end]

#     while start < end:
#         if arr[start] <= pivot:
#             arr[start], arr[pIndex] = arr[pIndex] , arr[start]
#             pIndex += 1
#         start += 1
#     arr[pIndex], arr[end] = arr[end], arr[pIndex]
#     return pIndex

# def qsort(arr, start, end):
#     if start < end:
#         mid = partition(arr, start, end)
#         qsort(arr, start, mid - 1)
#         qsort(arr, mid + 1, end)


# a = [9,8,7,6,5,4,11,12]
# qsort(a, 0, len(a)-1)
# print(a)


###################################################
# 08-31-19
###################################################

# num1 = "1234"
# num2 = "567"

# class Solution:
#     def multiply(self, num1, num2):
#         res = [0] * (len(num1) + len(num2))
#         for i in range(len(num1)-1, -1, -1):
#             carry = 0
#             for j in range(len(num2)-1, -1, -1):
#                 print(f'res:{res}')
#                 print(f'i:{i}, j:{j}')
#                 tmp = int(num1[i])*int(num2[j])+carry
#                 # take care of the order of the next two lines
#                 carry = (res[i+j+1] + tmp) // 10
#                 res[i+j+1] = (res[i+j+1] + tmp) % 10
#                 # or simply: carry, res[i+j+1] = divmod((res[i+j+1] + tmp), 10)
#             res[i] += carry
#         print(f'res:{res}')
#         res = "".join(map(str, res))
#         return '0' if not res.lstrip("0") else res.lstrip("0")

# s = Solution()
# print(s.multiply(num1, num2))



###################################################s
# 09-01-19
###################################################

# n = len([1,2,3,4,5])
# for i in range(n-1):
#     print(i)

###################################################
# 09-08-19
###################################################

nums = [1,2,3,4,5,6]

L = nums[0:2]
R = nums[2:4]
L[0] = 9
print(f'nums:{nums}, L:{L}, R:{R}')

