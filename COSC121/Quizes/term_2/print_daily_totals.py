'''Docstring
This bih does not work for some reason

'''
def print_daily_totals(filename):
    """Docstring"""
    infile = open(filename)
    content = infile.read()
    lines = content.splitlines()
    total = 0
    for line in lines:
        split = line.split(',')
        numbers = split[1:]
        for i in range(len(numbers)):
            total += float(numbers[i])
        print(f'{split[0]} = {total:.2f}')
        total = 0



print_daily_totals('data.txt')
