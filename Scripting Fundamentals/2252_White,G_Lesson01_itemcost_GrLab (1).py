# FILE:2252_WhiteG_Lesson01_GrLab.py  
# NAME:Cost of 3 items
# AUTHOR(s): Garrison White
# DATE: 9/14/2025
# PURPOSE: Calculate cost of sale containing 3 items

#This is the welcome text which explains the goal of the program
print('''Welcome! \n\nThis program will calculate the total cost of a sale by using the
price of 3 items and a given sales tax rate.\n''')
      
#These are the propts for the user to enter the price of 3 items and the tax rate
item1 = float(input("Start by entering the price of the first item:\t$"))
item2 = float(input("Enter the price of the second item:\t\t$"))
item3 = float(input("Enter the price of the third item:\t\t$"))
taxrate = float(input("What is the sales tax?\t"))

#Create values for the subtotal, total tax amount, total amount with tax
subtotal = item1 + item2 + item3
taxtotal = subtotal * taxrate
totalamount = subtotal + taxtotal

#Display the results to the user
print(f"\n\nSubtotal of sale:\t\t\t${subtotal:.2f}")
print(f"Amount of tax to be collected:\t\t${taxtotal:.2f}")
print(f"Total amount to pay:\t\t\t${totalamount:.2f}")

print(input('\n\nHit Enter to Close\n'))
