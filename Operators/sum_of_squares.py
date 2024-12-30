"""
Write a program to calculate the sum of squares of two numbers only if their product is greater than 100.
"""
def sum_of_squares(n1, n2):
    if (n1 * n2) > 100:
        return n1**2 + n2**2
    else:
        return False

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

squares_sum = sum_of_squares(num1, num2)

print("\nOutput:")
if squares_sum == False:
    print("Sum of their squares is less than 100")
else:
    print(f"Number 1: {num1}\nNumber 2: {num2}")
    print(f"Sum of squares = {squares_sum}")