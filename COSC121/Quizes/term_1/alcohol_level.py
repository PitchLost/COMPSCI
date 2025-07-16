'''
Hello World!
'''

def main():
    '''
    Hello World!
    '''
    alcohol_level = float(input("Enter blood alcohol level (mg/100ml): "))
    age = int(input("Enter age in years: "))

    if age < 20 and alcohol_level > 0:
        print("You're not allowed to drive")
    elif alcohol_level >= 50:
        print("You're not allowed to drive")
    elif 30 <= alcohol_level < 50:
        print("You're legally allowed to drive, but please don't")
    else:
        print("You're allowed to drive")

main()