# created a class 'Library' with attributes book_name, and price
class Library:
    def __init__(self, book_name, price):
        self.book_name = book_name
        self.price = price

# created another class 'Book' 
class Book:
    def __init__(self):
        self.books = []

    # method that display all books
    def display_books(self):
        if self.books == []:
            print("No books found!!!")
        else:
            for i, book in enumerate(self.books, start=1):
                print(f"{i} : {book.book_name} - RS. {book.price}")

    # method that add books into a list 'books'
    def add_books(self, book_name, price):
        new_book = Library(book_name, price)
        self.books.append(new_book)
        print(f"\n'{new_book.book_name}' book added successfully!!\n")

    # method to delete books from books list
    def delete_books(self, book_name):
        for i in self.books:
            if i.book_name == book_name:
                self.books.remove(i)
        print(f"'{book_name}' book deleted successfully!!")

# function that validates the integer number
def get_interger_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("\nPlease Enter a positive integer number\n")

def main():
    # created an instance of a class 'Book'
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

        choose = get_interger_number("Choose any options: ")
        print("\n")
        if choose == 1:
            users_books = input("Enter Book name: ")
            user_books_price = get_interger_number("Enter its price: ")
            book.add_books(users_books, user_books_price)
            
        elif choose == 2:
            book.display_books()
            print("\n")
        elif choose == 3:
            users_books = input("Enter Book name: ")
            book.delete_books(users_books)
        elif choose == 4:
            print("Exiting from Library Management System...........\n")
            break
        else:
            print("Invalid!!!!\nChoose between (1 to 4)")

if __name__ == '__main__':
    main()