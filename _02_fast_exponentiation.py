# franko4don Jan 4th
# Good morning guyz
# Challenge 2: 
#  Fast Exponentiation - Ask the user to enter 3 integers a, b and c output (a^b) mod c  in O(lg n) time complexity. N:B do not use inbuilt function. Write your own implementation. made a little adjustment 

def fast_expon(inp):
    a,b,c = map (int, inp.split())
    bg = 1
    for _ in xrange(b):
        bg *= a
    if (bg / float(c)) == 1:
        return 0
    sm = c
    while sm < bg:
        if (sm + c) > bg:
            return bg - sm
        sm += c
    return bg

print fast_expon(raw_input('Enter numbes in this format: a b c '))