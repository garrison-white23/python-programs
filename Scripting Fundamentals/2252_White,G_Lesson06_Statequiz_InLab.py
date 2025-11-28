# FILE:2252_White,G_Lesson06_InLab.py  / change "InLab" to "GrLab" for group labs
# NAME: 50 States Quiz
# AUTHOR(s): Garrison White
# DATE: 11/12/2025
# PURPOSE: Quiz user on the U.S. state abbreviations.

import random

def main():
    '''
    When user chooses to play, dictionary of all states/abbreviations is created.
    The dictionary is sent to state_quiz(), where user completes the quiz and the
    score, incorrect answers, and total number of questions is returned. Then those
    variables are sent to results() where the final score along with incorrect
    answers are displayed. Then user chooses to play again or quit in play_again().
    '''
    playagain = welcome()
    if playagain == "1":
        while playagain == "1":
            states = {
        "Alabama": "AL","Alaska": "AK","Arizona": "AZ","Arkansas": "AR","California": "CA",
        "Colorado": "CO","Connecticut": "CT","Delaware": "DE","Florida": "FL","Georgia": "GA",
        "Hawaii": "HI","Idaho": "ID","Illinois": "IL","Indiana": "IN","Iowa": "IA",
        "Kansas": "KS","Kentucky": "KY","Louisiana": "LA","Maine": "ME","Maryland": "MD",
        "Massachusetts": "MA","Michigan": "MI","Minnesota": "MN","Mississippi": "MS","Missouri": "MO",
        "Montana": "MT","Nebraska": "NE","Nevada": "NV","New Hampshire": "NH","New Jersey": "NJ",
        "New Mexico": "NM","New York": "NY","North Carolina": "NC","North Dakota": "ND","Ohio": "OH",
        "Oklahoma": "OK","Oregon": "OR","Pennsylvania": "PA","Rhode Island": "RI","South Carolina": "SC",
        "South Dakota": "SD","Tennessee": "TN","Texas": "TX","Utah": "UT","Vermont": "VT",
        "Virginia": "VA","Washington": "WA","West Virginia": "WV","Wisconsin": "WI","Wyoming": "WY"}
            num_correct, missed_states, questions = state_quiz(states)
            results(num_correct, missed_states, questions)
            playagain = play_again()
            
        print("\n\nThanks for playing!")
        print(input('\n\nHit Enter to Close\n'))
    else:
        print("\nGoodbye!")
        print(input('\n\nHit Enter to Close\n'))


def welcome():
    print("****************************************")
    print("             50 STATES QUIZ             ")  
    print("****************************************")
    print('''
For each state abbreviation displayed,
type in the corresponding state name.''')
    playagain = ""
    while playagain not in ["1", "2"]:
        playagain = input("\n[1]Start quiz\n[2]Exit\n>")
        if playagain not in ["1", "2"]:
            print("Invalid response. Please enter '1' or '2'")
    return playagain


def state_quiz(states):
    '''
    User can choose to take a 10, 30, or 50 question quiz. Prompt user with state
    abbreviation for each question. Return the number of correct answers, a list
    of all abbreviations user got incorrect, and total number of questions.
    '''
    #Number of correct answers, and empty list for missed states
    num_correct = 0
    missed_states = []
    
    #User chooses how many questions the quiz will be (10, 30, or 50)
    quizlen = 0
    while quizlen not in [1, 2, 3]:
        try:
            quizlen = int(input("\nChoose the length of your quiz:\n[1]Short (10 questions)\n[2]Medium (30 questions)\n[3]Long (50 questions)\n>"))
            if quizlen not in [1, 2, 3]:
                print("\nPlease enter 1, 2, or 3.")
            else:
                break
        except ValueError:
            print("\nInvalid input. Please enter 1, 2, or 3.")
    if quizlen == 1:
        questions = 10
    elif quizlen == 2:
        questions = 30
    else:
        questions = 50
    
    print("\nQUIZ START!")
    
    #Create list of keys out of the 'states' dictionary. This will contain all of the full state names.
    keys = list(states.keys())
    
    for q in range(questions):
        #A random state is selected out of the keys list. Once selected, it's removed from the list so there are no repeat questions.
        randstate = keys[random.randint(0, len(keys) - 1)]
        keys.remove(randstate)
        
        #Display question number and score.
        print("------------------------")
        print(f"{q+1}/{questions}:         Score: {num_correct}")
        
        #Display random state abbreviation. User inputs answer.
        print(f"{states[randstate]}\n")
        answer = input("> ")
        
        #Determine if answer is correct.
        if answer.lower() == randstate.lower():
            print("* CORRECT *")
            num_correct += 1 #Incriment number of correct answers
        else:
            print(f"X WRONG X \n({randstate})")
            missed_states.append(states[randstate]) #Add abbreviation to missed_states list
        
    return num_correct, missed_states, questions
    
    
def results(num_correct, missed_states, questions):
    '''
    Display number of correct answers out of total number
    of questions,and display abbreviations user got incorrect.
    '''
    print("\n-------- RESULTS --------")
    print(f"Score: {num_correct}/{questions}")
    
    #If statement determines whether to display 'question' or 'questions.'
    if len(missed_states) > 1:
        print(f"\n{len(missed_states)} missed questions:")
        x = 0
        for i in missed_states:
            print(i, end = "  ")
            x += 1
            if x % 10 == 0:  #Start a new line for every 10 abbreviations displayed.
                print()
    elif len(missed_states) == 1:
        print("\n1 missed question:")
        print (missed_states[0])
    else: #No incorrect answers
        print("\n*** PERFECT SCORE ***")
        
        
def play_again():
    playagain = ""
    while playagain not in ["1", "2"]:
        playagain = input("\n\n[1]Start a new quiz\n[2]Quit\n>")
        if playagain not in ["1", "2"]:
            print("Invalid response. Please enter '1' or '2'")
    return playagain
        
        
if __name__ == "__main__":
    main()


