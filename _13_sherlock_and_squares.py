def find_squares(ls):
    a,b = map(int, ls)
    min_sq = int(a**0.5)
    sq = min_sq**2
    n = 0
    while sq <= b:
        if sq >= a and sq <= b:
            n += 1
        min_sq += 1
        sq = min_sq**2
    return n

for _ in range(input()):
    print find_squares(raw_input().split())