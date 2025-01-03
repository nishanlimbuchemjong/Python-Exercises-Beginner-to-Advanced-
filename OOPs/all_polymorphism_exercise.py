"""
Q.1) Demonstrate method overloading using a class Calculator.
Input:
Add: 2 + 3
Add: 2 + 3 + 5

Output:
Sum: 5
Sum: 10

"""
print("Question-1:\n")

class Calculator:
    # method for adding two numbers
    # def add(self, a, b):
    #     return (a + b)

    # method for adding numbers
    def add(self, a, b, c=0):
        return a + b + c

# creating an instances of a class 'Calculator'
cal = Calculator()

# initializing the values of num1, num2, and num3
num1, num2, num3 = 2, 3, 5

# result = cal.add(num1, num2, num3)

# passing the values and calling the method for addition
# print(f"\nPassing two numbers:\n\tAdd = {num1} + {num2} = {cal.add(num1, num2)}")
print(f"\nPassing two numbers:\n\tAdd = {num1} + {num2} = {cal.add(num1, num2)}")
print(f"\nPassing three numbers:\n\tAdd = {num1} + {num2} + {num3} = {cal.add(num1, num2, num3)}")

print("..............................................................................\n")


"""
Q.2) Implement method overriding in a class hierarchy.
Input:
Parent Method: Greet
Child Method: Greet

Output:
Parent says: Hello
Child says: Hi

"""
print("Question-2: \n")

class Hierarcy:
    pass

# created a class 'Parent' that inherits from 'Hierarcy' class
class Parent(Hierarcy):
    def Greet(self):
        print("Parent says: Hello")

# created a class 'Son' that inherits from 'Parent' class
class Son(Parent):
    def Greet(self):
        print("Child says: Hi")

# creating an instances of subclasses
parent = Parent()
son = Son()

# calling the method Greet()
parent.Greet()
son.Greet()

print("............................................................\n")