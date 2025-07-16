'''Docstring'''

def num_rushes(slope_height, rush_height_gain, back_sliding):
    '''Docstring'''
   
    if rush_height_gain <= back_sliding:
        return "Impossible" 

    rushes = 0
    current_height = 0

    while current_height < slope_height:
        rushes += 1
        current_height += rush_height_gain  
        if current_height >= slope_height:
            break 
        current_height -= back_sliding 

    return rushes

ans = num_rushes(100, 10, 0)
print(ans)
