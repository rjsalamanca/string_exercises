# Version 1 - Goes through ascii

"""

cipher = 'lbh zhfg hayrnea jung lbh unir yrnearq'.lower()
decoded = ''

for letter in cipher:
    #ord will get the character ascii number
    ascii_number = ord(letter)
    #checks for alphabets
    if letter.isalpha():
        #lower case ascii alphabet goes from 97-122 
        #109 is m ( the middle of the alphabet )
        if ascii_number < 109 :
            #chr will change the ascii number to a character
            decoded += chr(ascii_number+13)
        else:
            #alphabetical ascii only goes until 122
            #If we need to loop around to the beginning of the alphabet we need the remaining
            #amount we need to shift, then we add it to the beginning
            decoded += chr(97+(ascii_number+13-123))
    else:
        decoded += letter

print(decoded)

"""

# Version 2 - Goes through a list

"""
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
cipher = 'lbh zhfg hayrnea jung lbh unir yrnearq'
decoded = ''

for letter in cipher:
    if letter.isalpha():
        get_index_of_letter = alphabet.index(letter)
        if get_index_of_letter < 12:
            decoded += alphabet[get_index_of_letter+13]
        else:
            decoded += alphabet[get_index_of_letter+13-26]
    else:
        decoded += letter
print (decoded)
"""

# Version 3 - Use of make trans found on https://stackoverflow.com/questions/36367883/shift-n-letters-in-python

import string

def shift_n_letters(text, n):
    intab = string.ascii_lowercase # "abcdefghijklmnopqrstuvwxyz"
    outtab = intab[n % 26:] + intab[:n % 26] # alphabet shifted by n
    trantab = str.maketrans(intab, outtab) # translation made b/w patterns

    return text.translate(trantab) # text is shifted to right

cipher = 'lbh zhfg hayrnea jung lbh unir yrnearq'
print(shift_n_letters(cipher,13))