# FILE:2252_White,G_Lesson08_FinalLab.py  / change "InLab" to "GrLab" for group labs
# NAME: Final Exam Lab 
# AUTHOR(s): Garrison White
# DATE: 
''' PURPOSE: Play a trivia game with multiple choice questions with a variety of categories.

There is a .txt file for each category, and the questions come from a database of trivia questions
found on the GitHub repository 'OpenTriviaQA' by user uberspot (link: https://github.com/uberspot/OpenTriviaQA).

For each category I used 50 questions from OpenTriviaQA. I made an automation script 'making_questions.py'
to randomly select questions out of the list. This way I could have a wide variety of questions without
using the full list (which is much to large). '''

import random

def main():
    playagain = welcome()
    if playagain == "1":
        while playagain == "1":
            questions, num_questions = get_questions()
            num_correct = quiz(questions, num_questions)
            results(num_correct, num_questions)
            playagain = play_again()
        
        print("\nThanks for playing!")
        print(input('Hit Enter to Close\n'))
    else:
        print("\nGoodbye!")
        print(input('Hit Enter to Close\n'))


def welcome():
    print("-------------------------")
    print("       TRIVIA GAME       ")
    print("-------------------------\n")

    print("Choose a category, and answer 10 trivia questions")
    
    playagain = ""
    while playagain not in ["1", "2"]:
        playagain = input("\nSelect an option below:\n[1] Play\n[2] Quit\n>")
        if playagain in ["1", "2"]:
            break
        else:
            print("\nInvalid input. Try again.")

    return playagain


def get_questions():
    '''User selects a cateogry 1-8. Then a text file is opened from 'triviaQuestions' 
    with the corresponding number in the file name. A list of questions is made, each 
    question being a dictionary with 6 attributes: the question itself, the 4 answer
    choices, and the correct answer letter. Return the list of questions to be used.'''

    #User inputs number for quiz category.
    category = ""
    while category not in ["1", "2", "3", "4", "5", "6", "7"]:
        category = input('''\nSelect a trivia category:
[1] Science & Technology
[2] History
[3] Geography
[4] Music
[5] Literature
[6] Movies
[7] TV
[8] General Knowledge                         
>''').strip()
        if category in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            break
        else:
            print("\nInvalid input. Try again.")

    #Open file for correct category. Each txt file is named 'q_x' where x is the number category.
    fin = open(f"triviaQuestions/q_{category}.txt", encoding="utf-8")  
                                                    # Note: I could not get this open() function to work
                                                    # without adding this 'encoding' parameter.   
    
    #List of each question containing ALL components such as the question, answer choices, and the answer. 
    full_questions = fin.read().split("\n\n")
    
    # A new list is made to split up the questions into their components with a dictionary.
    # This way each individual component can be accessed later on.
    questions = []
    for i in full_questions:
        q_parts = i.split("\n")
        question = {"q": q_parts[0][3:],    # These strings are sliced to cut off characters at the beginning
                    "ans": q_parts[1][2:],  # that are included in the OpenTriviaQA database.
                    "a": q_parts[2],
                    "b": q_parts[3],
                    "c": q_parts[4],
                    "d": q_parts[5],}
        questions.append(question)

    random.shuffle(questions)  #Randomize order of questions
    
    #User chooses how many questions the quiz will be.
    quizlen = 0
    while quizlen not in [1, 2, 3]:
        try:
            quizlen = int(input("\nChoose the length of your game:\n[1] Short (10 questions)\n[2] Medium (20 questions)\n[3] Long (30 questions)\n>"))
            if quizlen not in [1, 2, 3]:
                print("\nPlease enter 1, 2, or 3.")
            else:
                break
        except ValueError:
            print("\nInvalid input. Please enter 1, 2, or 3.")
    if quizlen == 1:
        num_questions = 10
    elif quizlen == 2:
        num_questions = 20
    else:
        num_questions = 30

    return questions, num_questions


def quiz(questions, num_questions):
    num_correct = 0
    question_num = 1
    questions_answered = 0

    #Display the question and 4 multiple choice options, and prompt for user answer.
    for q in questions:
        answer = ""
        print(f"\nQuestion {question_num}: \n{q["q"]}")
        while answer.lower() not in ["a", "b", "c", "d"]:
            answer = input(f"\n{q["a"]} \n{q["b"]} \n{q["c"]} \n{q["d"]} \n\nAnswer: ")
            if answer in ["a", "b", "c", "d"]:
                break
            else:
                print("\nInvalid input. Try again.")

        # This variable is equal to a question value using the user's answer (a, b, c, d) 
        # as the key, in order to check against the real answer.
        answer_check = q[f"{answer.lower()}"][2:]
        
        #Check if answer is correct.
        if answer_check == q["ans"]:
            print("Correct!")
            num_correct += 1
        else:
            print(f"Wrong, the answer is: {q["ans"]}")

        question_num += 1
        questions_answered += 1
        if questions_answered == num_questions:  #Break loop when user answers enough questions.
            break

    return num_correct


def results(num_correct, num_questions):
    print("\n-------- RESULTS --------")
    print(f"Score: {num_correct}/{num_questions}")


def play_again():
    playagain = ""
    while playagain not in ["1", "2"]:
        playagain = input("\nSelect an option below:\n[1] Play again\n[2] Quit\n>")
        if playagain in ["1", "2"]:
            break
        else:
            print("\nInvalid input. Try again.")
        
    return playagain
        

if __name__ == "__main__":
    main()
