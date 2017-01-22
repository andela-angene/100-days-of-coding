one_to_ninteen = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten","Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
twenty_up = ["","","Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

#This function names up to three numbers only
def name_three(numbrs):
    if int(''.join(numbrs)) == 0:
        return []
    num_name = []
    if len(numbrs) == 3:
        if int(numbrs[0]) != 0:
            num_name.append(one_to_ninteen[int(numbrs[0])])
            num_name.append('Hundred')
        numbrs.pop(0)
    num = int(''.join(numbrs))
    if num < 20:
        num_name.append(one_to_ninteen[num])
    else:
        num_name.append(twenty_up[int(numbrs[0])])
        if int(numbrs[1]) != 0:
            num_name.append(one_to_ninteen[int(numbrs[1])])
    return num_name

#This functions adds the appropriate unit 
def large_num(num):
    if num >= 13:
        return ["Trillion"]
    if num >= 10:
        return ["Billion"]
    if num >= 7:
        return ["Million"]
    if num >= 4:
        return ["Thousand"]
    return []

#This does the actual naming; it splits the number in groups of 3 and names them, adding the correct units
def name_num(num):
    if int(num) == 0:
        return 'Zero'
    work_on =[]
    n = 0
    ln = len(num)
    final_name = []
    add_to_final = []
    threes = ln%3
    if (threes == 0):
        threes = 3
    while n < ln:
        for _ in range(threes):
            work_on.append(num[n])
            n += 1
        threes = 3
        add_to_final = name_three(work_on)
        final_name = final_name + add_to_final
        if add_to_final != []:
            final_name += large_num(ln-n+1)
        work_on = []
    return ' '.join(final_name)

for _ in xrange(input()):
    print name_num(raw_input())