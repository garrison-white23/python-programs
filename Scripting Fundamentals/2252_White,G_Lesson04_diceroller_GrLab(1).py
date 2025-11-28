# FILE:2252_White,G_Lesson04_GrLab(1).py  / change "InLab" to "GrLab" for group labs
# NAME: Dice roller
# AUTHOR(s): Garrison White
# DATE: 
# PURPOSE: Simulate rolling dice with randomly generated numbers

import random

print("==================================")
print("           Dice Roller            ")
print("==================================")
print("Roll the 6 sided die to see what number you get!")

#This loop takes a user input and then prints a random number for dice roll.
#If input is 'q', loop breaks.
while True:
    print("----------------------------------")
    print("Press 'Enter' to roll the dice. \nType 'q' to quit.")
    user_input = input()
    if user_input == "q" or user_input == "Q":
        break
    print(f"You rolled: {random.randint(1,6)}")
print("\nGoodbye!")
    
print(input('\n\nHit Enter to Close\n'))    
          
