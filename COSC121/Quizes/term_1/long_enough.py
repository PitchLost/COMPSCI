'''
Write a function long_enough(strings, min_length) that returns a list of 
all the strings in the list strings with a length greater than or equal 
to the given min_length.
'''

def long_enough(strings, min_length):
    '''Function to determine what strings are larger or equal to min_length'''
    long_enough_list = []
    for string in strings:
        if len(string) >= min_length:
            long_enough_list.append(string)
    return long_enough_list

list_of_strings = ['a', 'bc', 'def', 'ghij', 'klmno']
print(long_enough(list_of_strings, 3))