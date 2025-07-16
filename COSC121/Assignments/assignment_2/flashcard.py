"""Flashcard Deck Manager"""
import json
import glob 
import copy 
import os
from datetime import datetime
from datetime import timedelta

FMT_DATE = "%Y/%m/%d"
FMT_ROW = "{:10} {:>4} {:>4} {:>4}"

def read_deck(f):
    '''Docstring'''
    with open(f, encoding='utf-8') as d:
        data = json.load(d)
    for x in data:
        if x["due"]:
            x["due"] = datetime.strptime(x["due"], FMT_DATE)
    return data

def write_deck(f, data):
    '''Docstring'''
    temp = copy.deepcopy(data)
    for x in temp:
        if x["due"]:
            x["due"] = x["due"].strftime(FMT_DATE)
    with open(f, "w", encoding='utf-8') as d:
        json.dump(temp, d, indent=4)

def deck_files():
    '''Docstring'''
    return sorted(glob.glob("*.json"))

def user_prompt(opts):
    '''Docstring'''
    def ask():
        for i, x in enumerate(opts):
            print(f"{i}: {x}")
        try:
            n = int(input("enter a number: "))
        except ValueError:
            return None
        return n if 0 <= n < len(opts) else None

    while (sel := ask()) is None:
        print("Invalid selection")
    return sel

def select_deck():
    '''Docstring'''
    files = deck_files() + ["Back"]
    n = user_prompt([x.rsplit('.', 1)[0] for x in files])
    if n == len(files) - 1:
        return
    deck = read_deck(files[n])
    run_test(deck)
    write_deck(files[n], deck)

def due_cards(cards):
    '''Docstring'''
    lst = []
    for i, x in enumerate(cards):
        if x["due"] is None or x["due"] <= datetime.today():
            lst.append(i)
    return lst

def run_test(cards):
    '''Docstring'''
    lst = due_cards(cards)
    print(f"You have {len(lst)} to translate today")
    for i in lst:
        x = cards[i]
        print(f"{x['lang1']}: {x['term1']}")
        a = input(f"{x['lang2']}: ")
        ans = x['term2']
        if a.casefold() == ans.casefold():
            print("Correct")
            x["streak"] += 1
            x["due"] = datetime.today() + timedelta(days=2**(x['streak'] - 1))
        else:
            print("Incorrect\nAnswer: " + ans)
            x["streak"] = 0
            x["due"] = datetime.today()

def overview():
    '''Docstring'''  
    today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
    print(FMT_ROW.format("", "New", "Due", "Done"))

    for name in deck_files():
        new = due = done = 0
        for x in read_deck(name):
            if x['due'] is None:
                new += 1
            elif x['due'].replace(hour=0, minute=0, second=0, microsecond=0) <= today:
                due += 1
            else:
                done += 1
        print(FMT_ROW.format(name.rsplit('.', 1)[0], new, due, done))
    print('')

def make_card(l1, t1, l2, t2):
    '''Docstring'''
    return {'due': None, 'lang1': l1.strip(), 'term1': t1.strip(),
            'lang2': l2.strip(), 'term2': t2.strip(), 'streak': 0}

def create_deck():
    '''Docstring'''
    f = input('File name: ')
    try:
        with open(f, 'r', encoding='utf-8') as d:
            lines = d.readlines()
    except FileNotFoundError:
        print("File not found.")
        return
    if not lines:
        print("File is empty.")
        return

    h = lines[0].strip().split(',')
    if len(h) != 2:
        print("Header must contain exactly two languages.")
        return

    dname = input(f"Deck name [{os.path.splitext(f)[0]}]: ").strip() or os.path.splitext(f)[0]
    l1 = input(f"Language one [{h[0]}]: ").strip() or h[0]
    l2 = input(f"Language two [{h[1]}]: ").strip() or h[1]
    mode = user_prompt(["Forward", "Reverse", "Bidirectional"])
    cards = []

    for line in lines[1:]:
        if ',' in line:
            t1, t2 = line.strip().split(',', 1)
            if mode == 0:
                cards.append(make_card(l1, t1, l2, t2))
            elif mode == 1:
                cards.append(make_card(l2, t2, l1, t1))
            elif mode == 2:
                cards.append(make_card(l1, t1, l2, t2))
                cards.append(make_card(l2, t2, l1, t1))

    with open(dname + '.json', 'w', encoding='utf-8') as d:
        json.dump(cards, d, indent=4)

    print(f"Deck {dname} Created ({len(cards)} Terms)")

def main():
    '''Docstring'''
    while True:
        i = user_prompt(["Study", "Overview", "Create Deck", "Quit"])
        if i == 0:
            select_deck()
        elif i == 1:
            overview()
            user_prompt(["Back"])
        elif i == 2:
            create_deck()
        else:
            print("Bye!")
            return

main()