# FILE:2252_White,G_Lesson07_InLab.py  / change "InLab" to "GrLab" for group labs
# NAME: World Series Winners
# AUTHOR(s): Garrison White
# DATE: 11/27/2025
# PURPOSE: Display the years a given baseball team won World Series using an imported txt file.

file = open("WorldSeriesWinners.txt")

#Make a list of all individual lines of txt file
lines = file.read().splitlines()

#List of teams will be every other line starting with index 0
#List of years will be every other line starting with index 1
teams = lines[0::2]
years = lines[1::2]

print(len(teams), len(years))
team = input("Enter team name, or type 'No Winner':\n>")

#Display num of times team won, and list the years they won
numWins = 0
winYears = []
for i in range(len(teams)):
    if teams[i].lower().strip() == team.lower():
        numWins += 1
        winYears.append(years[i])

if team.lower() == "no winner":
    print("Here are the years where there was no winner in the World Series:")
else:
    print(f"This team won {numWins} times in the following years:")

for i in winYears:
    print (i)