'''Docstring'''

def print_cumulative_items(items):
    """Prints the first item on a line by itself, then on 
       the next line the first two items separated by a space, etc
       until all items in the list are printed on a single
       line separated by spaces."""
    index = 0
    output = ""
    while index < len(items):
        output += items[index] + " "
        print(output)
        index += 1




print_cumulative_items(['John', 'Mary', 'Donald'])
print_cumulative_items(['Victor'])