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