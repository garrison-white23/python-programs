import json


def main():
    with open("data.json", "r") as f:
        data = json.load(f)
    choice = ""
    
    while choice != "5":
        choice = main_menu()

        if choice == "1":
            user = login(data)
            if user:
                note_taker(user)
        elif choice == "2":
            create_user(data)
        elif choice == "3":
            change_info(data)
        elif choice == "4":
            delete_user(data)

    
    print(input("\nGoodbye!\nPress Enter to close...\n"))


def main_menu():
    choice = ""
    while choice not in ["1", "2", "3", "4", "5"]:
        choice = input('''
    [1] Login
    [2] Create new user
    [3] Change username or password
    [4] Delete user
    [5] Quit \n>''')
        
    return choice
    

def create_user(data):
    while True:
        username = input("\nCreate username: ")
        if username not in data.keys():
            break
        else:
            print("Sorry, that username already exists.")
            continue
    
    pw = input("\nCreate password: ")
    
    while True:
        pw_check = input("Confirm password: ")
        if pw_check != pw:
            print("Invalid. Try again.")
        else:
            break

    data[username] = pw



def login(data):
    while True:
        user_check = input("\nEnter username: ")
        if user_check not in data.keys():
            print("Invalid. Try again.")
        else:
            break

    while True:
        pw_check = input("\nEnter password: ")
        if pw_check != data[user_check]:
            print("\nIncorrect password. Try again.")
        else:
            break


def change_info(data):
    pass


def delete_user(data):
    pass


def note_taker():
    print(input("\nUnder construction.\nPress Enter to return.\n"))








