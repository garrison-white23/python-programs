# FILE:2252_White,G_Lesson07_InLab.py  / change "InLab" to "GrLab" for group labs
# NAME: World Series Winners
# AUTHOR(s): Garrison White
# DATE: 11/28/2025
# PURPOSE: Display the years a given baseball team won World Series using an imported txt file.

def main():
    print("--------------------------")
    print("   World Series Winners   ")
    print("--------------------------")
    print("\nThis program lets you enter the name of any baseball team to see which years they won the World Series.")

    file = open("WorldSeriesWinners.txt")
    lines = file.read().splitlines()

    #List of teams will be every other line starting with index 0
    #List of years will be every other line starting with index 1
    teams_upper = lines[0::2]
    teams = []
    for i in teams_upper:  #Convert teams to lowercase
        teams.append(i.lower().strip())                 
    years = lines[1::2]                                     
    
    choice = "1"
    while choice == "1":
        team = get_team(teams)
        result(team, teams, years)
        choice = playagain()

    print("\nGoodbye!")
    print(input('\n\nHit Enter to Close\n'))


def get_team(teams):
    while True:
        team = input("\nEnter team name, or type 'No Winner':\n>")
        if team.lower() in teams:
            break
        else:
            print("\nThat is not a valid baseball team.")

    return team


def result(team, teams, years):
    #Number of wins starts at 0, and empty list of the years the team won is defined.
    num_wins = 0
    years_won = []

    #If entered team equals a team in the list, incriment numWins by 1,
    #and append the appropriate year to the list 'winYears.'
    for i in range(len(teams)):
        if teams[i].lower().strip() == team.lower():
            num_wins += 1
            years_won.append(years[i])

    #Display num of times team won, and list the years they won
    if team.lower() == "no winner":
        print("\nHere are the years where there was no winner in the World Series:")
        for i in years_won:
            print (i)
    elif len(years_won) == 1:
        print(f"\nThis team won 1 time in the year {years_won[0]}")
    else:
        print(f"\nThis team won {num_wins} times in the following years:")
        for i in years_won:
            print (i)


def playagain():
    choice = ""
    while choice not in ["1", "2"]:
        choice = input("\nSelect an options:\n[1]New baseball team\n[2]Quit\n>")
        if choice in ["1", "2"]:
            break
        else:
            print("Invalid response. Try again.")

    return choice

        
if __name__ == "__main__":
    main()
