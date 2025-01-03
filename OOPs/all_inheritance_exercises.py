"""
Q.1) Write a program with a base class Animal and derived classes Dog and Cat.
Input:
Animal: Dog

Output:
Dog says: Woof!
"""
print("Question-1: \n")
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog says: Woof!")
    
# creating an instance of a Dog
dog = Dog()

# calling the method speak()
dog.speak()

print("................................................................\n")

"""
Q.2) Override the area method in Square and Circle.
Input:
Square Side: 4, Circle Radius: 3

Output:
Square Area: 16
Circle Area: 28.27
"""

print("Question-2: \n")

class Area:
    def __init__(self, length):
        self.length = length

class Square(Area):
    def area(self):
        return self.length * self.length

class Circle(Square):
    def area(self):
        return (22 * self.length * self.length) / 7
    
# creating an instances of different sub classes
square = Square(4)
circle = Circle(3)

# printing the area of square and circle:
print(f"Square Area = {square.area()}")
print(f"Circle Area = {circle.area(): .2f}")

print("...............................................................\n")