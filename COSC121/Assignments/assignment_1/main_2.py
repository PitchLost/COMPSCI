'''Hello World!'''        
def get_translations(translations): 
    """Extract translations from a string and return a list of tuples."""
    lines = translations.splitlines()
    translations_list = [tuple(line.split(',')) for line in lines]

    # Ensure there is at least a header and one translation
    if len(translations_list) < 2:
        return "Invalid input format!"

    translations_order = translations_list.pop(0)

    # Validate headers
    valid_headers = {"māori", "english"}
    if set(translations_order) !=    valid_headers:
        print("Header language not recognized!")
        return []

    # Reverse order if needed
    if translations_order == ("māori", "english"):
        translations_list = [(eng, maori) for maori, eng in translations_list]

    return translations_list


# Get strings from file
def get_translations_from_file(filename):
    '''Get the list of translations from text file'''
    infile = open(filename, 'r', encoding='utf-8')
    content = infile.read()
    infile.close()
    return get_translations(content)
    

# Answer mask
def answer_mask(reo, attempt):
    '''Return a hint of the answer, not the actual answer'''
    hidden_ans = []
    
    for i, char in enumerate(reo):
        if i < len(attempt) and char.lower() == attempt[i].lower():
            hidden_ans.append('*')
        else:
            hidden_ans.append(reo[i])
    
    return ''.join(hidden_ans)



def main():
    '''Translater quiz program'''
    filename = input('Please enter a filename: ')
    translations = get_translations_from_file(filename)
    len_translations = len(translations)
    
       # Early exit function if translations were not valid
    if len_translations < 1:
        print("We can't play, hōhā!")
        return -1

    # Game logic
    print("Kia ora, you have", len_translations,"terms to translate today :-)")

    # Init the score var
    score = 0

    # Game loop
    for translation in translations:
        print('en:', translation[0])
        users_response =input('mi: ')

        if users_response.lower() == translation[1].lower():
            print('Ka pai')
            score += 1
        else:
            print(f"A: {answer_mask(translation[1], users_response)}")
            translations.append(translation)

    # Calc score percent
    final_score = score / len(translations) * 100
    print('You translated all the terms!')
    print(f"You scored {final_score:.2f}%")


main()


        