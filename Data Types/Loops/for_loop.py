"""
All Questions Related to 'For Loop in Python'
"""

# Q.1) Write a program to calculate the sum of all even numbers from 1 to 100 using a for loop.
print("Question-1: Sum of Even Numbers\n")

# initial value of sum 
total = 0

# using for loop for calculating the sum of all even numbers from 1 to 100
for i in range(1, 101):
    if i % 2 == 0:    #checking if the number is even or not
        total += i
print(f"Sum of even numbers from 1 to 100 = {total}")
print("......................................................\n")

# Q.2) Write a program that prints all multiples of any number taken from user using a for loop.
print("Question-2: Multiples of Given Number")

# taking a number from a user for a multiplication table
user_number = int(input("Enter the number for a multiplication table: "))

# calculating and printing the multiplication table of a given number
print(f"\nMultiplication Table of {user_number}:")
for i in range(1, 11):
    print(f"{user_number} X {i} = {user_number * i}")

print("................................................\n")

# Q.3) Write a program that finds the maximum number entered by the users using a for loop.
print("Question-3: Find Maximum from Users Input")

# taking numbers from the user
total_number = int(input("Enter total number to entered: "))

# creating an empty list for storing the numbers that user have entered
nums = []

print("Enter your numbers: ")
for i in range(total_number):
    nums.append(int(input()))
print(f"\nNumbers you have given: {nums}")


print(f"\nResult:\tMaximum number you have entered: {max(nums)}")
print("...........................................................\n")