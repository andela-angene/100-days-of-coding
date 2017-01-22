# This puzzle is very similar to the one given on Hackerrank: 
# https://www.hackerrank.com/contests/code-leader/challenges/string-counter
# so I solved for that since it can be tested against different cases
words = raw_input().split()
wd_dict = {}
lst = []
for word in words:
    if word in wd_dict:
        wd_dict[word] += 1
        if wd_dict[word] == 2:
            lst.append(word)
    else:
        wd_dict[word] = 1
count = 0
for word in lst:
    print wd_dict[word], word
    count += 1
if count == 0:
    print 0