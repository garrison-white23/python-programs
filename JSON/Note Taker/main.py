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
    while choice not in ["1", "2", "3", "4"]:
        choice = input('''
1. Login
2. Create new user
3. Delete user
4. Quit \n>''')
        if choice not in ["1", "2", "3", "4"]:
            print("Invalid response. Try again.")
        
    return choice
    

def create_user(data):
    print("\n<Create User>")
    print("(Type 'back' to return to the menu)")
    while True:
        username = input("\nCreate username: ")
        if username.lower() == "back":
            break
        elif username not in data[0].keys():
            break
        else:
            print("Sorry, that username already exists.")
            continue
    
    if username.lower() != "back":
        pw = input("Create password: ")
    
        while True:
            pw_check = input("Confirm password: ")
            if pw_check != pw:
                print("Invalid. Try again.")
            else:
                break
        print("\n*User succesfully created*")
        data[0][username] = pw
        data[1][username] = []
        save(data)


def login(data):
    print("\n<Login>")
    print("(Type 'back' to return to the menu)")
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
            pw_check = input("Enter password: ")
            if pw_check.lower() == "back":
                break
            elif pw_check != data[0][user_check]:
                print("\nIncorrect password. Try again.")
            else: 
                return user_check
                break


def delete_user(data):
    print("\n<Delete User>")
    print("(Type 'back' to return to the menu)")
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
                        del data[1][user_check]
                        print("\n*User succesfully deleted*")
                        save(data)
                    elif choice.lower() == "n":
                        break
                    else:
                        print("Invalid response. Please enter 'Y' or 'N'")
                break


def note_taker(user, data):

    def add_note():
        print("\nWhile creating a note, press enter to start a new line, and when you're finished press enter on an empty line.\n")
        note = ""
        note_line = " "
        while note_line != "":
            note_line = input(">")
            note += f"{note_line}\n"

        data[1][user].append(note)
        save(data)
        print("\n*Note succesfully created*")

    def view_notes():
        print()
        for x in range(len(data[1][user])):
            print(f"{x + 1}. \n{data[1][user][x]}")

        print(input("\nPress Enter to return..."))

    def del_note():
        print("\n<Delete Note>")
        print("(Type 'back' to return to the menu)")
        while True:
            delete = input("\nEnter note # to delete: ")
            if delete.lower() == "back":
                break
            try:
                delete = int(delete)
            except ValueError:
                print("Invalid input. Please enter a number or 'back'.")
                continue
            if delete-1 in range(len(data[1][user])):
                choice = ""
                while choice.lower() not in ["y", "n"]:
                    choice = input(f"\n'{data[1][user][delete-1][:30]}...'\nAre you sure you want to delete this note? (Y/N):")
                    if choice.lower() == "y":
                        del data[1][user][delete-1]
                        print("\n*Note succesfully deleted*")
                        save(data)
                    elif choice.lower() == "n":
                        break
                    else:
                        print("Invalid response. Please enter 'Y' or 'N'")
                break
            else:
                print("That note doesn't exist. Please enter a valid number.")

    print(f"\n<Logged in: {user}>")
    while True:
        choice = input('''
1. Add a note
2. View all notes
3. Delete a note
4. Return to menu\n>''')
        
        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            del_note()
        elif choice == "4":
            break
        else:
            print("Invalid response. Try again.") 


def save(data):
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)


if __name__ == "__main__":
    main()







