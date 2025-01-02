# creating a class 'Person'
class Person:
    __name = "Nishan"

    # method to get the name
    def get_name(self):
        return self.__name
    
    # method to set or update the name
    def set_name(self, name):
        self.__name = name

# creating an object of a class "Person"
obj = Person()

# printing the result:
print(obj.get_name())
obj.set_name("Nishan Limbu")
print(obj.get_name())