'''Docstring'''

def diagonals(game):
    """Returns the two diagonals of a 3x3 tic-tac-toe board."""
    diagonal1 = [game[0][0], game[1][1], game[2][2]]  # Top-left to bottom-right
    diagonal2 = [game[0][2], game[1][1], game[2][0]]  # Top-right to bottom-left
    return (diagonal1, diagonal2)


board = [['O', 'O', 'O'],
         ['X', 'X', ' '],
         [' ', 'O', 'X']]
diags = diagonals(board)
print(diags)