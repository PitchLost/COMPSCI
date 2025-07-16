'''
Define a function print_numbered_lines(filename) that reads from 
the file with the given name and prints out all the lines of the 
file with the line number given at the start of each line 
followed by ': ' (colon and space) and then the contents of the 
line. Lines should be printed in the same order as in the file 
and the numbers should start from 1.
'''

def print_numbered_lines(filename):
    '''Function'''
    infile = open(filename, 'r')
    content = infile.readlines()
    for i, line in enumerate(content):
        line = line.rstrip('\n')
        print(f'{i+1}: {line}')

print_numbered_lines('Tests/marks1.txt')
print_numbered_lines('Tests/marks2.txt')