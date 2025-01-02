# Q) Write a function factorial that takes a number and returns its factorial.

# Method-1: Recursive Function
def get_number_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("\nInvalid! Enter integer number!!!\n")

def factorial(num):
    """
        factorial function that takes one parameter
        return 1, if given number is 1, else return the factorial of number
    """
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

# taking number from the user
user_number = get_number_integer("Enter number to find factorial: ")

# calling the factorial() function
result = factorial(user_number)

# printing the factorial of users entered number
print(f"Factorial of {user_number} is {result}")

print(".....................................................................\n")

# Method-2: Normal Function
def factorial(num):
    fact = 1
    if num == 0 or num == 1:
        return 1
    else:
        for i in range(1, num+1):
            fact *= i
        return fact

num = get_number_integer("Enter a number to find the factorial: ")
result = factorial(num)
print(f"Factorial of {num}! = {result}")
print("................................................................\n")