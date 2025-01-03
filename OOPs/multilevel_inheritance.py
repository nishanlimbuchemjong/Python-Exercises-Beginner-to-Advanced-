# creating a parent class 'Father'
class Father:
    def hair(self):
        print("Dark Black")
    
# creating a class 'Son' which is a subclass of 'Father' i.e. that inherits the properties of parent class
class Son(Father):
    def hair(self):
        print("Black ") 

# creating a class 'GradSon' which is a subclass of 'Son' i.e. that inherits the properties of parent class
class GrandSon(Son):
    def hair(self):
        print("Light Black ") 

# creating an instances of class 'GrandSon'
gson = GrandSon()

# accessing all the properties of parent classes
gson.hair()