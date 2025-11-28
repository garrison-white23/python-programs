import random

loop = 1
while loop == 1:
    
    comp = random.randint(1,3)
    user = int(input('Enter 1, 2, or 3:\n\n1. Rock\n2. Paper\n3. Scissors\n'))
    if comp == user: 
            print('\nIt’s a tie!\n')
    elif (user == 1) and (comp == 2):
            print('\nYou chose: Rock\nComputer chose: Paper\nPaper covers rock\nYOU LOSE\n')
    elif (user == 1) and (comp == 3):
            print('\nYou chose: Rock\nComputer chose: Scissors\nRock smashes scissors\nYOU WIN\n')
    elif (user == 2) and (comp == 1):
            print('\nYou chose: Paper\nComputer chose: Rock\nPaper covers rock\nYOU WIN\n')
    elif (user == 2) and (comp == 3):
            print('\nYou chose: Paper\nComputer chose: Scissors\n Scissors cut paper\nYOU LOSE\n')
    elif (user == 3) and (comp == 1):
            print('\nYou chose: Scissors\nComputer chose: Rock\n Rock Smashes scissors\nYOU LOSE\n')
    elif (user == 3) and (comp == 2):
            print('\nYou chose: Scissors\nComputer chose: Paper\n Scissors cut paper\nYOU WIN\n')
    else:
            print('Invalid  response. Try again.')
    loop = int(input('1. Play again\n2. Quit\n'))
print('\nThanks for playing!')
