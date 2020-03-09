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

# nums = [1,2,3,4,5,6]

# L = nums[0:2]
# R = nums[2:4]
# L[0] = 9
# print(f'nums:{nums}, L:{L}, R:{R}')

#-------------------------------------------------------------------------------
# 10-19-19
#-------------------------------------------------------------------------------
# Need to pass set or stack by value not ref

# arr =
# def perm(arr):
#     new_arr = arr[:]
#     for a in new_arr:
#         new = .pop()
#         perm(new)
#     print(arr)
#     return arr

# perm(arr)

# const result = getCats(123).then((images) => {
#   images.forEach(img => addImage(img));
# });

# const result = getCats(123).then((images) => {
#   images.forEach(img => addImage(img));
# });

#-------------------------------------------------------------------------------
# challenge with Hatchways
#-------------------------------------------------------------------------------

'''
# Find the intersection of two arrays
# [10, 1, 3, 5] and [4, 2, 1, 5] -> [1, 5]

# key,val

# def f(arr1, arr2):
#     d = dict()
#     result = []
#     for i in arr1:
#         d[i] = True

#     for i in arr2:
#         if i in d:
#             result.append(i)
#     print(result)

# f([10, 1, 3, 5], [4, 2, 1, 5])

# Comment 1
# .  Comment 3
# .     Comment 4
# .  Comment 2
# .  Comment 5
# Comment 10
import functools

def tree(comments):
    def dfs(root, prefix, graph):
        print(f"{prefix}{graph[root]['comment']}")
        for nei in graph[root]['children']:
            dfs(nei, prefix + "  ", graph)

    graph = {}
    for c in comments:
        parent = c['parent']
        id = c['id']
        comment = c['comment']
        if id not in graph:
            graph[id] = {'comment': comment, 'children': []}
        elif graph[id]['comment'] is None:
            graph[id]['comment'] = comment
        if parent is not None:
            if parent not in graph:
                graph[parent] = {'comment': None, 'children': [id]}
            else:
                graph[parent]['children'].append(id)

    roots = filter(lambda x: x['parent'] == None, comments)
    rootIds = map(lambda x: x['id'], roots)
    for r in sorted(list(rootIds)):
        dfs(r, "", graph)

    #traverse graph from node with no parent
    #filter out from comments parent = None


comments = [{
    "id": 5,
    "comment": "Comment 5",
    "parent": 1
}, {
    "id": 4,
    "comment": "Comment 4",
    "parent": 3
}, {
    "id": 3,
    "comment": "Comment 3",
    "parent": 1
 },{

    "id": 2,
    "comment": "Comment 2",
    "parent": 1
}, {
    "id": 1,
    "comment": "Comment 1",
    "parent": None
},{
    "id": 6,
    "comment": "Comment 6",
    "parent": None
    }

            ]

tree(comments)

'''

