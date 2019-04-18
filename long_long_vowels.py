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

# goes through each letter in the word
for letter in word:
    # checks if the current letter is duplicated
    if previous_letter == letter:
        #if it is we will multiply it 4 times because it is added once previously
        new_word += letter * 4
    else:
        #if the letter wasnt duplicate, add it anyway
        new_word += letter
    # before we go to the next letter, we change the previous letter to the current one 
    previous_letter = letter

print(new_word)