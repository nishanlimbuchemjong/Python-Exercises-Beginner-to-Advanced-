# Q) Write a function factorial that takes a number and returns its factorial.


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
user_number = int(input("Enter number to find factorial: "))

# calling the factorial() function
result = factorial(user_number)

# printing the factorial of users entered number
print(f"Factorial of {user_number} is {result}")