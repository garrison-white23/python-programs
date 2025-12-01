# This is a temporary script used to sort a list of questions from GitHub database of trivia questions,
# (https://github.com/uberspot/OpenTriviaQA) containing 1k+ questions, into 250 questions with 4
# multiple choice answers to be used in the main .py file.

import random

#First, I pasted the entire list of questions into 'questionlist.txt'
fin = open(f"questionlist.txt", encoding="utf-8")  
full_questions = fin.read().split("\n\n")
questions = []
for q in full_questions:
    if len(q.splitlines()) == 6:  #Questions with 4 multiple choice answers will contain 6 lines (excludes true/false, etc...)
        questions.append(q)

random.shuffle(questions)

print(len(questions))

for i in range(250):  #Print the 250 randomly selected questions, and copy/paste them into a new .txt file under 'triviaQuestions'
    print(questions[i]) 
    print()