#-------------------------------------------------------------------------------
# Interview with Sonder
#-------------------------------------------------------------------------------
'''
# Booking Start Date
# Sonder wants to help guests plan their stay
# by finding check-in and check-out dates that accommodate a desired length of stay.

# Sonder determines availability based on existing bookings,
# serialized as colon-separated pairs of integers.
# The first integer is a check-in date, and the second is a check-out date.
# Each integer represents an offset since Jan 1, 2019.
# E.g. '0:1' represents a booking where the check-in date is Jan 1st 2019,
# and the check-out date is Jan 2nd 2019.

# Directions
# Implement a method, booking_start_date(string bookings, int stay_length, int current_date)
# that will return the first day that can accommodate a booking of length stay_length.

# Examples:
# Input: bookings: '0:2 3:5 7:14', stay_length: 1, current_date: 4
# Output: 5
# Input: bookings: '0:3 3:6 7:14', stay_length: 2, current_date: 4
# Output: 14
# Input: bookings: '0:2 5:6 7:14', stay_length: 1, current_date: 3
# Output: 3

# Rules:
# Input is well-formed
# Bookings will not overlap
# Bookings are sorted in order of check-in date
# Only dates later than or equal to current date should be returned

# start-date:end-date.

# cur date: 6 len: 1
#(6:7)

# loop through and get rid of past bookings
# 1. Within a booking
#    1a. End date is equal to cur date: see if next booking start date <= curdate + len
#    2a. Endate is not: take difference between end date and curdate + len, see if fit in next booking
# 2. not in booking
#    1a. check the start date + len <= start date of next booking


def booking_start_date(bookings, stay_length, current_date):
    # bookings = [(int(time[0]), int(time[1]))
    #             for time in [b.split(':') for b in bookings.split()]]

    # for b in bookings.split():
    #     for i in b:
    #         start, end = b.split(':')
    #         print(f'{start}, {end}')

    # bookings = [(start, end) for b in bookings.split() for time in b.split(':')]

    bookings = [(int(start), int(end)) for start,end in [b.split(':') for b in bookings.split()]]
    print(bookings)
    result = 0
    i = 0
    while i < len(bookings):
        b = bookings[i]
        start = 0
        end = 1
        # booking end date > curdate or cur date within booking date: move pointer to booking end date
        if b[end] <= current_date or (b[end] >= current_date
                                      and b[start] <= current_date):
            i += 1
            result = b[end]
        elif b[start] >= current_date:
            if result + stay_length <= b[start]:
                return result
            else:
                i += 1
                result = b[end]
    return result


def booking_start_date(bookings, stay_length, current_date):
    print(
        f'\nbookings:{bookings} stay_length:{stay_length} current{current_date}'
    )
    result = 0
    booking_bit = 0
    window_bit = 1
    good_window = [0, 1, 1 << (stay_length + 1), (1 << (stay_length)) | 1]
    for i in range(stay_length):
        window_bit = window_bit << 1
        window_bit = window_bit | 1
    print(f'window: {"{0:b}".format(window_bit)}')
    bookings = [(int(b[0]), int(b[1]))
                for b in [b.split(':') for b in bookings.split()]]
    print(bookings)
    for b in bookings:
        for i in range(b[0], b[1] + 1):
            booking_bit = booking_bit | 2**i
    print(f'booking_bit: {"{0:b}".format(booking_bit)}')

    for i in range(current_date):
        booking_bit = booking_bit >> 1
        result += 1

    print(f'\nstartinglLoop')
    while booking_bit > 0:
        print(f'booking_bit_filtered: {"{0:b}".format(booking_bit)}')
        print(f'result:{result}')
        if window_bit & booking_bit in good_window:
            return result
        else:
            booking_bit = booking_bit >> 1
            result += 1

# 3 days
# window = 1111
# Good windows:
# 1001
# 0001
# 1000
# 0000

# i = 0
# while i <= bookings[:-1][1]:
#     if 2**i & booking_bit == 2** i:

# good stay
# 111 & 001 == 1

# bad stay
# 111 & 111 != 1

# Input: bookings: '0:2 3:5 7:14', stay_length: 1, current_date: 4
# Input: bookings: '0:3 3:6 7:14', stay_length: 2, current_date: 4
# Input: bookings: '0:2 5:6 7:14', stay_length: 1, current_date: 3
print(booking_start_date('0:2 3:5 7:14', 1, 4))
print(booking_start_date('0:3 3:6 7:14', 2, 4))
print(booking_start_date('0:2 5:6 7:14', 1, 3))
print(booking_start_date('0:2 5:6 7:14', 3, 2))

'''
#-------------------------------------------------------------------------------
# 11-06-19
#-------------------------------------------------------------------------------

'''
class maxHeap():

    def __init__(self):
        self.heap = []
        self.currentSize = 0

    def heapifyUp(self, i):
        parent = (i-1) // 2

    def heapPush(self, value):
        self.heap.append(value)
        self.currentSize += 1
        self.heapifyUp(self.currentSize-1)
'''

#-------------------------------------------------------------------------------
# 11-11-19
#-------------------------------------------------------------------------------

'''
def flip(arr, k):
    if k > len(arr):
        return None
    for i in range(k//2):
        arr[i], arr[k-i-1] = arr[k-i-1], arr[i]
    return arr

def next_smallest(arr, max_k):
    k = 1
    min_val = arr[0]
    for i in range(max_k):
        if arr[i] < min_val:
            k = i + 1
            min_val = arr[i]
    print(f'k:{k} smalles:{arr[k-1]}')
    return k

def pancake(arr):
    n = len(arr)
    max_k = n
    for i in range(n):
        k = next_smallest(arr , max_k)
        flip(arr,k)
        print(arr)
        flip(arr,max_k)
        print(arr)
        max_k -= 1
    flip(arr,n)
    return arr


# arr = [1,2,3,4,5]
# k = 3
# new_arr = print(flip(arr,3))

# max_k = 4
# k = next_smallest(arr, max_k)
# print(k)
# print(flip(arr,k))
# print(flip(arr,max_k))

arr = [5,2,3,6,1]
print(pancake(arr))
'''

#-------------------------------------------------------------------------------
# 11-14-19
#-------------------------------------------------------------------------------

