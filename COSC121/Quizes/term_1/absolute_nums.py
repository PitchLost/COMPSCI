'''
Write a function absolute_nums(numbers) that takes a list of numbers as a parameter 
and returns a list of the absolute values of those numbers. Your code must not 
modify the original list.
'''

def absolute_nums(numbers):
    '''Docstring'''
    absolute_nums_list = []
    for number in numbers:
        if number < 0:
            absolute_nums_list.append(number * -1)
        else: 
            absolute_nums_list.append(number)
    return absolute_nums_list

print(absolute_nums([2, -3, -7]))