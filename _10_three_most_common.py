# boundlesslove Jan 13th
# CHALLENGE 10:                                                                   You are given a string . 
# 1)The string contains only lowercase English alphabet characters.
# 
# 2)Your task is to find the top three most common characters in the string .
# 
# 3)The length of the String shouldn't be less than 3 or greater than 10000. 
# 4)Print the three most common characters along with their occurrence count each on a separate line.
# 5)Sort output in descending order of occurrence count. If the occurrence count is the same, sort the characters in ascending order.
# 
# An input of 'aabbbccde'
# 
# Should Output
# 
# b 3
# a 2
# c 2
# 
# HaPpY CoDiNg

inpt = raw_input()
letter_dict = {}
for i in xrange(len(inpt)):
    letter = inpt[i]
    if letter in letter_dict:
        letter_dict[letter] += 1
    else:
        letter_dict[letter] = 1
count = 0
while count < 3:
    k = letter_dict.keys()
    v = letter_dict.values()
    max_k = k[v.index(max(v))]
    print max_k + ' ' + str(letter_dict[max_k])
    del letter_dict[max_k]
    count += 1