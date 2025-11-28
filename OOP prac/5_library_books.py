class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.checked_out = False
    def check_out(self):
        self.checked_out = True
    def return_book(self):
        self.checked_out = False
    def is_checked_out(self):
        return self.checked_out
    
print("Welcome to the library!\n\n")
library = []

while True:
    choice = input("[1]Add a book\n[2]View books\n[3]Check out a book\n[4]Reuturn a book\n[5]Exit\n")
    if choice not in ["1", "2", "3", "4", "5"]:
        print("Invalid input. Try again.")
        continue

    if choice == "1":
        title = input("Title: ")
        author = input("Author: ")
        year = input("Year: ")

        new_book = Book(title, author, year)
        library.append(new_book)
        print("Book added.")
        continue

    if choice == "2":
        for book in library:
            print(f"{book.title}, {book.author}, {book.year}, ", end = "")
            if book.is_checked_out():
                print("Checked out")
            else:
                print("Available")
        continue

    if choice == "3":
        title_wanted = input("Enter book title to check out: ")
        for book in library:
            if book.title == title_wanted:
                if not book.is_checked_out():
                    book.check_out()
                    print("Success!")
                else:
                    print("Book is not available.")
        continue

    if choice == "4":
        book_return = input("Title to be returned: ")
        for book in library:
            if book.title == book_return:
                book.return_book()
                print("Success!")
        continue

    else:
        break

print("Goodbye!")




