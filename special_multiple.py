def find_multiple(number):
    n = 1
    while True:
        multiple = 9*int(bin(n)[2:])
        if multiple % number == 0:
            return multiple
        n += 1

for _ in range(input()):
    print find_multiple(input())