'''
def str_split_recur(s, start, end):
    if end == len(s):
        return []
    if s[end] == " ":
        return str_split_recur(s, end+1, end+1)
    elif end+1 == len(s) or s[end+1] == ' ':
        word =  s[start:end+1]
        print(f'word:{word}')
        return [word] + str_split_recur(s, end+1, end + 1)
    else:
        return str_split_recur(s, start, end+1)

string = "Today  is a good day "
print(str_split_recur(string,0,0))

def str_reverse_words(s, start, cur):
    if cur == len(s):
        return []
    if s[cur] == " ":
        return str_reverse_words(s, cur+1, cur+1)
    elif cur+1 == len(s) or s[cur+1] == ' ':
        word =  s[start:cur+1]
        print(f'word:{word}')
        return str_reverse_words(s, cur+1, cur + 1) + [word]
    else:
        return str_reverse_words(s, start, cur+1)

string = "Today  is a good day "
print(str_reverse_words(string,0,0))
'''
#-------------------------------------------------------------------------------
# 12-07-19
#-------------------------------------------------------------------------------

'''
d = {}
d['a'] = 1
d['c'] = 2
d['b'] = 3

print(list(d.items()))
[key for key,val in  d.items()]

'''
#-------------------------------------------------------------------------------
# 01-29-19
#-------------------------------------------------------------------------------


'''
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def push_to_tail(self, x):
        node = Node(x)
        if self.tail is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        return self.tail

    def to_array(self):
        array = []
        cur = self.head
        while cur:
            array.append(cur.data)
            cur = cur.next
        return array

    def insert_at_pos(self, x, pos):
        node = Node(x)
        cur = self.head
        if cur is None or pos == 0:
            node.next = self.head
            self.head = node
            return node

        while pos > 0 and cur:
            prev = cur
            cur = cur.next
            pos -= 1
        prev.next = node
        node.next = cur
        return node

# ll = LinkedList()
# ll.push_to_tail(1)
# ll.push_to_tail(2)
# ll.push_to_tail(3)
# ll.push_to_tail(5)
# ll.insert_at_pos(4, 1)
# print(ll.to_array())

class TaskManager():

    def __init__(self, backlog, commands):
        self.backlog = self.backlog_linked_list(backlog)
        self.backlog_order = self.create_order(backlog)
        self.today = []
        self.commands = commands

    def create_order(self, backlog):
        d = {}
        for i,v in enumerate(backlog):
            if v not in d:
                d[v] = i
        return d

    def backlog_linked_list(self, backlog):
        ll = LinkedList()
        for b in backlog:
            ll.push_to_tail(b)
            return ll

    def add(self, x):
        pass


t = TaskManager(["a", "b", "c", "d"], [])
print(t.backlog_order)
print(t.backlog.to_array())

'''

#-------------------------------------------------------------------------------
# 2020-02
#-------------------------------------------------------------------------------

'''
import functools

def makeChangeMachine(coins):
    inventory = coins

    def update_inventory(combo):
        nonlocal inventory
        for c in combo:
            if c not in inventory:
                return False
            inventory[c] -= 1
        print(inventory)


    def get_combo(amount):

        coins_array = functools.reduce(
            lambda acc,x: acc + [x[0]] * x[1],
            list(coins.items()),
            [])[::-1]

        result = []
        if sum(coins_array) < amount:
            return False

        def recur(amount, coins_array, pos, n, combo):
            nonlocal result
            if amount == 0:
                result = combo
                return True
            if amount < 0 or pos == n:
                return False

            for i in range(pos, n):
                current_coin = coins_array[i]
                new_combo = combo[:] + [current_coin] if combo else [current_coin]
                remaining = amount - current_coin
                if recur(remaining, coins_array, pos + 1, n, new_combo):
                    return True
            return False

        recur(amount, coins_array, 0, len(coins_array), [])
        return result

    def f(amount, on_success, on_failure):
        nonlocal inventory
        if not(all([amount, on_success, on_failure])):
            print("Missing Args")
            return False
        else:
            combo = get_combo(amount)
            if combo:
                coins = [0] * (max(combo) + 1)
                for c in combo:
                    coins[c] += 1
                if on_success(coins):
                    update_inventory(combo)
                    return True
                return False
            else:
                return on_failure()
    return f

def dump(combo):
    print(f'{combo[1]} Pennies\n{combo[5]} nickels\n{combo[10]} dimes\n{combo[25]} quarters')

def on_error():
    print("I cannot do that!")

def picky(combo):
    dump(combo)
    # print(combo)
    if combo[1]:
        print ("Nope I hate pennies")
        return False
    return True

def easy(combo):
    dump(combo)
    # print(combo)
    return True

coins = { 1: 20, 5: 3, 10: 4, 25:3 }
myChangeMachine = makeChangeMachine(coins)
print(myChangeMachine(131,picky,on_error))
print(myChangeMachine(131,easy,on_error))
print(myChangeMachine(131,easy,on_error))


'''
#-------------------------------------------------------------------------------
# 02-17-20
#-------------------------------------------------------------------------------



# avail = [0,0,0,0,0,0,0 ....]
