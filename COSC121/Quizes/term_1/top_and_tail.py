'''Write a function top_and_tail(string) that takes a string as a 
parameter and returns the string with its first and last characters removed. 
You may assume the string has at least one character in it.
'''

def top_and_tail(string):
    '''This function takes a string as a parameter and returns 
    the string with its first and last characters removed.'''
    return string[1:-1]


print(top_and_tail('stubby'))
print(top_and_tail('another test string'))