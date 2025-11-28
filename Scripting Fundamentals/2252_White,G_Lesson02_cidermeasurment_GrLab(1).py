# FILE:2252_White,G_Lesson02_GrLab(1).py  / change "InLab" to "GrLab" for group labs
# NAME:Drams/gills conversion
# AUTHOR(s): Garrison White
# DATE: 9/18/2025
# PURPOSE: Convert ounces of apple cider into drams and gills

#Ask user for the amount of apple cider in ounces.
ounces = float(input("How many ounces of apple cider would you like to purchase?\t"))

#Based on the number of ounces, variables are created that convert the ounces into drams and gills.
#Then a message is displayed telling the user how much apple cider this is in drams and ounces
drams = ounces * 8
gills = ounces / 4
print(f'\n{ounces} ounces converts to:\n{drams} drams, or {gills} gills.\n')

#A message is displayed depending on how many drams of apple cider the user is trying to purchase. 
if drams > 1024:
    print('This is a large amount, you will need to purchase your cider in gallons.')
elif drams < 100:
    print('This is small amount, you should just order a pint.')

print(input('\n\nHit Enter to Close\n'))
