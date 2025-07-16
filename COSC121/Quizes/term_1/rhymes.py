def rhymes(string_1: str, string_2: str, syllable: str) -> bool:
    '''
    Write a boolean-valued function rhymes(string_1, string_2, syllable) 
    that takes three non-empty string parameters and returns True if both 
    string_1 and string_2 contain syllable, except if string_1 is equal to string_2 
    in which case the function returns False. In all other cases the function 
    returns False.
    '''
    if string_1 == string_2:
        return False

    return syllable in string_1 and syllable in string_2

print(rhymes("flubber", "blubber", "lubber"))
print(rhymes("flubber", "flubber", "lubber"))
print(rhymes("flubber", "feast", "lubber"))
print(rhymes("broke", "blubber", "lubber"))