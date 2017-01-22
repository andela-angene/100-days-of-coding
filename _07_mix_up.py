# boundlesslove Jan 10th
# boundlesslove [8:34 AM] 
# CHALLENGE 7:  D. MixUp
# Given strings a and b, return a single string with a and b separated by a space but with the first 2 chars of each string swapped.  
# For example:   mix_up('mix' , 'pod') SHOULD RETURN  'pox mid'
# mix_up('dog', 'dinner')  SHOULD RETURN  'dig donner'
# Assume a and b are length 2 or more.

def mix_up(lst):
    a,b = lst
    return b[:2] + a[2:], a[:2] + b[2:]
print mix_up(raw_input('enter 2 words separated by a space: ').split())