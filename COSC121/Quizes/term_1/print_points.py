'''
Write a function print_points(point_tuples) that takes a list of (x, y) 
tuples of points and prints each point in the format 
"Point {position in list}: x = {x value}, y = {y value}".
'''
def print_points(point_tuples):
    '''Docstring'''
    for i, (x, y) in enumerate(point_tuples):
        print(f"Point {i}: x = {x}, y = {y}")


points = [(0, 0), (1, 2), (2, 5), (4, 6)]
print_points(points)