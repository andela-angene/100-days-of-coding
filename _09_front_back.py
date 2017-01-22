# boundlesslove Jan 12th
# CHALLENGE FOR TODAY: front_back
# Consider dividing a string into two halves. If the length is even, the front and back halves are the same length. If the length is odd, we'll say that the extra char goes in the front half. e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
# a-front + b-front + a-back + b-back     
# front_back('abcd', 'xy') SHOULD RETURN  'abxcdy'
# front_back('abcde', 'xyz')  SHOULD RETURN 'abcxydez'
# front_back('Kitten', 'Donut')  SHOULD RETURN 'KitDontenut')

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