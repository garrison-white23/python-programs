# FILE:2252_White,G_Lesson05_InLab.py  / change "InLab" to "GrLab" for group labs
# NAME: De/Coder
# AUTHOR(s): Garrison White
# DATE: 11/6/2025
# PURPOSE: Encode/decode a message using a "Caesar Cipher" method. (A=1, B=2, C=3, etc.)

def main():
    welcome()
    playagain = play_again()
    while playagain != "3":
        if playagain == "1":
            encode()
            playagain = play_again()
        else:
            decode()
            playagain = play_again()
    print("\n\nGoodbye!")
    print(input('\n\nHit Enter to Close\n')) 

def welcome():
    print("     --- MESSAGE DECODER ---")
    print("\nInstructions:\n---------------\n1. Select to either encode, or decode a message")
    print("2. The letters in each word are replaced with their corresponding number (A=1, B=2, C=3, etc.)")
    print("3. Each number is seperated by a '-' symbol, and the words are seperated by a space")
    print("4. When decoding a message, remember to only enter numbers 1-26, and use proper formatting")

def play_again():
    playagain = input("\nSelect an option below:\n[1]Encode\n[2]Decode\n[3]Quit\n>")
    while playagain not in ["1", "2", "3"]:
        playagain = input("\nInvalid response. Please type 1, 2, or 3:\n[1]Encode\n[2]Decode\n[3]Quit\n>")
    return playagain
    
#Function used for encoding. Checks if each character is either a letter, or a space.
def is_letter_or_space(text):
    for char in text:
        if not (char.isalpha() or char.isspace()):
            return False
    return True

#Function used for decoding. Checks if each character is a number, space, or dash.
def is_num_or_space(text):
    for char in text:
        if not (char.isnumeric() or char.isspace() or char == "-"):
            return False
    return True

#User inputs a message and 'is_letter_or_space' validates the message contains letters only.
def encode():
    message = input("\nEnter a message to be encoded (letters only):\n>")
    while is_letter_or_space(message) == False:
        message = input("\nMessage can only contain letters and spaces.\nEnter a new message:\n>")

    #Split message into a list of individual words and create an empty string to add encoded words to create new message.
    words = message.lower().split()
    encoded_message = ""

    #For loop iterates through each word, and each letter of the word.
    #Letter is replaced with corresponding number.
    for word in words:
        encoded_word = ""
        for letter in word:
            number = (letter.replace('a','1').replace('b','2').replace('c','3').replace('d','4').replace('e','5').replace('f','6')
            .replace('g','7').replace('h','8').replace('i','9').replace('j','10').replace('k','11')
            .replace('l','12').replace('m','13').replace('n','14').replace('o','15').replace('p','16')
            .replace('q','17').replace('r','18').replace('s','19').replace('t','20').replace('u','21')
            .replace('v','22').replace('w','23').replace('x','24').replace('y','25').replace('z','26'))

            #If statement checks if the letter is the last letter of the word.
            #If it is not, a dash is added between to make the number more readable.
            #No dash is added if this is the last letter.
            if letter not in word[-1]:
                encoded_word += (number + "-")
            else:
                encoded_word += number
        #Add encoded word to encoded message, followed by a space.
        encoded_message += encoded_word + " "

    print("\nYour encoded message is:")
    print(encoded_message)

#User enters a coded message to be decoded, and 'is_num_or_space' checks that the message contains only
#numbers, dashes, and spaces.
def decode():
    message = input("\nEnter a message to be decoded:\n(Must be in this format: '13-25 14-1-13-5 9-19 20-9-13')\n>")
    while is_num_or_space(message) == False:
        message = input("\nMessage can only contain numbers, dashes, and spaces.\nEnter a new message:\n>")

    #Split each encoded word in a list, and create empty string for decoded message
    words = message.split()
    decoded_message = ""

    #For each encoded word, split them up at every dash, and create empty string to create a new decoded word
    for word in words:
        numbers = word.split("-")
        decoded_word = ""
        
        #Each number is just an encoded letter. Iterate through each number and replace it with the corresponding letter.
        #Start by replacing double digit numbers to avoid replacing the wrong letter. (Example: 13 is replaced with 'a' because 13 starts with 1.)
        for number in numbers:
            letter = (number.replace('26','z').replace('25','y').replace('24','x').replace('23','w').replace('22','v').replace('21','u')
                      .replace('20','t').replace('19','s').replace('18','r').replace('17','q').replace('16','p')
                      .replace('15','o').replace('14','n').replace('13','m').replace('12','l').replace('11','k')
                      .replace('10','j').replace('9','i').replace('8','h').replace('7','g').replace('6','f')
                      .replace('5','e').replace('4','d').replace('3','c').replace('2','b').replace('1','a'))

            #Add decoded letter to the empty word string
            decoded_word += letter

        #Add decoded word to empty message string
        decoded_message += (decoded_word + " ")

    print("\nYour decoded message is:")
    print(decoded_message)
        

if __name__ == "__main__":
    main()
















