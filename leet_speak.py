# Version 1

'''
leet_this = (input('Type in anything: ')).upper()
leet_result = ''

for letter in leet_this:
    print(letter)
    if letter == 'A':
        leet_result += '4'
    elif letter == 'E':
        leet_result += '3'
    elif letter == 'G':
        leet_result += '6'
    elif letter == 'I':
        leet_result += '1'
    elif letter == 'O':
        leet_result += '0'
    elif letter == 'S':
        leet_result += '5'
    elif letter == 'T':
        leet_result += '7'
    else:
        leet_result += letter

print(leet_result)
'''

# Version 2 - Use of replace

leet_this = (input('Type in anything: ')).upper()
alpha_to_leet =   ['A','E','G','I','O','S','T']
leet_characters = ['4','3','6','1','0','5','7']

for i in range(len(alpha_to_leet)):
    leet_this = leet_this.replace(alpha_to_leet[i],leet_characters[i])

print(leet_this)