# creating a class 'Animal' that contains one method 'eat()'
class Animal:
    def eat(self):
        print("Eating.....")

# creating a subclass 'Dog' that inherits the parent class 'Animal' and have one method 'bark()'
class Dog(Animal):  # Single Inheritance
    def bark(self):
        print("Barking....")

# creating a subclass 'Puppy' that inherits the parent class 'Animal', 'Dog' and have one method 'walk()'
class Puppy(Dog, Animal):   # Multiple Inheritance 
    def walk(self):
        print("Walking....")

# creating a subclass 'Cat' that inherits the parent class 'Animal' and have one method 'meow()'
class Cat(Animal):
    def meow(self):
        print("Meowing....")

  
# creating an instances of subclasses
puppy = Puppy()
cat = Cat()

# calling the methods
puppy.bark()
puppy.eat()
puppy.walk()

print()

cat.meow()
cat.eat()