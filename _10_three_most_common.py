inpt = raw_input()
letter_dict = {}
for i in xrange(len(inpt)):
    letter = inpt[i]
    if letter in letter_dict:
        letter_dict[letter] += 1
    else:
        letter_dict[letter] = 1
count = 0
while count < 3:
    k = letter_dict.keys()
    v = letter_dict.values()
    max_k = k[v.index(max(v))]
    print max_k + ' ' + str(letter_dict[max_k])
    del letter_dict[max_k]
    count += 1