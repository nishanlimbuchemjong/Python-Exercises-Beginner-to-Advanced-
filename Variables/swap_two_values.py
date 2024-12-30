""" 
Q.1) Write a Python script to swap the values of two variables without using a temporary variable
""" 
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

# swapping the users two numbers using Addition and Subtraction Operators
num1 = num1+num2
num2 = num1-num2
num1 = num1-num2
print("Method-1")
print("After swapping:")
print(f"Number 1: {num1}\tNumber 2: {num2}")
print("```````````````````````````````````````````````")
# swapping using simple built-in method:
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

num1, num2 = num2, num1
print("Method-2")
print("After swapping: \n")
print(f"Number 1: {num1}\tNumber 2: {num2}")
print("```````````````````````````````````````````````")
