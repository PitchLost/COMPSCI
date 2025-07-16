'''Docstring'''

def row_sums(square):
    '''Docstring'''
    row_totals = []
    for row in square:
        total = 0
        for num in row:
            total += num
        row_totals.append(total)
    return row_totals


bigger_square = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
print(row_sums(bigger_square))