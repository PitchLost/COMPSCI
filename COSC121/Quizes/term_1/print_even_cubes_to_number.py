'''
Write a function print_even_cubes_to_number(number) that takes a single integer 
nd prints a table of all the even integers and their cubes from 2 up to and 
including number.

The program should print the error message 'ERROR: number must be at least 2' 
when number is less than 2.
'''

def print_even_cubes_to_number(number):
    '''Docstring'''
    if number < 2: 
        print('ERROR: number must be at least 2')
    all_evens = []
    i = 1
    while i < number:
        if i % 2 == 0:
            all_evens.append(i)
        i += 1
    for even in all_evens:
        print(f"{even} * {even} * {even} = {even * even * even}")


print_even_cubes_to_number(10)