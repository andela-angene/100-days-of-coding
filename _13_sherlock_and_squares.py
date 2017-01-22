# franko4don Today at 9:15 AM
# sherlock-and-squares
# Good morning ladies and gentlemen
# Today's challenge: 
# https://www.hackerrank.com/challenges/sherlock-and-squares 
# Its really simple so have fun
# HackerRank
# Solve Sherlock and Squares
# Find the count of square numbers between A and B Solving code challenges on HackerRank is one of the best ways to prepare for programming interviews.

def find_squares(ls):
    a,b = map(int, ls)
    min_sq = int(a**0.5)
    sq = min_sq**2
    n = 0
    while sq <= b:
        if sq >= a and sq <= b:
            n += 1
        min_sq += 1
        sq = min_sq**2
    return n

for _ in range(input()):
    print find_squares(raw_input().split())