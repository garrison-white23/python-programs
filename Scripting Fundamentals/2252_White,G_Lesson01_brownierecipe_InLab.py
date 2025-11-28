# FILE:2252_White,G_Lesson01_InLab.py  / change "InLab" to "GrLab" for group labs
# NAME:Brownie recipe
# AUTHOR(s): Garrison White
# DATE: 9/14/2015
# PURPOSE: Determine the amount of ingredients needed to yield a certain number of brownies

#First, the program asks how many brownies to make, and creates the variable numbrownies. 
numbrownies = int(input('''This program will calculate the amount of ingredients needed
for a desired amount of brownies \n\nHow many brownies would you like to make?\t'''))

#To find the correct measurment of each ingredient, I take the measurment from the original
#recipe (which yields 9 brownies) and divide by 9, then multiply by the variable numbrownies.

butter = (0.5 / 9) * numbrownies
eggs = (2 / 9) * numbrownies
#Eggs are rounded becuase you cannot have a decimal number of eggs
eggs = round(eggs)
vanilla = (1 / 9) * numbrownies
sugar = (1 / 9) * numbrownies
flour = (0.5 / 9) * numbrownies
cocoa = (0.5 / 9) * numbrownies
bakingpowder = (0.25 / 9) * numbrownies
salt = (0.25 / 9) * numbrownies

#The measurment for each ingredient is displayed
print (f'''\nThe recipe requires:\n
{butter:.2f} cups butter
{eggs} eggs
{vanilla:.2f} teaspoons vanilla
{sugar:.2f} cups sugar
{flour:.2f} cups flour
{cocoa:.2f} cups cocoa powder
{bakingpowder:.2f} teaspoons baking powder
{salt:.2f} teaspoons salt''')




print(input('\n\nHit Enter to Close\n'))
