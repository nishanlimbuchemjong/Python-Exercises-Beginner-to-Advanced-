# Design a class Library to manage books.
# Input:
# Add books: Python Basics, AI Guide

# Search: Python Basics
# Output:
# Book found: Python Basics

class Library:
    def __init__(self, book_name, price):
        self.book_name = book_name
        self.price = price

class Book:
    def __init__(self):
        self.books = []

    def display_books(self):
        if self.books == []:
            print("No books found!!!")
        else:
            for i, book in enumerate(self.books, start=1):
                print(f"{i} : {book.book_name} - RS. {book.price}")

    def add_books(self, book_name, price):
        new_book = Library(book_name, price)
        self.books.append(new_book)
        print("\nBook added successfully!!\n")

def main():
    book = Book()

    while True:
        print("\n................................................")
        print("\nWelcome to Library Management System\n")
        print("LIBRARY BOOK MANAGEMENT:")
        print("`````````````````````````````")
        print("1. Add Books")
        print("2. Display Books")
        print("3. Delete Books")
        print("4. Exit")
        print("................................................\n")
        choose = int(input("Choose any options: "))
        print("\n")
        if choose == 1:
            users_books = input("Enter Book name: ")
            user_books_price = int(input("Enter its price: "))
            book.add_books(users_books, user_books_price)
            
        elif choose == 2:
            book.display_books()
            print("\n")
        elif choose == 3:
            pass
        elif choose == 4:
            print("Exiting from Library Management System...........\n")
            break
        else:
            print("Invalid!!!!\nChoose between (1 to 4)")

if __name__ == '__main__':
    main()