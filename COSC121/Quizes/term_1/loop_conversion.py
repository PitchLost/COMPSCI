'''Docstring'''
def print_names2(people):
    """Print a list of people's names, where each person's name
       is itself a list of names (first name, second name, etc).
    """
    index = 0
    while index < len(people):
        person = people[index]
        to_print = ""
        name_index = 0
        while name_index < len(person):
            to_print += person[name_index] + " "
            name_index += 1
        print(to_print)
        index += 1


print_names2([['John', 'Smith'], ['Mary', 'Keyes'], ['Jane', 'Doe']])
print_names2([['Bilbo', 'Baggins'], ['Gollum'], ['Tom', 'Bombadil'], ['Aragorn']])
