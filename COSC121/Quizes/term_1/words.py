'''Docstring'''

def set_lowercase(strings):
    for i in range(len(strings)):
        strings[i] = strings[i].lower()


words = ['Right', 'SAID', 'Fred']
set_lowercase(words)
print(words)