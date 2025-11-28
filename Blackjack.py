#   BLACKJACK 
#   Author: Garrison White
#   Date: 10/11/2025
#   Description: Simple blackjack game using lists and dictionaries.

print('''
=======================================================================
                                                                   
     ▄▄▄▄▄  ▀▀█                  █         ▀                 █     
     █    █   █     ▄▄▄    ▄▄▄   █   ▄   ▄▄▄    ▄▄▄    ▄▄▄   █   ▄      
     █▄▄▄▄▀   █    ▀   █  █▀  ▀  █ ▄▀      █   ▀   █  █▀  ▀  █ ▄▀  
     █    █   █    ▄▀▀▀█  █      █▀█       █   ▄▀▀▀█  █      █▀█   
     █▄▄▄▄▀   ▀▄▄  ▀▄▄▀█  ▀█▄▄▀  █  ▀▄     █   ▀▄▄▀█  ▀█▄▄▀  █  ▀▄ 
                                           █                       
                                         ▀▀     
======================================================================
''')

import random

def main():
    startingwallet = 0     
    playagain = welcome()          
    if playagain == "1":
        wallet, startingwallet = starting_balance()
    while playagain == "1":
        wallet, startingwallet = gameplay(wallet, startingwallet)
        if wallet == 0:
            break
        playagain = play_again()
    if startingwallet > 0:
        closing_statement(wallet, startingwallet)
    else:
        print("\nGoodbye!")
        
    print(input('\n\nHit Enter to Close\n'))


#Create/shuffle 52 card deck when game starts, and whenever the deck runs out.
#Lists for suits and ranks are iterated through to make 13 cards of each suit.
#Each card is its own dictionary storing 3 elements for rank, suit, and value.
def reshuffle():
        
    suits = ['♥', '♦', '♣', '♠']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    values = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
        'J': 10, 'Q': 10, 'K': 10, 'A': 11}
    
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

        
#Calculate numeric running total of player/dealer hands
def calculate_hand_value(hand):                                                         
    total = sum(card['value'] for card in hand)
    num_aces = sum(1 for card in hand if card['rank'] == 'A')
    while total > 21 and num_aces > 0:
        total -= 10  #For every ace that puts hand total over 21, change to equal 1
        num_aces -= 1
    return total  


def welcome():
    playagain = ""
    while playagain not in ["1", "2"]:
        playagain = input("[1]Play\n[2]Quit\n[3]Rules\n\n>")

        if playagain in ["1", "2"]:
            break

        elif playagain == "3":
            print('''\n\t\t\t--- Welcome to Blackjack! ---\n
The goal of Blackjack is to get as close to 21 as possible without going over.
At the start of each hand, you’ll place a bet. You and the dealer will each be
dealt two cards. You’ll only see one of the dealer’s cards. Cards 2–10 are worth
their face value, face cards (Jack, Queen, King) are worth 10, and Aces are
worth 1 or 11 — whichever helps your hand most. On your turn, press 1 to Hit (get
another card) or 2 to Stay (end your turn). If your hand goes over 21, you bust
and lose the round. Once you stay, the dealer plays. Whoever has the higher hand
without going over 21 wins. Good luck!
    ''')

        else:
            print("\nInvalid response.\n")

    return playagain


#Player chooses how much money to start with
def starting_balance():
    while True:
        startingwallet = int(input("How much money did you bring to the casino?\n$"))

        if startingwallet > 0:
            break

        else:
            print("\nCannot play without any money!")
                
    wallet = startingwallet
    return wallet, startingwallet


