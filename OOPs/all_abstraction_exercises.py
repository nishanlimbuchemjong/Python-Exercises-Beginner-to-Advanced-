from abc import ABC, abstractmethod

# Q.1) Create an abstract class Vehicle and implement it in Car and Bike.
print("Question-1: \n")
class Vehicle:
    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Car is moving")
        
class Bike(Vehicle):
    def move(self):
        print("Bike is moving")

# creating an instances of subclasses
car = Car()
bike = Bike()

# calling the method
car.move()
bike.move()
print("..................................................................\n")

# Q.2) Create an abstract base class Appliance with derived classes.
print("Question-2: \n")

class Appliance:
    @abstractmethod
    def run(self):
        pass

# creating a class that inherits a parent class 'Appliance'
class Washing_Machine(Appliance):
    @abstractmethod
    def run(self):
        print("Washing Machine running")

# creating an instance of subclass
washing_machine = Washing_Machine()

# calling the run() method
washing_machine.run()

print("......................................................\n")