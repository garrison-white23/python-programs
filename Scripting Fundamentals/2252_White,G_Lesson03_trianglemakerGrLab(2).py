# FILE:2252_White,G_Lesson03_GrLab(2).py  / change "InLab" to "GrLab" for group labs
# NAME:Triangle Creator
# AUTHOR(s): Garrison White
# DATE: 10/8/25
# PURPOSE: Draw a triangle using the # symbol

linebreak = "="*70
print(f"{linebreak}\n")
print(f"\t\tWelcome to the triangle creator.\n\n{linebreak}")

triangles = 0 #keeps track of total number of triangles created
playagain = input("Create a triangle?[Y/N]:\t") #While the user answers yes, they can keep making triangles

#2 for loops are used to make the shape of the triangle. The loop iterates through a range to determine the
#number of spaces in between the '#' symbol in order to make the shape. 
while playagain == "Y" or playagain == "y":
    space = ' '
    print('\n#')
    for x in range(4):
        print('#',space*x,'#',sep='')
    for x in range(4,-1,-1):
        print('#',space*x,'#', sep='')
    print('#')

    triangles += 1 #triangles is incrimented by 1

    #Ask user to play again and display their total triangle count
    if triangles == 1:
        playagain = input(f"\nYou have created 1 triangle.\n\nCreate another triangle?[Y/N]:\t")
    else:
        playagain = input(f"\nYou have created {triangles} triangles.\n\nCreate another triangle?[Y/N]:\t")

#When user is done, ending statement displays the final number of triangles. The program doesn't like when
#the user doesn't make any triangles.
if triangles == 1:
    print("\n\n\nCongratulations. You made 1 triangle.\n\nHave a nice day.")
elif triangles == 0:
    print("\n\n\nWhy even bother?")
else:
    print(f"\n\n\nCongratulations. You made {triangles} triangles. \n\nHave a nice day.")
