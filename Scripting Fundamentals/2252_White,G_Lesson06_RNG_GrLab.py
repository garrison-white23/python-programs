# FILE:2252_White,G_Lesson06_GrLab.py  / change "InLab" to "GrLab" for group labs
# NAME: Random number generator
# AUTHOR(s): Garrison White
# DATE: 11/12/2025
# PURPOSE: User enters a number, then generate that many random integers in a list. Display a summary of the list of numbers including min, max, sum, and average.

import random

def main():
    playagain = "1"
    welcome()
    while playagain == "1":
        number_generator()
        playagain = play_again()
    print("\nGoodbye!")
    print(input('\n\nHit Enter to Close\n')) 
        
        
def welcome():    
    print("\n               -------- RANDOM NUMBER GENERATOR --------")
    print("\nThis program generates a list of random numbers, and makes a summary of those numbers.")
    print("You can create a maximum of 100 numbers, and the numbers will range from 0 - 99.")
    
    
def number_generator():
    # User enters the number of numbers they would
    # like to make. If a whole number 1-100 is entered,
    # create a list of random numbers and display summary.

    num_of_nums = 0  
    
    #Ask user how many numbers to generate. Validate input with while loop. 
    while num_of_nums not in range(1,101):  
        try:
            num_of_nums = int(input("\n\nHow many numbers would you like to generate?\n>"))

            if num_of_nums < 1:
                print("You must generate at least 1 number.")
            elif num_of_nums > 100:
                print("You cannot generate over 100 numbers.")
            else:
                break

        except ValueError:
            print("Invald input. Please enter a whole number between 1 and 100.")

    #Create an empty list, then append random numbers to the list with for loop.
    numbers = []
    for num in range(num_of_nums):
        numbers.append(random.randint(0,99))

    print("\nGenerating numbers...\n ")

    #Display numbers with a for loop.
    for i in range(len(numbers)):
        print(f"{numbers[i]} ", end = '')

        if (i + 1) % 10 == 0:  #This starts a new line for every 10 numbers printed (for readability).
            print()

    #Print a summary  using list functions.
    print()
    print("---------------------")
    print("       SUMMARY       ")
    print("---------------------")
    print(f"Minimum:      {min(numbers)}")
    print(f"Maximim:      {max(numbers)}")
    print(f"Sum total:    {sum(numbers):,}")
    print(f"Average:      {(sum(numbers))/(len(numbers))}")
    
def play_again():
    playagain = ""
    while playagain not in ["1", "2"]:
        playagain = input("\n\nSelect one of the following:\n[1]Create a new list\n[2]Quit\n>")
        if playagain not in ["1", "2"]:
            print("Invalid response. Please enter '1' or '2'")
    return playagain
    
    
if __name__ == "__main__":
    main()


