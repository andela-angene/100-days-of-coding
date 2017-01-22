def prime_factors(num):
    i = 2
    ls = []
    while num > 1:
        if num % i == 0:
            ls.append(i)
            num = num / i
            i = 1
        i += 1
    return ls

print prime_factors(input('Enter a number: '))