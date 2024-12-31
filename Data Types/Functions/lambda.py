"""
Performing different arithmetic operations using 'Lambda' function
"""

# function to validate and get interger number 
def get_valid_number(values_entered):
    while True:
        try:
            return int(input(values_entered))
        except ValueError:
            print("\nInvalid input! Please enter a valid integer.\n")

# taking validated input from users
num1 = get_valid_number("Enter first number: ")
num2 = get_valid_number("Enter second number: ")
num3 = get_valid_number("Enter third number: ")

# printing users entered numbers
print(f"\nYour entered numbers:Number-1 = {num1}\nNumber-2 = {num2}\nNumber-3 = {num3}\n")

# finding all the arithmetic operations using lambda
addition = lambda a, b, c: a + b + c
multiplication = lambda a, b, c: a * b * c
sum_square_of_numbers = lambda a, b, c: a**2 + b**2 + c**2

# printing the results of all arithmetic operations
print("Result:\n")
print(f"Addition = {addition(num1, num2, num3)}")
print(f"Multiplication = {multiplication(num1, num2, num3)}")
print(f"Sum of Squares = {sum_square_of_numbers(num1, num2, num3)}")