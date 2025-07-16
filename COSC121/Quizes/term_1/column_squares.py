'''Docstring'''

def column_sums(square):
    '''Docstring'''
    num_columns = len(square[0]) 
    col_totals = [0] * num_columns  

    for row in square:
        for col_index in range(num_columns):
            col_totals[col_index] += row[col_index] 

    return col_totals
