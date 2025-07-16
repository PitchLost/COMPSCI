'''
Write a function lower_case(strings) which takes a list of strings 
as a parameter and returns a list of those strings converted to 
lower case. Your code must not modify the original list.
'''

def lower_case(strings):
    '''Docstring'''
    lower_string_list = []
    for string in strings:
        lower_string_list.append(string.lower())
    return lower_string_list