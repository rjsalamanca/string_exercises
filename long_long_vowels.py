# Version 1

'''
word = input('Enter a word: ')
new_word = ''

for i in range(len(word)):
    #look for voels only
    if word[i] == 'a' or word[i] == 'e' or word[i] == 'i' or word[i] == 'o' or word[i] == 'u':
        #dont check the last letter because nothing is infront of it.
        if i < (len(word)-1):
            #check if next letter is repeated.
            if word[i] == word[i+1]:
                #only multipied by 3 because the current vowel and the next vowel is added by default
                new_word += word[i]*3
    new_word += word[i]

print(new_word)
'''

# Version 2 

word = input('Enter a word: ')
previous_letter = ''
new_word = ''

for letter in word:
    if previous_letter == letter:
        new_word += letter * 4
    else:
        new_word += letter
    previous_letter = letter

print(new_word)