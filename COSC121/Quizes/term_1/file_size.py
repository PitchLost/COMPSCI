'''
Write a function file_size(filename) that returns a 
count of the number of characters in the file whose 
name is given as a parameter. You may assume that 
when being tested in this CodeRunner question your 
function will never be called with a non-existent filename.
'''

def file_size(filename):
    '''Function'''
    infile = open(filename, 'r')
    content = infile.read()
    return len(content)


print(file_size('Tests/data.txt'))