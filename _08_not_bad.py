# boundlesslove Jan 11th
# CHALLENGE FOR TODAY IS TAGGED: not_bad
# Given a string, find the first appearance of the substring 'not' and 'bad'. If the 'bad' follows the 'not', replace the whole 'not'...'bad' substring with 'good'. Return the resulting string.
# FOR EXAMPLE: 'This dinner is not that bad!' yields:
# This dinner is good! Since 'not' appeared before 'bad' just change from 'not....bad' words to 'good'. Also, 'The tea is not hot' yields 'The tea is not hot'. No changes because there is no 'bad' after 'not'.  HaPpY CodInG...

def not_bad(strg):
    n,b = [False, False]
    for i in xrange(len(strg)):
        if strg[i] == 'not' and n == False:
            n = i
        if (strg[i] in ['bad','bad!'] and n != False) and b == False:
            b = i
    if n != False and b != False:
        return ' '.join(strg[:n]) + ' good ' + ' '.join(strg[(b+1):])
    else:
        return ' '.join(strg)
    
print not_bad(raw_input().split())