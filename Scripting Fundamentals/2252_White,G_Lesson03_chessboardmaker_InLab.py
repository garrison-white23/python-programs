# FILE:2252_White,G_Lesson03_InLab.py  / change "InLab" to "GrLab" for group labs
# NAME: Chess Board
# AUTHOR(s): Garrison White
# DATE: 10/7/25
# PURPOSE: Create a text-based chess board

print(("#" * 35), "\n###\tChess Board Maker\t###")
print("#" * 35)


#The string 'columns' contains letters a through h. Each letter of the string will be
#interated in the for statement below to create each column of the chess board.
columns = "abcdefgh"

#Ask the user to create a chess board. First, 'playagain' is set to equal nothing, then the while loop checks that the user inputs
#either a 1 or a 0. The same code is used in line 46 to check future inputs from the user. 
playagain = ""
while playagain != "1" or playagain != "2":
    playagain = input("\n--- Please select one of the following: ---\n\n[1] Make a chess board\n[2]Exit\n")
    if playagain == "1" or playagain == "2":
        break
    else:
        print("\nInvalid response.", end = '')
        
    

while playagain == "1":
#Variable 'row' starts at 8. After each iteration of the for loop, 'row'
# is subtracted by 1 to create 8 rows of decending order.
    print()
    row = 8

#The outer for loop is responsible for creating each of the 8 rows. After each iteration,
# 'row' is subtracted by 1. The inner for loop creates the 8 chess squares on each row.
#The element 'y' of the column string is printed, followed by the variable row.
    for x in columns:    
        print('-'*40)
        for y in range(8):
            print(columns[y], row, sep='', end=' | ')
        print()
        row -= 1
    print('-'*40)

    row -= 1
    
    playagain = ''
    while playagain != "1" or playagain != "2":
        playagain = input("\n--- Please select one of the following: ---\n\n[1] Make a chess board\n[2]Exit\n")
        if playagain == "1" or playagain == "2":
            break
        else:
            print("\nInvalid response.", end = '')

print("\n--- Goodbye! ---")

    


print(input('\n\nHit Enter to Close\n'))
