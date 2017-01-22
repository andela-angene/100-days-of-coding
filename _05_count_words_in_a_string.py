# frantz Jan 8th
# CHALLENGE 5 :  Count Words in a String - Counts the number of individual words in a string. For added complexity read these strings in from a text file and generate a summary.  SO OUR CODE SHOULD BE ABLE TO RECEIVE A TEXT, AND TELL HOW MANY WORDS ARE IN THAT TEXT. FOR ADDITIONAL FUNCTIONALITY, IT CAN GET THIS TEXT BY READING A FILE                    OPTIONAL : LET YOURS FUNCTION ACTUALLY ANALYSE THE TEXT PASSED IN BY THE USER. IT SHOULD RETURN THE WORD COUNT, ALSO, RETURN THE NUMBER OF DUPLICATE WORDS, FOR EXAMPLE, IF THERE ARE A 100 WORDS, AND THE WORD "THE" APPEARS 3 TIMES, OUR FUNCTION SHOULD TELL US :sunglasses:
# COMMENT: This puzzle is very similar to the one given on Hackerrank: 
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