'''
Write a function num_words(string) that takes a string argument and returns a 
count of the number of words in the string, where a word is defined as a 
maximal-length sequence of characters other than "white space" characters.

Note: You will need the split method of a string for your answer. 
(Remember that you can find out more about this method by typing help(str.split) 
into the shell.)
'''
def num_words(param):
    '''Return the number of words in a string'''
    return len(param.split())

print(num_words('This is a test'))  # 4
print(num_words('ggtty'))  # 5
print(num_words(''))  # 0
