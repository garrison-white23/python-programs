# FILE:2252_White,G_Lesson04_GrLab(2).py  / change "InLab" to "GrLab" for group labs
# NAME: Math quiz
# AUTHOR(s): Garrison White
# DATE: 10/14/2025 
# PURPOSE: Quiz user on addition math problems with randomly generated numbers

import random

#Main function:
def main():
    playagain = "1"
    welcome()
    while playagain == "1":
        math_problem()
        playagain = play_again()
    closing_statement()

#Welcome statement
def welcome():
    print("   --- MATH QUIZ ---")
    print("\nInstructions: Solve the following addition problems by entering the answer below.")
    print("When you are finished, type 'quit' to exit.\n\n")
    input("Press Enter to start...\n\n")

#Create 2 numbers for the math problem, and takes the user's answer.
#Result is 1:Correct or 2: incorrect.
#Display result to user.
def math_problem():
    a = random.randint(1,99)
    b = random.randint(1,99)
    answer = a + b
    print(f'''
 {a}
+{b}
----''')
    useranswer = int(input(">"))
    if useranswer == answer:
        result = 1
    else:
        result = 2

    if result == 1:
        print("\n*** CORRECT ***\nGreat job, keep it up!\n")
    else:
        print(f"\nXXX WRONG XXX\nCorrect answer: {answer}\n")

#Ask user to play again after every question. 1 for yes, 2 for no.
def play_again():
    while True:
        playagain = input("[1]Play again\n[2]Quit\n>")
        if playagain == "1" or playagain == "2":
            break
        else: 
            print("\nInvalid response.\n")
    return playagain

#Closing statement after player decides to quit.
def closing_statement():
    print("\n\nThanks for playing!")

    print(input('\nHit Enter to Close\n'))

#Call on main function.
if __name__ == "__main__":
    main()
    
    
