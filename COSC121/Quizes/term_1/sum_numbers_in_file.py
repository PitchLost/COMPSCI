'''Define the function sum_numbers_in_file(filename) that reads all the numbers in a file and 
returns the sum of the numbers. You can assume that the files contain only integers, 
that there is one integer per line in the file and that files contain at least one line.'''

def sum_numbers_in_file(filename):
    '''Function '''
    infile = open(filename, 'r')
    content = infile.readlines()
    ans = 0
    for number in content:
        number = int(number)
        ans += number
    return ans


print(sum_numbers_in_file('Tests/sum_nums_test_01.txt')) # 186