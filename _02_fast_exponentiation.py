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

print fast_expon(raw_input())