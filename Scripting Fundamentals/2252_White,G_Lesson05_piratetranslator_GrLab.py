# FILE:2252_White,G_Lesson05_GrLab.py  / change "InLab" to "GrLab" for group labs
# NAME: Pirate Translator
# AUTHOR(s): Garrison White
# DATE: 11/8/2025
# PURPOSE: Translate a phrase into pirate speak

import random

def main():
    playagain = welcome()
    while playagain == "1":
        translator()
        playagain = play_again()
    print("\n\nGoodbye!")

def welcome():
    print("     --- PIRATE TRANSLATOR ---     \n")
    print("Ahoy there! This program takes any sentence you type and turns it into pirate-speak.")
    playagain = ""
    while playagain not in ["1", "2"]:
        playagain = input("\nSelect one of the following:\n[1]Translate sentence\n[2]Quit\n>")
        if playagain not in ["1" , "2"]:
            print("Invalid response. Please type '1' or '2'")
    return playagain


def translator():
    #User enters phrase to be translated. Split the phrase into a list of individual words.
    #Create an empty string variable for the newly translated phrase.
    phrase = input(f"Enter a phrase to be translated into pirate speak:\n\n>")
    words = phrase.split()
    newphrase = ""

    #For loop iterates through each word of the phrase, and if any are in the following list, it's replaced with the corresponding pirate word.
    for word in words:

        #if statement checks if the word ends in a non-alphabetic character. If so, it replaces the word up until the last character
        #to accomodate for punctuation.
        if not word[-1].isalpha():
            if word[:-1] in ["Hello", "hello", "Hi", "hi", "My", "my", "Friend", "friend", "Sir", "sir",
                    "Where", "where", "Is", "is", "The", "the", "There", "there", "You", "you"]:
                word = (word
                .replace("hello","ahoy").replace("Hello","Ahoy")
                .replace("hi","yo-ho-ho").replace("Hi","Yo-ho-ho")
                .replace("my","me").replace("My","Me")
                .replace("friend","bucko").replace("Friend","Bucko")
                .replace("sir","matey").replace("Sir","Matey")
                .replace("where","whar").replace("Where","Whar")
                .replace("is","be").replace("Is","Be")
                .replace("the","th'").replace("The","Th'")
                .replace("there","thar").replace("There","Thar")
                .replace("you","ye").replace("You","Ye")
                )

        #If there's no puncuation, replace the full word.  
        else:
            if word in ["Hello", "hello", "Hi", "hi", "My", "my", "Friend", "friend", "Sir", "sir",
                    "Where", "where", "Is", "is", "The", "the", "There", "there", "You", "you"]:
                word = (word
                .replace("hello","ahoy").replace("Hello","Ahoy")
                .replace("hi","yo-ho-ho").replace("Hi","Yo-ho-ho")
                .replace("my","me").replace("My","Me")
                .replace("friend","bucko").replace("Friend","Bucko")
                .replace("sir","matey").replace("Sir","Matey")
                .replace("where","whar").replace("Where","Whar")
                .replace("is","be").replace("Is","Be")
                .replace("the","th'").replace("The","Th'")
                .replace("there","thar").replace("There","Thar")
                .replace("you","ye").replace("You","Ye")
                )
            
        #If statement determines if the word ends in 'ing' and changes it to end in 'in.'
        #Accomodates for words ending in a non-alphabetic character.
        if word.endswith("ing"):
            word = word[:-3] + "in'"
        elif (not word[-1].isalpha()) and word[-4:-1] == "ing":
            word = word[:-4] + "in" + word[-1]

        #1 in 15 chance to add 'ARR' after the word.
        if random.randint(1,15) == 1:
            word = word + " ARR"

        #Once the new word is determined, add it to the existing string to create the translated phrase.
        newphrase = newphrase + word + " "

    #Display new phrase
    print("\n*** Translating... ***\n")
    print(newphrase)
    print("\n\n")

def play_again():
    playagain = ""
    while playagain not in ["1", "2"]:
        playagain = input("Select one of the following:\n[1]Translate a new sentence\n[2]Quit\n>")
        if playagain not in ["1", "2"]:
            print("\nInvalid response. Please type '1' or '2'\n")
    return playagain
    
if __name__ == "__main__":
    main()
    
