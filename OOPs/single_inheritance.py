# created a class 'Animal' that have speak() method
class Animal:
    def speak(self):
        print("Some sound")

# creating a class 'Dog' that inherits all the properties of parent class 'Animal'
class Dog(Animal):
    def speak(self):
        print("Bark")

# creating an instance of a subclass 'Dog'
dog = Dog()

# calling the method speak()
dog.speak()
