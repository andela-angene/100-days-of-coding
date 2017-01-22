# boundlesslove Jan 9th
# TODAY'S CHALLENGE IS PIG LATIN - Pig Latin is a game of alterations played on the English language game. To create the Pig Latin form of an English word the initial consonant sound is transposed to the end of the word and an ay is affixed (Ex.: "banana" would yield anana-bay). Read Wikipedia for more information on rules. https://en.wikipedia.org/wiki/Pig_Latin  ....SUBMISSION OF SOLUTION IS BY 7PM NIGERIAN TIME. HaPpY CodiNg
# Wikipedia
# Pig Latin
# Pig Latin is a language game in which words in English are altered. The objective is to conceal the words from others not familiar with the rules. The reference to Latin is a deliberate misnomer, as it is simply a form of jargon, used only for its English connotations as a strange and foreign-sounding language.

words = raw_input().split()
pig_latin = []
for word in words:
    pig_latin.append(word[1:] + word[0] + 'ay')
print ' '.join(pig_latin)