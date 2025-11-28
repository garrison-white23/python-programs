# FILE:2252_White,G_Lesson02_InLab.py  / change "InLab" to "GrLab" for group labs
# NAME:
# AUTHOR(s): Garrison White
# DATE: 
# PURPOSE: The Python Rocks amusement park has a tiered admission policy.
#This program will take the users height, inches, and return the name of the
#tier, and the price of the ticket.

#Get the height of the user as an integer.
height = int(input('Enter your height in inches:'))

#Use if/else statements to determine the tier, and ticket price.
if height < 30 and height > 0:
    print('Your tier is Guppy. Price: FREE')
elif height >= 30 and height <36:
    print('Your tier is Pollywog. Price: $2')
elif height >= 36 and height <42:
    print('Your tier is Apprentice. Price: $5')
elif height >= 42 and height <48:
    print('Your tier is Explorer. Price: $8')
elif height >= 48:
    print('Your tier is Adventurer. Price: $10')
else:
    print("Can't use a negative number!")
    





print(input('\n\nHit Enter to Close\n'))
