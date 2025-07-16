'''
Write a function copy_last(data) that takes a list as a 
parameter and returns a new list containing all the elements 
of the parameter data but with the last item appearing twice. 
Your function should not modify the list it is given.
'''
def copy_last(data):
    '''Why do we need so many bloody docstrings???!!!??!!'''
    new_list = data.copy()
    new_list.append(data[-1])
    return new_list

# Tests:
print(copy_last([1, 2, 3, 4, 5]))
print(copy_last([5, 2, 4, 6]))
print(copy_last(['Hello', 'World', 'Python!']))