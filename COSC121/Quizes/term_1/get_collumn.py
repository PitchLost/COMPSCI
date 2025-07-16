'''Docstring'''

def get_column(game, col_num):
    '''Doctring'''
    return [game[row][col_num] for row in range(3)]


board = [['O', 'X', 'O'],
         ['X', ' ', ' '],
         ['X', ' ', ' ']]
column2 = get_column(board, 2)
print(column2)