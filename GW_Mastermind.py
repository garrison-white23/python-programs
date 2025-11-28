#   MASTERMIND 
#   Author: Garrison White
#   Date: 11/13/2025
#   Description: Plays the boardgame 'Mastermind' where the computer is the codemaker.

import random

def main():
    playagain = welcome()
    if playagain == "1":
        while playagain == "1":
            result, code = gameplay()
            results(result, code)
            playagain = play_again()
        print("\n\nThanks for playing!")
        print(input('\nHit Enter to Close\n'))
    else:
        print("\nGoodbye!")
        print(input('\nHit Enter to Close\n'))


def welcome():
    print("--------------------")
    print("     MASTERMIND     ")
    print("--------------------\n")

    playagain = ""
    while playagain not in ["1", "2"]:
        playagain = input("[1]Play\n[2]Quit\n[3]Rules\n>")
        if playagain in ["1", "2"]:
            break
        elif playagain == "3":
             print("\nMastermind is a code-breaking game where the computer secretly generates a\n"
                   "4-digit code using the numbers 1 through 6, with digits possibly repeating.\n"
                   "Your goal is to guess the exact code.\n")
    
             print("After each guess, the game will display clues using two types of pegs:")
             print("  ●  Black peg = correct digit in the correct position")
             print("  ○  White peg = correct digit in the wrong position\n")

             print("Example:")
             print("  Secret code:  4 1 6 2")
             print("  Your guess:   4 2 3 1")
             print("  Result:       ●")
             print("                ○ ○")
    
             print("\nPegs are not shown in any particular order, so you must interpret the total\n"
                   "counts rather than peg placement. Each matched digit is only counted once.\n")
    
             print("Use these clues to refine your guesses and break the code!\n")
             

            
        else:
            print("\nInvalid response.\n")

    return playagain


def gameplay():
    print("\nBreak the code to win!")
    guess = ""
    
    one = random.randint(1,6)
    first = str(one)
    two = random.randint(1,6)
    second = str(two)
    three = random.randint(1,6)
    third = str(three)
    four = random.randint(1,6)
    fourth = str(four)
    code = first+second+third+fourth

    #for i in code:
        #print(i, end='')

    remaining_attempts = 12
    
    while guess != code and remaining_attempts > 0:
        
        correct_positions = 0
        incorrect_positions = 0

        while True:
            guess = str(input(f"\nRemaining attempts:{remaining_attempts}\n----------------------\n>"))
            
            if len(guess) != 4:
                print("Code must 4 numbers 1 through 6!")
                continue
    
            valid = True
            for char in guess:
                if char not in ["1", "2", "3", "4", "5", "6"]:
                    print("Code must 4 numbers 1 through 6!")
                    valid = False
                    break
            
            if not valid:
                continue
    
            break
        
        code_copy = list(code)
        guess_copy = list(guess)
        
        x=0
        for position in guess_copy:
            if position == code_copy[x]:
                correct_positions += 1
                guess_copy[x] = None
                code_copy[x] = None
            x += 1   
       
        x = 0
        for position in guess_copy:
            if position is not None and position in code_copy:
                incorrect_positions += 1
                code_copy[code_copy.index(position)] = None
                guess_copy[x] = None
            x += 1

        if correct_positions > 0 or incorrect_positions > 0:       
            for i in range(correct_positions):
                print("●", end = '')
            print()
            for i in range(incorrect_positions):
                print("○", end = '')
        else:
            print("No matches...")

        
        remaining_attempts -= 1
        print()

    if guess == code:
        result = 1
    else:
        result = 2

    return result, code


def results(result, code):
    if result == 1:
        print("Correct! You've cracked the code!\nYOU WIN")
    else:
        print("Out of attempts!\nGAME OVER")
        print(f"The answer was: {code}")
    

        
def play_again():
    playagain = ""
    while playagain not in ["1", "2"]:
        playagain = input("\n[1]Play again\n[2]Quit\n>")
        if playagain not in ["1", "2"]:
            print("\nInvalid response.\n")
    return playagain
    


if __name__ == "__main__":
    main()













