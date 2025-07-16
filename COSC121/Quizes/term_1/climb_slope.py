'''Docstring'''

def num_rushes(slope_height, rush_height_gain, back_sliding):
    '''Docstring'''
    
   
    if rush_height_gain <= back_sliding:
        return "Impossible"  

    rushes = 0
    current_height = 0
    current_rush_height = rush_height_gain
    current_back_sliding = back_sliding

    while current_height < slope_height:
        rushes += 1
        current_height += current_rush_height  # Rush up the slope

       
        if current_height >= slope_height:
            break
        
        # After the rush, slide back
        current_height -= current_back_sliding

        # Apply the 5% reduction for the next rush
        current_rush_height *= 0.95
        current_back_sliding *= 0.95

    return rushes



ans = num_rushes(100, 15, 7)
print(ans)