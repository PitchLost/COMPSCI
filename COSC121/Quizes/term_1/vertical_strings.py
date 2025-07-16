'''
Write a procedural function vertical_strings(string) that takes a 
string as a parameter and prints each letter of the string on a new line. 
Each letter is repeated for the length of the word (for example: given a 
three letter word each letter is printed three times).
'''

def vertical_strings(string): 
    '''This function takes a string as a parameter and prints each 
    letter of the string on a new line. Each letter is repeated for the 
    length of the word.'''
    for letter in string:
        print(letter * len(string))

vertical_strings('Hi')
vertical_strings('Pineapple')