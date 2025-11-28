# FILE:2252_White,G_Lesson03_GrLab(1).py  / change "InLab" to "GrLab" for group labs
# NAME: Brutus the Dog Distance Calculator
# AUTHOR(s): Garrison White
# DATE: 10/7/25
# PURPOSE: Calculate total distance Brutus ran while playing fetch over a certain number of hours

#Opening statement - introduces the program
linebreak = "="*70
print(f"{linebreak}\n")
print(f"\tHello and welcome to the Brutus the Dog simulator!\n\n{linebreak}")

#Creates 'play again' variable. The program will let the user play with Brutus as many times as they want
playagain = input("Would you like to play fetch with Brutus?[Y/N]:\t")

#As long as the user enters yes for play again, the program will run
while playagain == 'Y' or playagain == 'y':

#Asks user for time spent playing with Brutus, and the speed of Brutus. User cannot enter a time more than 8 hours
        time = int(input('\nHow many hours did you and Brutus play fetch?\t'))
        while time > 8:
                time = int(input("\nThat's too long! Can only play up to 8 hours\nPlease re-enter the number of hours:\t"))
        speed = int(input("What was Brutus's speed (kmh)?\t"))
            

#For loop is used to display the distance traveled at every hour. Ask user to enter y/n for playagain to continue or stop the while loop.
        print(f"\n{linebreak}\nSummary of Brutus's distance:\n{linebreak}\nHour:\t Brutus's Distance:")

        for hour in range(1,time+1):
                distance = hour * speed
                print(hour, '\t', distance, 'km')

        playagain = input(f"\n{linebreak}\nWould you like to play with Brutus again?[Y/N]:\t")

print('''\n

⠀⠀⠀⠀⠀⠀⠀/ \__
      (    @\___
      /         O   Thanks for playing!
     /   (_____/
    /_____/   U
''')

print(input('\n\nHit Enter to Close\n'))
