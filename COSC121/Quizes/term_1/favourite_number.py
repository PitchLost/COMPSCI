def favourite_number():
    """Prints silly messages about favourite numbers"""
    num = int(input("What's your favourite number? "))
    if    num == 2:
        print("That's my favourite too!")
    if    num < 0:
        print("That's a bit negative, don't you think?")
    elif  num < 10:
        print("Aw, what a cute little number.")
    elif  num >= 50:
        print("Wow, what a big number!")
    if    num % 2 == 1:
        print("What an odd number.")
    else :
        print("Even better!")
    print("I can see why it's your favourite.")

favourite_number()