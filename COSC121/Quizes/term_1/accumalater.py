'''
Use the accumulator pattern to write a function concatenate(strings) that 
takes a list of strings as a parameter and returns a single string formed by 
concatenating all the strings. 
'''

def concatenate(strings):
    '''Docstring!'''
    return_string = ''
    for string in strings:
        return_string = return_string + string
    return return_string

print(concatenate(["x", "yy", "zzz"]))