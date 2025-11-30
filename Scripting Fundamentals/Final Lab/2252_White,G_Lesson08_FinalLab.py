# FILE:2252_White,G_Lesson08_FinalLab.py  / change "InLab" to "GrLab" for group labs
# NAME: Final Exam Lab 
# AUTHOR(s): Garrison White
# DATE: 
# PURPOSE:

import random

def main():
    playagain = welcome()
    if playagain == "1":
        while playagain == "1":
            questions = get_questions()
            num_correct, num_wrong = quiz(questions)
            results(num_correct, num_wrong)
            playagain = play_again()
        
        print("\nThanks for playing!")
    else:
        print("\nGoodbye!")


def welcome():
    print("-------------------------")
    print("     TRIVIA GAMESHOW")
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
    '''User selects a cateogry 1-7. Then a text file is opened from 'triviaQuestions' 
    with the corresponding number in the file name. A list of questions is made, each 
    question being a dictionary with 6 attributes: the question itself, the 4 answer
    choices, and the correct answer letter. Return the list of questions to be used.'''

    #User inputs number for quiz category.
    category = ""
    while category not in ["1", "2", "3", "4", "5", "6", "7"]:
        category = input('''\nSelect a trivia category:
[1] Science
[2] History
[3] Geography
[4] Movie & TV
[5] Literature
[6] Technology
[7] General Knowledge
>''').strip()
        if category in ["1", "2", "3", "4", "5", "6", "7"]:
            break
        else:
            print("\nInvalid input. Try again.")

    #Open file for correct category. Each txt file is named 'q_x' where x is the number category.
    fin = open(f"triviaQuestions/q_{category}.txt", encoding="utf-8")  
                                                    # Note: I could not get this open function to work
                                                    # without adding this 'encoding' parameter. 
    
    #List of each question containing ALL components such as the question, answer choices, and the answer. 
    full_questions = fin.read().split("\n\n")
    
    #A new list is made to split up the questions into their components with a dictionary.
    #This way each individual component can be accessed later on.
    questions = []
    for i in full_questions:
        q_parts = i.split("\n")
        question = {"q": q_parts[0],
                    "a": q_parts[1],
                    "b": q_parts[2],
                    "c": q_parts[3],
                    "d": q_parts[4],
                    "ans": q_parts[5]}
        questions.append(question)
    
    return questions


def quiz(questions):
    random.shuffle(questions)  #Randomize order of questions
    num_correct = 0
    num_wrong = 0
    question_num = 1
    for q in questions:
        answer = ""
        print(f"\nQuestion {question_num}: \n{q["q"]}")
        while answer.lower() not in ["a", "b", "c", "d"]:
            answer = input(f"A) {q["a"]}\nB) {q["b"]}\nC) {q["c"]}\nD) {q["d"]}\n\nAnswer: ")
            if answer in ["a", "b", "c", "d"]:
                break
            else:
                print("\nInvalid input. Try again.")
        
        question_num += 1

        if answer.lower() == q["ans"]:
            print("Correct!")
            num_correct += 1
        else:
            print(f"Wrong, the answer was {q["ans"].upper()}")
            num_wrong += 1


def results(num_correct, num_wrong):
    print()


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
