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

print("Git test")


print(teams)
print(years)