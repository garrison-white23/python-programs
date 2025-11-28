print()
print('''-------- The Game  of --------         
▄▄      ▄▄    ▄▄     ▄▄▄▄▄▄             
██      ██   ████    ██▀▀▀▀██           
▀█▄ ██ ▄█▀   ████    ██    ██           
 ██ ██ ██   ██  ██   ███████            
 ███▀▀███   ██████   ██  ▀██▄           
 ███  ███  ▄██  ██▄  ██    ██           
 ▀▀▀  ▀▀▀  ▀▀    ▀▀  ▀▀    ▀▀▀                                                   
''')


############################################################
############### FUNCTIONS / DECK ELEMENTS ##################
############################################################
import random

def comparecards(a, b):
    if a > b:
        result = 1
    elif b > a:
        result = 2
    else:
        result = 3
    return result

def displaydecks():
    print("User:")
    for card in userdeck:
        print(f"{card['rank']} {card['suit']}", end = ', ')
    print("\n")
    print("Computer:")
    for card in compdeck:
        print(f"{card['rank']} {card['suit']}", end = ', ')

def play_again():
    while True:
        playagain = input("[1]Play again\n[2]Quit\n>")
        if playagain == "1" or playagain == "2":
            break
        else: 
            print("\nInvalid response.\n")
    return playagain

def reshuffle():
    deck = []
    for suit in suits:
        for rank in ranks:
            card = {
                'rank': rank,
                'suit': suit,
                'value': values[rank],
            }
            deck.append(card)
    random.shuffle(deck)
    return deck

#Lists for card attributes: suite and rank
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

#Dictionary to associate card ranks with numeric value
values = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 11, 'Q': 12, 'K': 13, 'A': 14
}


deck = reshuffle()
pile = []

userdeck = []
compdeck = []
for i in range (26):
    userdeck.append(deck.pop())
    compdeck.append(deck.pop())

print("Press 'enter' to play a card")
print(f"\n\nPlayer:\t\t Computer:")
while True:
    pile = []
    input()
    usercard = userdeck.pop()
    pile.append(usercard)
    compcard = compdeck.pop()
    pile.append(compcard)

    result = comparecards(usercard['value'], compcard['value'])

    print("\n------------------------------")
    print(f"{usercard['rank']} {usercard['suit']:<15}{compcard['rank']} {compcard['suit']}")
    
    
    random.shuffle(pile)
    if result == 1:
        for card in pile:
            userdeck.insert(0, card)
        print(f"\n+1\nDeck:{len(userdeck)}")
    elif result == 2:
        for card in pile:
            compdeck.insert(0, card)
        print(f"\n-1\nDeck:{len(userdeck)}")
    else:
        while result == 3:
            random.shuffle(pile)
            print("\t*** WAR ***\nPress enter to commence war...\n")
            for x in range(3):
                pile.append(userdeck.pop())
                pile.append(compdeck.pop())
            usercard = userdeck.pop()
            compcard = compdeck.pop()
            pile.append(usercard)
            pile.append(compcard)

            result = comparecards(usercard['value'], compcard['value'])

            for x in range(3):
                input()
                print("[Face down]      [Face down]")
            input()
            print(f"{usercard['rank']} {usercard['suit']:<15}{compcard['rank']} {compcard['suit']}")
        if result == 1:
            print(f"\n+{len(pile)/2}\n")
            for card in pile:
                userdeck.insert(0, card)
            print(f"Deck:{len(userdeck)}")
        else:
            print(f"\n-{int(len(pile)/2)}\n")
            for card in pile:
                compdeck.insert(0, card)
            print(f"Deck:{len(userdeck)}")
            
            
    
    if len(userdeck) == 0 or len(compdeck) == 0:
        break

print("\n\n")

if len(compdeck) == 0:
    print("You win!")
else:
    print("You lose!")






