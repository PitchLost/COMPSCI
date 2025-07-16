'''
Find a value to enter into silly() so it prints:
4
[5, 3, 1, 5, -3]
'''

def silly(stuff, more_stuff=None):
    data = [] # Create the empty list
    for i, thing in enumerate(stuff): # for index, value in 
        if thing >= 0 or i < 2:
            data.append(thing + i)
    print(len(stuff))
    if more_stuff is not None:
        data += more_stuff
    print(data)

silly()