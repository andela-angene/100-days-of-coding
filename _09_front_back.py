def split_word(word):
    ln = int(len(word)/2)
    if len(word) % 2 == 0:
        return [word[:ln], word[ln:]]
    else:
        return[word[:(ln + 1)], word[(ln + 1):]]

def front_back(two_words):
    a_front, a_back = split_word(two_words[0])
    b_front, b_back = split_word(two_words[1])
    return a_front + b_front + a_back + b_back

print front_back(raw_input('Enter two words separated by a space: ').split())