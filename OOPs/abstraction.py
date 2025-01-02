from abc import ABC, abstractmethod

# abstract base class for Car
class Car(ABC):
    def show(self):
        print("Has 4 weels")

    # abstract method that must be implemented by subclasses
    @abstractmethod
    def speed(self):
        pass

class Suzuki(Car):
    def speed(self):
        print("Speed is 70km/hr")

class Maruti(Car):
    def speed(self):
        print("Speed is 100km/hr")

# creating an object
obj1 = Suzuki()

# calling the methods
obj1.show()
obj1.speed()
