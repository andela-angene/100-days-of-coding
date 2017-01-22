def not_bad(strg):
    n,b = [False, False]
    for i in xrange(len(strg)):
        if strg[i] == 'not' and n == False:
            n = i
        if (strg[i] == 'bad' and n != False) and b == False:
            b = i
    if n != False and b != False:
        return ' '.join(strg[:n]) + ' good ' + ' '.join(strg[(b+1):])
    else:
        return ' '.join(strg)
    
print not_bad(raw_input().split())