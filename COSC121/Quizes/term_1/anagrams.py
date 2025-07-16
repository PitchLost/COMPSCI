'''Two words are anagrams if they contains exactly the same letters but in a
 different order. Write a function are_anagrams(word1, word2) which returns 
 True if the two parameters are anagrams.
'''

def are_anagrams(word1, word2):
    '''This function takes two words as parameters and returns True if 
    the two words are anagrams.'''
    return not word1 == word2 and sorted(word1) == sorted(word2)

print(are_anagrams("looped", "poodle")) #True
print(are_anagrams("lopped", "poodle")) #False
print(are_anagrams("poodle", "poodle")) # False