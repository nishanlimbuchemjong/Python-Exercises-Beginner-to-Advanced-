# Q1: Create a class Person with attributes name and age. Write a method greet to print a personalized greeting.
print("Question-1:\n")

# creting a class with attributes name, and age
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print(f"Hello, my name is {self.name}, and I am {self.age} years old.")

# creating an instance of a class 'Person'
obj = Person("Nishan Limbu", 23)

# calling the method of a class 'Person'
obj.greeting()

print("......................................................................\n")


# Q.2) Create multiple objects of a class Car with different attributes and print their details.
print("Question-2:\n")

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

# creating an instances of a class 'Car'
car1 = Car("Tesla", "Model S")
car2 = Car("Tesla", "X5")

# printing the result of car1
print(f"\nDetails of Car1:\n\tBrand: {car1.brand}\n\tModel: {car1.model}")
# printing the result of car2
print(f"\nDetails of Car2:\n\tBrand: {car2.brand}\n\tModel: {car2.model}")
print("......................................................................\n")


# Q3: Implement a class Rectangle with methods to calculate and return its area and perimeter.
print("Question-3: ")
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    # method to calculate the area of a rectangle
    def area(self):
        return self.length * self.breadth
    
    # method to calculate the perimeter of a rectangle
    def perimenter(self):
        return 2 * (self.length + self.breadth)

# creating an instance of a class 'Rectangel'
rect = Rectangle(5, 3)

# calling a method 'area()' to find out the area of the rectangle
print(f"\nResult: \n\tArea of rectangle = {rect.area()}")

# calling a method 'area()' to find out the area of the rectangle
print(f"\n\tPerimeter of a rectangle = {rect.perimenter()}")
print("......................................................................\n")