def gameplay(wallet, startingwallet):
    
    plays = 0
    if plays == 0: 
        deck = reshuffle()
        
    #Deal hands - Create empty lists for player and dealer, add 2 cards to each
    playerhand = []
    dealerhand = []
    for i in range(2):
        playerhand.append(deck.pop())
        if len(deck) == 0:
            print("*Re-shuffling*")
            deck = reshuffle()
        dealerhand.append(deck.pop())
        if len(deck) == 0:
            print("*Re-shuffling*")
            deck = reshuffle()

    #'move' is the player's option to (1)hit or (2)pass on a hand.
    #'hits' is the total number of  times player chooses to hit on a hand.
    move = "1"
    hits = 0
    print("\n\n\n\n\n")


    ############### BETTING STAGE ###############
    
    print(f'''
=========================
Balance: ${wallet:,}
=========================''')

    #Player must bet at least $1
    while True:
        bet = int(input(f"Place bet: $"))
        if 0 < bet <= wallet:
            break
        else:
            print(f"\nInvalid amount. You have ${wallet:,}.")

        
    ############### PLAY HAND ###############

    while move == "1":

        #Add card to players hand after a hit
        if hits > 0:
            playerhand.append(deck.pop())
            if len(deck) == 0:
                print("*Re-shuffling*")
                deck = reshuffle()
        playervalue = calculate_hand_value(playerhand)

        #Hands are revealed and player can hit or stay. Loop breaks if player busts, or gets a blackjack
        print("-"*25)
        print("Dealer's  hand:\n")
        for card in dealerhand:
            print(f"{card['rank']}{card['suit']}")
            break
        print("-"*25)
        print(f"Your Hand ({playervalue}):\n")
        for card in playerhand:
            print(f"{card['rank']}{card['suit']}")
        print("-"*25)

        #Check if player got a blackjack
        if playervalue == 21 and hits == 0:
            break
        #Check if player busted
        if playervalue > 21:
            break

        #Ask player to hit or stay
        while True:
            print("[1]Hit\n[2]Stay")
            move = input("\n>")
            if move == "1" or move == "2":
                print("\n\n\n\n\n")
                break
            else:
                print("\nInvalid response.\n")
        
        if move == "1":
            hits += 1
    
    ############### DETERMINE WINNER ###############
    #*** 2 possible ways to exit gameplay loop WITHOUT selecting stay: ***
        
    #(1) Player busted:
    if playervalue > 21:
        wallet -= bet
        print(f"Bust! (-${bet:,})")

            
    #(2) Player got a Blackjack:
    elif playervalue == 21 and hits == 0:
        wallet += round(bet * 1.5)
        print(f"\n***BLACKJACK***\n\nYou win! (+${round(bet*1.5):,})\n")

    else:
        #When player stays, add cards to dealer's hand and determine value
        dealervalue = calculate_hand_value(dealerhand)
        while dealervalue < 17:
            dealerhand.append(deck.pop())
            if len(deck) == 0:
                print("*Re-shuffling*")
                deck = reshuffle()
            dealervalue = calculate_hand_value(dealerhand)

        print("-"*25)

        #Player reveals each card of dealer's hand by pressing enter to
        #imitate the act of drawing the cards one at a time 
        print(f"Press enter to reveal\ndealer's hand:\n")
        for card in dealerhand:
            print(f"{card['rank']} of {card['suit']}", end = '')
            if card == dealerhand[-1]:
                print()
                break
            print(input(), end='')
        print("-"*25)
        print(f"Dealer:\t{dealervalue}\nPlayer:\t{playervalue}")
        print("-"*25)

        #*** 4 outcomes after player chooses to stay ***

        #(1) Player beats dealer
        if dealervalue < playervalue:
            wallet += (bet)
            print(f"You win! (+${bet:,})\n")

        #(2) Dealer busts            
        elif dealervalue > playervalue:
            if dealervalue > 21:
                wallet += (bet)
                print(f"Dealer busts, you win! (+${bet:,})\n")

            #(3) Dealer beat player
            else:
                wallet -= bet
                print(f"You lose! (-${bet:,})\n")

        #(4) Player and dealer tied
        else:
            print("It's a tie! (+$0)\n")

    plays += 1

    return wallet, startingwallet


#Function asks user to deal a new hand or quit
def play_again():
    playagain = ""
    while playagain not in ["1", "2"]:
        playagain = input("[1]Play again\n[2]Quit\n>")
        if playagain not in ["1", "2"]:
            print("\nInvalid response.\n")
    return playagain


def closing_statement(wallet, startingwallet):
    #If player's balance reaches 0, or if they choose to quit, their balance and total earnings are displayed.
    #If startingwallet is 0, this means the player quit from the initial menu, and there is no balance or earnings to be displayed.
    if startingwallet > 0:
        earnings = wallet - startingwallet
        loss = startingwallet - wallet
        print(f"\nYou started with ${startingwallet:,}\nFinal balance: ${wallet:,}\n")
        if loss == startingwallet:
            print("You lost all your money!\n\nGAME OVER.")
        elif earnings > 0:
            print(f"You won ${earnings:,}.\nThanks for playing!")
        elif earnings < 0:
            print(f"You lost ${loss:,}.\nBetter luck next time!")
        else:
            print("You broke even!")


if __name__ == "__main__":
    main()

