'''
Write a function max_num_in_file(filename) that returns the largest integer 
found in the file (as an integer). The file contains only numbers and has 
one number per line. The file will contain at least one line.
'''

def max_num_in_file(filename):
    '''Function'''
    infile = open(filename, 'r')
    content = infile.readlines()
    ans = int(content[0])
    for number in content:
        number = int(number)
        if number > ans:
            ans = number
    return ans

print(max_num_in_file('Tests/max_num_in_file_test_01.txt'))