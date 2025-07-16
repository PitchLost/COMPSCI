'''Docstring'''
def print_nth_item_divided(data, n, divisor):
    '''Docstring'''
    try:
        print((data[n] / divisor))
    except IndexError:
        print('Invalid position provided.')
    except TypeError:
        print('Parameters must be numbers.')
    except ZeroDivisionError:
        print('Cannot divide by zero.')
    

def get_even_num():
    """gets an even number or throws an error if it's not even."""
    num_str = input("Enter an even number: ")
    num = int(num_str)
    if num % 2 != 0:
        raise ValueError(f'{num} is not even!') # Raise a ValueError here.
        print("This line should never execute. Did you forget to raise an exception?")
    else:
        return num



get_even_num()