import json


def main():
    with open("data.json", "r") as f:
        data = json.load(f)
    choice = ""
    
    while choice != "4":
        choice = main_menu()

        if choice == "1":
            user = login(data)
            if user:
                note_taker(user, data)
        elif choice == "2":
            create_user(data)
        elif choice == "3":
            delete_user(data)

    
    print(input("\nGoodbye!\nPress Enter to close...\n"))


def main_menu():
    choice = ""
    while choice not in ["1", "2", "3", "4", "5"]:
        choice = input('''
[1] Login
[2] Create new user
[3] Delete user
[4] Quit \n>''')
        
    return choice
    

def create_user(data):
    while True:
        username = input("\nCreate username (Type 'back' to return to menu): ")
        if username.lower() == "back":
            break
        elif username not in data[0].keys():
            break
        else:
            print("Sorry, that username already exists.")
            continue
    
    if username.lower() != "back":
        pw = input("\nCreate password: ")
    
        while True:
            pw_check = input("Confirm password: ")
            if pw_check != pw:
                print("Invalid. Try again.")
            else:
                break

        data[0][username] = pw
        data[1][username] = []
        with open("data.json", "w") as f:
            json.dump(data, f, indent=4)



def login(data):
    print("\n*Type 'back' to return to the menu*")
    while True:
        user_check = input("\nEnter username: ")
        if user_check.lower() == "back":
            break
        elif user_check not in data[0].keys():
            print("User not found. Try again.")
        else:
            break
    if user_check.lower() != "back":
        while True:
            pw_check = input("\nEnter password: ")
            if pw_check.lower() == "back":
                break
            elif pw_check != data[0][user_check]:
                print("Incorrect password. Try again.")
            else: 
                return user_check
                break


def delete_user(data):
    print("\n*Type 'back' to return to the menu*")
    while True:
        user_check = input("\nEnter user to delete: ")
        if user_check.lower() == "back":
            break
        elif user_check not in data[0].keys():
            print("User not found. Try again.")
        else:
            break
    if user_check.lower() != "back":
        while True:
            pw_check = input("\nEnter password: ")
            if pw_check.lower() == "back":
                break
            elif pw_check != data[0][user_check]:
                print("Incorrect password. Try again.")
            else: 
                choice = ""
                while choice.lower() not in ["y", "n"]:
                    choice = input("\nAre you sure you want to delete this user? (Y/N):")
                    if choice.lower() == "y":
                        del data[0][user_check]
                        #del data[1][user_check]
                        print("\nUser succesfully deleted")
                        with open("data.json", "w") as f:
                            json.dump(data, f, indent=4)
                    elif choice.lower() == "n":
                        break
                    else:
                        print("Invalid response. Please enter 'Y' or 'N'")
                break


def note_taker(user, data):
    print(input("\nUnder construction.\nPress Enter to return.\n"))
    '''
    1. Add a note
    2. View all notes
    3. Delete a note
    4. Return to menu'''    


if __name__ == "__main__":
    main()







