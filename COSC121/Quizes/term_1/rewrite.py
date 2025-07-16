'''Docstring'''

def truncated(values):
    '''Docstring'''
    value_limit = 50
    result = []
    
    i = 0
    while i < len(values):

        item = values[i]
        if item > value_limit:
            item = value_limit
        result.append(item)
        i+= 1
    return result
print(truncated([20, 100, 30, 10, 4, 200]))
print(truncated([1, 2, 3]))


def truncated_old(values):
    """Mystery exam function :-) """
    value_limit = 50
    result = []
    for item in values:
        if item > value_limit:
            item = value_limit
        result.append(item)
    return result