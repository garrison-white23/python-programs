# FILE:2252_White,G_Lesson07_GrLab.py  / change "InLab" to "GrLab" for group labs
# NAME: Random number generator
# AUTHOR(s): Garrison White
# DATE: 11/29/2025
# PURPOSE: User enters a number, then generate that many random integers and store in a txt file. Display a summary of the numbers including min, max, sum, and average.

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
    print("Create up to 1,000 numbers, ranging from 0 to 999.")
    
    
def number_generator():
    # User enters the number of numbers they would
    # like to make. If a whole number 1-1,000 is entered,
    # create a list of random numbers and display summary.

    num_of_nums = 0  
    
    #Ask user how many numbers to generate. Validate input with while loop. 
    while not 1 <= num_of_nums <= 1000:  
        try:
            num_of_nums = int(input("\n\nHow many numbers would you like to generate?\n>"))

            if num_of_nums < 1:
                print("You must generate at least 1 number.")
            elif num_of_nums > 1000:
                print("You cannot generate over 1,000 numbers.")
            else:
                break

        except ValueError:
            print("Invald input. Please enter a whole number between 1 and 100.")

    print("\nGenerating numbers...\n ")

    #Open new txt file and write random numbers into it.
    fout = open("output.txt", "w")
    for i in range(num_of_nums):
        fout.write(f"{random.randint(0,999)}\n")
    fout.close()

    #Open txt file again to read it, and put each number in a list.
    fin = open("output.txt")
    numbers = []
    for line in fin:
        numbers.append(int(line.strip()))
    fin.close()
    
    #Display numbers with a for loop.
    for i in range(len(numbers)):
        if i == len(numbers) - 1:
            print(f"{numbers[i]}")
        else:
            print(f"{numbers[i]}", end = ', ')

        if (i + 1) % 20 == 0:  #This starts a new line for every 20 numbers printed (for readability).
            print()

    #Print a summary  using list functions.
    print("\n\n*** Your numbers can be found in 'output.txt'")
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