# Finding out the fibonaccic series
# Method-1: Normal Function
print("Method-1: Normal Function\n")

# function for validating integer number
def get_integer_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("\nPlease enter integer number: ")

def fibonacci(num):
    num1, num2 = 0, 1
    for i in range(num):
        print(num1, end=", ") 
        num1, num2 = num2, (num1 + num2)

# taking a number from user
num = get_integer_number("Enter a number for fibonacci series: ")

# calling the function
fibonacci(num)

print("\n...................................................\n")


# Method-2: Recursive Function
print("Method-2: Recursive Function\n")

# function for generating fibonacci series
def fibonacci_series(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci_series(num-1) + fibonacci_series(num-2)
    
# taking number from user to print the fibonacci series
number = get_integer_number("Enter a number to print fibonacci series: ")

# checking the given number is positive or not; if positive then it prints fibonacci series else error
if number < 0:
    print("\nPlease enter Positive number.!!!!")
else:
    for i in range(number):
        print(fibonacci_series(i), end=", ")
print("\n................................................\n")
