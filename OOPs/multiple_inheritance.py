# creating a class 'Father' that have one method 'profession()'
class Father:
    def profession(self):
        print("Farmer")

# creating a class 'Mother' that also have on emethod 'profession()'
class Mother:
    def profession(self):
        print("House Wife")

# creating a subclass 'Child' that inherits all the methods of both 'Father' and 'Mother' parent class
class Child(Father, Mother):
    def profession(self):
        print("Backend Developer")

# creating an instance of a 'Child' class
child = Child()

child.profession()