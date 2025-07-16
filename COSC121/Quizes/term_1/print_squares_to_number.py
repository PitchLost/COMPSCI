'''
Write a function print_squares_to_number(number) that takes a single positive integer 
and prints a table of all integers and their squares from 1 up to and including number.

The program should print the error message ERROR: number must be at least 1 when number is 
less than 1.
'''

def print_squares_to_number(number):
    '''Docstring'''
    if number < 1:
        print('ERROR: number must be at least 1')
    else:
        for i in range(1, number+1):
            print(f'{i} * {i} = {i**2}')


print_squares_to_number(5)
print_squares_to_number(3)
print_squares_to_number(0)
