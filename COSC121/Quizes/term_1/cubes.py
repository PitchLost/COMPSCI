'''
Using the mapped list pattern, write a function cubes(data) that 
takes a list of numbers as an argument and returns a list of the 
cubes of all those numbers. Your code must not modify the original 
list
'''

def cubes(data):
    '''
    Function docstring
    '''
    cube_list = []
    for number in data:
        cube_list.append(number * number * number)
    return cube_list
# Tests
cubes_list = cubes([1, 2, 4])
print(cubes_list)

cubes_list = cubes([5])
print(cubes_list)