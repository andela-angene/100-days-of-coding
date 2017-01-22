# franko4don Jan 18th
# special-multiple
# 
# CHALLENGE FOR TODAY: 
# https://www.hackerrank.com/challenges/special-multiple
# HackerRank
# Solve Special Multiple
# Can you find the least positive integer that is made of only 0s and 9s? - 30 Points Solving code challenges on HackerRank is one of the best ways to prepare for programming interviews.

def find_multiple(number):
    n = 1
    while True:
        multiple = 9*int(bin(n)[2:])
        if multiple % number == 0:
            return multiple
        n += 1

for _ in range(input()):
    print find_multiple(input())