words = raw_input().split()
pig_latin = []
for word in words:
    pig_latin.append(word[1:] + word[0] + 'ay')
print ' '.join(pig_latin)