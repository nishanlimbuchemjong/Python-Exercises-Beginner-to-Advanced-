# creating a class 'Animal' that contains one method 'eat()'
class Animal:
    def eat(self):
        print("Eating.....")

# creating a subclass 'Dog' that inherits the parent class 'Animal' and have one method 'bark()'
class Dog(Animal):
    def bark(self):
        print("Barking....")

# creating a subclass 'Cat' that inherits the parent class 'Animal' and have one method 'meow()
class Cat(Animal):
    def meow(self):
        print("Meowing....")
    
# creating an instances of subclasses
dog = Dog()
cat = Cat()

# calling the methods
dog.bark()
dog.eat()

print()

cat.meow()
cat.eat()