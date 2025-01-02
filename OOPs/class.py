"""
Create a class Book with attributes title, author, and price. 
Add a method display_info() to print the details of the book in a formatted way. 
Create an instance of this class and call the method.

"""

# creating a class name 'Book', whose attributes are title, author, and price
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    # a method that displays the information of a Book
    def display_info(self):
        print(f"\nBook info:\n\tTitle = {self.title}\n\tAuthor = {self.author}\n\tPrice = {self.price}")

# an object of Book created
obj = Book("Mathematics", "D.R. Bajracharya", 900)

# display_info() method called
obj.display_info()
    