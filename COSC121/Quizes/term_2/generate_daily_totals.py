'''Docstring
This bih does not work for some reason

'''
def generate_daily_totals(filename, totals):
    """Docstring"""
    infile = open(filename)
    outfile = open(totals, 'w')
    content = infile.read()
    lines = content.splitlines()
    total = 0
    for line in lines:
        split = line.split(',')
        numbers = split[1:]
        for i in range(len(numbers)):
            total += float(numbers[i])
        
        outfile.write(f"{split[0]} = {total:.2f} \n")
        # print(f'{split[0]} = {total:.2f}')
        total = 0
    infile.close()
    outfile.close()



generate_daily_totals('data.txt', 'results.txt')
