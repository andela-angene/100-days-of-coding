# franko4don Jan 7th
# Challenge 4:
# Fibonacci Sequence - Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number. N:B the last last number in the sequence should be less than or equal to the input value

last_num = input('Enter max number: ')
a,b = [0,1]
lst = [a]
while b <= last_num:
    lst.append(b)
    b = b + a
    a = b - a
print lst