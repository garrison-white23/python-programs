# Automation script to get 50 random questions from GitHub database of trivia questions,
# (https://github.com/uberspot/OpenTriviaQA) to be used in main program.

import random

#First, paste the entire list of questions into 'questionlist.txt'

fin = open(f"questionlist.txt", encoding="utf-8")  
full_questions = fin.read().split("\n\n")
questions = []
for q in full_questions:
    if len(q.splitlines()) == 6:  #Questions with 4 multiple choice answers will contain 6 lines (excludes true/false, etc...)
        questions.append(q)

random.shuffle(questions)

for i in range(50):  #Print questions, and copy/paste them into .txt file under 'triviaQuestions'
    print(questions[i]) 
    print()