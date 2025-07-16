'''
Define a function my_enumerate(items) that behaves in a similar way to the built-in 
enumerate function. It should return a list of tuples (i, item) where item is the 
ith item, with 0 origin, of the list items (see the examples below). Check the 
test cases for how the function should work. Your function must not call 
python's inbuilt enumerate function.'''

def my_enumerate(items):
    '''Docstring'''
    return_list = []
    for i in range(len(items)):
        item = items[i]
        return_list.append((i, item))
    return return_list
    

ans = my_enumerate([10, 20, 30])
print(ans)