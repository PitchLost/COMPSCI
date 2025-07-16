def find_first(value, data):
    """Return the index of the first occurrence of item in data or -1 if not found."""
    for i in range(0, len(data)):
        if value == data[i]:
            return i
        

test = [ 
    'Apple',
    'Dog',
    'Cat',
    'Frog',
    'Water'
]
print(find_first(1, [ 
    'Apple',
    'Dog',
    'Cat',
    'Frog',
    'Water'
]))

