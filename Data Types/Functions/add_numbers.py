# Write a function named add_numbers that takes two numbers as arguments and returns their sum.

def add_numbers(a, b):
    return a + b

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

sum = add_numbers(num1, num2)    

print(f"\nNumber-1 = {num1}\nNumber-2 = {num2}\n\nResult:\n\tSum = {sum}")