'''Assignment #1'''


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


def get_translations_from_file(filename):
    infile = open(filename)
    content = infile.read()
    get_translations(content)

filename = 'places.txt'
for terms in get_translations_from_file(filename):
    print(terms)




# Game function

def reo_test(string):
    '''Game function'''

    # Now use the get_translations function to convert the string to a list of tuples
    translations = get_translations_from_file(string)
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
            print('A:',translation[1])

    # Calc score percent
    final_score = score / len_translations * 100
    return final_score