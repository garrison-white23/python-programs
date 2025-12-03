#!/usr/bin/env python  #What is this line for? Watch the SHEBANG video in lesson 01

# FILE:2252_RectorA_Lesson7#_GrLab.py  / change "InLab" to "GrLab" for group labs
# NAME: List of Numbers Generator 2
# AUTHOR(s): Alexa Rector
# DATE: month/day/year  11/12/2025
# PURPOSE: exp: Generates a list of numbers, the sequel.

import random

def generate_list(gl_numbers):
    gl_output = []
    # need a list
    
    for i in range(0, gl_numbers):
        gl_output.append(random.randint(0, 50))
    # create random numbers, append to list

    return gl_output
    # pass the list off

def list_statistics(ls_list):
    ls_low = 2147483647
    ls_high = -2147483648
    ls_sum = 0
    # set some variables
    
    for i in ls_list:
        if i < ls_low:
            ls_low = i
            # low check
            
        if i > ls_high:
            ls_high = i
            # high check

        ls_sum += i
        # add to sum

    ls_average = ls_sum / len(ls_list)
    # get average

    return ls_low, ls_high, ls_sum, ls_average
    # hand em over

def main():
    print('Welcome to the random number list generator!')
    numbers = 'invalid input' # loop setup

    while numbers.isnumeric() == False:
        numbers = input('How many numbers would you like to generate? ')
        if numbers.isnumeric() == False:
            print('You must enter a positive whole number for this.') # check for integer
        elif int(numbers) < 1:
            print('You must ask for at least one number.') # no zeros allowed
            numbers = 'invalid input' # we don't want to exit the loop, so make the condition happen again

    print('Generating...')
    numbers = int(numbers)
    output_list = generate_list(numbers)
    list_low, list_high, list_sum, list_average = list_statistics(output_list)
    # generate list and statistics

    fout = open('numbers.txt', 'w')
    for i in output_list:
        fout.write(str(i))
        fout.write('\n')
    # write list of numbers
    fout.close() # gotta do it

    print()
    print('Your list:', output_list)
    print('Lowest number:', list_low)
    print('Highest number:', list_high)
    print('Sum of all numbers:', list_sum)
    print('Average number in list:', list_average)
    print()
    print('List of numbers has been saved as numbers.txt in the same folder that you saved this program in.')
    input('Press Enter to exit. Remember to grab your statistics if you need them.')
    # outputs

if __name__ == "__main__":
    main() 