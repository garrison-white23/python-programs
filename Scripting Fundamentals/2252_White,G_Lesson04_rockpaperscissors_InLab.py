# FILE:2252_White,G_Lesson04_InLab.py  / change "InLab" to "GrLab" for group labs
# NAME: Rock Paper Scissors
# AUTHOR(s): Garrison White
# DATE: 10/16/2025
# PURPOSE: Play rock paper scissors against the computer

import random

#Main function
def main():
    playagain = start_menu()
    if playagain == "1":
        userscore, compscore, rounds, username = scores_and_name()
        while playagain == "1":
            rounds, userscore, compscore = gameplay(userscore, compscore, rounds, username)
            playagain = play_again()
    else:
        rounds = 0
        username = ""
        userscore = 0
        compscore = 0
    closing_statement(rounds, username, userscore, compscore)
    
        
#Initial starting menu - Ask user to play or quit, must enter 1 or 2
def start_menu():
    print('''-----------------------------------
        Rock Paper Scissors
-----------------------------------
    ''')

    while True:
        playagain = input("[1]Play\n[2]Quit\n\n>")
        if playagain == "1" or playagain == "2":
            break
        else:
            print("\nInvalid response.\n")
    return playagain

#Create user and computer score starting at 0, and set rounds to 0
def scores_and_name():
    userscore = 0
    compscore = 0
    rounds = 0

    #Ask user's name - Must be 1-15 characters in length
    while True:
        username = str(input("\nPlease enter your name (max 15 characters):\n>"))
        if len(username)>0 and len(username)<16:
            break
        else:
            print("\nInvalid response.\n")
    return userscore, compscore, rounds, username

#Gameplay - User selects rock, paper, or scissors and computer makes random selection.
#Winner is determined with if statements, and a point is given to either 'userscore' or 'compscore'.
def gameplay(userscore, compscore, rounds, username):
    comp = random.randint(1,3)
    while True:
        user = int(input(f"\n\n{'-'*32}\n{username}: {userscore}\nComputer: {compscore}\n{'-'*32}\nEnter one of the following:\n[1]Rock  [2]Paper  [3]Scissors\n>"))
        if user == 1 or user == 2 or user == 3:
            break
        else:
            print("\nInvalid response.\n")
    if comp == user: 
        print("\nIt’s a tie!\n")
    elif (user == 1) and (comp == 2):
        print("\nYou chose: Rock\nComputer chose: Paper\nPaper covers rock\nYOU LOSE\n")
        compscore += 1
    elif (user == 1) and (comp == 3):
        print("\nYou chose: Rock\nComputer chose: Scissors\nRock smashes scissors\nYOU WIN\n")
        userscore += 1
    elif (user == 2) and (comp == 1):
        print("\nYou chose: Paper\nComputer chose: Rock\nPaper covers rock\nYOU WIN\n")
        userscore += 1
    elif (user == 2) and (comp == 3):
        print("\nYou chose: Paper\nComputer chose: Scissors\nScissors cut paper\nYOU LOSE\n")
        compscore += 1
    elif (user == 3) and (comp == 1):
        print("\nYou chose: Scissors\nComputer chose: Rock\nRock Smashes scissors\nYOU LOSE\n")
        compscore += 1
    else:
        print("\nYou chose: Scissors\nComputer chose: Paper\nScissors cut paper\nYOU WIN\n")
        userscore += 1

    rounds += 1

    return rounds, userscore, compscore
    
#Ask user to play again - 1 for yes, 2 for no
def play_again():
    while True:
        playagain = input("[1]Play again\n[2]Quit\n>")
        if playagain == "1" or playagain == "2":
            break
        else: 
            print("\nInvalid response.\n")
    return playagain

#Closing statements
def closing_statement(rounds, username, userscore, compscore):
    if rounds == 0:
        print("\nGoodbye!")
    else:
        print(f'''

    ===================
        FINAL SCORE
    ===================
    Rounds: {rounds}

    {username}: {userscore}
    Computer: {compscore}
    ===================

    Thanks for playing!''')
    print(input('\n\nHit Enter to Close\n'))

#Call on main function.
if __name__ == "__main__":
    main()
    

