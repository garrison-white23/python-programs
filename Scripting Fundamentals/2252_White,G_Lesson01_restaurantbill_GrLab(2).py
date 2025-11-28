# FILE:2252_WhiteG_Lesson01_GrLab.py  
# NAME:Restaurant bill program
# AUTHOR(s): Garrison White
# DATE: 9/14/2025
# PURPOSE: Calculate restaurant bill total

#Welcome text to explain the purpose of the program
print('''This program will allow you determine the total of your restaurant bill including sales tax,
and a 20% tip for the server.\n''')

#Ask user to enter the cost of food and drink
subtotal = float(input('Enter the total cost of food and drink:\n$'))

#Create variable for tip, tax, and total amount
#The tax variable is made first, then total is made to include subtotal and tax
#Then the tip variable is determined based on the total variable, and total and tip are added together
tax = subtotal * 0.065
total = subtotal + tax
tip = total * 0.2
total += tip

#Finally, the subtotal, tip, tax, and total amount are displayed
print (f'\nSubtotal:\t${subtotal:.2f}\nTax:\t\t${tax:.2f}\nTip:\t\t${tip:.2f}\nTotal:\t\t${total:.2f}\n')

print(input('\n\nHit Enter to Close\n'))
