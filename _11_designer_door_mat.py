# boundlesslove Jan 16th
# designer-door-mat
# 
# https://www.hackerrank.com/contests/pythonist2/challenges/designer-door-mat
# HackerRank
# Solve Designer Door Mat
# Print a designer door mat. Solving code challenges on HackerRank is one of the best ways to prepare for programming interviews.

N, M = map(int,raw_input().split()) # More than 6 lines of code will result in 0 score. Blank lines are not counted.
for i in xrange(1,N,2): 
    print '-'*((M - i*3)/2) + '.|.'*i + '-'*((M - i*3)/2)
print '-'*((M - 7)/2) + 'WELCOME' + '-'*((M - 7)/2)
for i in xrange(N-2,-1,-2): 
    print '-'*((M - i*3)/2) + '.|.'*i + '-'*((M - i*3)/2)