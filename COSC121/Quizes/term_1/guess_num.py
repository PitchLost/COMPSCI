'''Docstring'''

def guess_a_number(target_number, lower_bound, upper_bound, max_tries):
    '''Docstring'''
    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}.")
    
    tries = 0
    while tries < max_tries:
        # Ask the user for a guess
        guess = int(input('What do you think it is? '))
        
        if guess == target_number:
            print("Congratulations! That was my number!")
            break  # Exit the loop if the guess is correct
        else:
            print("That's not my number. Try again.")
            tries += 1  # Increment the number of tries
    
    # If the user runs out of tries, print a failure message
    if tries >= max_tries:
        print("Sorry, too many failed guesses.")