'''Docstring'''
def print_daily_totals(rainfalls):
    '''Docstring'''
    for day_index, day in enumerate(rainfalls):
        total = 0 
        for rainfall in day:
            total += rainfall  
        print(f"Day {day_index} total: {total}")  


patchy_rain = [ 
      [1, 7, 9],
      [],
      [9, 1, 2],
      [10, 5],
      [20]
]
print_daily_totals(patchy_rain)