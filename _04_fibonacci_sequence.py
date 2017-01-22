last_num = input()
a,b = [0,1]
lst = [a]
while b <= last_num:
    lst.append(b)
    b = b + a
    a = b - a
print lst