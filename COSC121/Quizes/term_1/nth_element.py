'''
Write a function that takes a list and an i
nteger as arguments and returns the nth element 
of the list.'''

def nth_element(data, pos):
    '''Return the nth element of a list'''
    return data[pos]

nth_element([1, 2, 3, 4, 5], 2)  # 3
nth_element([1, 2, 3, 4, 5], 4)  # 5
nth_element([1, 2, 3, 4, 5], -1)  # 1