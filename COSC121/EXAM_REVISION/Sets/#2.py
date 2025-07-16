'''Take two lists of words and return a sorted list of all the words that: 
1. Appear in both lists (Case insensitive)
2. Are at least 5 char long
3. Do not contain the letter e
'''
def common_words_filter(a, b):
    # Using a set
    for i in a, b:
        for idx, k in enumerate(i): 
            i[idx] = k.lower()
    common = set(a).intersection(set(b))
    print('Set is:', common)
    return_set = []
    # Now perform our checks
    for i, word in enumerate(list(common)):
        letters = [*word]
        if 'e' in letters or len(letters) < 5:
            continue
        return_set.append(word)
    return return_set
        
        
list1 = ["banana", "Apple", "mango", "Cherry", "plum", "fig", "grape", "grapefruit"]
list2 = ["BANANA", "grapefruit", "kiwi", "Mango", "fig", "Peach", "apricot"]
print(common_words_filter(list1, list2))