"""
Without using multiplication (*), write a program to calculate the product of two integers.
"""
# taking two nubmers from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# initializing the value of sum
sum = 0

# calculating the sum 
for i in range(1, num2+1):
    sum = sum + num1

# printing the product of two number without using (*) sign
print(f"\nProduct of {num1} and {num2} is {sum}")