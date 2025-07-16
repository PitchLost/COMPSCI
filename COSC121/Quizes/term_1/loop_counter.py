'''
Write a function print_integers_in_range(start, stop) that prints 
every integer from start up to - and including - stop, as shown in 
the For example table below.

You may assume that stop will always be greater than start.
'''

def print_integers_in_range(start, stop):
    '''Docstring'''
    for i in range(start, stop+1):
        print(i)

print_integers_in_range(1, 5)
print_integers_in_range(-5, 5)