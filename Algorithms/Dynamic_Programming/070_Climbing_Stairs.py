# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    070_Climbing_Stairs.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/01/15 19:56:09 by kcheung           #+#    #+#              #
#    Updated: 2018/01/16 13:54:08 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you
climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output:  2
Explanation:  There are two ways to climb to the top.

1. 1 step + 1 step
2. 2 steps

Example 2:

Input: 3
Output:  3
Explanation:  There are three ways to climb to the top.

1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

def climbStairs(self, n):
	:type n: int
	:rtype: int

'''

class Solution1(object): # Time:O(2^n) Space:O(n)
	def climbStairsHelper(self, i,  n ):
		if i > n:
			return 0
		if i == n:
			return 1
		return (self.climbStairsHelper(i + 1, n) + self.climbStairsHelper(i + 2, n))

	def climbStairs(self, n):
		return(self.climbStairsHelper(0, n))

'''
f(i+1, n) + f(i+2, n)

L

                                  ....f(10,10) = > 1
                                 /
                          f(3,10)
                         /
                  f(2,10) => ?
                         \
                          f(5,10)
                 /
          f(1,10) => ?
                 \
                  f(3,10)
        /
f(0,10)
        \
                  f(3, 10)
                 /
          f(2,10) => memo[2]
                 \
                  f(5, 10)
R
'''

class Solution2(object): # Time:O(n) Space:O(n)

	def climbStairsHelper(self, i, n, memo):
		if i > n:
			return 0
		if i == n:
			return 1
		if memo[i] > 0:
			return memo[i]
		memo[i] = self.climbStairsHelper(i + 1, n, memo) + self.climbStairsHelper(i + 2, n, memo)
		return memo[i]

	def climbStairs(self, n):
		memo = [0] * (n + 1)
		return(self.climbStairsHelper(0, n, memo))

class Solution3(object): # Time:O(n) Space:O(1)
	def climbStairs(self, n):
		if n == 1:
			return 1
		first = 1
		second = 2
		for i in range(3, n+1):
			third = first + second
			first, second = second, third
		return second


s = Solution3()
print(s.climbStairs(5))

