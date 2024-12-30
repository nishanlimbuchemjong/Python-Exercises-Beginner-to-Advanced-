"""
Write a program that takes an integer and determines whether it is divisible by 2, 3, or both using a combination of logical operators and conditionals.
"""

number = int(input("Enter your number: "))

if (number % 3 == 0) and (number % 2 == 0):
    print(f"Number {number} is divisible by both (2 and 3)")
elif (number % 3 == 0) and (number % 2 == 0):
    if number % 3 == 0:
        print(f"Number {number} is divisible by 3")
    else:
        print(f"Number {number} is divisible by 2")
else:
    print(f"Number {number} is not divisible by any of them")
