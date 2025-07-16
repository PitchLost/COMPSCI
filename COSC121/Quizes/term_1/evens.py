'''
Write a function evens(numbers) which takes a list of ints as a 
parameter and returns a new list containing just the even elements 
from numbers.
'''

def evens(numbers):
    '''Return a list of only even numbers'''
    list_of_evens = []
    for number in numbers:
        if number % 2 != 1:
            list_of_evens.append(number)

    return list_of_evens

print(evens([1, 2, 3, 4, 5, 6, 10, 11]))