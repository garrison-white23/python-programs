#   WORDLE 
#   Author: Garrison White
#   Date: 11/14/2025
#   Description: Guess the secret 5-letter word

import random    
from wordle_answers import wordle_list
from wordle_answers import dictionary

def main():
    playagain = welcome()
    if playagain == "1":
        while playagain == "1":
            result, word, attempts = gameplay()
            results(result, word, attempts)
            playagain = play_again()
        print("\n\nThanks for playing!")
        print(input('\nHit Enter to Close\n'))
    else:
        print("\nGoodbye!")
        print(input('\nHit Enter to Close\n'))


def welcome():
    print("----------------------")
    print("        WORDLE        ")
    print("----------------------\n")

    playagain = ""
    while playagain not in ["1", "2"]:
        playagain = input("[1]Play\n[2]Quit\n[3]Rules\n>")
        if playagain in ["1", "2"]:
            break
        elif playagain == "3":
             print('''\nWelcome to Wordle!

-Guess the secret word in 8 tries.
-Each guess must be a 5-letter word.
-The symbols below the word change to show
how close your guess was to the word.

Example:   SPACE
           ●○--○
                 
           'S' is in the word and in the correct spot.
           'P' and 'E' are both in the word, but in the wrong spot.
           'A' and 'C' are not in the word.\n''')
                       

            
        else:
            print("\nInvalid response.\n")

    return playagain


def gameplay():
    print("\nGuess the 5-letter word to win!")
    guess = ""
    
    #Select random word from Wordle answer list.
    r = random.randint(0, len(wordle_list) - 1)
    word = wordle_list[r]

    attempts = 0
    remaining_attempts = 8
    exhausted_letters = []
    
    while guess.upper() != word and remaining_attempts > 0:
        
        feedback = ["-","-","-","-","-"]

        while True:
            guess = input(f"\nRemaining attempts:{remaining_attempts}\n----------------------\n>")
            
            if len(guess) != 5:
                print("You must enter a 5-letter word.")
                continue
            elif not guess.isalpha():
                print("You must enter a 5-letter word.")
                continue
            elif guess.upper() not in dictionary and guess.upper() not in wordle_list:
                print("That is not a valid word.")
                continue

            break
        
        word_copy = list(word)
        guess_copy = list(guess.upper())

        x=0
        for position in guess_copy:
            if position == word_copy[x]:
                feedback[x] = "●"
                guess_copy[x] = None
                word_copy[x] = None
            x += 1   
       
        x = 0
        for position in guess_copy:
            if position is not None and position in word_copy:
                feedback[x] = "○"
                word_copy[word_copy.index(position)] = None
                guess_copy[x] = None
            else:
                if position is not None and position not in word and position not in exhausted_letters:
                    exhausted_letters.append(position)
                    exhausted_letters.sort()
            x += 1    
        
        print(" ", end = "")
        for i in feedback:
            print(i, end = "")

 
        print("\t\tNot in word: ", end = "")
        
        x = 0
        for i in exhausted_letters:
            if x != len(exhausted_letters)-1:
                print(i, end = ", ")
                x += 1
                if x % 7 == 0:
                    print("\n" + " " * 29, end="")
            else:
                print(i)
    
        remaining_attempts -= 1
        attempts += 1
        

    if guess.upper() == word:
        result = 1
    else:
        result = 2

    return result, word, attempts


def results(result, word, attempts):
    if result == 1:
        print(f"\n   Correct!\n***YOU WIN***\nAttempts: {attempts}")
    else:
        print("Out of attempts!\nGAME OVER")
        print(f"The answer was: {word}")
    
    
def play_again():
    playagain = ""
    while playagain not in ["1", "2"]:
        playagain = input("\n[1]Play again\n[2]Quit\n>")
        if playagain not in ["1", "2"]:
            print("\nInvalid response.\n")
    return playagain


if __name__ == "__main__":
    main()
