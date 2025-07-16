'''
Write a function funny(strings) which takes a list of strings as a 
parameter and modifies that list by replacing each string with 
the title-case version of itself AND filling up any strings that 
have less than 5 characters with enough '#' characters to make 
them exactly 5 characters long.

Title case means that the first letter of each word is uppercase and 
the rest lower-case.
'''

def funny(strings):
    funny_strings = []
    for string in strings: 
        if len(string.split()) < 5:
     
        funny_strings.append(string.title())
        