"""
Define a parent class Animal with a method speak() that prints a generic message like "This animal makes a sound."
Then, define two child classes:

Dog that overrides the speak() method to print "Woof!"
Cat that overrides the speak() method to print "Meow!"
Create objects of Dog and Cat and call their speak() methods.

"""
# defining a parent class 'Animal'
class Animal:
    def __init__(self):
        pass
    
    # created a method speak()
    def speak(self):
        print("This animal makes a sound.")

# defining a child class 'Dog'
class Dog(Animal):
    def speak(self):
        print("Woof!")

# defining a child class 'Cat'
class Cat(Animal):
    def speak(self):
        print("Meow!")


# creating an object of child class 'Dog' and 'Cat'
cat = Cat()
dog = Dog()

# calling the method
cat.speak()     # output: Meow!
dog.speak()     # Woof!