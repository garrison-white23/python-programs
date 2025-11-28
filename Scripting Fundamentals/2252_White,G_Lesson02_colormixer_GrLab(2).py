# FILE:2252_White,G_Lesson02_GrLab(2).py  / change "InLab" to "GrLab" for group labs
# NAME: Primary color mixures
# AUTHOR(s): Garrison White
# DATE: 9/21/2025
# PURPOSE: User can input two primary colors and program will return the color when those two are mixed

#Ask the user for 2 colors, and create variables for color1 and color2
color1 = input('Select 2 primary colors to be combined: red, blue, or yellow\n\nWhat is the first color?\t')
color2 = input('What is the second color?\t')

#Convert these 2 strings to be all lowercase. This allows the following if statements to work even if the user does not enter all lowercase.
color1 = color1.lower()
color2 = color2.lower()

#Using if statements, determine which color is made with the combination of the 2 colors entered by the user.
#If there is an invalid color entered, or if 2 of the same color is entered, an error message is displayed
if (color1 != 'red' and color1 != 'blue' and color1 != 'yellow') or (color2 != 'red' and color2 != 'blue' and color2 != 'yellow'):
    print('Invalid response.')
elif color1 == 'red' and color2 == 'blue':
    print('\nYour new color is: Purple')
elif color1 == 'blue' and color2 == 'yellow':
    print('\nYour new color is: Green')
elif color1 == 'yellow' and color2 == 'red':
    print('\nYour new color is: Orange')
else:
    print('\nYou cannot enter 2 of the same color!')



print(input('\n\nHit Enter to Close\n'))
